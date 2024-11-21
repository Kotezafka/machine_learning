# Введение в визуализацию. Библиотека Matplotlib
## Описание

### Цели недели

Мы начнем погружение в визуализацию данных с рассмотрения составляющих диаграмм — глифов. Также мы рассмотрим когнитивные законы, которые необходимо учитывать при создании графиков, и изучим создание графиков в библиотеке Matplotlib.

### После освоения темы:
- Вы узнаете когнитивные законы и принципы восприятия информации человеком
- Узнаете виды графического представления данных и ситуации их использования
- Узнаете возможности библиотеки Matplotlib для построения различных видов графиков и настройки их отображения
- Сможете применять функции для построения основных видов графиков и настраивать внешний вид графиков (цвет, подписи, легенда, сетка)
- Сможете строить 3D-изображения с помощью библиотек Python и использовать их для задач компьютерного зрения

### План занятия 
- Как мы воспринимаем информацию 
- Методы визуализации 
- Введение в Matplotlib 
- 3D-визуализация графики для машинного обучения

### Итоги занятия
1. Диаграмма состоит из элементов — глифов и их графических атрибутов. Чтобы правильно их выбирать, следует учитывать теоретические основы — гештальт-правила и превентивные атрибуты, а также иерархию визуальных атрибутов


2. Грамотная визуализация помогает сделать данные более доступными и понятными, что может быть полезно для принятия решений и проведения анализа


3. Использование того или иного способа визуализации определяется ее целью:
- Гистограмма – распределение числовой переменной
- Круговая диаграмма – части целого, в сумме части составляют 1 или 100%
- Столбчатая диаграмма – количественные данные различных категорий или переменных
- Диаграмма рассеяния – совместное распределение двух величин, используют для анализа связи между двумя количественными переменными
- Тепловая карта – количественные данные, которые имеют градацию от низкого до высокого значения. Представляет собой график матричной структуры
- Географическая диаграмма (картограмма) – данные, связанные с географическими областями. Представляет обычно карту с областями, окрашенными в соответствии со значением какой-то переменной в определенный цвет


4. Библиотека matplotlib – основа визуализации в Python. Библиотека содержит функции для построения двумерных и трехмерных графиков, а также настройки их внешнего вида. Большинство графиков в matplotlib можно построить с помощью субмодуля __pyplot__


5. Помимо построения простых графиков с помощью matplotlib вы сможете построить следующие виды диаграмм:
- рассеяния (scatter)
- столбчатая (bar)
- гистограмма (hist)
- круговая (pie)


6. Библиотека matplotlib предоставляет широкие возможности для кастомизации графиков:
- функции __xlabel()__ и __ylabel()__ — установка названия осей
- функция __title()__ — вставка названия графика
- параметр __color__ — настройка цветового оформления  
- параметр __legend__ — вставка легенды  
- функция __grid()__ — наложение сетки на график  

Полная информация о библиотеке matplotlib и ее возможностях представлена в документации


7. Существуют библиотеки для создания 3D-изображений в Python, которые могут быть полезны в задачах машинного обучения. В Python можно создавать собственные 3D-фигуры, выгружать их и использовать в других приложениях


8. Библиотека NumPy-stl используется для отображения 3D-моделей, которые состоят из вершин, ребер, граней, полигонов и поверхностей
---

### В результате выполнения заданий вы сможете:

- строить и настраивать диаграммы с использованием библиотеки matplotlib
- строить и визуализировать 3D-изображения с помощью библиотеки matplotlib