# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
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

class Ui_error(object):
    def setupUi(self, error):
        if not error.objectName():
            error.setObjectName(u"error")
        error.resize(424, 229)
        icon1 = QIcon()
        icon1.addFile(u"../images/error.png", QSize(), QIcon.Normal, QIcon.Off)
        error.setWindowIcon(icon1)
        error.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.label = QLabel(error)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 62, 241, 81))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label.setWordWrap(True)
        self.icon = QLabel(error)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(20, 50, 111, 101))
        self.icon.setPixmap(QPixmap(u"../images/error2.png"))
        self.icon.setScaledContents(True)
        self.button = QPushButton(error)
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

        self.retranslateUi(error)

        QMetaObject.connectSlotsByName(error)
    # setupUi

    def retranslateUi(self, error):
        error.setWindowTitle(QCoreApplication.translate("error", u"\u041f\u043e\u043c\u0438\u043b\u043a\u0430", None))
        self.label.setText("")
        self.icon.setText("")
        self.button.setText(QCoreApplication.translate("error", u"\u0417\u0440\u043e\u0437\u0443\u043c\u0456\u043b\u043e", None))
    # retranslateUi

