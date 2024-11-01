"""Задача 2
Анализ продаж и ассортимента магазина фруктов

Используя имеющийся фрагмент кода (см. окно ввода ответа), выполните последовательно следующие задания:
1.	Сделайте срез по условию для df. Выберите все строки со значением Q больше 3,
    для которых значение переменной Shop — это Shop A. Сохраните результат в переменную subset.
    Получите значение колонки total для второй строки получившегося среза subset и сохраните его в переменную total2.

2.	Посчитайте общую выручку в разбивке по всем фруктам (колонка total),
    результат (объект Series) сохраните в переменную fruit_total.

3.	Посчитайте общее количество (колонка Q) всех фруктов в разбивке по названию,
    результат (объект Series) сохраните в переменную fruit_quantity.

4.	Посчитайте среднюю цену (колонка P) лимонов, результат (объект Series)
    сохраните в переменную lemon_average_price"""

import pandas as pd
import numpy as np


fruit = np.array(
    [
        "lemons",
        "lemons",
        "lemons",
        "lemons",
        "apples",
        "apples",
        "apples",
        "apples",
        "apples",
        "apples",
        "apples",
    ],
    dtype=object,
)

shop = np.array(
    [
        "Shop A",
        "Shop A",
        "Shop A",
        "Shop B",
        "Shop A",
        "Shop A",
        "Shop A",
        "Shop B",
        "Shop B",
        "Shop B",
        "Shop A",
    ],
    dtype=object,
)

pl = np.array(
    [
        "online",
        "online",
        "offline",
        "online",
        "online",
        "offline",
        "offline",
        "online",
        "offline",
        "offline",
        "offline",
    ],
    dtype=object,
)

df = pd.DataFrame(
    {
        "fruit": fruit,
        "shop": shop,
        "pl": pl,
        "Q": [1, 2, 2, 3, 3, 4, 5, 6, 7, 4, 4],
        "P": [5, 4, 5, 5, 6, 6, 8, 9, 9, 3, 3],
    }
)

df["total"] = df["Q"] * df["P"]
print(f"{df}\n")

subset = df.loc[(df.Q > 3) & (df.shop == "Shop A")]
print(
    f"Все строки со значением Q > 3, для которых значение переменной Shop — это Shop A:\n{subset}\n"
)

total2 = subset["total"][6]
print(
    f"Значение колонки total для второй строки получившегося среза subset:\n{total2}\n"
)

fruit_total = df.groupby("fruit")["total"].sum()
print(f"Общая выручка в разбивке по всем фруктам:\n{fruit_total}\n")

fruit_quantity = df.groupby("fruit")["Q"].sum()
print(
    f"Общее количество (колонка Q) всех фруктов в разбивке по названию:\n{fruit_quantity}\n"
)

lemon_average_price = df[df.fruit == "lemons"].groupby("fruit")["P"].mean()
print(f"Средняя цена (колонка P) лимонов:\n{lemon_average_price}")
