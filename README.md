# **Оглавление**

* Введение
* Установка
* Цвета
* Даты
* Текст
* Числа
* Рисование


## Widgets you need

Для выполнения шестой практической работы по дисциплине ВвПД 1 курса "Программной инженерии" ИКИТ СФУ требуется добавить к своему коду GUI.             
Однако, не все студенты знакомы с [Qt](https://doc.qt.io/qtforpython/) и тем, какие интересные виджеты и готовые диалоговые окна он предоставляет. Для этого и был создан этот проект. Я постарался уместить сюда все виджеты, которые могут быть использованы в вариантах заданий.


## Установка пакетов

В привычном для нас PyPi вы не найдёте официального пакета для разработки на Qt с Python (можно попробовать [PyQt5](https://www.youtube.com/watch?v=dQw4w9WgXcQ), но лучше всё же обратить внимание на официальное решение). Чтобы установить PySide2 и shiboken2 (система для предоставления API Qt C++ для Python), нужно перейти по [этой](http://download.qt.io/) ссылке, и пройти по следующему пути:

> snapshots / ci / pyside / 5.15 / latest / pyside2 /

Вы окажетесь в папке с .whl файлами. Нам нужны файлы `PySide2-5.15*win_amd64.whl` и `shiboken2-5.15*win_amd64.whl`, если вы сидите на Windows. Для других ОС выбираете соответствующие файлы. После того, как скачаете эти файлы, просто воспользуйтесь пакетным менеджером pip:

> pip install shiboken2-5.15.0a1.dev1605705360-5.15.2-cp35.cp36.cp37.cp38.cp39-none-win_amd64.whl
> pip install PySide2-5.15.0a1.dev1605705360-5.15.2-cp35.cp36.cp37.cp38.cp39-none-win_amd64.whl

Если ошибок не произошло, то проект должен запуститься без проблем.


## Ввод цвета

Нужно получить код какого-либо цвета, а писать проверку ввода вручную лень? Можно воспользоваться классом [QColorDialog](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QColorDialog.html). Помимо создания и настройки окошка выбора с нуля тут стоит обратить внимение на статический метод `getColor(initial, parent, title, options)`. Метод позволяет открыть окно выбора в палитре и с последующем возвратом выбранного цвета. Полученный объект класса `QColor` обладает методом `name()`, который по умолчанию возвращает цвет в виде строки в формате #RRGGBB.

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/1.gif "Цвета меняются")


## Ввод даты

Нужно получить определённый день, месяц и год, а писать проверку снова лень? Для этих целей придуманы виджеты [QDateEdit](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QDateEdit.html) и [QCalendarWidget](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QCalendarWidget.html). Первый жутко неудобный для пользователя, поэтому остановимся на втором виджете. Он позволяет открыть красивую таблицу с календарём, в котором пользователь может сам выбрать необходимую ему дату. Выбранную дату можно получить через метод `selectedDate()` - будет возвращен объект класса `QDate`, который обладает методом `toString(format)`, который возвращает строку даты, соответствующую переданному формату.

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/3.gif "Календарь делает бррр")


## Ввода строковых значений

Порой, печать в консоль надоедает. Хочется снова наблюдать привычные окошки с краями и полосами прокрутки. Чтобы реализовать ввод текстовых данных в Qt предусмотрены два интересных виджета - [QLineEdit](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLineEdit.html) и [QTextEdit](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QTextEdit.html). Принцип работы у обоих виджетов примерно одинаковый. Изменение текста в них отслеживается сигналом `textChanged[text]`, который вместе с собой передаёт их текущий текст. Получить текущий текст можно из объекта `QLineEdit` методом `text()`, а из объекта `QTextEdit` - методом `toPlainText()`. Установка текста происходит посредством метода `setText(text)`.

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/2.gif "Квадратик мигает так приятно")

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/5.gif "Адвпдырвопрыловрп")


## Ввод числовых значений

Числовые значения постоянно нужно проверять на соответствие типу, формату, диапазону значений и т.д и т.п. Специально для этого существуют счётчики [QSpinBox](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QSpinBox.html) и [QDoubleSpinBox](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QDoubleSpinBox.html), а также ползунок [QSlider](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QSlider.html). Первые два - счётчики - предназначены для изменения значения в некотором заданном диапазоне с определённым шагом при помощи стрелок. Метод `value()` для первого возвращает целое число, а для второго - число с плавающей точкой. Ползунок работает примерно таким же образом: задаётся диапазон значений, меняется текущее значение. Для всех трёх виджетов работает сигнал `valueChanged[int]` (`valueChanged[double]`), испускаемый во время изменения текущего значения.

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/4.gif "1, 1, 2, 3, 5, что там дальше?")


## Рисование

Свободное рисование того, чего душа пожелает, в Qt представлено классами [Graphics View Framework](https://doc.qt.io/qtforpython/overviews/graphicsview.html#graphics-view-framework) (для начала попробуем поработать с тремя классами) - [QGraphicsView](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QGraphicsView.html), [QGraphicsScene](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QGraphicsScene.html) и [QGraphicsItem](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QGraphicsItem.html). Каждый класс здесь входит в свою иерархию: `QGraphicsItem` задаёт правило отрисовки какого-либо объекта, `QGraphicsScene` отрисовывает множество переданных ей `QGraphicsItem`, а `QGraphicsView` служит представлением того, что содержит `QGraphicsScene`. Чтобы рисовать на нашей "сцене" нам достаточно вызвать её соответствующие методы: `addEllipse()` для рисования кругов и овалов, `addRect()` для рисования прямоугольников, `addLine()` для отрисовки линий, `addItem()` для отрисовки специфичного объекта - правила для его рисования мы задаём сами в классе наследнике. Чтобы это всё отображалось в конкретном представлении, необходимо у `self.ui.graphicsView` вызвать метод `setScene(scene)`, который позволит конкретному представлению отслеживать изменения конкретной сцены.

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/6.gif "Раз кружочек, два кружочек...")

**Пример взаимодействия:**

![Не прогрузилось, а жаль](gifs/7.gif "Мы сделали тебе треугольник в треугольнике")

---

По всем вопросам (или идеям для дополнения) пишите в социальной сети [ВКонтакте](https://vk.com/ikit.nikit).