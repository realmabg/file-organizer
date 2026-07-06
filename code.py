from pathlib import Path
import shutil
from datetime import datetime

#Comment

def organize_by_type(folder_path):
    folder = Path(folder_path)

    for file in folder.iterdir():
        if file.is_file():

            extension = file.suffix[1:]

            if extension == "":
                extension = "no_extension"

            new_folder = folder / extension
            new_folder.mkdir(exist_ok=True)

            shutil.move(file, new_folder / file.name)

            print(f"Moved {file.name} → {extension}/")


def organize_by_date(folder_path):
    folder = Path(folder_path)

    for file in folder.iterdir():
        if file.is_file():


            timestamp = file.stat().st_mtime
            date = datetime.fromtimestamp(timestamp)


            folder_name = date.strftime("%Y-%m")

            new_folder = folder / folder_name
            new_folder.mkdir(exist_ok=True)

            shutil.move(file, new_folder / file.name)

            print(f"Moved {file.name} → {folder_name}/")


def organize_by_keyword(folder_path, keyword):
    folder = Path(folder_path)

    keyword_folder = folder / keyword
    keyword_folder.mkdir(exist_ok=True)

    for file in folder.iterdir():
        if file.is_file():

            if keyword.lower() in file.name.lower():

                shutil.move(file, keyword_folder / file.name)

                print(f"Moved {file.name} → {keyword}/")

print("File Organizer")
print("1. Organize by file type")
print("2. Organize by date")
print("3. Organize by keyword")

choice = input("Choose option: ")

folder = input("Enter folder path: ")


if choice == "1":
    organize_by_type(folder)

elif choice == "2":
    organize_by_date(folder)

elif choice == "3":
    keyword = input("Enter keyword: ")
    organize_by_keyword(folder, keyword)

else:
    print("Invalid option")