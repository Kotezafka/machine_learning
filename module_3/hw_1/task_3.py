"""Задача 3
Анализ похожих товаров по их описанию

Допустим, вы аналитик данных в компании, которая занимается
продажей мебели. Ваша задача — определить, какие товары наиболее
похожи друг на друга по описанию. Для этого необходимо использовать
косинусную меру угла с помощью библиотеки spacy

Шаги выполнения задания:
1.  Скачайте датасет с описанием товаров
    (исходный файл — product_description.csv)


2.  Импортируйте библиотеку spacy и загрузите
    модель языка en_core_web_sm

    Дополнительно для выполнения задания выполните
    импорт функций из библиотек Python:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity


3.	Проведите предобработку текста: удалите стоп-слова,
    лемматизируйте слова, удалите пунктуацию

    Используйте следующий код для предобработки текста:
    def preprocess_text(text):
        doc = nlp(text)
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return " ".join(tokens)

    data['processed_text'] = data['description'].apply(preprocess_text)


4.	Создайте матрицу векторов для каждого товара

    Используйте следующий код для векторизации:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data['processed_text'])


5.	Рассчитайте косинусную меру угла между каждой парой товаров


6.	Отобразите топ-5 товаров, которые наиболее похожи друг на друга"""

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def preprocess(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return " ".join(tokens)


def vectoriz(df):
    vectorizer = TfidfVectorizer()

    return vectorizer.fit_transform(df["processed_text"])


def main():
    # 1. Загрузка csv-файла и преобразование в объект DataFrame
    df = pd.read_csv("./module_3/hw_1/product_description.csv")
    print(f"Объект DataFrame:\n{df.to_string()}\n\n")

    # 3. Предобработка текста
    df["processed_text"] = df["description"].apply(preprocess)
    print(f"Предобработка текста:\n{df['processed_text']}\n\n")

    # 4. Создаем матрицу векторов для каждого товара
    vectors = vectoriz(df)
    print(f"Создаем матрицу TF-IDF векторов из обработанных текстов:\n{vectors}\n\n")

    # 5. Вычисляем матрицу косинусного сходства между всеми парами векторов
    # 5. Рассчитаем косинусную меру угла между каждой парой товаров
    cos_similar = cosine_similarity(vectors)
    print(
        f"Вычисляем матрицу косинусного сходства между всеми парами векторов:\n{cos_similar}\n\n"
    )

    # 6. Отобразим топ-5 товаров, которые наиболее похожи друг на друга
    for i, row in df.iterrows():
        similar_ind = cos_similar[i].argsort()[
            :-6:-1
        ]  # Находит индексы 5 самых похожих товаров

        res = [
            [df["product_name"][j], cos_similar[i][j]] for j in similar_ind if j != i
        ]  # Создает список пар (название товара, косинусное сходство) для похожих товаров, исключая сам товар

        print(f"Топ-5 товаров похожих по описанию для {row['product_name']}:\n")
        for r in res:
            print(f"{r}")
        print(f"\n\n")


if __name__ == "__main__":
    main()
