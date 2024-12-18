"""Задача 1
Линейная регрессия

Вам даны два вектора признаков и вектор целевой переменной. Постройте
модель линейной регрессии и выведите на экран вектор весов модели
для факторов x1 и x2 в формате массива numpy"""

import numpy as np
from sklearn.linear_model import LinearRegression

x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([6, 7, 8, 9, 10])
y = np.array([11, 12, 13, 14, 15])

X = np.column_stack((x1, x2))

reg = LinearRegression()
reg.fit(X, y)

np.array(reg.coef_)
print(reg.coef_[0])
print(reg.coef_[1])
