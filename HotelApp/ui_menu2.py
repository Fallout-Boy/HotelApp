# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_menu2(object):
    def setupUi(self, menu2):
        if not menu2.objectName():
            menu2.setObjectName(u"menu2")
        menu2.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../images/search2.png", QSize(), QIcon.Normal, QIcon.Off)
        menu2.setWindowIcon(icon)
        menu2.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.searchButton = QPushButton(menu2)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(140, 240, 111, 31))
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
        self.label = QLabel(menu2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 311, 81))
        self.label.setStyleSheet(u"font-size: 22px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.doubleSpinBox = QDoubleSpinBox(menu2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(200, 130, 62, 25))
        self.doubleSpinBox.setMaximum(100000.990000000005239)
        self.label_9 = QLabel(menu2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 130, 51, 21))
        self.label_9.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_10 = QLabel(menu2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(130, 170, 51, 21))
        self.label_10.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.doubleSpinBox_2 = QDoubleSpinBox(menu2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(200, 170, 62, 25))
        self.doubleSpinBox_2.setMaximum(100000.990000000005239)

        self.retranslateUi(menu2)

        QMetaObject.connectSlotsByName(menu2)
    # setupUi

    def retranslateUi(self, menu2):
        menu2.setWindowTitle(QCoreApplication.translate("menu2", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.searchButton.setText(QCoreApplication.translate("menu2", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.label.setText(QCoreApplication.translate("menu2", u"\u041f\u043e\u0448\u0443\u043a \u043d\u043e\u043c\u0435\u0440\u0456\u0432 \u0437\u0430 \u0434\u0456\u0430\u043f\u0430\u0437\u043e\u043d\u043e\u043c \u0432\u0430\u0440\u0442\u043e\u0441\u0442\u0456", None))
        self.label_9.setText(QCoreApplication.translate("menu2", u"\u0412\u0456\u0434:", None))
        self.label_10.setText(QCoreApplication.translate("menu2", u"\u0414\u043e:", None))
    # retranslateUi

