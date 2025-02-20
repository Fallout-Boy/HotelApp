# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question.ui'
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

class Ui_question(object):
    def setupUi(self, question):
        if not question.objectName():
            question.setObjectName(u"question")
        question.resize(424, 229)
        icon1 = QIcon()
        icon1.addFile(u"../images/question.png", QSize(), QIcon.Normal, QIcon.Off)
        question.setWindowIcon(icon1)
        question.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.label = QLabel(question)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 59, 241, 91))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label.setWordWrap(True)
        self.icon = QLabel(question)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(20, 50, 101, 101))
        self.icon.setPixmap(QPixmap(u"../images/question2.png"))
        self.icon.setScaledContents(True)
        self.buttonYes = QPushButton(question)
        self.buttonYes.setObjectName(u"buttonYes")
        self.buttonYes.setGeometry(QRect(90, 170, 111, 31))
        self.buttonYes.setStyleSheet(u"QPushButton {\n"
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
        self.buttonNo = QPushButton(question)
        self.buttonNo.setObjectName(u"buttonNo")
        self.buttonNo.setGeometry(QRect(220, 170, 111, 31))
        self.buttonNo.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(question)

        QMetaObject.connectSlotsByName(question)
    # setupUi

    def retranslateUi(self, question):
        question.setWindowTitle(QCoreApplication.translate("question", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.label.setText("")
        self.icon.setText("")
        self.buttonYes.setText(QCoreApplication.translate("question", u"\u0422\u0430\u043a", None))
        self.buttonNo.setText(QCoreApplication.translate("question", u"\u041d\u0456", None))
    # retranslateUi

