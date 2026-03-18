import os
import shutil
from datetime import datetime

# Folder to organize
SOURCE_FOLDER = input("Enter the path of the folder to organize: ")

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp"]
}

def get_category(file_ext):
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def make_unique(dest_path):
    base, ext = os.path.splitext(dest_path)
    counter = 1
    while os.path.exists(dest_path):
        dest_path = f"{base} ({counter}){ext}"
        counter += 1
    return dest_path

def organize():
    if not os.path.exists(SOURCE_FOLDER):
        print("❌ Folder not found!")
        return

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            category = get_category(ext)

            category_folder = os.path.join(SOURCE_FOLDER, category)
            os.makedirs(category_folder, exist_ok=True)

            # Optional rename with date
            created_time = os.path.getctime(file_path)
            date_str = datetime.fromtimestamp(created_time).strftime("%Y-%m-%d")

            new_name = f"{date_str}_{file}"
            dest_path = os.path.join(category_folder, new_name)

            dest_path = make_unique(dest_path)

            shutil.move(file_path, dest_path)
            print(f"✅ Moved: {file} → {category}/")

    print("\n🎉 Organization Complete!")

if __name__ == "__main__":
    organize()