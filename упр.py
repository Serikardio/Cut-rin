# Открываем исходный файл для чтения
x = "bookaboutai_rus.txt"
with open(x, 'r', encoding='utf-8') as input_file:
    # Читаем содержимое файла
    text = input_file.read()

# Разделяем текст по запятым, точкам и знакам вопроса и добавляем переводы строк
text_with_newlines = text.replace('.', '.\n').replace(',', ',\n').replace('?', '?\n').replace(';', ';\n').replace(':', ':\n')

# Открываем новый файл для записи
with open(x, 'w', encoding='utf-8') as output_file:
    # Записываем обновленный текст в новый файл
    output_file.write(text_with_newlines)

print("Процесс завершен.")

