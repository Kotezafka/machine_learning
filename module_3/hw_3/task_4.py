"""Задача 4
Метод главных компонент

Используя библиотеку sklearn.decomposition.PCA, найдите 3 главных компоненты
для заданных данных. Рассчитайте долю объясненной дисперсии каждой главной
компоненты. Для этого можно воспользоваться атрибутом explained_variance_ratio_
объекта PCA и вывести получившийся вектор"""

import numpy as np
from sklearn.decomposition import PCA


np.random.seed(42)
X = np.random.rand(100, 5)

pca = PCA(n_components=3)
pca.fit(X)
loadings = pca.explained_variance_ratio_

print(loadings)

print(round(loadings[0], 3) == 0.289)
print(round(loadings[1], 3) == 0.236)
