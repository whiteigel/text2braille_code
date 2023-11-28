from braille_dict import *

input_string = input(str('Введите слово: '))
def convert_to_braille(message, braille_dict):
    message = message.upper()
    braille_message = ''
    for char in message:
        if char in braille_dict:
            braille_message += braille_dict[char] + ' '
        else:
            return "Неподдерживаемый язык"
    return braille_message.strip()

braille_message = convert_to_braille(input_string, braille_dict)
print("Сообщение:", braille_message)