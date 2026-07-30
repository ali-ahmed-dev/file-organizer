# File Organizer

A Python command-line tool that automatically organizes files by their extensions, resolves duplicate filename conflicts, and generates a detailed text report summarizing the organization process.

---

## Features

- Organize files into folders based on their extensions.
- Automatically create extension folders when needed.
- Safely handle duplicate filenames without overwriting existing files.
- Generate a detailed organization report.
- Export the report as a UTF-8 encoded text file.
- Display useful statistics about the organization process.

---

## Requirements

- Python 3.6+
- Standard library only (pathlib, shutil, datetime) — no external packages required.

---

## Installation

Clone the repository:

    git clone https://github.com/ali-ahmed-dev/file-organizer.git

Navigate to the project directory:

    cd file-organizer

---

## Usage

Run the program:

    python file_organizer.py

When prompted, enter the full path of the folder you want to organize.

---

## Example Output

    ==================================================
                     FILE ORGANIZER
    ==================================================

    Date: 2026-07-29 14:35:12

    Total files: 45
    Extensions count: 8

    Files by extension:
      pdf: 10
      jpg: 12
      png: 6
      txt: 5
      py: 7
      zip: 3
      mp3: 1
      no_extension: 1

    ==================================================
                     END OF REPORT
    ==================================================

    Report exported successfully.
    File name : file_organizer_report.txt
    Location  : C:\Users\Ali\Desktop\file-organizer\file_organizer_report.txt

---

## Project Structure

    file-organizer/
    │
    ├── file_organizer.py
    └── README.md

---

## Future Improvements

- Export reports in JSON format.
- Add recursive subfolder organization support.
- Ignore hidden and system files.
- Add configurable output location for reports.
- Improve report details with full file lists per extension.
- Add optional logging support.

---

## License

This project is licensed under the MIT License.

---

## Version

v1.0.0

---

## Author

Ali Ahmed
