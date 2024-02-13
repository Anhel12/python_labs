#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}
def result(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    
# TODO здесь заполнение словаря
for keys in sites.keys():
    distances[keys] = {}
    for keys1 in sites.keys():
        if keys1 != keys:
            distances[keys][keys1] = result(sites[keys], sites[keys1])
print(distances)




