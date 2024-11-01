"""Задача 3
Анализ продаж и ассортимента магазина фруктов (продолжение)

Используя имеющийся фрагмент кода (см. окно ввода ответа), выполните следующее задание:
1.	Создайте сводную таблицу датафрейма df, где будет выведено значение
    переменной total с разбиением по строкам — категориям переменной shop
    и колонками по переменной pl. Используйте сумму как метод сведения
    и сохраните таблицу в переменную pivot.

2.	Выведите значение для второй колонки второй строки таблицы pivot"""

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

pivot = pd.pivot_table(df, values="total", index="shop", columns="pl", aggfunc="sum")
print(
    f"Таблица, где значение переменной total с разбиением по строкам — категориям переменной shop и колонками по переменной pl:\n{pivot}\n"
)

print(f"Значение для второй колонки второй строки таблицы pivot:\n{pivot.iloc[1, 1]}")
