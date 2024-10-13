# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:20:34 2024

@author: KoreAnna

@title: Нахождение наиболее частых элементов списка

Если необходимо найти несколько наиболее часто повторяющихся значений,
лучше воспользоваться счетчиком Counter из библиотеки collections.

Метод Counter.most_common(x) возвращает x кортежей, в которых
первое значение – элемент, а второе – количество его повторений.
"""

from collections import Counter
a = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b', 'd', 'e', 'a']
cnt = Counter(a)
result = cnt.most_common(3)

print(result)
# [('b', 4), ('a', 3), ('c', 2)]
