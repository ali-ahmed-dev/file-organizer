from pathlib import Path
# import shutil
# import datetime


def organize_by_extension(folder):
    pass


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
