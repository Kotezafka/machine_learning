# Введение в линейную алгебру для машинного обучения
## Описание

### Цели недели

Линейная алгебра играет важную роль в машинном обучении и необходима для успешной работы в этой области. В этой неделе мы вспомним основные принципы и операции, связанные с векторами и матрицами, и затем применим их на практике с помощью библиотеки NumPy.

### После освоения темы:
- Вы вспомните понятия вектора и матрицы, векторного пространства, нормы вектора, ортогональности и гиперплоскости
- Вспомните, как выполнять базовые операции над векторами и матрицами
- Сможете применять NumPy для работы с векторами и матрицами
- Сможете вычислять косинусную меру близости векторов и использовать ее для нахождения разницы между словами

### План занятия
- Векторы. Основные операции над векторами
- Матрицы. Основные операции над матрицами
- Линейная алгебра в NumPy

### Итоги занятия

1.  Линейная алгебра — один из основных математических инструментов в машинном обучении. Мы будем работать с векторами и матрицами:
- __Вектор__ – упорядоченный набор чисел, который может быть представлен в виде столбца или строки
- __Матрица__ — таблица чисел, упорядоченных в виде строк и столбцов


2.  Основные рассмотренные понятия линейной алгебры:
- __Векторное пространство__ — математическая структура, состоящая из набора элементов, называемых векторами, на которых определены операции сложения и умножения на скаляр
- __Скалярное произведение векторов__ — операция, результатом которой является скаляр, то есть число. Определяется как произведение длин векторов на косинус угла между ними
- __Норма вектора__ — числовая характеристика, определяющая длину или размер вектора, может быть вычислена по различным формулам
- __Угол между векторами__ — угол, образованный двумя векторами, может быть вычислен с использованием скалярного произведения и норм векторов
- __Проекция вектора__ — вектор, полученный путем опускания перпендикуляра из начала координат на плоскость или прямую
- __Гиперплоскость__ — подпространство размерности n-1 в n-мерном пространстве; делит пространство на две части и определяется уравнением, которое связывает n координат и имеет вид wa₁x₁ + w₂x₂ +...+ wₙxₙ + b = 0, где w₁, w₂, ..., wₙ — коэффициенты, определяющие направление нормали к гиперплоскости, x₁, x₂, ..., xₙ – координаты точки в пространстве, b — свободный член
- __Ортогональность векторов__ — свойство векторов, которое означает, что два вектора перпендикулярны друг другу, то есть угол между ними равен 90 градусам


3.  Оперировать векторами и матрицами в Python позволяет библиотека NumPy


4.  __Косинусная мера близости слов__ — это метрика, используемая для определения семантической схожести между словами. Она помогает понять семантическую связь между словами и использовать эту информацию для анализа текста. Для вычисления косинусной меры близости необходимо представить слова в виде числовых векторов и далее воспользоваться функциями библиотеки NumPy
---

### В результате выполнения заданий вы сможете:

- Рассчитывать косинусную меру угла между словами и предложениями с использованием библиотек Python для машинного обучения
- Анализировать косинусную меру и делать вывод о близости слов и предложений

