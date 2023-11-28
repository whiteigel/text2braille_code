from braille_dict import *

BRAILLE_DICT = BRAILLE_DICT

input_string = input(str('Введите слово: '))
def convert_to_braille(message, dictionary):
    message = message.upper()
    braille_message = ''
    for char in message:
        if char in dictionary:
            braille_message += dictionary[char] + ' '
        else:
            return "Неподдерживаемый язык"
    return braille_message.strip()

braille_message = convert_to_braille(input_string, BRAILLE_DICT)
print("Сообщение:", braille_message)