# This Python file uses the following encoding: utf-8
import sys
from random import randint, shuffle

# Импортируем нужные нам модули и классы из соответствующих модулей PySide2
# Их гораздо больше, поэтому ограничимся только самым необходимым
# QtWidgets - классы для расширения графического интерфейса Qt с помощью виджетов
# QtCore - основные неграфические классы, используемые другими модулями
# QtGui - базовые классы для компонентов графического интерфейса пользователя (GUI)
from PySide2.QtWidgets import QApplication, QMainWindow, QColorDialog, QGraphicsScene, QGraphicsItem, QMessageBox
from PySide2.QtCore import Qt, QRectF
from PySide2.QtGui import QColor, QBrush, QPen, QIcon

from ui_mainwindow import Ui_MainWindow


def fibonacci_sequence():
    '''Генерация ряда Фибоначчи
    
    Создаёт список из первых 98 чисел ряда Фибоначчи
    Использовать будем гораздо меньшее количество, я просто хочу 98
    
    '''
    sequence = [1]
    a = b = 1
    for _ in range(97):
        sequence.append(b)
        a, b = b, a + b
    return sequence


class QPointGraphicsItem(QGraphicsItem):
    '''
    Считайте это забавным, но чтобы нарисовать жалкий пиксель (точку),
    нам необходимо наследоваться и переопределять соответствующие методы
    у класса QGraphicsItem, потому что drawPoint может делать только класс
    QPainter, а QGraphicsScene так не умеет
    :ivar x: координата по X
    :ivar y: координата по Y
    :vartype x: float
    :vartype y: float
    
    '''
    def set_pos(self, x, y):
        '''Установка координат
        
        :param x: координата по X
        :type x: float
        :param y: координата по Y
        :type y: float
        
        '''
        self.x = x
        self.y = y

    def boundingRect(self):
        '''Возвращение границ объекта
        
        Обязательно переопределяемый метод класса. Нужен для
        просчитывания столкновения с объектом и его отрисовки
        
        :returns: прямоугольник с границами объекта
        :rtype: :class:`QRectF`
        
        '''
        return QRectF(self.x, self.y, 1., 1.)

    def paint(self, painter, option, widget):
        '''Отрисовка объекта
        
        Обязательно переопределяемый метод класса. Нужен для
        отрисовки объекта через объект класса QPainter
        
        '''
        painter.drawPoint(self.x, self.y)


class MainWindow(QMainWindow):
    '''Класс главного окна. И сказать-то нечего
    
    Здесь хранится вся логика нашего приложения. В идеале -
    только логика взаимодействия с пользователем. Все окошки,
    заполнения полей и нажатия на кнопки должны обрабатываться
    в этом классе. Доступ к элементам GUI осуществляется через
    атрибут self.ui.<название элемента интерфейса>
    
    '''
    def __init__(self):
        '''Инициализация окна
        
        Здесь настраивается то, что нельзя настроить в QtDesigner.
        Слоты (методы) соединяются с сигналами элементов интерфейса,
        создаются какие-либо вспомогательные объекты, флаги и т.п.
        
        :ivar fibonacci_sequence: последовательность ряда Фибоначчи
        :vartype fibonacci_sequence: list
        :ivar circle_scene: графическая сцена для отрисовки трёх кругов
        :vartype circle_scene: QGraphicsScene
        :ivar circle_brushes: набор кистей трёх цветов для рисования трёх кругов
        :vartype circle_brushes: list
        :ivar circle_queue: очередь для рисования кругов (чтобы всегда было лишь три круга)
        :vartype circle_queue: list
        :ivar fractal_scene: графическая сцена для отрисовки фрактального треугольника
        :vartype fractal_scene: QGraphicsScene
        :ivar is_clear: флаг чистой сцены, чтобы не начинать отрисовку, пока сцену не очистят
        :vartype is_clear: boolean
        :ivar vertex: список вершин фрактального треугольника
        :vartype vertex: list
        
        '''
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fibonacci_sequence = fibonacci_sequence()

        self.circle_scene = QGraphicsScene()
        self.circle_brushes = [QBrush(QColor(255, 0, 0, 128)),
                               QBrush(QColor(0, 255, 0, 128)),
                               QBrush(QColor(0, 0, 255, 128)),
                               ]
        self.circle_queue = []
        self.ui.graphicsView.setScene(self.circle_scene)

        self.fractal_scene = QGraphicsScene()
        self.is_clear = True
        self.vertex = []
        self.ui.graphicsView_2.setScene(self.fractal_scene)

        # Блок с соединением сигналов и слотов. Сейчас попробую объяснить.
        # Каждый элемент интерфейса при взаимодействии с ним испускает какой-либо
        # сигнал. Например, при нажатии на кнопку генерируется сигнал clicked, а при
        # зажатии - pressed. Связав какой-либо метод с таким сигналом, Qt гарантирует,
        # что при появлении в очереди определённого сигнала, будут вызваны все методы,
        # которые присоединены к этому сигналу. Такие события в Qt и именуют сигналами.
        # А методы, которые реагируют на сигналы, называют слотами (slots)
        
        self.ui.pushButton.clicked.connect(self.color_dialog_clicked) # нажатие на кнопку
        self.ui.lineEdit.textChanged.connect(self.line_edit_changed) # изменение текста в строке
        self.ui.calendarWidget.clicked.connect(self.calendar_clicked) # нажатие по календарю
        self.ui.spinBox.valueChanged.connect(self.fibonacci_num_changed) # смена значения в спинбоксе
        self.ui.horizontalSlider.valueChanged.connect(self.fibonacci_num_changed) # движение слайдера
        self.ui.pushButton_4.clicked.connect(self.circle_paint_clicked) # нажатие на кнопку
        self.ui.pushButton_5.clicked.connect(self.fractal_create_clicked) # нажатие на кнопку
        self.ui.pushButton_6.clicked.connect(self.fractal_clear_clicked) # нажатие на кнопку
        self.ui.pushButton_2.clicked.connect(self.shuffle_text_clicked) # нажатие на кнопку
        self.ui.pushButton_3.clicked.connect(self.unwind_text_clicked) # нажатие на кнопку

    def color_dialog_clicked(self):
        '''Создание цветной надписи
        
        В первом блоке интерфейса можно нажать на кнопку "Выбери меня!", откуда
        последует сигнал к этому слоту. Здесь создаётся окно для выбора цвета,
        выделяется имя этого цвета, а затем метке присваивается текст этого имени
        и стиль оформления (цвет текста) с выбранным цветом
        
        '''
        color = QColorDialog.getColor(Qt.white, self, 'Выберите цвет, пожалуйста')
        color_text = color.name()
        self.ui.label_3.setStyleSheet(f'color: {color_text}')
        self.ui.label_3.setText(color_text)

    def line_edit_changed(self, text):
        '''Проверка написания строки
        
        Во втором блоке интерфейса можно в строку написать любой набор символов. Здесь
        происходит классификация введенных значений при помощи простых строковых функций.
        В связи с полученным результатом квадратик справа от строки получает соответствующий
        стиль оформления (цвет фона)
        
        '''
        if text:
            if text.isalpha():
                self.ui.label_9.setStyleSheet(f'background-color: red; border: 1px solid black;')
            elif text.isdigit():
                self.ui.label_9.setStyleSheet(f'background-color: yellow; border: 1px solid black;')
            else:
                self.ui.label_9.setStyleSheet(f'background-color: green; border: 1px solid black;')
        else:
            self.ui.label_9.setStyleSheet(f'background-color: white; border: 1px solid black;')

    def calendar_clicked(self, date):
        '''Форматирование даты
        
        В третьем блоке интерфейса можно выбрать любую дату в календаре. Затем эта
        дата будет сконвертирована в строку соответствующего формата и установлена
        на соответствующую метку в качестве текста
        
        '''
        date_text = date.toString('dd.MM.yyyy')
        self.ui.label_4.setText('Текущая дата: ' + date_text)

    def fibonacci_num_changed(self, pos):
        '''Изменение числа Фибоначчи
        
        В четвёртом блоке можно либо передвигать слайдер, либо менять значения спинбокса.
        Не зависимо от взаимодействия, в метод будет передано число - текущее значение спинбокса
        или слайдера - номер нужного нам элемента ряда Фибоначчи. Остается только назначить метке
        в качестве текста это число и скорректировать значение в противоположном виджете
        
        '''
        self.ui.horizontalSlider.setValue(pos)
        self.ui.spinBox.setValue(pos)
        self.ui.label_6.setText(str(pos))
        self.ui.label_7.setText(str(self.fibonacci_sequence[pos - 1]))

    def shuffle_text_clicked(self):
        '''Перемешивание текста
        
        В пятом блоке можно напечатать текст в первое окошко, а по нажатию на кнопку "Запутать"
        получить во втором окне перемешанный текст. Преобразование текста в list необходимо, т.к.
        функция shuffle не работает со строками
        
        '''
        shuffled_text = list(self.ui.textEdit.toPlainText())
        shuffle(shuffled_text)
        self.ui.textEdit_2.setText(''.join(shuffled_text))

    def unwind_text_clicked(self):
        '''Исправление текста
        
        В пятом блоке можно напечатать текст в первое окошко, а по нажатию на кнопку "Распутать"
        получить во втором окне копию этого текста
        
        '''
        self.ui.textEdit_2.setText(self.ui.textEdit.toPlainText())

    def circle_paint_clicked(self):
        '''Отрисовка кругов
        
        В шестом блоке можно выбрать координаты текущего круга и его радиус, а по нажатию
        на кнопку "Отрисовать" увидеть на сцене круг соответствующего цвета. Цвета прозрачны
        на 50%, поэтому видно все пересечения этих кругов (как удобно)
        
        '''
        self.circle_scene.clear()
        self.circle_queue.append([self.ui.doubleSpinBox.value(),
                                  self.ui.doubleSpinBox_2.value(),
                                  self.ui.spinBox_2.value(),
                                  self.ui.spinBox_2.value(),
                                  ])
        if len(self.circle_queue) == 4:
            self.circle_queue.pop(0)
            self.circle_brushes.append(self.circle_brushes.pop(0))
        for circle, brush in zip(self.circle_queue, self.circle_brushes):
            self.circle_scene.addEllipse(*circle, QPen(Qt.black), brush)
        self.circle_scene.update()

    def fractal_create_clicked(self):
        '''Отрисовка фрактального треугольника
        
        В седьмом блоке можно назначить через соответсвующие спинбоксы координаы для вершин
        треугольника, внутри которого будет отрисовываться фрактальный рисунок (треугольник
        Серпинского, если интересно). После одной успешной отрисовки мы блокируем холст
        через флажок self.is_clear, который будет снят методом очистки
        
        '''
        if self.is_clear:
            if self.ui.doubleSpinBox_3.value() == self.ui.doubleSpinBox_4.value() == .0 or \
               self.ui.doubleSpinBox_5.value() == self.ui.doubleSpinBox_6.value() == .0 or \
               self.ui.doubleSpinBox_7.value() == self.ui.doubleSpinBox_8.value() == .0:
                QMessageBox.critical(self, 'Ошибочка вышла', 'Я не буду рисовать точки на нулевых координатах!')
            else:
                self.is_clear = False
                current_point = QPointGraphicsItem()
                current_point.set_pos(randint(0, 100),
                                      randint(0, 100))
                vertex = [(self.ui.doubleSpinBox_3.value(), self.ui.doubleSpinBox_4.value()),
                          (self.ui.doubleSpinBox_5.value(), self.ui.doubleSpinBox_6.value()),
                          (self.ui.doubleSpinBox_7.value(), self.ui.doubleSpinBox_8.value()),
                          ]
                for _ in range(10000):
                    self.fractal_scene.addItem(current_point)
                    direction = randint(0,2)
                    d_x = (vertex[direction][0] + current_point.x) / 2
                    d_y = (vertex[direction][1] + current_point.y) / 2
                    current_point = QPointGraphicsItem()
                    current_point.set_pos(d_x, d_y)

    def fractal_clear_clicked(self):
        '''Очистка сцены фрактального треугольника
        
        В седьмом блоке можно очистить окно путём вызова у сцены метода clear(),
        а также изменением флага self.is_clear, чтобы запустить отрисовку повторно
        
        '''
        self.fractal_scene.clear()
        self.is_clear = True

# Тут совсем ничего интересного. Если файл не запущен как подключаемый модуль, то создаётся
# наше главное окно, запускается цикл обработки событий и начинается привычная работа приложения
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle('Widgets you need')
    window.setWindowIcon(QIcon('icon.png'))
    window.show()
    sys.exit(app.exec_())
