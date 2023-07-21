import os
from utils import choose_folder


def find_files_with_intersection(folder_path, should_have_words, should_not_have_words):
    matching_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                if all(word.lower() in text for word in should_have_words) and not any(word.lower() in text for word in should_not_have_words):
                    matching_files.append(file_name)
    return matching_files


if __name__ == "__main__":
    should_have_words_input = input("Enter words that should be present in the files (comma-separated list): ")
    should_not_have_words_input = input("Enter words that should not be present in the files (comma-separated list): ")
    should_have_words = [word.strip() for word in should_have_words_input.split(",")]
    should_not_have_words = [word.strip() for word in should_not_have_words_input.split(",")]

    folder_path = choose_folder()
    if not folder_path:
        print("No folder selected.")
    else:
        matching_files = find_files_with_intersection(folder_path, should_have_words, should_not_have_words)
        if len(matching_files) > 0:
            print(f"Files containing all of {should_have_words} but none of {should_not_have_words}:")
            for file_name in matching_files:
                print(file_name)
        else:
            print(f"No files found with the specified criteria in the selected folder.")
