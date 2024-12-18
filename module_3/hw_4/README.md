# Основы нейронных сетей
## Описание

### Цели недели

На этой неделе мы погрузимся в основы нейронных сетей и изучим архитектуры, используемые для создания различных типов нейросетей. Этот материал дает обзорное представление о нейросетях для последующего более глубокого изучения в следующем семестре.

### После освоения темы:
- Вы познакомитесь с терминологией, используемой в нейросетях, и архитектурами нейронных сетей
- Узнаете основные библиотеки Python, используемые для работы с нейросетями
- Сможете написать программу для вычисления результата сигмоидальной функции активации для заданных входных данных
- Сможете написать код, реализующий свертку изображения и фильтра
- Сможете реализовать простую нейросеть, состоящую из одного входного слоя, одного скрытого слоя и одного выходного слоя

### План занятия
- Основы нейронных сетей
- Архитектуры нейронных сетей

### Используемые термины

__Нейронная сеть__ — алгоритм машинного обучения, который использует математические функции, моделирующие работу мозга, чтобы извлекать закономерности из данных.

__Нейрон в нейронной сети__ — элементарная единица обработки информации, которая принимает входные данные, обрабатывает их и генерирует выходные данные.

__Глубокое обучение (Deep Learning)__ — подмножество нейронных сетей, которые имеют множество скрытых слоев и позволяют извлекать более сложные закономерности из данных.

__Сверточная нейросеть (Convolutional Neural Network, CNN)__ — одна из самых популярных и мощных архитектур нейронных сетей, применяемых в обработке изображений, видео и звука.

__Рекуррентные сверточные нейронные сети (Recurrent Convolutional Neural Network, RCNN)__ — комбинация сверточных и рекуррентных слоев, которая позволяет моделировать пространственные и временные зависимости в данных.

### Итоги занятия

1. Нейронная сеть использует математические функции для извлечения закономерностей из данных. Использование нейронов в нейронных сетях имитирует работу биологических нейронов и позволяет обрабатывать информацию. 


2. Нейроны в нейронной сети принимают входные данные, обрабатывают их и передают результаты следующим нейронам. 


3. Библиотеки Python для работы с нейросетями: __TensorFlow, Keras, PyTorch и Caffe__.


4. __Сверточные нейросети (Convolutional Neural Network, CNN)__ — мощная архитектура для обработки изображений, видео и звука, использующая __свойства локальности и инвариантности__. Они состоят из нескольких типов слоев, включая сверточные, активационные и полносвязные слои, которые позволяют выделять признаки, классифицировать и нормализовать данные.

__Преимущества CNN включают:__
- Эффективную обработку больших объемов данных
- Возможность автоматического извлечения признаков

__Но требуют:__
- Сложной настройки параметров
- Большого количества обучающих данных


5. __Рекуррентная нейросеть (Recurrent Neural Network, RNN)__ - используется для обработки последовательных данных и сохранения контекста входных данных. Архитектура RNN включает слои, которые обрабатывают данные и обновляют скрытое состояние.

__Преимущества RNN включают:__ 
- Обработку последовательных данных различной длины
- Использование предыдущего контекста для прогнозирования будущих значений


6. Современные нейросетевые продукты используют различные архитектуры — __автоэнкодер, рекуррентные сверточные нейронные сети, трансформер и U-Net__.

С их помощью решаются такие задачи, как: 
- Сжатие изображений
- Устранение шума из аудио
- Обработка текстов и аудиофайлов
- Сегментация изображений и лечение рака
---

### В результате выполнения заданий вы сможете:

- Написать программу для вычисления результата сигмоидальной функции активации для заданных входных данных
- Написать код, реализующий свертку изображения и фильтра
- Реализовать простую нейросеть, состоящую из одного входного слоя, одного скрытого слоя и одного выходного слоя