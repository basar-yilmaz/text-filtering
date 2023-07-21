import os
from utils import choose_folder

def check_word_count_in_files(folder_path, min_word_count):
    files_below_word_count = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                word_count = len(text.split())
                if word_count <= min_word_count:
                    files_below_word_count.append(file_name)
    return files_below_word_count

def check_text_length_in_files(folder_path, min_text_length):
    files_below_text_length = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                text_length = len(text)
                if text_length <= min_text_length:
                    files_below_text_length.append(file_name)
    return files_below_text_length



if __name__ == "__main__":
    preference = input("[1] Word count \n[2] Text Length\nEnter your preference:")
    if (preference == "1"):
        min_word_count = int(input("Enter the min word count: "))
        folder_path = choose_folder()
        if not folder_path:
            print("No folder selected.")
        else:
            files_below_word_count = check_word_count_in_files(folder_path, min_word_count)
            if len(files_below_word_count) > 0:
                print(f"Files with {min_word_count} or fewer words:")
                for file_name in files_below_word_count:
                    print(file_name)
            else:
                print(f"All files have more than {min_word_count} words in the selected folder.")
    elif (preference == "2"):
        min_text_length = int(input("Enter the min text length: "))
        folder_path = choose_folder()
        if not folder_path:
            print("No folder selected.")
        else:
            files_below_text_length = check_text_length_in_files(folder_path, min_text_length)
            if len(files_below_text_length) > 0:
                print(f"Files with {min_text_length} or fewer length:")
                for file_name in files_below_text_length:
                    print(file_name)
            else:
                print(f"All files have more than {min_text_length} length in the selected folder.")
