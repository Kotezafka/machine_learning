"""Задача 1
Построение круговой диаграммы

Выполните построение круговой диаграммы по данным файла Electric_Сars.csv,
содержащим сведения о моделях электромобилей

Для построения диаграммы:
1.	Сформируйте данные по количеству моделей (столбец Brand) и
    выполните их сортировку по столбцу TopSpeed_KmH

2.	Используйте библиотеку matplotlib, чтобы построить круговую диаграмму по полученным
    в первом пункте данным. Диаграмма должна показывать долю в процентном отношении
    первых 5 и всех остальных моделей (rest)

3.	Покажите на диаграмме наименование брендов и соответствующую им долю в процентах

4.	Увеличьте радиус диаграммы в 3 раза

5.	Сохраните график под именем auto_pie.png"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("./module_2/hw_1/Electric_Car.csv")
print(f"Датафрейм:\n{df.to_string()}\n\n")


brand_counts = df.groupby(["Brand"])["Model"].count().sort_values(ascending=False)
print(
    f"Подсчет количества моделей каждого бренда и их вывод в порядке уменьшения:\n{brand_counts}\n\n"
)

top_speeds = df.groupby("Brand")["TopSpeed_KmH"].max()
print(f"Получение максимальных скоростей для каждого бренда:\n{top_speeds}\n\n")


part_table = brand_counts.to_frame().reset_index()
df_top5 = part_table[part_table["Model"] > 5]
print(f"Датафрейм топ-5 автомобилей по количеству:\n{df_top5}\n\n")

rest = part_table[part_table["Model"] <= 5].sum().iloc[1]
print(f"Количество всех остальных автомобилей:\n{rest}\n")

df_rest = pd.DataFrame([{"Brand": "Rest", "Model": rest}])
print(f"Датафрейм остальных автомобилей:\n{df_rest}\n\n")

# Конкатинация двух датафреймов для построения круговой диаграммы
df_for_pie = pd.concat([df_top5, df_rest])
print(f"Датафрейм для построения круговой диаграммы:\n{df_for_pie}\n\n")


# Создание круговой диаграммы по брендам
values = np.array([13, 9, 8, 8, 6, 59])
categories = ["Tesla", "Audi", "Nissan", "Volkswagen", "Skoda", "Rest"]
mycolors = ["purple", "salmon", "pink", "lightgreen", "skyblue", "yellow"]
plt.pie(values, labels=categories, colors=mycolors, autopct="%0.1f%%", radius=1.4)
# plt.show()

# Сохранение графика
plt.savefig("./module_2/hw_1/auto_pie.png")
