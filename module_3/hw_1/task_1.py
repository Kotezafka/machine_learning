"""Задача 1
Расчет косинуса угла между словами

Напишите программу, которая рассчитывает
косинус угла между словами cat и cow,
используя библиотеку spacy и модель en_core_web_sm
для векторизации слов

Результат вычислений округлите до 3-х знаков
после запятой и введите в поле ввода ответа в LMS"""

import spacy
import numpy as np


def count_cos(vec1, vec2):
    mult = np.linalg.norm(vec1) * np.linalg.norm(vec2)

    if mult > 0:
        return np.dot(vec1, vec2) / mult
    else:
        return 0


def main():
    nlp = spacy.load("en_core_web_sm")
    word_1 = "cat"
    word_2 = "cow"

    tok1 = nlp(word_1)
    tok2 = nlp(word_2)

    cos = count_cos(tok1.vector, tok2.vector)
    print(f"Косинус угла между словами cat и cow равен {cos:.3f}")


if __name__ == "__main__":
    main()
