"""Задача 2
Иерархическая кластеризация

В этом задании вы выполните иерархическую кластеризацию на примере случайного
набора данных и вычислите силуэтный коэффициент кластеризации — метрику,
показывающую качество кластеризации.

Для вас сгенерирован искусственный набор данных с помощью
функции make_blobs из библиотеки sklearn.datasets.

Что нужно сделать:
1. Используйте функцию linkage из библиотеки scipy.cluster.hierarchy для проведения
    иерархической кластеризации над созданным набором данных. В качестве
    параметра method можно использовать ward

2. Используйте функцию silhouette_score из библиотеки sklearn.metrics для вычисления
    силуэтного коэффициента кластеризации. Силуэтный коэффициент может принимать
    значения от -1 до 1, где ближе к 1 — лучше

3. Сохраните полученное значение силуэтного коэффициента и выведите его на экран

4. Повторите шаги 1–3 не менее чем для 10 случайных наборов данных и усредните
    полученные значения силуэтных коэффициентов

5. В качестве результата задания выведите на экран средний силуэтный коэффициент"""

from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.metrics import silhouette_score


X, y = make_blobs(n_samples=100, n_features=4, centers=4, random_state=42)
Z = linkage(X, method="ward")
labels = fcluster(Z, t=4, criterion="maxclust")
silhouette = silhouette_score(X, labels)
print(f"{silhouette}")

silhouette_sum = 0

for i in range(10):
    X, y = make_blobs(n_samples=100, n_features=4, centers=4, random_state=i)
    Z = linkage(X, method="ward")
    labels = fcluster(Z, t=4, criterion="maxclust")
    silhouette = silhouette_score(X, labels)
    silhouette_sum += silhouette

silhouette_avg = silhouette_sum / 10
print(silhouette_avg)

print(silhouette_avg == 0.7320912174491637)
