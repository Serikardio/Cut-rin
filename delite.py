def process_file(file_path, characters_to_remove):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        # Удаление пробелов в начале и конце строки
        processed_line = line.strip()

        # Удаление указанных символов
        for char_to_remove in characters_to_remove:
            processed_line = processed_line.replace(char_to_remove, '')

        # Замена двойных пробелов на одинарные
        processed_line = ' '.join(processed_line.split())

        processed_lines.append(processed_line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(processed_lines))

file_path = 'bookaboutai_rus.txt'
symbols_to_remove = ['(', ')', '"', '“', '”', ' –', '»', '«', ' -', '— ', '– ']  # Укажите символы, которые нужно удалить

process_file(file_path, symbols_to_remove)
