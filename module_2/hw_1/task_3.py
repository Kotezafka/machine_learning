"""Задача 3
Построение и визуализация 3D-цилиндра

Напишите программу для построения и визуализации 3D-цилиндра с помощью библиотеки matplotlib.

Шаги выполнения задания:
1.	Сформируйте вершины для построения цилиндра из 20 угловых секторов.
    Сначала постройте вершины одного основания (круга) — используйте углы
    поворота и радиус окружности равный 1

    Координаты вершин основания определяются по формуле:
    0,cos(2*pi*(i)/N),sin(2*pi*(i)/N),
    где выражение (2*pi*(i)/N) задает углы поворота на каждом шаге i

2.	Аналогично постройте вершины второго основания, взяв высоту равную 1.
    Координаты вершин основания можно найти по формуле:
    1,cos(2*pi*(i)/N),sin(2*pi*(i)/N)

3.	Используйте библиотеку spatial, чтобы сформировать грани для
    построения цилиндра из 20 угловых секторов

4.	Создайте сетку для построения цилиндра

5.	Визуализируйте полученный цилиндр

6.	Сохраните изображение в формате stl"""

from scipy import spatial
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh as stl_mesh


# Создание вершин
vertices = np.array([[0, 0, 0]])
sector = 20  # количество секторов для цилиндра

# Циклы генерируют координаты вершин для двух кругов, образующих основания цилиндра
for i in range(0, sector):
    vertices_1 = np.array(
        [[0, np.cos(2 * np.pi * (i) / sector), np.sin(2 * np.pi * (i) / sector)]]
    )
    vertices = np.append(vertices, vertices_1, axis=0)

for i in range(0, sector):
    vertices_1 = np.array(
        [[1, np.cos(2 * np.pi * (i) / sector), np.sin(2 * np.pi * (i) / sector)]]
    )
    vertices = np.append(vertices, vertices_1, axis=0)

"""Создаем объект hull (выпуклая оболочка) из заданных вершин vertices.
    Выпуклая оболочка - минимальный выпуклый многогранник, содержащий все заданные точки"""
hull = spatial.ConvexHull(vertices)

# Извлекаем треугольники, которые образуют грани выпуклой оболочки
facets = hull.simplices
print(f"Массив описывает грани:\n{facets}\n\n")

# Создаем объект cylinder_mesh типа mesh.Mesh с нулевым массивом данных (заполняем его в цикле)
#cylinder_mesh = mesh.Mesh(np.zeros(facets.shape[0], dtype=mesh.Mesh.dtype))
cylinder_mesh = stl_mesh.Mesh(np.zeros(facets.shape[0], dtype=stl_mesh.Mesh.dtype))
for i, f in enumerate(facets):
    for j in range(3):
        cylinder_mesh.vectors[i][j] = vertices[f[j], :]


mesh = cylinder_mesh

# Определяем параметры размера графика и разрешение изображения
x = 10
y = 10
dpi = 80

# Создаем окно графика
figure = plt.figure(figsize=(x, y), dpi=dpi)

# Создаем 3D-ось внутри figure
axes = mplot3d.Axes3D(figure)

# Добавляем 3D-коллекцию (сетка из треугольников) к графику с черными краями
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors, edgecolor="black"))
figure.add_axes(axes)

# Получаем массив координат всех точек сетки
scale = mesh.points.flatten()

# Автоматически подбирается масштаб осей x, y, z по границам координат scale
axes.auto_scale_xyz(scale, scale, scale)
# plt.show()

# Запись сетки в файл
cylinder_mesh.save("./module_2/hw_1/cylinder.stl")
