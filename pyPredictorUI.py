# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyPredictorUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadTrain = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadTrain.setGeometry(QtCore.QRect(0, 340, 491, 31))
        self.btnLoadTrain.setObjectName("btnLoadTrain")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 371, 19))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(500, 20, 256, 351))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 0, 241, 19))
        self.label_2.setObjectName("label_2")
        self.editTrain = QtWidgets.QTextEdit(self.centralwidget)
        self.editTrain.setGeometry(QtCore.QRect(0, 180, 491, 151))
        self.editTrain.setReadOnly(True)
        self.editTrain.setObjectName("editTrain")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 160, 481, 19))
        self.label_3.setObjectName("label_3")
        self.btnClearUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearUser.setGeometry(QtCore.QRect(380, 140, 106, 31))
        self.btnClearUser.setObjectName("btnClearUser")
        self.editUser = QtWidgets.QTextEdit(self.centralwidget)
        self.editUser.setGeometry(QtCore.QRect(0, 20, 491, 111))
        self.editUser.setObjectName("editUser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовый предиктор"))
        self.btnLoadTrain.setText(_translate("MainWindow", "Загрузить текст для обучения предиктора"))
        self.label.setText(_translate("MainWindow", "Вводите текст для предиктора"))
        self.label_2.setText(_translate("MainWindow", "Возможные продолжения"))
        self.label_3.setText(_translate("MainWindow", "Загруженный в предиктор обучающий текст"))
        self.btnClearUser.setText(_translate("MainWindow", "Очистить"))
