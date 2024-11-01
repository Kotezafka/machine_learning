"""Задача 2
Расчет доверительного интервала

У вас есть данные возрастов репрезентативной выборки сотрудников компании,
которые генерируются кодом (см. окно ввода ответа).

Рассчитайте промежуток, в котором будет находиться среднее генеральной совокупности с 99% надежностью?
Ответом должен выступать кортеж. Сохраните его в переменную ci"""

import random
import scipy.stats as st
import numpy as np


random.seed(10)
ages = []
for i in range(0, 30):
    n = random.randint(18, 75)
    ages.append(n)

# Рассчитываем доверительный интервал для среднего
conf_level = 0.99

# Стандартная ошибка среднего
std_err = st.sem(ages)

ci = st.t.interval(
    confidence=conf_level, df=len(ages) - 1, loc=np.mean(ages), scale=std_err
)

print(f"Доверительный интервал: {ci}")
