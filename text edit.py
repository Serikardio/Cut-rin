import re
import tkinter as tk
from tkinter import filedialog, messagebox

def num_to_words(num):
    # Список числительных для единиц
    units = [
        'бірінші', 'екінші', 'үшінші', 'төртінші', 'бесінші',
        "алтыншы", "жетінші", "сегізінші", "тоғызыншы"
    ]

    # Список числительных для чисел от 10 до 19
    teens = [
        "оныншы", "он бірінші", "он екінші", "он үшінші", "он төртінші",
        "он бесінші", "он алтыншы", "он жетінші", "он сегізінші", "он тоғызыншы"
    ]

    # Список числительных для десятков
    tens = [
        '', '', "жиырма", "отыз", "қырық", "елу",
        "алпыс", "жетпіс", "сексен", "тоқсан"
    ]
    # Дополнение списка tens
    for i in range(1, 10):
        tens.append(units[i - 1] + 'десятая')

    # Исключения для определенных чисел
    exceptions = {
        20: 'жиырмасыншы',
        30: 'отызыншы',
        40: 'қырқыншы',
        50: 'елуінші',
        60: 'алпысыншы',
        70: 'жетпісінші',
        80: 'сексенінші',
        90: 'тоқсаныншы'
    }

    # Проверка наличия исключения
    if num in exceptions:
        return exceptions[num]

    # Проверка на диапазон чисел от 1 до 100
    if num < 1 or num > 100:
        return "Число вне диапазона от 1 до 100"

    # Обработка чисел от 1 до 9
    if num <= 9:
        return units[num - 1]

    # Обработка чисел от 10 до 19
    elif num <= 19:
        return teens[num - 10]

    # Обработка чисел от 20 до 99
    elif num <= 99:
        ten = num // 10
        unit = num % 10
        if unit == 0:
            return tens[ten]
        else:
            return tens[ten] + ' ' + units[unit - 1]

    # Обработка числа 100
    else:
        return "жүзінші"

def modified_num_to_words(word):
    if "-" in word:
        word = word.replace("-", " ")
    if word.isdigit():
        word = num_to_words(int(word))
    return word

def replace_numbers_in_text(text):
    # Регулярное выражение для поиска чисел
    pattern = r'\b\d+\b'
    # Заменяем числа в тексте с помощью функции modified_num_to_words
    modified_text = re.sub(pattern, lambda x: modified_num_to_words(x.group()), text)
    return modified_text

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        # Удаление пробелов в начале и конце строки
        processed_line = line.strip()

        # Замена двойных пробелов на одинарные
        processed_line = ' '.join(processed_line.split())

        processed_lines.append(processed_line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(processed_lines))

def remove_numbers_from_beginning(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines_without_initial_spaces = [line.lstrip() for line in lines]

    with open(file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines_without_initial_spaces)

def select_and_process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        process_file(file_path)
        messagebox.showinfo("Успех", "Файл успешно обработан и сохранен!")

def select_and_remove_numbers():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        remove_numbers_from_beginning(file_path)
        messagebox.showinfo("Успех", "Цифры из начала строк файла успешно удалены!")

def select_and_replace_numbers():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            text = input_file.read()
        modified_text = replace_numbers_in_text(text)
        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if output_file_path:
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(modified_text)
            messagebox.showinfo("Успех", "Числа в файле успешно заменены и сохранены!")

root = tk.Tk()
root.title("Обработка текстовых файлов")

process_button = tk.Button(root, text="Обработать файл", command=select_and_process_file)
process_button.pack(pady=10)

remove_numbers_button = tk.Button(root, text="Удалить цифры из начала строк", command=select_and_remove_numbers)
remove_numbers_button.pack(pady=10)

replace_numbers_button = tk.Button(root, text="Заменить числа в тексте", command=select_and_replace_numbers)
replace_numbers_button.pack(pady=10)

root.mainloop()
