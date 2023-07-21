from utils import choose_folder
import os
import hashlib
from collections import defaultdict

def compute_hash(file_path):
    # Compute the SHA-256 hash of the file's content.
    with open(file_path, 'rb') as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def find_duplicates(folder_path):
    hash_to_files = defaultdict(list)

    # Get a list of all txt files in the directory.
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    # Group files with the same hash value together.
    for file in txt_files:
        file_path = os.path.join(folder_path, file)
        file_hash = compute_hash(file_path)
        hash_to_files[file_hash].append(file)

    # Print files with the same content.
    duplicates_found = False
    for files_with_same_hash in hash_to_files.values():
        if len(files_with_same_hash) > 1:
            duplicates_found = True
            print("Files with the same content:")
            print(", ".join(files_with_same_hash))
            print()

    if not duplicates_found:
        print("No files with the same content found.")

def find_delete_duplicates(folder_path, delete_duplicates=True):
    hash_to_files = defaultdict(list)

    # Get a list of all txt files in the directory.
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    # Group files with the same hash value together.
    for file in txt_files:
        file_path = os.path.join(folder_path, file)
        file_hash = compute_hash(file_path)
        hash_to_files[file_hash].append(file)

    # Delete duplicate files, keeping only the first occurrence.
    deleted_files = set()
    duplicate_count = 0
    for files_with_same_hash in hash_to_files.values():
        if len(files_with_same_hash) > 1:
            duplicate_count += len(files_with_same_hash) - 1
            files_to_delete = files_with_same_hash[1:]
            for file_to_delete in files_to_delete:
                file_path_to_delete = os.path.join(folder_path, file_to_delete)
                if delete_duplicates:
                    os.remove(file_path_to_delete)
                    deleted_files.add(file_to_delete)

    if delete_duplicates:
        print(f"{duplicate_count} duplicate files found and deleted.")
        if deleted_files:
            print("Deleted files:")
            print(", ".join(deleted_files))
        else:
            print("No duplicate files deleted.")
    else:
        print(f"{duplicate_count} duplicate files found but not deleted.")


if __name__ == "__main__":

    folder_path = choose_folder()
    if not folder_path:
        print("No folder selected.")
        exit()
    user_in = int(input("[1] to find duplicates\n[2] to # of duplicates\n[3] to delete duplicates\nEnter your preference: "))
    
    if (user_in == 1):
        find_duplicates(folder_path)
    
    elif (user_in == 2):
        find_delete_duplicates(folder_path, delete_duplicates=False)
        
    elif (user_in == 3):
        find_delete_duplicates(folder_path, delete_duplicates=True)

