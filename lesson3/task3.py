"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей
буквы. Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus(*args, sort=False):
    thesaurus_dict = {}
    for name in args:
        if name.istitle() and name.isalpha():
            if not (name[0] in thesaurus_dict.keys()):
                thesaurus_dict[name[0]] = []
            thesaurus_dict[name[0]].append(name)
    if sort:
        return sorted(thesaurus_dict.items())
    else:
        return thesaurus_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Максим", "Павел"))
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Максим", "Павел", sort=True))
