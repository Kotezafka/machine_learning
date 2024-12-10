"""Задача 3
Алгоритм DBSCAN

В этом задании вы выполните кластеризацию на примере случайного набора данных, применив
алгоритм DBSCAN, и вычислите силуэтный коэффициент кластеризации.

Для вас созданы искусственные данные с помощью модуля sklearn.datasets.make_blobs() с
количеством кластеров, достаточным для проведения кластеризации.

Что нужно сделать:
1.	Импортируйте модуль sklearn.cluster.DBSCAN для реализации алгоритма DBSCAN

2.	Реализуйте функцию, которая на вход принимает значения eps и min_samples, использует
    алгоритм DBSCAN для кластеризации данных и вычисляет силуэтный коэффициент для
    каждой точки. Функция должна возвращать средний силуэтный коэффициент для всех точек

3.	Напишите цикл, который перебирает различные значения eps и min_samples, и для каждой
    комбинации вызывает функцию из пункта 1, сохраняя оптимальные значения eps и min_samples
    с наибольшим средним силуэтным коэффициентом

4.	Выведите найденные оптимальные значения eps и min_samples, а также средний
    силуэтный коэффициент для них"""

from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score


X, y = make_blobs(n_samples=1000, centers=3, random_state=42)


def dbscan_silhouette(eps, min_samples):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
    labels = db.labels_
    if len(set(labels)) > 1:
        return silhouette_score(X, labels)
    else:
        return -1


best_eps, best_min_samples, best_silhouette = None, None, -1

for eps in [0.1, 0.5, 1]:
    for min_samples in [5, 10, 20]:
        silhouette = dbscan_silhouette(eps, min_samples)
        if silhouette > best_silhouette:
            best_silhouette = silhouette
            best_eps = eps
            best_min_samples = min_samples

print([best_eps, best_min_samples, best_silhouette])

print(best_min_samples == 10)
print(best_silhouette == 0.8229345005215011)
