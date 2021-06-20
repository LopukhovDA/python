"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
"""

num_translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                      'five': 'пять', 'six': 'шесть', 'seven': 'семь',
                      'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(num):
    print(num_translate_dict.get(num))


# Выборочная проверка

num_translate('one')
num_translate('three')
num_translate('five')
num_translate('seven')
num_translate('nine')

# Проверим вывод None при невозможности перевести

num_translate('e')
num_translate(42)
