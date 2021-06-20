"""
2. Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""

num_translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                      'five': 'пять', 'six': 'шесть', 'seven': 'семь',
                      'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(num):
    if num.istitle() and num.lower() in num_translate_dict.keys():
        print(num_translate_dict.get(num.lower()).capitalize())
    else:
        print(num_translate_dict.get(num))


# Проверим работу функции
num_translate_adv('Two')
num_translate_adv('one')
num_translate_adv('Nine')

# Проверим вывод None
num_translate_adv('j')
num_translate_adv('Joker')
