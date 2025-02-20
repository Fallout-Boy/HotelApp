# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu1.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_menu1(object):
    def setupUi(self, menu1):
        if not menu1.objectName():
            menu1.setObjectName(u"menu1")
        menu1.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        menu1.setWindowIcon(icon)
        menu1.setStyleSheet(u"background-color: rgb(104, 104, 104);\n"
"")
        self.label = QLabel(menu1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 311, 91))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.dateEdit = QDateEdit(menu1)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(170, 140, 110, 25))
        self.dateEdit.setStyleSheet(u"border: 1px solid #353535;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.label_4 = QLabel(menu1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(123, 170, 41, 21))
        self.label_4.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.dateEdit_2 = QDateEdit(menu1)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(170, 170, 110, 25))
        self.dateEdit_2.setStyleSheet(u"border: 1px solid #353535;\n"
"border-radius: 5px;\n"
"font-size: 14px;")
        self.label_3 = QLabel(menu1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 140, 41, 21))
        self.label_3.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.searchButton = QPushButton(menu1)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(150, 240, 111, 31))
        self.searchButton.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(menu1)

        QMetaObject.connectSlotsByName(menu1)
    # setupUi

    def retranslateUi(self, menu1):
        menu1.setWindowTitle(QCoreApplication.translate("menu1", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.label.setText(QCoreApplication.translate("menu1", u"\u041f\u043e\u0448\u0443\u043a \u0432\u0456\u043b\u044c\u043d\u0438\u0445 \u043d\u043e\u043c\u0435\u0440\u0456\u0432 \u043d\u0430            \u0432\u043a\u0430\u0437\u0430\u043d\u0456 \u0434\u0430\u0442\u0438", None))
        self.label_4.setText(QCoreApplication.translate("menu1", u"\u0434\u043e:", None))
        self.label_3.setText(QCoreApplication.translate("menu1", u"\u0412\u0456\u0434:", None))
        self.searchButton.setText(QCoreApplication.translate("menu1", u"\u041f\u043e\u0448\u0443\u043a", None))
    # retranslateUi

