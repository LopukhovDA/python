"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"',
'+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""


# Напишем функцию для добавления кавычек в список

def add_quotes(index, some_list):
    some_list.insert(index, '"')
    some_list.insert(index + 2, '"')
    index += 1
    return index


our_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0

while i != len(our_list):
    if our_list[i][0] in ['+', '-'] and our_list[i][1:].isdigit():
        our_list[i] = our_list[i][0] + our_list[i][1:].zfill(2)
        i = add_quotes(i, our_list)
    elif our_list[i].isdigit():
        our_list[i] = our_list[i].zfill(2)
        i = add_quotes(i, our_list)
    i += 1

print(our_list)

# Соберем строку из списка

result_string = ' '.join(our_list)
result_string = ' ' + result_string + ' '

# Теперь нужно избавиться от пробелов между кавычками, алгоритм простой:
# если кавычки открывающиеся значит удаляем пробел после них, если закрывающиеся - до.

i = 0

while i < result_string.count('"'):
    if not i % 2:
        result_string = result_string.replace(' " ', ' "', 1)
    else:
        result_string = result_string.replace(' " ', '" ', 1)
    i += 1

result_string = result_string.strip()
print(result_string)

# Шуточная проверка результата

print('УРА!' if result_string == 'в "05" часов "17" минут температура воздуха была "+05" градусов'
      else 'ОО НЕТ!')
