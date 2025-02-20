# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result.ui'
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

class Ui_result(object):
    def setupUi(self, result):
        if not result.objectName():
            result.setObjectName(u"result")
        result.resize(496, 283)
        icon = QIcon()
        icon.addFile(u"../images/result.png", QSize(), QIcon.Normal, QIcon.Off)
        result.setWindowIcon(icon)
        result.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.label = QLabel(result)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 311, 181))
        self.label.setStyleSheet(u"font-size: 20px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.button = QPushButton(result)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(190, 230, 111, 31))
        self.button.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(result)

        QMetaObject.connectSlotsByName(result)
    # setupUi

    def retranslateUi(self, result):
        result.setWindowTitle(QCoreApplication.translate("result", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label.setText("")
        self.button.setText(QCoreApplication.translate("result", u"\u0417\u0440\u043e\u0437\u0443\u043c\u0456\u043b\u043e", None))
    # retranslateUi

