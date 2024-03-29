import re
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

# Проверка работы функции num_to_words с различными входными значениями
test_numbers = [25]
for num in test_numbers:
    print(f"{num}: {num_to_words(num)}")


# Функция для замены чисел в тексте
def replace_numbers_in_text(text):
    # Регулярное выражение для поиска чисел
    pattern = r'\b\d+\b'
    # Заменяем числа в тексте с помощью функции modified_num_to_words
    modified_text = re.sub(pattern, lambda x: modified_num_to_words(x.group()), text)
    return modified_text

# Открыть файл для чтения
input_file_path = 'connection_kaz-a-1.txt'
output_file_path = 'connection_kaz-a-1.txt'
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    text = input_file.read()

# Заменить числа в тексте
modified_text = replace_numbers_in_text(text)

# Записать измененный текст обратно в файл
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(modified_text)

print("Числа в файле успешно заменены и сохранены в новый файл.")
