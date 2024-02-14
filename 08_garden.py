#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)



# выведите на консоль все виды цветов
# TODO здесь ваш код
print(garden_set)
print(meadow_set)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print(" ".join(garden_set & meadow_set))

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
for flower in garden_set:
    if flower not in meadow_set:
        print(flower, end=" ")
print()
# print(all_flower)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
for flower in meadow_set:
    if flower not in garden_set:
        print(flower, end=" ")
print()