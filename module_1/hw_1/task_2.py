"""Задача 2
Базовые операции с массивами NumPy (часть 2)

Ваш коллега создал структуру данных (см. окно ввода ответа) и передал вам в работу.
Преобразуйте ее в массив NumPy и выполните следующие задания:

1.	Создайте подмассив lines, содержащий все строки со 2-й по 4-ю включительно.
2.	Создайте подмассив last_column, содержащий последний столбец исходного массива.
3.	Транспонируйте исходный массив и сохраните результат в переменную array_t.
4.	Вычислите сумму элементов исходного массива, результат сохраните в переменную array_sum.
5.	Вычислите среднее значение элементов исходного массива, результат сохраните в переменную array_avg.

Для выполнения заданий 2.2–2.5 используйте функции библиотеки NumPy"""

import numpy as np

some_data = [
    [3, 8, 1, 0, 1, 2],
    [9, 2, 7, 3, 0, 4],
    [2, 5, 1, 3, 1, 8],
    [5, 1, 2, 1, 1, 0],
]

arr_some_data = np.array(
    [[3, 8, 1, 0, 1, 2], [9, 2, 7, 3, 0, 4], [2, 5, 1, 3, 1, 8], [5, 1, 2, 1, 1, 0]]
)

lines = arr_some_data[1:4]
print(f"Подмассив, содержащий все строки со 2-й по 4-ю включительно:\n{lines}\n")

last_column = arr_some_data[:, -1]
print(f"Подмассив, содержащий последний столбец исходного массива:\n{last_column}\n")

array_t = np.transpose(arr_some_data)
print(f"Транспонированный исходный массив:\n{array_t}\n")

array_sum = sum(sum(arr_some_data))
print(f"Сумма элементов исходного массива:\n{array_sum}\n")

array_avg = np.mean(arr_some_data)
print(f"Среднее значение элементов исходного массива:\n{array_avg}")
