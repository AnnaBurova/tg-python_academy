# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:02:51 2024

@author: KoreAnna

@title: Сортировка словаря по значениям

Распространена практика использования словарей в качестве таблиц для хранения
данных. Сортировка данных словаря по значениям ключей, а не самим ключам,
нередко ставит в тупик. Задача решается довольно просто при помощи аргумента
key для указания функции, которая будет вызываться на каждом элементе до
сравнения.
"""

d = {'apples': 40, 'oranges': 80, 'bananas': 70}
result = sorted(d, key=d.get)

print(result)
# ['apples', 'bananas', 'oranges']