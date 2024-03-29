import re

def remove_numbers_from_beginning(file_path):
    # Открываем файл для чтения
    with open(file_path, 'r', encoding='utf-8') as file:
        # Читаем все строки из файла
        lines = file.readlines()

    # Паттерн для поиска цифр в начале строк и следующих за ними символов
    pattern = re.compile(r'^\d+\S*\s*')

    # Удаляем цифры из начала каждой строки
    modified_lines = [pattern.sub('', line) for line in lines]

    # Открываем файл для записи и записываем измененные строки
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

# Пример использования функции для удаления цифр из начала строк в файле "example.txt"
remove_numbers_from_beginning("bookaboutai_rus.txt")