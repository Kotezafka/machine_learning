"""Задача 5
Исследование произвольных данных

Это задание не проверяется LMS, но выполняя его, вы тренируете и закрепляете навыки работы
с функциями библиотеки Pandas на различных исходных данных.
Для этого задания вы можете использовать любой доступный вам набор данных,
например, загрузите заинтересовавший вас набор данных с сайта kaggle.

Что нужно сделать:
1. Создайте Python-ноутбук, загрузите в него данные из csv-файла и преобразуйте в объект DataFrame;

2. Просмотрите полученный объект;

3. Вычислите описательные статистики для DataFrame;

4. Поразмышляйте, как вы можете использовать срезы для анализа
    вашего набора данных, получите необходимый срез(ы) DataFrame;

5. Определите, какую полезную информацию, вы можете получить о данных,
    используя отбор и фильтрацию, сформируйте необходимый поднабор данных и проанализируйте его;

6. Выполните сортировку применительно к исследуемому набору данных;

7. Потренируйтесь в переименование колонок исследуемого DataFrame;

8. Проверьте DataFrame на наличие пропущенных значений,
    выберите один из методов работы с пропусками и примените его;

9. Проверьте DataFrame на наличие дубликатов;

10. Сделайте предположение, какой новый признак вы могли бы ввести
    для исследуемого набора данных, и реализуйте его в созданном DataFrame.

По каждому пункту задания сделайте выводы"""

import pandas as pd
import numpy as np
import re


# 1. Загрузите данные из csv-файла и преобразуйте в объект DataFrame
df = pd.read_csv("./full_netflix.csv", sep=",")
print(f"Объект DataFrame:\n{df.head(15).to_string()}\n\n")


# 2. Просмотрите полученный объект
print(f"Вывод первых 5 строк:\n{df.head().to_string()}\n\n")


# 3. Вычислите описательные статистики для DataFrame
print(f"Описательные статистики для DataFrame:\n{df.describe()}\n\n")


# 4. Срезы DataFrame
high_rated_movies = df[df["imdbAverageRating"] > 8]
print(f"Фильмы с рейтингом выше 8:\n{high_rated_movies.head().to_string()}\n")
high_rated_mask = df["imdbAverageRating"] > 8
print(f"Количество фильмов с рейтингом выше 8:\n{np.sum(high_rated_mask)}\n\n")

recent_movies = df[df["releaseYear"] > 2000]
print(f"Фильмы, выпущенные после 2000 года:\n{recent_movies.head().to_string()}\n")
recent_movies_mask = df["releaseYear"] > 2000
print(
    f"Количество фильмов, выпущенных после 2000 года:\n{np.sum(recent_movies_mask)}\n\n"
)

movies_in_germany = df[df["availableCountries"].str.contains("DE")]
print(f"Фильмы, доступные в Германии:\n{movies_in_germany.head().to_string()}\n")
movies_in_germany_mask = df["availableCountries"].str.contains("DE")
print(
    f"Количество фильмов, доступных в Германии:\n{np.sum(movies_in_germany_mask)}\n\n"
)


# 5. Отбор и фильтрация для получения информации
movies_2000s = df[
    (df["releaseYear"] >= 2000)
    & (df["releaseYear"] < 2010)
    & (df["imdbAverageRating"] > 8.0)
]
print(
    f"Фильмы, выпущенные в 2000-х годах, с рейтингом больше 8:\n{movies_2000s.head(15).to_string()}\n\n"
)


# 6. Сортировка
sorted_by_votes = df.sort_values(by="imdbNumVotes", ascending=False)
print(
    f"Фильмы, отсортированные по количеству голосов на IMDb в порядке убывания:\n{sorted_by_votes.head().to_string()}\n\n"
)

sorted_by_rating = df.sort_values(by="imdbAverageRating")
print(
    f"Фильмы, отсортированные по рейтингу в порядке возрастания:\n{sorted_by_rating.head().to_string()}\n\n"
)


# 7. Переименование колонок
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


# 8. Проверка на наличие пропущенных значений
print(
    f"Вывод количества пропущенных значений в каждом столбце:\n{df.isnull().sum()}\n\n"
)

df = df.dropna(how="any")
print(f"Удалили строки с пропущенными значениями:\n{df.isnull().sum()}\n\n")


# 9. Проверка на наличие дубликатов
print(f"Количество дубликатов:\n{df.duplicated().sum()}\n\n")


# 10. Реализуем новые признаки
# Возраст фильма
df["film_age"] = pd.Timestamp.now().year - df["release_year"]

# Критический успех
df["critical_success"] = 0
df.loc[df["imdb_average_rating"] > 8, "critical_success"] = 1

print(f"Реализованы новые признаки:\n{df.head(10).to_string()}")
