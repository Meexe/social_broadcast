# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mpak/Desktop/design.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(50, 490, 151, 32))
        self.clear_btn.setObjectName("clear_btn")
        self.message_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_box.setGeometry(QtCore.QRect(50, 40, 300, 200))
        self.message_box.setObjectName("message_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 211, 16))
        self.label_2.setObjectName("label_2")
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.setGeometry(QtCore.QRect(200, 490, 151, 32))
        self.send_btn.setObjectName("send_btn")
        self.file_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.file_box.setGeometry(QtCore.QRect(50, 290, 301, 151))
        self.file_box.setObjectName("file_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Message"))
        self.label_2.setText(_translate("MainWindow", "Drag\'n\'drop your pictures here"))
        self.send_btn.setText(_translate("MainWindow", "Send"))
