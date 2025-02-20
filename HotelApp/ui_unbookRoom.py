# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unbookRoom.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_unbookRoom(object):
    def setupUi(self, unbookRoom):
        if not unbookRoom.objectName():
            unbookRoom.setObjectName(u"unbookRoom")
        unbookRoom.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../images/unbooking.png", QSize(), QIcon.Normal, QIcon.Off)
        unbookRoom.setWindowIcon(icon)
        unbookRoom.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.label = QLabel(unbookRoom)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 341, 51))
        self.label.setStyleSheet(u"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font-size: 24px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.comboBox = QComboBox(unbookRoom)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 120, 141, 31))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #5b5b5b; \n"
"    selection-background-color: #007ACC; \n"
"	color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #ccc; \n"
"    background-color: #ffffff; \n"
"    selection-background-color: #007ACC;\n"
"}\n"
"")
        self.unbookButton = QPushButton(unbookRoom)
        self.unbookButton.setObjectName(u"unbookButton")
        self.unbookButton.setGeometry(QRect(60, 220, 111, 31))
        self.unbookButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #410000;\n"
"	color: #fff;\n"
"	padding: 0px 5px;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 5px;\n"
"	transition: background-color 0.3s, color 0.3s;\n"
"	font-size: 14px;\n"
"	font-family: Roobert\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #a80000;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #df0000;\n"
"	border: 3px solid #000000;\n"
"}")
        self.cancelButton = QPushButton(unbookRoom)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(220, 220, 111, 31))
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #410000;\n"
"	color: #fff;\n"
"	padding: 0px 5px;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 5px;\n"
"	transition: background-color 0.3s, color 0.3s;\n"
"	font-size: 14px;\n"
"	font-family: Roobert\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #a80000;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #df0000;\n"
"	border: 3px solid #000000;\n"
"}")
        self.label_3 = QLabel(unbookRoom)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 124, 111, 21))
        self.label_3.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")

        self.retranslateUi(unbookRoom)

        QMetaObject.connectSlotsByName(unbookRoom)
    # setupUi

    def retranslateUi(self, unbookRoom):
        unbookRoom.setWindowTitle(QCoreApplication.translate("unbookRoom", u"\u0420\u043e\u0437\u0431\u0440\u043e\u043d\u044e\u0432\u0430\u043d\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("unbookRoom", u"\u0420\u043e\u0437\u0431\u0440\u043e\u043d\u044e\u0432\u0430\u043d\u043d\u044f \u043d\u043e\u043c\u0435\u0440\u0430", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("unbookRoom", u"-", None))
        self.unbookButton.setText(QCoreApplication.translate("unbookRoom", u"\u0420\u043e\u0437\u0431\u0440\u043e\u043d\u044e\u0432\u0430\u0442\u0438", None))
        self.cancelButton.setText(QCoreApplication.translate("unbookRoom", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("unbookRoom", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0434\u0430\u0442\u0443:", None))
    # retranslateUi

