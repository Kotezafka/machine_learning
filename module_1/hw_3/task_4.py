"""Задача 4
Исследование датасета (продолжение)

Мы продолжаем работать с датасетом Pandas practices. Исследуйте данные и ответьте на вопросы:

1. Водителей какого пола в датасете больше?
Выберите один ответ:
- невозможно определить
- женщин
- мужчин

2. Можно ли по предыдущему пункту сделать вывод, что к одному из полов
    относятся предвзято, чаще останавливают?
Выберите один ответ:
- Нет нельзя, так как мы не знаем пропорцию по водителям (какую долю составляют мужчины и женщины)
- Да. Останавливают чаще мужчин, причем в среднем на больший промежуток времени
- Нет, нельзя, потому что такой вывод можно сделать только из выборки, где присутствуют молодые мужчины (до 21 года)"""

import pandas as pd


police = pd.read_csv("./module_1/hw_3/police.csv", sep=",")

gender_counts = police["driver_gender"].value_counts()
print(f"Количество женщин и мужчин:\n{gender_counts}\n")

most_common_gender = gender_counts.idxmax()
print(f"Больше всего водителей пола: {most_common_gender}")
