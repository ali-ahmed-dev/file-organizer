from pathlib import Path
import shutil
from datetime import datetime

SEPARATOR = "=" * 50
REPORT_FILENAME = "file_organizer_report.txt"
REPORT_FILE = Path(REPORT_FILENAME)

HEADER = f"{SEPARATOR}\n                 FILE ORGANIZER\n{SEPARATOR}"
FOOTER = f"{SEPARATOR}\n                 END OF REPORT\n{SEPARATOR}"


def organize_by_extension(folder):
    extensions = {}

    for file in folder.glob("*"):
        if file.is_file():
            ext = file.suffix.lower()[1:] if file.suffix else "no_extension"
            if ext in extensions:
                extensions[ext].append(file)
            else:
                extensions[ext] = [file]

    for extension, files in extensions.items():
        new_folder = folder / extension
        new_folder.mkdir(exist_ok=True)

        for file in files:
            target = new_folder / file.name

            if target.exists():
                copy_number = 1
                while True:
                    new_name = f"{file.stem} ({copy_number}){file.suffix}"
                    target = new_folder / new_name
                    if not target.exists():
                        break
                    copy_number += 1
            shutil.move(file, target)

    stats = {
        "total_files": sum(len(files) for files in extensions.values()),
        "extensions_count": len(extensions),
        "files_by_extension": {
            ext: len(files)
            for ext, files in extensions.items()
        }
    }

    return stats


def generate_report(stats):
    report = [
        HEADER,
        "",
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Total files: {stats['total_files']}",
        f"Extensions count: {stats['extensions_count']}",
        "",
        "Files by extension:",
        *[f"  {ext}: {count}" for ext, count in stats["files_by_extension"].items()],
        "",
        FOOTER
    ]
    return "\n".join(report)


def export_report(report_text):
    REPORT_FILE.write_text(report_text, encoding="utf-8")


def main():
    print("Welcome to the File Organizer Tool")
    try:
        folder_path = input("Enter the folder path to organize: ")
        folder = Path(folder_path)
        if folder.exists() and folder.is_dir():
            stats = organize_by_extension(folder)
            report_text = generate_report(stats)
            print(report_text)
            export_report(report_text)
            print("\nReport exported successfully.")
            print(f"File name : {REPORT_FILE.name}")
            print(f"Location  : {REPORT_FILE.resolve()}")
        else:
            print("The folder does not exist or is not a directory.")

    except PermissionError:
        print("Error: Permission denied. Please check folder permissions.")

    except OSError:
        print("Error: A file system error occurred.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
