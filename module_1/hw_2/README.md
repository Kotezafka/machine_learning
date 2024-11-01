# Получение и предобработка данных. Первичная работа с объектом DataFrame
## Описание

### Цели недели

В рамках этой недели начнем изучать возможности библиотеки Pandas для анализа данных и рассмотрим материал, касающийся различных источников данных, предобработки данных и работы с объектом DataFrame в Pandas.

### После освоения темы:
- Вы узнаете виды, источники и способы хранения данных (csv, tsv-файлы и другие)
- Узнаете структуры данных и инструменты, предоставляемые библиотекой Pandas для работы с данными
- Сможете выполнять выгрузку данных с использованием библиотеки Pandas
- Сможете проводить предварительную обработку данных с использованием библиотеки Pandas — получать информацию о DataFrame, работать со строками и столбцами
- Сможете осуществлять группировку и агрегацию таблиц с использованием Pandas

### План занятия
- Виды и источники данных
- Предобработка данных
- Первичная работа с DataFrame
- Введение в агрегирование и сводные таблицы

### Используемые термины

__Источник данных__ — ресурс, из которого мы берем данные для анализа

__Репозиторий__ — место хранения данных

__.csv (comma-separated values)__ — значения, разделенные запятыми

__.tsv (tabulation-separated values)__ — разделителем выступает табуляция

__.sav__ — расширение баз данных формата пакета SPSS (часто используется опросными компаниями, социологическими службами)

__.dta__ — расширение пакета Stata (научные исследования)

__.xls, .xlsx__ — расширения Excel

__.json__ — текстовый формат обмена данными, основанный на JavaScript

__.rmd__ — формат сохранения данных пакета R Studio (на базе языка R, популярного для статистики)

__Data pre-processing__ — исследование структуры данных на предмет возможности протестировать необходимые аналитические гипотезы и соответствующая коррекция имеющейся базы данных

### Итоги занятия

1.  Источник данных — это ресурс, из которого мы берем данные для анализа. Репозиторий Kaggle хранит коллекции самых различных данных, которые можно использовать в тренировочных целях для анализа данных


2.  Данные хранятся в файлах с разными расширениями. Часто используют csv-файлы, в которых значения разделены запятыми. Python позволяет выгрузить данные в специальную структуру — датафрейм


3.  Важно проверять используемые данные на достоверность


4.  Предобработка данных (data pre-processing) — это исследование структуры данных на возможность протестировать необходимые аналитические гипотезы и соответствующая коррекция имеющейся базы данных


5.  При предобработке используют методы библиотеки Pandas языка программирования Python. Методы библиотеки Pandas позволяют получить информацию о DataFrame, работать с дубликатами и пропущенными значениями. Полная информация о работе с объектом DataFrame содержится в документации


6.  Первичное исследование структуры данных DataFrame может быть выполнено с помощью функций:
- __head(n)__ — вывод первых n строк DataFrame
- __tail(n)__ — вывод последних n строк DataFrame
- __describe()__ — вывод описательных статистик (только для колонок типа float и int)

7.  Мы можем обратиться к содержимому DataFrame поэлементно или выбрать подтаблицу, используя индексацию — функции loc (получает строки и/или столбцы с определенными метками) и iloc (получает строки и/или столбцы по определенным целочисленным позициям)


8.  Pandas включает методы агрегации данных, то есть обобщение вложенных структур данных. Для группировки данных по одному или нескольким столбцам и применения функций агрегирования к группам используют метод groupby


9.  Еще один инструмент обобщения и представления данных — сводные таблицы, которые реализуются с помощью метода pivot_table. Сводная таблица позволяет просмотреть данные в более удобном формате
---

### В результате выполнения заданий вы сможете:

- Проводить предварительную обработку данных с использованием
библиотеки Pandas — получать информацию о DataFrame, работать со строками и столбцами
- Осуществлять группировку и агрегацию таблиц с использованием Pandas

### Вот некоторые функции библиотеки Pandas, которые можно использовать для предобработки данных и исследования данных: 

- __info()__ — выводит краткую сводку о DataFrame
- __isnull()__ — возвращает объект, содержащий булевы значения, которые показывают, какие значения отсутствуют
- __dropna()__ — по умолчанию удаляет все строки, где есть хотя бы одно пропущенное значением в колонках
- __duplicated()__ – возвращает булев объект Series, который для каждой строки показывает, есть в ней дубликаты или нет
- __drop_duplicates()__ — удаляет повторяющиеся строки