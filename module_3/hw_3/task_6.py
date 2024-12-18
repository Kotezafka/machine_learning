"""Задача 6
Исследование факторов успеха продаж

В этом задании вы выполните анализ данных о продажах и выявите основные
факторы, влияющие на успешность продаж.

Вам дан набор данных, содержащий информацию о продажах различных видов одежды в различных
регионах за последний год. Набор данных представлен в виде матрицы размером 1000x10, где
каждая строка соответствует отдельной продаже, а каждый столбец — определенному атрибуту продажи.

Ваша задача:
1.	При помощи библиотеки Scikit-learn выполнить алгоритм PCA для
    сокращения размерности данных до 3-х компонент

2.	Определить путем анализа факторной нагрузки, какие три фактора
    первой главной компоненты являются наиболее важными факторами,
    влияющими на успешность продаж

3.	Округлить сумму весов этих наиболее важных факторов до двух
    знаков после запятой и предоставить ее в качестве ответа"""

import numpy as np
from sklearn.decomposition import PCA


np.random.seed(42)

# Создание искусственных данных
data = np.random.rand(1000, 10)

# Выполнение алгоритма PCA для сокращения размерности до 3-х компонент
pca = PCA(n_components=3)
pca.fit(data)
transformed_data = pca.transform(data)

# Анализ факторной нагрузки
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# Выбор наиболее важных факторов
most_important_factors = np.argsort(np.abs(loadings[:, 0]))[::-1][:3]

# Вычисление суммы весов наиболее важных факторов
sum_weights = np.sum(np.abs(loadings[most_important_factors, 0]))

# Округление ответа до двух знаков после запятой
sum_weights_rounded = round(sum_weights, 2)

print(sum_weights_rounded)

print(sum_weights_rounded == 0.47)
