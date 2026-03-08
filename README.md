# Bulk File Renamer CLI

**Rename files in bulk — fast, safe, and powerful.**

A simple yet feature-packed command-line tool to batch rename hundreds or thousands of files in seconds. Perfect for organizing photos, downloads, scans, music libraries, project files, and more.

- Add prefixes/suffixes  
- Replace text or use regex  
- Add sequential numbering (with zero-padding)  
- Insert dates from file metadata  
- Change extensions  
- Preview changes first (dry-run)  
- Recursive mode for subfolders  
- Cross-platform (Windows, macOS, Linux)

No heavy dependencies — runs on pure Python (optional color support).

## Features

- **Safe by default**: Always preview with `--dry-run` before making changes  
- **Powerful**: Supports regex, date formatting, numbering, filtering by extension  
- **Undo-friendly**: Optional rename log file for easy rollback  
- **Fast**: Handles 10,000+ files without issues  
- **Zero or minimal dependencies**: Works with Python 3.8+ standard library

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/xobe/bulk-file-renamer.git
   cd bulk-file-renamer

(Optional) Install color support for nicer output:Bashpip install colorama

That's it — no other setup needed!
Quick Start Examples
Navigate to your target folder or provide the path.
1. Add prefix to all photos
Bashpython src/renamer.py "photos/" --prefix "Bali-2025-" --ext jpg jpeg png
2. Add numbering with zero-padding
Bashpython src/renamer.py "scans/" --number --start 1 --pad 3
# → scan_001.pdf, scan_002.pdf, ...
3. Replace text in filenames
Bashpython src/renamer.py "downloads/" --replace "IMG_" "Vacation-"
4. Change all .jpeg to .jpg
Bashpython src/renamer.py "images/" --change-ext jpeg jpg
5. Add date prefix (from last modified time)
Bashpython src/renamer.py "memes/" --add-date "%Y-%m-%d_" --prefix
# → 2025-03-08_meme.jpg
6. Regex replace (power users)
Bashpython src/renamer.py "." --regex "(\d{4})-(\d{2})-(\d{2})" "20\1-\2-\3"
7. Preview only (always recommended first!)
Bashpython src/renamer.py "folder/" --prefix "Backup-" --dry-run
8. Recursive + log changes
Bashpython src/renamer.py "projects/" --recursive --prefix "v2-" --log
Full list of options:
Bashpython src/renamer.py --help
Full Command Reference
textusage: renamer.py [-h] [--prefix PREFIX] [--suffix SUFFIX] [--replace OLD NEW]
                  [--regex PATTERN REPL] [--change-ext OLD_EXT NEW_EXT]
                  [--number] [--start START] [--pad PAD] [--add-date FORMAT]
                  [--date-from-creation] [--ext EXT [EXT ...]] [--recursive]
                  [--dry-run] [--log]
                  folder

Bulk File Renamer - rename files in batch safely

positional arguments:
  folder                Target folder path

options:
  -h, --help            show this help message and exit
  --prefix PREFIX       Add prefix to filename
  --suffix SUFFIX       Add suffix before extension
  --replace OLD NEW     Replace OLD with NEW in filename
  --regex PATTERN REPL  Regex replace: PATTERN -> REPL
  --change-ext OLD_EXT NEW_EXT
                        Change file extension
  --number              Add sequential numbering
  --start START         Starting number (default: 1)
  --pad PAD             Zero-padding digits (default: 3)
  --add-date FORMAT     Add date prefix, format e.g. '%Y-%m-%d_' (from modified time)
  --date-from-creation  Use creation date instead of modified
  --ext EXT [EXT ...]   Only process these extensions (without dot)
  --recursive           Process subfolders too
  --dry-run             Preview only, no changes
  --log                 Save rename log to renamed_log.txt
Contributing
Pull requests welcome! Especially:

Additional date formats or sorting options
Better error handling for special characters
GUI version (Tkinter or something lightweight)

License
MIT License — feel free to use, modify, and distribute.
Made with ❤️ by xobe
Star ⭐ the repo if this tool saves you time!
