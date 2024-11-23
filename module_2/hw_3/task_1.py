''' Задача 1
Построение дашборда

Для выполнения задания вам понадобится набор данных. Мы предлагаем
на выбор три набора данных в порядке возрастания сложности работы с ними.

Выберите один из них:
- Показатели результативности российских вузов: объединенные
    данные за 2013–2017 годы (ссылка на данные и их техническое описание)

- Загрязнение поверхностных вод в России: ежемесячные данные
    о высоком и экстремально высоком загрязнении водных объектов
    за 2008–2021 гг. (ссылка на данные и их техническое описание)

    В этом датасете несколько таблиц, нужно выбрать подходящие для вашей задачи
    и, при необходимости, соединить их нужным образом.

- Экспорт и импорт российских регионов: таможенная статистика
    с детализацией до товаров за 2016–2021 гг. (ссылка на данные
    и их техническое описание)


Что обязательно сделать перед построением дашборда по этому конкретному датасету:
1. В поле code вместо числовых кодов подставить названия,
    взяв их из ТН ВЭД (например, вместо «8458» должно быть
    «станки токарные» и т.д.)

2. В поле country вместо Alpha2-кода подставить название
    страны (например, вместо RU должно быть «Россия» и т.д.)

3. В полях region и district также должны быть заменены
    числовые коды на названия регионов

4. Данных очень много, если будут проблемы с работой визуализационных
    инструментов, подумайте, какое подмножество данных можно
    отобрать (семплировать) так, чтобы сохранить интересные закономерности


Указанные выше дополнения важны, поскольку приведение данных в отчетах и дашбордах
к доступному для восприятия человека виду — неотъемлемая часть работы специалиста по данным.


Что нужно сделать:
Построить дашборд по выбранному датасету с учетом технических требований:
1. Дашборд выполняется либо с использованием сервиса
    Yandex DataLens, либо библиотеки Altair

2. В качестве решения задания прикрепите ссылку
    на построенный график в Yandex DataLens или
    ссылку на Python-ноутбук с решением

3. Если выполнялась какая-либо нетривиальная
    предобработка данных, опишите ее отдельным
    текстовым пояснением

Важно:
- Дашборд предназначен для работы с данными «в моменте» (если данные исторические,
    для исследовательского анализа и поиска закономерностей в данных) и не должен быть
    абсолютно статичным: у пользователя должна быть возможность хотя бы минимально
    управлять «видом на данные». Хорошо, когда на дашборде присутствуют уместные фильтры,
    а на диаграммах настроены tooltips с детализацией данных

- Цель дашборда: обеспечить пользователю среду для формирования мыслей по данным

- В задании предполагается, что в идеале дашборд может помочь вам
    самим самостоятельно увидеть интересные особенности в данных'''


# import pandas as pd
# import altair as alt
#
#
# alt.themes.enable('dark')
# alt.data_transformers.disable_max_rows()
#
# superstore_data = pd.read_excel('superstore.xlsx')
# superstore_data = superstore_data.set_index('Row ID')
# superstore_data['Order Date'] = pd.to_datetime(superstore_data['Order Date'])
# superstore_data['Ship Date'] = pd.to_datetime(superstore_data['Ship Date'])
# superstore_data.head(1)
#
#
# selection = alt.selection_multi(fields=['Customer Segment'], bind='legend')
#
# chart = alt.Chart(
#     superstore_data
# ).mark_bar(
# ).add_selection(
#     selection
# ).encode(
#     x='day(Order Date):O',
#     y=alt.Y('mean(Sales)', axis=alt.Axis(grid=False)),
#     color=alt.condition(selection, 'Customer Segment',
# alt.ColorValue('darkgrey')),
#     opacity=alt.condition(selection, alt.value(1), alt.value(0.3))
# ).properties(
#     width=500
# )
# print(chart)


import pandas as pd
import altair as alt


# Загрузите данные из csv-файла и преобразуйте в объект DataFrame
df = pd.read_csv("./dataset/data.csv", sep=";")
print(f"Объект DataFrame:\n{df.head(15).to_string()}\n\n")


# Создание словарей для замены кодов на названия (предполагается, что есть файл с кодами и названиями)
# 1. ТН ВЭД
#tn_ved = pd.read_csv("tn_ved.csv", sep=";")
#code_to_name = dict(zip(tn_ved["code"], tn_ved["name"]))

# 2. Страны
#countries = pd.read_csv("countries.csv", sep=";")
#code_to_country = dict(zip(countries["code"], countries["name"]))

# 3. Регионы и районы
#regions = pd.read_csv("regions.csv", sep=";")
#code_to_region = dict(zip(regions["code"], regions["name"]))

#districts = pd.read_csv("districts.csv", sep=";")
#code_to_district = dict(zip(districts["code"], districts["name"]))


# Замена кодов на названия
#df["code"] = df["code"].map(code_to_name)
#df["country"] = df["country"].map(code_to_country)
#df["region"] = df["region"].map(code_to_region)
#df["district"] = df["district"].map(code_to_district)


# Сохранение обработанного датасета
#df.to_csv("processed_dataset.csv", sep=";", index=False)


# Предобработка данных
df["year"] = pd.to_datetime(df["year"], format="%Y")
print(f'Преобразованное поле в формат datetime для удобства использования в Altair:\n{df["year"]}\n\n')

df["total_students"] = df["e1"] + df["e2"] + df["e3"] + df["e4"] + df["e5"] + df["e6"]
print(f'Сумма значений полей e1, e2, e3, e4, e5, e6:\n{df["total_students"]}\n\n')

df["rnd_efficiency"] = df["rnd"] / df["total_income"]
print(f'Отношение rnd к total_income:\n{df["rnd_efficiency"]}\n\n')


# Фильтр по году
year_filter = alt.binding_select(options=list(df["year"].dt.year.unique()), name="Год:")
year_selection = alt.selection_point(bind=year_filter, fields=["year"], clear=False)

df_sample = df.sample(frac=0.1)

# Создание диаграмм
chart_students = alt.Chart(df_sample).mark_bar().encode(
    alt.X("year:T", title="Год"),
    alt.Y("total_students:Q", title="Количество студентов"),
    color="federal_district_short:N",
    tooltip=["name", "year", "rnd_efficiency", "federal_district", "region_name"],
).add_params(year_selection).transform_filter(str(year_selection))

chart_efficiency = alt.Chart(df_sample).mark_point().encode(
    alt.X("year:T", title="Год"),
    alt.Y("rnd_efficiency:Q", title="Эффективность НИОКР"),
    color="federal_district_short:N",
    tooltip=["name", "year", "rnd_efficiency", "federal_district", "region_name"],
).add_params(year_selection).transform_filter(str(year_selection))


# Композиция дашборда
t = alt.vconcat(
    chart_students,
    chart_efficiency
).configure_axis(labelFontSize=12, titleFontSize=14).configure_title(fontSize=18).configure_legend(labelFontSize=12, titleFontSize=14).configure_view(strokeWidth=0)


alt.Chart.save(t, "my_dashboard.json", ppi=200)
print(1)