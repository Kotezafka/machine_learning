"""Задача 1
Базовые операции с массивами NumPy (Часть 1)

У вас есть два одномерных массива:
array = np.arange(10) ** 4 — массив платежей по играм из сервиса;
array_2 = np.arange(10) ** 3 — массив платежей по подпискам в сервисе.

Выполните последовательно следующие задания применительно к исходным массивам:
1.	Определите общую сумму дохода сразу по двум потокам. Для этого сначала сложите полученные массивы,
    после чего получите сумму всех элементов. Результат сохраните в переменную array_sum.

2.	Вычислите, насколько больше денег принесла продажа игр за указанный период.
    Результат сохраните в переменную array_difference.

3.	Сохраните 2-й элемент массива по платежам игр в переменную game_payments2.

4.	Сохраните последний элемент массива по платежам подписок в переменную subscription_last"""

import numpy as np

array = np.arange(10) ** 4
array_2 = np.arange(10) ** 3

print(f"Массив платежей по играм из сервиса:\n{array}\n")
print(f"Массив платежей по подпискам в сервисе:\n{array_2}\n")

array_sum = sum(array + array_2)
array_difference = sum(array) - sum(array_2)

print(f"Общая сумма дохода по двум потокам:\n{array_sum}\n")
print(
    f"На {array_difference} денег больше принесла продажа игр, чем продажа подписок за указанный период.\n"
)

game_payments2 = array[1]
subscription_last = array_2[-1]

print(f"2-й элемент массива по платежам игр:\n{game_payments2}\n")
print(f"Последний элемент массива по платежам подписок:\n{subscription_last}")