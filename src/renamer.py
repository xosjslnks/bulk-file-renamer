#!/usr/bin/env python3
"""
Bulk File Renamer CLI
Simple, safe, powerful batch file renaming tool
"""

import argparse
import os
import re
from pathlib import Path
from datetime import datetime
import sys

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False

def cprint(text, color=Fore.WHITE, **kwargs):
    """
    Custom print with color support and **kwargs forwarding (end='', flush, etc.)
    """
    if COLOR:
        print(color + text + Style.RESET_ALL, **kwargs)
    else:
        print(text, **kwargs)

def get_modified_date(file_path):
    """Get file's last modified date"""
    try:
        ts = os.path.getmtime(file_path)
        return datetime.fromtimestamp(ts)
    except Exception:
        return datetime.now()

def preview_rename(files, new_names):
    """Show preview of changes"""
    cprint("\nPreview of changes:", Fore.CYAN)
    for old, new in zip(files, new_names):
        if old.name != new.name:
            cprint(f"  {old}  →  {new}", Fore.GREEN)
        else:
            print(f"  {old}  →  (unchanged)")

def perform_rename(files, new_names, log_file=None):
    """Actually rename the files"""
    renamed_count = 0
    log_lines = []

    for old_path, new_path in zip(files, new_names):
        if old_path == new_path:
            continue

        try:
            old_path.rename(new_path)
            renamed_count += 1
            log_line = f"{old_path} -> {new_path}"
            log_lines.append(log_line)
            cprint(f"Renamed: {log_line}", Fore.GREEN)
        except Exception as e:
            cprint(f"Error renaming {old_path}: {e}", Fore.RED)

    if log_file and log_lines:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("\n".join(log_lines) + "\n")
        cprint(f"\nLog saved to: {log_file}", Fore.YELLOW)

    return renamed_count

def main():
    parser = argparse.ArgumentParser(
        description="Bulk File Renamer - rename files in batch safely",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("folder", type=str, help="Target folder path")

    # Basic operations
    parser.add_argument("--prefix", type=str, help="Add prefix to filename")
    parser.add_argument("--suffix", type=str, help="Add suffix before extension")
    parser.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="Replace OLD with NEW in filename")
    parser.add_argument("--regex", nargs=2, metavar=("PATTERN", "REPL"), help="Regex replace: PATTERN -> REPL")
    parser.add_argument("--change-ext", nargs=2, metavar=("OLD_EXT", "NEW_EXT"), help="Change file extension")

    # Numbering
    parser.add_argument("--number", action="store_true", help="Add sequential numbering")
    parser.add_argument("--start", type=int, default=1, help="Starting number (default: 1)")
    parser.add_argument("--pad", type=int, default=3, help="Zero-padding digits (default: 3 → 001, 002, ...)")

    # Date
    parser.add_argument("--add-date", type=str, help="Add date prefix, format e.g. '%%Y-%%m-%%d_' (from file modified time)")
    parser.add_argument("--date-from-creation", action="store_true", help="Use creation date instead of modified")

    # Filters
    parser.add_argument("--ext", nargs="+", help="Only process these extensions (without dot)")
    parser.add_argument("--recursive", action="store_true", help="Process subfolders too")

    # Safety
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no changes")
    parser.add_argument("--log", action="store_true", help="Save rename log to renamed_log.txt")

    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        cprint(f"Error: '{folder}' is not a valid directory.", Fore.RED)
        sys.exit(1)

    # Collect files
    if args.recursive:
        files = list(folder.rglob("*"))
    else:
        files = list(folder.glob("*"))

    # Filter by extension if specified
    if args.ext:
        exts = {f".{e.lower()}" for e in args.ext}
        files = [f for f in files if f.is_file() and f.suffix.lower() in exts]
    else:
        files = [f for f in files if f.is_file()]

    if not files:
        cprint("No files found to rename.", Fore.YELLOW)
        return

    files.sort(key=lambda p: p.name.lower())  # consistent order

    new_names = []
    log_file = folder / "renamed_log.txt" if args.log else None

    for idx, old_path in enumerate(files, start=args.start):
        name = old_path.stem
        ext = old_path.suffix

        new_name = name

        # 1. Date prefix
        if args.add_date:
            dt = get_modified_date(old_path) if not args.date_from_creation else datetime.fromtimestamp(old_path.stat().st_ctime)
            date_str = dt.strftime(args.add_date)
            new_name = date_str + new_name

        # 2. Prefix
        if args.prefix:
            new_name = args.prefix + new_name

        # 3. Replace string
        if args.replace:
            old_txt, new_txt = args.replace
            new_name = new_name.replace(old_txt, new_txt)

        # 4. Regex replace
        if args.regex:
            pattern, repl = args.regex
            new_name = re.sub(pattern, repl, new_name)

        # 5. Numbering
        if args.number:
            num_str = f"{idx:0{args.pad}d}"
            new_name += num_str

        # 6. Suffix (before extension)
        if args.suffix:
            new_name += args.suffix

        # 7. Change extension
        if args.change_ext:
            old_ext, new_ext = args.change_ext
            if ext.lower() == f".{old_ext.lower()}":
                ext = f".{new_ext}"

        new_path = old_path.with_name(new_name + ext)
        new_names.append(new_path)

    # Preview
    preview_rename(files, new_names)

    if args.dry_run:
        cprint("\nDry-run mode: No files were renamed.", Fore.YELLOW)
        return

    # Konfirmasi dengan support end=""
    cprint(f"\nFound {len(files)} files. Proceed with rename? (y/N): ", Fore.CYAN, end="")

    confirm = input().strip().lower()
    if confirm not in ("y", "yes"):
        cprint("Aborted.", Fore.YELLOW)
        return

    renamed = perform_rename(files, new_names, log_file)

    cprint(f"\nDone! {renamed} files renamed.", Fore.GREEN)
    if log_file:
        cprint(f"Log saved at: {log_file}", Fore.YELLOW)

if __name__ == "__main__":
    main()
