"""Задача 1
Метод k-средних

В вашем распоряжении имеются данные о различных продуктах
в интернет-магазине. Задача — сгруппировать их на три кластера
с помощью алгоритма k-means. Осуществите алгоритм кластеризации
и выведите центроиды кластеров"""

import numpy as np
from sklearn.cluster import KMeans


np.random.seed(42)
X = np.random.rand(100, 2)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

y_pred = kmeans.predict(X)
center_coords = kmeans.cluster_centers_
print(center_coords)
