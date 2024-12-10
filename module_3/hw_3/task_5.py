"""Задача 5
Составление рекомендаций по матрице рейтингов

В этом задании вы будете использовать матрицу рейтингов для составления
предсказания пользовательских предпочтений.

Что нужно сделать:
1. Используя библиотеку Scikit-learn, разложите матрицу рейтингов на
    сингулярные значения с помощью метода SVD

2. Для выбранного пользователя user_id = 2 из матрицы рейтингов предскажите
    рейтинг для товара item_id = 4 с точностью до десятых на основе
    полученных после разложения матрицы сингулярных значений"""

import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform


np.random.seed(42)
X = np.random.rand(100, 5)

tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.show()
dist = pdist(X_tsne, "sqeuclidean")
sum_dist = np.sum(squareform(dist))
result = round(sum_dist, 2)

print(result)

print(result == 413138.06)
