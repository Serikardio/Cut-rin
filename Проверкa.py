from pydub import AudioSegment
import os
import tkinter as tk
from tkinter import filedialog

def check_double_spaces_in_file(file_path):
    lines_with_double_spaces = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            if '  ' in line:
                lines_with_double_spaces.append(i)

    if lines_with_double_spaces:
        result_text.insert(tk.END, "Обнаружены строки с двойными пробелами в строках:\n")
        for line_number in lines_with_double_spaces:
            result_text.insert(tk.END, f"Строка {line_number}\n")
        result_text.insert(tk.END, "\n")
    else:
        result_text.insert(tk.END, "Двойных пробелов не обнаружено.\n\n")

def find_lines_with_two_sentences(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if line.count('. ') >= 2:  # Проверяем наличие двух точек с пробелом
                    result_text.insert(tk.END, f"Обнаружены строки с двумя предложениями в строке {line_number}:\n")
                    result_text.insert(tk.END, f"{line.strip()}\n\n")
                    return
            result_text.insert(tk.END, "Двух предложений в одной строке не обнаружено.\n\n")
    except FileNotFoundError:
        result_text.insert(tk.END, "Файл не найден.\n\n")

def find_digits_in_file(file_path):
    try:
        digits_found = []  # Создаем пустой список для хранения найденных цифр
        with open(file_path, 'r', encoding='utf-8') as file:
            line_number = 0
            for line in file:
                line_number += 1
                for char in line:
                    if char.isdigit():
                        digits_found.append((char, line_number))  # Добавляем найденную цифру в список
        if digits_found:
            result_text.insert(tk.END, "Обнаружены цифры в текстовом файле:\n")
            for digit, line_num in digits_found:
                result_text.insert(tk.END, f"Цифра {digit} найдена в строке {line_num}\n")
            result_text.insert(tk.END, "\n")
        else:
            result_text.insert(tk.END, "В файле нет цифр.\n\n")
    except FileNotFoundError:
        result_text.insert(tk.END, "Файл не найден.\n\n")

def check_audio_duration(folder_path):
    found_long_audio = False  # Флаг для проверки наличия файлов длиннее 10 секунд
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.mp3', '.wav', '.ogg', '.flac')):  # Проверяем только аудиофайлы
            file_path = os.path.join(folder_path, file_name)
            audio = AudioSegment.from_file(file_path)

            duration = len(audio) / 1000  # Получаем длительность аудио в секундах

            if duration > 10:
                found_long_audio = True
                result_text.insert(tk.END, f"Обнаружен аудиофайл '{file_name}' длиной более 10 секунд ({duration} сек.)\n")

    if not found_long_audio:
        result_text.insert(tk.END, "Все аудиофайлы менее или равны 10 секунд\n")

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        result_text.delete(1.0, tk.END)  # Очищаем текстовое поле перед выводом новых результатов
        result_text.insert(tk.END, f"Выбран файл для анализа: {os.path.basename(file_path)}\n\n")
        check_double_spaces_in_file(file_path)
        find_lines_with_two_sentences(file_path)
        find_digits_in_file(file_path)

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        result_text.delete(1.0, tk.END)  # Очищаем текстовое поле перед выводом новых результатов
        result_text.insert(tk.END, f"Выбрана папка для анализа: {folder_path}\n\n")
        check_audio_duration(folder_path)

# Создаем графический интерфейс
root = tk.Tk()
root.title("Анализ текстов и аудио")

file_button = tk.Button(root, text="Выбрать текстовый файл для анализа", command=browse_file)
file_button.pack(pady=10)

folder_button = tk.Button(root, text="Выбрать папку с аудиофайлами для анализа", command=browse_folder)
folder_button.pack(pady=10)

result_text = tk.Text(root, height=25, width=100)
result_text.pack(pady=10)
root.mainloop()