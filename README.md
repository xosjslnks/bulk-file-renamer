# 📂 Bulk File Renamer CLI

> Rename files in bulk — **fast, safe, and powerful.**

A lightweight yet powerful command-line tool to rename hundreds or thousands of files in seconds. Perfect for organizing **photos, downloads, scans, music libraries, project files**, and more.

Built with **pure Python** and minimal dependencies.

---

# ✨ Features

* 🔒 **Safe by default** — preview changes with `--dry-run`
* ⚡ **Fast** — handles **10,000+ files**
* 🔍 **Regex support** for advanced renaming
* 🔢 **Sequential numbering** with zero-padding
* 📅 **Date insertion** from file metadata
* 🧠 **Extension filtering**
* 📁 **Recursive folder support**
* 🧾 **Optional rename log** for undo
* 🌍 **Cross-platform** (Windows, macOS, Linux)
* 🐍 **No heavy dependencies** — Python standard library

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/xobe/bulk-file-renamer.git
cd bulk-file-renamer
```

## 2. (Optional) Install color support

```bash
pip install colorama
```

That's it — no other setup needed.

---

# 🚀 Quick Start

Navigate to your target folder or specify the path.

---

## 1. Add prefix to photos

```bash
python src/renamer.py "photos/" --prefix "Bali-2025-" --ext jpg jpeg png
```

Result:

```
photo1.jpg → Bali-2025-photo1.jpg
```

---

## 2. Add sequential numbering

```bash
python src/renamer.py "scans/" --number --start 1 --pad 3
```

Result:

```
scan_001.pdf
scan_002.pdf
scan_003.pdf
```

---

## 3. Replace text in filenames

```bash
python src/renamer.py "downloads/" --replace "IMG_" "Vacation-"
```

Result:

```
IMG_001.jpg → Vacation-001.jpg
```

---

## 4. Change extension

```bash
python src/renamer.py "images/" --change-ext jpeg jpg
```

---

## 5. Add date prefix

```bash
python src/renamer.py "memes/" --add-date "%Y-%m-%d_"
```

Example:

```
meme.jpg → 2025-03-08_meme.jpg
```

---

## 6. Regex replace (advanced)

```bash
python src/renamer.py "." --regex "(\d{4})-(\d{2})-(\d{2})" "20\1-\2-\3"
```

---

## 7. Preview changes first

```bash
python src/renamer.py "folder/" --prefix "Backup-" --dry-run
```

This will show what **would change** without modifying files.

---

## 8. Recursive rename + logging

```bash
python src/renamer.py "projects/" --recursive --prefix "v2-" --log
```

Creates:

```
renamed_log.txt
```

Useful for **undo operations**.

---

# 📖 Full Command Reference

```
usage: renamer.py [-h] [--prefix PREFIX] [--suffix SUFFIX]
                  [--replace OLD NEW]
                  [--regex PATTERN REPL]
                  [--change-ext OLD_EXT NEW_EXT]
                  [--number]
                  [--start START]
                  [--pad PAD]
                  [--add-date FORMAT]
                  [--date-from-creation]
                  [--ext EXT [EXT ...]]
                  [--recursive]
                  [--dry-run]
                  [--log]
                  folder
```

---

# 📋 Options

| Option                 | Description                      |
| ---------------------- | -------------------------------- |
| `folder`               | Target folder path               |
| `--prefix`             | Add prefix to filename           |
| `--suffix`             | Add suffix before extension      |
| `--replace OLD NEW`    | Replace text in filenames        |
| `--regex PATTERN REPL` | Regex replace                    |
| `--change-ext OLD NEW` | Change file extension            |
| `--number`             | Add sequential numbering         |
| `--start`              | Starting number (default: 1)     |
| `--pad`                | Zero-padding digits (default: 3) |
| `--add-date`           | Add date prefix                  |
| `--date-from-creation` | Use creation date instead        |
| `--ext`                | Only process these extensions    |
| `--recursive`          | Process subfolders               |
| `--dry-run`            | Preview changes only             |
| `--log`                | Save rename log                  |

---

# 📂 Example Use Cases

### Organizing vacation photos

```
IMG_1001.jpg → Bali-2025-001.jpg
```

### Cleaning messy downloads

```
file (1).pdf → document_001.pdf
```

### Versioning project files

```
report.txt → v2-report.txt
```

---

# 🧠 Tips

✔ Always run **`--dry-run` first**
✔ Use **`--log`** if you want an undo trail
✔ Combine multiple options for powerful workflows

Example:

```bash
python src/renamer.py photos/ --prefix trip- --number --pad 4 --ext jpg png
```

---

# 🤝 Contributing

Pull requests are welcome.

Ideas for improvements:

* Additional **date formats**
* Better handling for **special characters**
* **Sorting options**
* Lightweight **GUI version (Tkinter)**

---

# 🗺 Roadmap

Planned features:

* File sorting before numbering
* Undo command
* Preview table output
* GUI version

---

# 📜 License

MIT License — free to use, modify, and distribute.

---

# ⭐ Support

If this tool saves you time, consider **starring the repo** ⭐

Made with ❤️ by **xobe**
