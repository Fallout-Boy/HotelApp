# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookRoom.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_bookRoom(object):
    def setupUi(self, bookRoom):
        if not bookRoom.objectName():
            bookRoom.setObjectName(u"bookRoom")
        bookRoom.resize(381, 451)
        icon = QIcon()
        icon.addFile(u"../images/booking.png", QSize(), QIcon.Normal, QIcon.Off)
        bookRoom.setWindowIcon(icon)
        bookRoom.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.label = QLabel(bookRoom)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 321, 51))
        self.label.setStyleSheet(u"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font-size: 24px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_2 = QLabel(bookRoom)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 85, 281, 71))
        self.label_2.setStyleSheet(u"font-size: 14px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(bookRoom)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 180, 151, 21))
        self.label_3.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_4 = QLabel(bookRoom)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(143, 210, 61, 21))
        self.label_4.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.dateEdit = QDateEdit(bookRoom)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(210, 180, 110, 25))
        self.dateEdit.setStyleSheet(u"border: 1px solid #353535;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.dateEdit_2 = QDateEdit(bookRoom)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(210, 210, 110, 25))
        self.dateEdit_2.setStyleSheet(u"border: 1px solid #353535;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.label_5 = QLabel(bookRoom)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 250, 111, 21))
        self.label_5.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.textEdit = QTextEdit(bookRoom)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(180, 250, 181, 71))
        self.bookButton = QPushButton(bookRoom)
        self.bookButton.setObjectName(u"bookButton")
        self.bookButton.setGeometry(QRect(60, 350, 111, 31))
        self.bookButton.setStyleSheet(u"QPushButton {\n"
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
        self.cancelButton = QPushButton(bookRoom)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(200, 350, 111, 31))
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
        self.unbookButton = QPushButton(bookRoom)
        self.unbookButton.setObjectName(u"unbookButton")
        self.unbookButton.setGeometry(QRect(120, 390, 131, 31))
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

        self.retranslateUi(bookRoom)

        QMetaObject.connectSlotsByName(bookRoom)
    # setupUi

    def retranslateUi(self, bookRoom):
        bookRoom.setWindowTitle(QCoreApplication.translate("bookRoom", u"\u0411\u0440\u043e\u043d\u044e\u0432\u0430\u043d\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("bookRoom", u"\u0411\u0440\u043e\u043d\u044e\u0432\u0430\u043d\u043d\u044f \u043d\u043e\u043c\u0435\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("bookRoom", u"\u0417\u0430\u0431\u0440\u043e\u043d\u044c\u043e\u0432\u0430\u043d\u0456 \u0434\u0430\u0442\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("bookRoom", u"\u0417\u0430\u0431\u0440\u043e\u043d\u044e\u0432\u0430\u0442\u0438 \u0432\u0456\u0434:", None))
        self.label_4.setText(QCoreApplication.translate("bookRoom", u"\u0434\u043e:", None))
        self.label_5.setText(QCoreApplication.translate("bookRoom", u"\u0414\u0430\u043d\u0456 \u0432\u043b\u0430\u0441\u043d\u0438\u043a\u0430:", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("bookRoom", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435 \u0456\u043c'\u044f \u043f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.bookButton.setText(QCoreApplication.translate("bookRoom", u"\u0417\u0430\u0431\u0440\u043e\u043d\u044e\u0432\u0430\u0442\u0438", None))
        self.cancelButton.setText(QCoreApplication.translate("bookRoom", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.unbookButton.setText(QCoreApplication.translate("bookRoom", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438 \u0431\u0440\u043e\u043d\u044c", None))
    # retranslateUi

