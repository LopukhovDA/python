"""
Задача №1
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""
# Константы
MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
YEAR = DAY * 365

# Попросим пользователя ввести продолжительность времени
while True:
    duration = int(input('Введите продолжительность времени в секундах: '))
    if duration < 0 or duration >= YEAR:
        print('Введеное Вами число не в требуемом диапазоне: от 0 до 31536000. Попробуйте еще раз')
        continue
    elif duration < MINUTE:
        print(f'до минуты: {MINUTE-duration} сек')
    elif duration < HOUR:
        print(f'до часа: {(HOUR - duration) // MINUTE} мин {(HOUR - duration) % MINUTE} сек')
    elif duration < DAY:
        print(f'до суток: {(DAY - duration) // HOUR} час {((DAY - duration) % HOUR) // MINUTE} мин {((DAY - duration) % HOUR) % MINUTE} сек')
    elif duration < YEAR:
        print(f'до года: {(YEAR - duration) // DAY} сут {((YEAR - duration) % DAY) // HOUR} час {(((YEAR - duration) % DAY) % HOUR) // MINUTE} мин {(((YEAR - duration) % DAY) % HOUR) % MINUTE} сек')
    break
