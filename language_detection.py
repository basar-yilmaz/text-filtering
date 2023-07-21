import os
from langdetect import detect_langs
import tkinter as tk
from tkinter import filedialog

def detect_language(text):
    # Detect the language probabilities using detect_langs
    lang_probabilities = detect_langs(text)

    # Find the probability for English
    if (lang_probabilities[0].lang == 'en'):
        english_probability = lang_probabilities[0].prob
    else:
        return f'Non-English with prob: {lang_probabilities[0]}'

    # If English probability is lower than 75%, classify as Non-English
    if english_probability < 0.75:
        return f'Non-English with prob: {english_probability}'
    else:
        return 'en'
    
def detect_non_english_files(folder_path):  
    non_english_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                detected_language = detect_language(text)
                if detected_language != 'en':
                    non_english_files.append(f"{file_name}, lang: {detected_language}")
    return non_english_files

def choose_folder():
    root = tk.Tk()
    root.withdraw() 
    folder_path = filedialog.askdirectory(title="Select the folder containing txt files")
    return folder_path

if __name__ == "__main__":
    folder_path = choose_folder()
    if not folder_path:
        print("No folder selected.")
    else:
        non_english_files = detect_non_english_files(folder_path)
        if len(non_english_files) > 0:
            print(f"{len(non_english_files)} non-eng files detected:")
            for file_name in non_english_files:
                print(file_name)
        else:
            print("No non-eng files detected.")
