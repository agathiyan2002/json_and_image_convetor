import os
import shutil

def organize_folders(source_folder, download_folder):
    with_image_folder = os.path.join(download_folder, 'with_image')
    without_image_folder = os.path.join(download_folder, 'without_image')

    # Create folders if they don't exist
    os.makedirs(with_image_folder, exist_ok=True)
    os.makedirs(without_image_folder, exist_ok=True)

    # Get a list of files in the source folder
    files = os.listdir(source_folder)

    # Organize files into with_image and without_image folders
    for file in files:
        if file.endswith('.json'):
            json_path = os.path.join(source_folder, file)
            image_path = os.path.join(source_folder, file.replace('.json', '.jpg'))

            if os.path.exists(image_path):
                shutil.copy(image_path, with_image_folder)
                shutil.copy(json_path, with_image_folder)
            else:
                shutil.copy(json_path, without_image_folder)

def extract_image_only(source_folder, download_folder):
    with_json_folder = os.path.join(download_folder, 'with_json')
    without_json_folder = os.path.join(download_folder, 'without_json')

    # Create folders if they don't exist
    os.makedirs(with_json_folder, exist_ok=True)
    os.makedirs(without_json_folder, exist_ok=True)

    # Get a list of files in the source folder
    files = os.listdir(source_folder)

    # Extract only image files without corresponding JSON files
    for file in files:
        if file.endswith('.jpg'):
            image_path = os.path.join(source_folder, file)
            json_path = os.path.join(source_folder, file.replace('.jpg', '.json'))

            if not os.path.exists(json_path):
                shutil.copy(image_path, without_json_folder)
            else:
                shutil.copy(image_path, with_json_folder)

if __name__ == "__main__":
    source_folder = "/home/alan/Documents/test/test sc 2/gt/"  # Change this to the path of your source folder
  #  download_folder = "/home/alan/Downloads/"  # Change this to the path of your download folder
    download_folder=source_folder

   # choice = int(input("Enter 1 to organize folders, 2 to extract image only: "))
    choice=2

    if choice == 1:
        organize_folders(source_folder, download_folder)
    elif choice == 2:
        extract_image_only(source_folder, download_folder)
    else:
        print("Invalid choice. Please enter either 1 or 2.")
