"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов,
взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=1, allow_repeat=True):
    """
    this function get the jokes
    :param n: count of jokes
    :param allow_repeat: is flag, set allow repeat words in jokes, default = True
    :return: print the jokes
    """
    nouns_f = nouns[:]
    adverbs_f = adverbs[:]
    adjectives_f = adjectives[:]
    if not allow_repeat and n > 5:
        print('Извините, вы требуете невозможного')
        return False
    jokes = []
    for i in range(n):
        if allow_repeat:
            jokes.append(f'{random.choice(nouns_f)} {random.choice(adverbs_f)} {random.choice(adjectives_f)}')
        else:
            noun, adverb, adjective = random.choice(nouns_f), random.choice(adverbs_f), random.choice(adjectives_f)
            jokes.append(f'{noun} {adverb} {adjective}')
            nouns_f.remove(noun)
            adverbs_f.remove(adverb)
            adjectives_f.remove(adjective)
    print(jokes)


get_jokes(3)
get_jokes(4, allow_repeat=False)
get_jokes(allow_repeat=False, n=5)
get_jokes(6)
get_jokes(allow_repeat=False, n=6)
