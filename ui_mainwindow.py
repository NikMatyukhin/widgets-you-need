# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 160, 80))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 50, 140, 20))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(10, 10, 140, 16))
        self.label.setCursor(QCursor(Qt.ArrowCursor))
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 90, 20))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QRect(100, 30, 50, 20))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 100, 301, 201))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.frame_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 10, 280, 156))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 280, 20))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 310, 301, 71))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.spinBox = QSpinBox(self.frame_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(10, 10, 60, 30))
        font = QFont()
        font.setFamily(u"System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(40)
        self.spinBox.setValue(1)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 10, 120, 30))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 10, 20, 30))
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizontalSlider = QSlider(self.frame_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 39, 280, 21))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(40)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(226, 9, 60, 30))
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 390, 301, 161))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 90, 130, 60))
        self.textEdit_2 = QTextEdit(self.frame_4)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(160, 90, 130, 60))
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 280, 40))
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 60, 130, 20))
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(160, 60, 130, 20))
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(180, 10, 610, 80))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 561, 20))
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(580, 50, 20, 20))
        self.label_9.setStyleSheet(u"background-color: white;\n"
" border: 1px solid black;")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 591, 31))
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(320, 100, 470, 220))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.graphicsView = QGraphicsView(self.frame_6)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 300, 200))
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 100, 80, 20))
        self.doubleSpinBox = QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(320, 30, 60, 20))
        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(400, 30, 60, 20))
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(320, 10, 140, 20))
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(320, 50, 140, 20))
        self.spinBox_2 = QSpinBox(self.frame_6)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(320, 70, 40, 20))
        self.spinBox_2.setMinimum(50)
        self.spinBox_2.setMaximum(130)
        self.spinBox_2.setValue(50)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(320, 330, 470, 220))
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.graphicsView_2 = QGraphicsView(self.frame_7)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(10, 10, 300, 200))
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(320, 10, 140, 40))
        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 50, 60, 20))
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(320, 90, 60, 20))
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(320, 130, 60, 20))
        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setGeometry(QRect(320, 70, 65, 20))
        self.doubleSpinBox_4 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setGeometry(QRect(395, 70, 65, 20))
        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setGeometry(QRect(320, 110, 65, 20))
        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setGeometry(QRect(395, 110, 65, 20))
        self.doubleSpinBox_7 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setGeometry(QRect(320, 150, 65, 20))
        self.doubleSpinBox_8 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setGeometry(QRect(395, 150, 65, 20))
        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(320, 180, 61, 30))
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(390, 180, 70, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menubar.setStyleSheet(u"background-color: rgb(106, 106, 106)")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(106, 106, 106)")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u043c\u0435\u043d\u044f!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0430\u0435\u043c \u043d\u0443\u0436\u043d\u044b\u0439 \u043d\u0430\u043c \u0446\u0432\u0435\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442:", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0434\u0430\u0442\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"-\u0435 \u0447\u0438\u0441\u043b\u043e \u0424\u0438\u0431\u043e\u043d\u0430\u0447\u0447\u0438 \u044d\u0442\u043e ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u0430\u0442\u0438\u0435 \u043d\u0430 \u043f\u0435\u0440\u0432\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 \u043f\u0435\u0440\u0435\u043c\u0435\u0448\u0438\u0432\u0430\u0435\u0442 \u0431\u0443\u043a\u0432\u044b \u0432\n"
"\u0442\u0435\u043a\u0441\u0442\u0435 \u0438\u0437 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043e\u043a\u043d\u0430. \u0412\u0442\u043e\u0440\u0430\u044f \u043a\u043d\u043e\u043f\u043a\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\n"
"\u0442\u0435\u043a\u0441\u0442 \u0432 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0442\u0430\u0442\u044c?", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0443\u0442\u0430\u0442\u044c?", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0436\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 \u043d\u0430\u0436\u0438\u043c\u0430\u0442\u044c \u043d\u0435 \u043d\u0443\u0436\u043d\u043e. \u0415\u0441\u043b\u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0438\u0437 \u043e\u0434\u043d\u0438\u0445 \u0446\u0438\u0444\u0440 - \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0441\u0432\u0435\u0442. \u0415\u0441\u043b\u0438 \u043d\u0435\n"
"\u0442\u043e\u043b\u044c\u043a\u043e \u0446\u0438\u0444\u0440\u044b - \u0436\u0451\u043b\u0442\u044b\u0439 \u0441\u0432\u0435\u0442. \u0415\u0441\u043b\u0438 \u0442\u043e\u043b\u044c\u043a\u043e \u0431\u0443\u043a\u0432\u044b - \u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0441\u0432\u0435\u0442.", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438 (x \u0438 y)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0438 \u0440\u0430\u0437\u0430 \u0449\u0451\u043b\u043a\u043d\u0438\u0442\u0435 \u043f\u043e\n"
"\u043b\u0438\u0441\u0442\u0443. \u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0431\u0443\u0434\u0443\u0442\n"
"\u0437\u0430\u043f\u043e\u043c\u043d\u0435\u043d\u044b \u043d\u0438\u0436\u0435.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u21161", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u21162", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u21163", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0443\u0434\u0435\u0441\u0430", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
    # retranslateUi

