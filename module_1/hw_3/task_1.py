"""Задача 1
Расчет статистических показателей подписчиков социальной сети

Вам даны показатели прироста подписчиков за месяц в 300 аккаунтах социальной сети,
которые сохранены в объект DataFrame с именем list_metrics.

Выполните следующие задания применительно к исходным данным:

1.	Рассчитайте стандартное отклонение прироста подписчиков.
    Результат округлите до второго знака после запятой и сохраните в переменную result1.

2.	Рассчитайте размах прироста подписчиков. Результат округлите до второго знака
    после запятой и сохраните в переменную result2.

* Дополнительное задание (не проверяется LMS, но предлагаем проделать его самостоятельно).
    Постройте гистограмму частот по значению прироста.
(Подсказка: для построения гистограммы используйте pandas.DataFrame.hist)"""

import random
import pandas as pd
import matplotlib.pyplot as plt


random.seed(10)

list_metrics = []

for i in range(0, 300):
    n = random.randint(-100, 1000)
    list_metrics.append(n)

list_metrics = pd.DataFrame({"Прирост": list_metrics})
print(f"{list_metrics}\n")

result1 = round(list_metrics["Прирост"].std(), 2)
print(f"Стандартное отклонение прироста подписчиков:\n{result1}\n")

result2 = float(list_metrics["Прирост"].max() - list_metrics["Прирост"].min())
print(f"Размах прироста подписчиков:\n{result2}\n")

# Построение гистограммы частот по значению прироста
plt.figure(figsize=(8, 6))
list_metrics.hist(column="Прирост", bins=10)
plt.title("Гистограмма прироста подписчиков")
plt.xlabel("Прирост подписчиков")
plt.ylabel("Частота")
plt.show()