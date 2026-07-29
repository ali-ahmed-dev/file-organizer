from pathlib import Path
import shutil
# import datetime

HEADER = "=" * 50 + "\n                 FILE ORGANIZER\n" + "=" * 50
FOOTER = "=" * 50 + "\n                 END OF REPORT\n" + "=" * 50

REPORT_FILE = Path("file_organizer_report.txt")


def organize_by_extension(folder):
    extensions = {}
    stats = {
        "total_files": 0,
        "extensions_count": 0,
        "files_by_extension": {}
    }

    for file in folder.glob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if not ext:
                ext = "no_extension"
            else:
                ext = ext[1:]
            if ext in extensions:
                extensions[ext].append(file)
            else:
                extensions[ext] = [file]

    for extension, files in extensions.items():
        new_folder = folder / extension
        new_folder.mkdir(exist_ok=True)
        for file in files:
            target = new_folder / file.name
            shutil.move(file, target)

    for files in extensions.values():
        stats["total_files"] += len(files)
    stats["extensions_count"] = len(extensions)
    for ext, files in extensions.items():
        stats["files_by_extension"][ext] = len(files)
    return stats


def generate_report(stats):
    report = []

    report.append(HEADER)
    report.append("")
    report.append(f"Total files: {stats['total_files']}")
    report.append(f"Extensions count: {stats['extensions_count']}")
    report.append("")
    report.append("Files by extension:")
    for ext, count in stats["files_by_extension"].items():
        report.append(f"  {ext}: {count}")
    report.append("")
    report.append(FOOTER)

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
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
