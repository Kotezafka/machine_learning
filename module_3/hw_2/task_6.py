"""Задача 6
Модели случайного леса и градиентного бустинга

Напишите программу на Python для обучения модели случайного леса
и градиентного бустинга на датасете iris. Используйте библиотеки sklearn
и numpy для работы с данными. Разделите данные на обучающую и тестовую
выборки в соотношении 70/30. Посчитайте accuracy для каждой модели
на тестовой выборке и сравните результаты"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import numpy as np


iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

rf_predictions = rf_classifier.predict(X_test)
rf_acc = accuracy_score(y_test, rf_predictions)


gb_classifier = GradientBoostingClassifier(random_state=42)
gb_classifier.fit(X_train, y_train)

gb_predictions = gb_classifier.predict(X_test)
gb_acc = accuracy_score(y_test, gb_predictions)

print("Accuracy случайного леса:", round(rf_acc, 2))
print("Accuracy градиентного бустинга:", round(gb_acc, 2))
