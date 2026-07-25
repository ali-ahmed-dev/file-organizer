from pathlib import Path
# import shutil
# import datetime


def organize_by_extension(folder):
    extensions = {}
    for file in folder.glob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if not ext:
                ext = "no_extension"
            else:
                ext = ext[1:]
            if ext in extensions:
                extensions[ext].append(file.name)
            else:
                extensions[ext] = [file.name]

    for extension in extensions:
        new_folder = folder / extension
        new_folder.mkdir(exist_ok=True)
        # Temporary test: display created folders
        print(extension)


def generate_report(stats, count):
    pass


def main():
    print("Welcome to the File Organizer Tool")
    try:
        folder_path = input("Enter the folder path to organize: ")
        folder = Path(folder_path)
        if folder.exists() and folder.is_dir():
            organize_by_extension(folder)
        else:
            print("The folder does not exist or is not a directory.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
