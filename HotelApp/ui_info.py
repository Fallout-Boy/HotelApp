# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_info(object):
    def setupUi(self, info):
        if not info.objectName():
            info.setObjectName(u"info")
        info.resize(424, 229)
        icon1 = QIcon()
        icon1.addFile(u"../images/info.png", QSize(), QIcon.Normal, QIcon.Off)
        info.setWindowIcon(icon1)
        info.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.icon = QLabel(info)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(20, 50, 111, 101))
        self.icon.setPixmap(QPixmap(u"../images/info2.png"))
        self.icon.setScaledContents(True)
        self.label = QLabel(info)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 52, 241, 91))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label.setWordWrap(True)
        self.button = QPushButton(info)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(160, 180, 111, 31))
        self.button.setStyleSheet(u"QPushButton {\n"
"    background-color: #5555ff; \n"
"    border: none; \n"
"    color: #ffffff;\n"
"    border-radius: 5px; \n"
"    transition: background-color 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1f618d; \n"
"}")

        self.retranslateUi(info)

        QMetaObject.connectSlotsByName(info)
    # setupUi

    def retranslateUi(self, info):
        info.setWindowTitle(QCoreApplication.translate("info", u"\u0421\u043f\u043e\u0432\u0456\u0449\u0435\u043d\u043d\u044f", None))
        self.icon.setText("")
        self.label.setText("")
        self.button.setText(QCoreApplication.translate("info", u"\u0417\u0440\u043e\u0437\u0443\u043c\u0456\u043b\u043e", None))
    # retranslateUi

