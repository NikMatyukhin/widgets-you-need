# This Python file uses the following encoding: utf-8
import sys
from random import randint, shuffle

from PySide2.QtWidgets import QApplication, QMainWindow, QColorDialog, QGraphicsScene, QGraphicsItem, QMessageBox
from PySide2.QtCore import Qt, QRectF
from PySide2.QtGui import QColor, QBrush, QPen, QIcon

from ui_mainwindow import Ui_MainWindow


def fibonacci_sequence():
    sequence = [1]
    a = b = 1
    for _ in range(97):
        sequence.append(b)
        a, b = b, a + b
    return sequence


class QPointGraphicsItem(QGraphicsItem):
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def boundingRect(self):
        return QRectF(self.x, self.y, 1., 1.)

    def paint(self, painter, option, widget):
        painter.drawPoint(self.x, self.y)


class MainWindow(QMainWindow):
    def __init__(self):
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

        self.ui.pushButton.clicked.connect(self.color_dialog_clicked)
        self.ui.lineEdit.textChanged.connect(self.line_edit_changed)
        self.ui.calendarWidget.clicked.connect(self.calendar_clicked)
        self.ui.spinBox.valueChanged.connect(self.fibonacci_num_changed)
        self.ui.horizontalSlider.valueChanged.connect(self.fibonacci_num_changed)
        self.ui.pushButton_4.clicked.connect(self.circle_paint_clicked)
        self.ui.pushButton_5.clicked.connect(self.fractal_create_clicked)
        self.ui.pushButton_6.clicked.connect(self.fractal_clear_clicked)
        self.ui.pushButton_2.clicked.connect(self.shuffle_text_clicked)
        self.ui.pushButton_3.clicked.connect(self.unwind_text_clicked)

    def color_dialog_clicked(self):
        color = QColorDialog.getColor(Qt.white, self, 'Выберите цвет, пожалуйста')
        color_text = color.name()
        self.ui.label_3.setStyleSheet(f'color: {color_text}')
        self.ui.label_3.setText(color_text)

    def line_edit_changed(self, text):
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
        date_text = date.toString('dd.MM.yyyy')
        self.ui.label_4.setText('Текущая дата: ' + date_text)

    def fibonacci_num_changed(self, pos):
        self.ui.horizontalSlider.setValue(pos)
        self.ui.spinBox.setValue(pos)
        self.ui.label_6.setText(str(pos))
        self.ui.label_7.setText(str(self.fibonacci_sequence[pos - 1]))

    def shuffle_text_clicked(self):
        shuffled_text = list(self.ui.textEdit.toPlainText())
        shuffle(shuffled_text)
        self.ui.textEdit_2.setText(''.join(shuffled_text))

    def unwind_text_clicked(self):
        self.ui.textEdit_2.setText(self.ui.textEdit.toPlainText())

    def circle_paint_clicked(self):
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
        if self.is_clear:
            if self.ui.doubleSpinBox_3.value() == self.ui.doubleSpinBox_4.value() == .0 or \
               self.ui.doubleSpinBox_5.value() == self.ui.doubleSpinBox_6.value() == .0 or \
               self.ui.doubleSpinBox_7.value() == self.ui.doubleSpinBox_8.value() == .0:
                QMessageBox.critical(self, 'Ошибочка вышла', 'Я не буду рисовать точки на нулевых координатах!')
            else:
                self.is_clear = False
                current_point = QPointGraphicsItem()
                current_point.set_pos(randint(0, self.fractal_scene.width()),
                                      randint(0, self.fractal_scene.width()))
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
        self.fractal_scene.clear()
        self.is_clear = True

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle('Widgets you need')
    window.setWindowIcon(QIcon('icon.png'))
    window.show()
    sys.exit(app.exec_())
