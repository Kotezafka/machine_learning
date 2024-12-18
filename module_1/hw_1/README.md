# Библиотека NumPy
## Описание

### Цели недели

Неделя курса посвящена изучению функций библиотеки NumPy. Библиотека предоставляет мощные инструменты для работы с массивами и матрицами, что делает ее необходимой для научных вычислений и обработки данных. 
Одно из главных преимуществ NumPy — возможность решать системы линейных уравнений в Python матричным методом. Это позволяет решать задачи линейной алгебры, такие как нахождение собственных значений и векторов, определение матричных норм и многое другое.

### После освоения темы:
- Вы узнаете о возможностях основных библиотек, используемых для анализа данных
- Узнаете, как библиотека NumPy помогает в научных вычислениях и обработке данных
- Сможете использовать базовые операции по работе с массивами, математические и статистические функции библиотеки NumPy для решения прикладных задач
- Сможете решать системы линейных уравнений в Python матричным методом, решать задачи с помощью системы линейных уравнений

### План занятия
- Вычислительные функции библиотеки NumPy. Массивы
- Векторы. Решение линейных уравнений
- Использование NumPy в задачах обработки данных. Генерация мелодии
- Работа с табличными данными и векторами
- Работа с изображением с использованием NumPy

### Итоги занятия
1. NumPy (Numeric Python) — одна из базовых библиотек Python, которая поддерживает линейные алгебраические вычисления, в том числе работу с многомерными массивами и соответствующими высокоуровневыми функциями


2. На основе NumPy работает множество других библиотек Python. Алгоритмы, основанные на NumPy, работают быстрее аналогичных, написанных на чистом Python
   
 
3. Массив — базовый тип данных библиотеки NumPy. Библиотека NumPy обеспечивает основные операции над массивами: создание одномерных и многомерных массивов, добавление элементов в массив, добавление новых строк и столбцов, удаление элементов массива, изменение размерности массива, транспонирование массива


4. С помощью индексирования мы можем выбрать подмножество массива NumPy или его отдельные элементы


5. Массивами NumPy поддерживаются арифметические операции основного Python: сложение, вычитание, умножение и др. Можно выполнять операции с массивом и числом. Кроме того, библиотека имеет различные математические и статистические функции, которые используют при решении аналитических задач


6. Полная информация о библиотеке NumPy и ее возможностях представлена в документации
---

### В результате выполнения заданий вы сможете:

- использовать базовые операции по работе с массивами, математические и
статистические функции библиотеки NumPy для решения прикладных задач
- решать системы линейных уравнений в Python матричным методом,
решать задачи с помощью системы линейных уравнений

### Вот некоторые возможности библиотеки NumPy, которые будут вам полезны при работе с массивами

__Функции для создания массивов:__
- numpy.array()
- numpy.zeros()
- numpy.ones()
- numpy.empty()
- numpy.arange()

__Атрибуты массивов:__
- numpy.ndarray.ndim
- numpy.ndarray.shape
- numpy.ndarray.size
- numpy.ndarray.dtype  

__Индексация и срезы осуществляются по одному или нескольким индексам,
можно выбрать как один элемент из массива, так и получить подмассив из исходных данных__

__Математические операции:__
- numpy.add()
- numpy.subtract()
- numpy.multiply()  

__Функции для вычисления статистических показателей массива:__
- numpy.mean()
- numpy.median()
- numpy.average()
- numpy.std()  

__Функции для генерации случайных чисел:__
- numpy.random.rand()
- numpy.random.randn()
- numpy.random.randint()