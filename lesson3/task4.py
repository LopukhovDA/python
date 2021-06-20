"""
4. Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы.
Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus_adv(*args):
    thesaurus_dict_adv = {}
    for name_surname in args:
        name, surname = name_surname.split()
        if surname.istitle() and surname.isalpha():
            if not (surname[0] in thesaurus_dict_adv.keys()):
                thesaurus_dict_adv[surname[0]] = {}
            if name.istitle() and name.isalpha():
                if not (name[0] in thesaurus_dict_adv[surname[0]].keys()):
                    thesaurus_dict_adv[surname[0]][name[0]] = []
                thesaurus_dict_adv[surname[0]][name[0]].append(name_surname)
    return thesaurus_dict_adv


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
print(sorted(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева").items()))
