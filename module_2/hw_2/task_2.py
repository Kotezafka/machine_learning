"""Задача 2
Построение графиков с помощью библиотек Python

Задание поможет закрепить навыки работы с библиотеками Altair и Seaborn
Для выполнения задания вам понадобится набор данных — информация
о пассажирах Титаника. На странице скачивания датасета
можно изучить описание данных

Что нужно сделать:

1.	Создать Python-ноутбук, загрузить в него данные для построения графиков

2.	Средствами библиотеки Altair или Seaborn построить сгруппированную
    полосковую диаграмму (grouped bar chart), которая отображает распределение
    выживших пассажиров по классу кают, и, независимо, по полу

3.	Настроить параметры диаграммы так, чтобы были выполнены условия:
    - на диаграмме имеется три группы (по классу каюты)
        по два столбика в каждом
    - оси (легенда) имеют понятные подписи на русском языке
    - на диаграмме отсутствует сетка (разлинованный фон)
    - у графика есть лаконичный осмысленный заголовок

4.	В качестве решения задания прикрепите ссылку на ноутбук и jpeg/png-файл, в котором сохранена сама диаграмма"""

import pandas as pd
import altair as alt


df = pd.read_csv("./module_2/hw_2/train.csv")
print(f"Объект DataFrame:\n{df.head().to_string()}\n\n")

df = df.replace({"Sex": {"male": "Мужчины", "female": "Женщины"}})
print(f"Переименовали значения поля Sex:\n{df.head().to_string()}\n\n")

alt.Chart(df).mark_bar().encode(
    x=alt.X(
        "count(PassengerId):Q", axis=alt.Axis(title="Кол-во пассажиров", grid=False)
    ),
    y=alt.Y("Sex:N", axis=alt.Axis(title="", labels=False)),
    row=alt.Row("Pclass:O", title="Классы кают"),
    color=alt.Color("Sex:N", scale=alt.Scale(), legend=alt.Legend(title="Пол")),
).properties(title=["Кол-во выживших пассажиров по полу и классу кают"]).configure(
    view=alt.ViewConfig(strokeWidth=0)
)

""" Этот код предназначен для создания диаграммы с помощью Altair.
Чтобы отобразить ее, вам нужно запустить этот код в среде,
где Altair может работать (например, Jupyter Notebook)"""
