from pathlib import Path
import shutil
from datetime import datetime

#Comment

SUPPORTED_TYPES = {
    "pdf",
    "txt",
    "png",
    "jpg",
    "jpeg",
    "csv",
    "py",
    "html",
    "docx"
}

def organize_by_type(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("Error: Folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: Path is not a folder.")
        return
    
    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        print("Folder contains no files.")
        return

    for file in files:
       

            extension = file.suffix[1:]


            if extension == "":
                extension = "no_extension"

            if extension not in SUPPORTED_TYPES and extension != "no_extension":
                print(f"Unsupported file type: {extension}")
                continue

            new_folder = folder / extension
            new_folder.mkdir(exist_ok=True)

            destination = new_folder / file.name

            if destination.exists():
                print(f"Skipping {file.name}: file already exists.")
            else:
                try:
                    shutil.move(file, destination)
                    print(f"Moved {file.name} → {new_folder.name}/")
                except Exception as e:
                    print(f"Could not move {file.name}: {e}")
                


def organize_by_date(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("Error: Folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: Path is not a folder.")
        return
    
    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        print("Folder contains no files.")
        return

    for file in files:
    


            timestamp = file.stat().st_mtime
            date = datetime.fromtimestamp(timestamp)


            folder_name = date.strftime("%Y-%m")

            new_folder = folder / folder_name
            new_folder.mkdir(exist_ok=True)

            destination = new_folder / file.name

            if destination.exists():
                print(f"Skipping {file.name}: file already exists.")
            else:
                try:
                    shutil.move(file, destination)
                    print(f"Moved {file.name} → {new_folder.name}/")
                except Exception as e:
                    print(f"Could not move {file.name}: {e}")
                


def organize_by_keyword(folder_path, keyword):
    folder = Path(folder_path)
    moved = 0
    if not folder.exists():
        print("Error: Folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: Path is not a folder.")
        return

    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        print("Folder contains no files.")
        return

    keyword_folder = folder / keyword
    keyword_folder.mkdir(exist_ok=True)

    

    for file in files:
       

            if keyword.lower() in file.name.lower():

                destination = keyword_folder / file.name

                if destination.exists():
                    print(f"Skipping {file.name}: file already exists.")
                else:
                    try:
                        shutil.move(file, destination)
                        moved += 1
                        print(f"Moved {file.name} → {keyword}/")
                    except Exception as e:
                        print(f"Could not move {file.name}: {e}")
                    

    if moved == 0:
        print("No files matched that keyword.")

def main():
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
        print("Error: Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()