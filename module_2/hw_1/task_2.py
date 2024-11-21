"""Задача 2
Построение столбчатой диаграммы

Постройте горизонтальную столбчатую диаграмму по данным
файла Electric_Сars.csv, который содержит сведения о моделях электромобилей

Для построения диаграммы:
1.	Сформируйте данные по количеству различных моделей (столбец Brand) и
    выполните сортировку по количеству

2.	Используйте библиотеку matplotlib, чтобы построить
    горизонтальную столбчатую диаграмму по данным из первого пункта

3.	При построении диаграммы укажите наименование модели и соответствующее ей количество

4.	Сохраните график под именем saved_figure_barh.png"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("./module_2/hw_1/Electric_Car.csv")
print(f"Датафрейм:\n{df.to_string()}\n\n")

# Группировка Brand по количеству уникальных моделей
brand_counts = df.groupby(["Brand"])["Model"].count().sort_values(ascending=False)
print(
    f"Подсчет количества моделей каждого бренда и их вывод в порядке уменьшения:\n{brand_counts}\n\n"
)


# Создание столбчатой диаграммы по брендам
x = brand_counts.index
y = brand_counts.values

fig, ax = plt.subplots()
plt.barh(x, y)  # сделаем столбчатую диаграмму горизонтальной
ax.set_title("Количество моделей определенного бренда")
ax.grid()  # добавление сетки
ax.invert_yaxis()
# plt.show()

# Сохранение графика
plt.savefig("./module_2/hw_1/saved_figure_barh.png")
