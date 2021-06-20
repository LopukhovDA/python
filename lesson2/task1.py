"""
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""


# Создадим функцию для определения и вывода типа результата выражений

def type_of_expression(expression):
    print(str(type(expression))[8:-2])


type_of_expression(15 * 3)
type_of_expression(15 / 3)
type_of_expression(15 // 2)
type_of_expression(15 ** 2)

# Проверка других типов

type_of_expression('15')
type_of_expression([1, '3d'])
