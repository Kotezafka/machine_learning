# Описательная статистика. Анализ данных с помощью Pandas
## Описание

### Цели недели

На этой неделе продолжим работу с библиотекой Pandas. Рассмотрим основные методы вычисления описательных статистик для числовых данных, таких как среднее значение, медиана, стандартное отклонение и квантили.

Лекция поможет освоить основные инструменты анализа данных с помощью библиотеки Pandas и научиться решать различные задачи по обработке и анализу табличных данных.

### После освоения темы:
- Вы сможете получить информацию о DataFrame, вычислить описательные статистики для числовых данных, обратиться к элементам DataFrame по индексу и порядковому номеру, изменить индекс
- Сможете выполнять поиск, фильтрацию и сортировку DataFrame с применением методов библиотеки Pandas
- Сможете вычислять статистику по признакам, применять функции к данным, рассчитывать новые значения
- Сможете работать с несколькими таблицами с помощью инструментов библиотеки Pandas

### План занятия
- Описательная статистика
- Базовые операции с DataFrame
- Работа с пропусками и операции над данными
- Работа с несколькими таблицами

### Итоги занятия 

1.  Числовые переменные описываются мерами центральности (среднее арифметическое, медиана, мода) и мерами вариации (размах, выбросы, дисперсия, стандартное отклонение). Вычислить перечисленные меры можно с помощью методов библиотеки Pandas


2.  Ящик с усами — специальный вид графика для визуализации основных метрик


3.  Анализ данных в Pandas начинается с загрузки датасета в ноутбук, получения информации о структуре данных и вычисления описательных статистик


4.  Библиотека Pandas позволяет выполнять отбор и фильтрацию данных:
- __filter()__ — возвращает подмножество строк или столбцов датафрейма в соответствии с заданным условием
- __sort_index()__ — сортирует данные по индексу или столбцу


5.  Для работы с пропусками используют следующие методы:
- __dropna()__ — удаляет пропущенные значения
- __fillna()__ — восполняет отсутствующие данные конкретными значениями
- __isnull()__ — возвращает объект, содержащий булевы значения, которые показывают, какие значения отсутствуют


6.  Метод __apply()__ позволяет пользователю передать функцию и применить ее к каждому отдельному значению серии. Таким образом мы можем получить новый признак на основе уже имеющихся в DataFrame


7.  В Pandas можно получать агрегированные данные и выполнять соединение таблиц:
- __groupby()__ — группирует данные по одному или нескольким столбцам, позволяет выполнять функции в группах
- __concat()__ — конкатенирует объекты по оси
- __merge()__ — соединяет строки в DataFrame на основе одного или нескольких ключей

---

### В результате выполнения заданий вы сможете:

- Выполнять базовые операции с объектом DataFrame, используя методы библиотеки Pandas
- Использовать методы библиотеки Pandas для решения прикладных задач анализа данных

### Библиотека Pandas предоставляет множество полезных функций для работы с данными:

__Чтение и запись данных в различных форматах__

__Обработка данных:__ 
- функции для фильтрации
- сортировка
- группировка
- агрегация
- преобразование
- объединение данных

__Индексация и выборка данных:__
- функции для выборки данных по условиям
- функции индексации по метке и индексу

__Работа с пропущенными данными и дубликатами:__
- функции для обнаружения, удаления и заполнения пропущенных значений
- функции для проверки и удаления дубликатов