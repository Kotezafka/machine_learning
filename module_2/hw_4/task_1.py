"""Задача 1
Построение матрицы корреляции для анализа продаж в супермаркетах

В этом задании предлагаем вам поработать с датасетом Supermarket sales,
который содержит данные о продажах в трех разных супермаркетах.
В LMS файл с данными supermarket.csv уже подгружен.

Ваша задача — рассчитать матрицу корреляции и сохранить ее в переменную corr.
Округлите значение коэффициентов корреляции до двух знаков после запятой"""

import pandas as pd


df = pd.read_csv("./module_2/hw_4/supermarket.csv", sep=",")
print(f"Объект DataFrame:\n{df.head().to_string()}\n\n")

df_numeric = df.select_dtypes(include=["number"])
corr = df_numeric.corr().round(2)
corr.style.background_gradient(cmap="coolwarm")
print(f"Матрица корреляции:\n{corr.to_string()}\n\n")


""" Теперь давайте проанализируем получившиеся коэффициенты корреляции. 

1. Какие поля датафрейма имеют сильную положительную
    корреляцию со стоимостью проданных товаров (cogs)?
Выберите один или несколько ответов:
- Total
- gross margin percentage
- Rating
- Quantity
- Unit price
- gross income
- Branch
- Tax 5%
- Invoice ID

2. Какие параметры из приведенных в списке ниже имеют наиболее
    сильный отрицательный коэффициент корреляции?
Выберите один ответ:
- “Unit price” и “Quantity”
- “Rating” и “gross margin percentage”
- “Rating” и “Total”
- “Rating” и “Unit price”"""
