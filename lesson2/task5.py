"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
* Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если,
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

* Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
* Создать новый список, содержащий те же цены, но отсортированные по убыванию.
* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию,
написав минимум кода?
"""

prices = [57.8, 46.51, 97, 35.01, 89.8, 100.9, 15, 68.5, 88, 14.7, 32, 199.99]


# Напишем функцию для создания требуемой строки

def format_prices(prices_list):
    result_string = ''
    for price in prices_list:
        result_string += f'{int(price)} руб {str(((price - int(price)) * 100).__round__()).zfill(2)} коп, '
    result_string = result_string[:-2]
    return result_string


# Выведем строку и id списка

print(format_prices(prices), '\n', id(prices))

# Выведем строку из отсортированного списка (по возрастанию) и его id

print(format_prices(sorted(prices)), '\n', id(sorted(prices)))

# Для проверки выведем строку из исходного списка цен

print(format_prices(prices))

# Сортировка по убыванию, создание нового списка

rev_prices = sorted(prices, reverse=True)
print(format_prices(rev_prices))

# Выведем 5 самых дорогих товаров (цен)

print(format_prices(sorted(prices)[-5:]))
