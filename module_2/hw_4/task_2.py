"""Задача 2
Анализ матрицы корреляции произвольных данных

Для этого задания вы можете использовать любой доступный вам
набор данных, например, загрузите заинтересовавший вас
набор данных с сайта kaggle.

Что нужно сделать:
    - создайте Python-ноутбук, загрузите в него данные
        из csv-файла и преобразуйте в объект DataFrame

    - изучите структуру данных и выполните их предобработку

    - рассчитайте матрицу корреляции

    - визуализируйте результат с применением различных способов

По каждому пункту задания сделайте выводы и отразите их"""

import pandas as pd
import re
from IPython.display import display


# 1. Загрузка csv-файла и преобразование в объект DataFrame
df = pd.read_csv("./module_2/hw_4/full_netflix.csv", sep=",")
print(f"Объект DataFrame:\n{df.head().to_string()}\n\n")


# 2. Изучение структуры данных и выполнение предобработки
print(
    f"Кол-во данных, которые содержит датасет:\n{df.shape} - {df.shape[1]} признаков и {df.shape[0]} строк\n\n"
)

print(f"Кол-во данных и их тип:")
print(f"{df.info()}\n\n")

# Переименование колонок
for column in df.columns:
    new_column_name = (
        re.sub(r"(?<=[a-z])(?=[A-Z])", " ", column)
        .replace(" ", "_")
        .replace("-", "_")
        .lower()
    )
    df = df.rename(columns={column: new_column_name})

print(
    f"Переименовали колонки - все слова начинаются со строчных букв и между словами нижнее подчеркивание:\n{df.head().to_string()}\n\n"
)

# Кол-во уникальных значений
print(
    f"Кол-во уникальных значений идентификатора release_year:\n{df['release_year'].nunique()}\n\n"
)
print(
    f"Кол-во уникальных значений идентификатора imdb_average_rating:\n{df['imdb_average_rating'].nunique()}\n\n"
)

# Проверка на наличие пропущенных значений
print(f"Проверим DataFrame на наличие пропусков, шт:\n{df.isnull().sum()}\n\n")
print(
    f"Проверим DataFrame на наличие пропусков, % (наибольшее кол-во пропусков в столбце url):\n{df.isnull().mean().sort_values(ascending=False)}\n\n"
)

df = df.dropna(how="any")
print(f"Проверим DataFrame на наличие пропусков, шт:\n{df.isnull().sum()}\n\n")

# Проверка на наличие дубликатов
print(f"Количество дубликатов:\n{df.duplicated().sum()}\n\n")

print(
    f"Количество фильмов определенного жанра:\n{df['genres'].value_counts(ascending=False)}\n\n"
)
print(f"Количество уникальных жанров:\n{df['genres'].nunique()}\n\n")
print(f"Список жанров:\n{df['genres'].unique()}\n\n")


df_numeric = df.select_dtypes(include=["number"])
print(
    f"Отбираем только те столбцы, которые имеют числовые значения:\n{df_numeric.head().to_string()}\n\n"
)

print(
    f"Проанализируем более подробно числовые данные DataFrame:\n{df_numeric.describe().to_string()}\n\n"
)


print(f"Рассмотрим числовые признаки: минимум, максимум, среднее и медианное значения:")
print(f"Минимальное значение:\n{df_numeric.min()}\n\n")
print(f"Максимальное значение:\n{df_numeric.max()}\n\n")
print(f"Среднее значение:\n{df_numeric.mean()}\n\n")
print(f"Медианное значение:\n{df_numeric.median()}\n\n")


# 3. Расчет матрицы корреляции
corr = df_numeric.corr().round(2)
styled_corr = corr.style.background_gradient(cmap="coolwarm")
print(f"Матрица корреляции:\n")
display(styled_corr)
print(f"Матрица корреляции:\n{corr.to_string()}\n\n")


# 4. Визуализация результата с применением различных способов
hist = df["imdb_average_rating"].hist()
figure = hist.get_figure()
figure.savefig("./module_2/hw_4/imdb_average_rating_histogram.png")

hist = df["release_year"].hist()
figure = hist.get_figure()
figure.savefig("./module_2/hw_4/release_year_histogram.png")

hist = df["imdb_num_votes"].hist()
figure = hist.get_figure()
figure.savefig("./module_2/hw_4/imdb_num_votes_histogram.png")
