"""Задача 4
Логистическая регрессия

Вам предложены искусственные данные, где зависимая переменная
является бинарной. Постройте модель логистической регрессии
на 80% выборки. Выведите на экран округленное до второго знака
после запятой значение f1 score на тестовой выборке"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split


X = np.random.rand(100, 5)
y = np.random.randint(0, 2, size=100)
model = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(round(f1_score(y_test, y_pred), 2))
