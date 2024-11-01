"""Задача 3
Исследование датасета (продолжение)

Мы продолжаем работать с датасетом Pandas practices. В этом задании вам необходимо
написать программу, которая удалит столбец с наибольшим количеством пропусков.

Подсказка: используйте результаты ранее выполненного задания"""

import pandas as pd


police = pd.read_csv("./police.csv", sep=",")

column_to_drop = police.isnull().sum().idxmax()
print(column_to_drop)

# Удалили столбец с наибольшим количеством пропусков
police.drop(column_to_drop, inplace=True, axis=1)
