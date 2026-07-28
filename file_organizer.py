from pathlib import Path
import shutil
# import datetime

HEADER = "=" * 50 + "\n                 FILE ORGANIZER\n" + "=" * 50
FOOTER = "=" * 50 + "\n                 END OF REPORT\n" + "=" * 50


def organize_by_extension(folder):
    extensions = {}
    stats = {}
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
    return stats


def generate_report(stats):
    pass


def main():
    print("Welcome to the File Organizer Tool")
    try:
        folder_path = input("Enter the folder path to organize: ")
        folder = Path(folder_path)
        if folder.exists() and folder.is_dir():
            stats = organize_by_extension(folder)
            generate_report(stats)
        else:
            print("The folder does not exist or is not a directory.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
