# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editRoom.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTextEdit, QWidget)

class Ui_editRoom(object):
    def setupUi(self, editRoom):
        if not editRoom.objectName():
            editRoom.setObjectName(u"editRoom")
        editRoom.resize(468, 518)
        icon = QIcon()
        icon.addFile(u"../images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        editRoom.setWindowIcon(icon)
        editRoom.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.label = QLabel(editRoom)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 211, 51))
        self.label.setStyleSheet(u"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font-size: 24px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.doubleSpinBox_2 = QDoubleSpinBox(editRoom)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(240, 350, 62, 25))
        self.doubleSpinBox_2.setMaximum(100000.990000000005239)
        self.label_10 = QLabel(editRoom)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 380, 161, 21))
        self.label_10.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_5 = QLabel(editRoom)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 190, 121, 21))
        self.label_5.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.doubleSpinBox = QDoubleSpinBox(editRoom)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(240, 250, 62, 25))
        self.doubleSpinBox.setMinimum(0.000000000000000)
        self.doubleSpinBox.setMaximum(150.000000000000000)
        self.label_8 = QLabel(editRoom)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 280, 141, 21))
        self.label_8.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_4 = QLabel(editRoom)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 160, 121, 21))
        self.label_4.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.radioButton_2 = QRadioButton(editRoom)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(310, 90, 91, 22))
        self.radioButton_2.setStyleSheet(u"color: #000000;color: #000000;")
        self.label_7 = QLabel(editRoom)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 250, 121, 21))
        self.label_7.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_2 = QLabel(editRoom)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 90, 101, 21))
        self.label_2.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.spinBox = QSpinBox(editRoom)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(240, 160, 61, 25))
        self.spinBox_2 = QSpinBox(editRoom)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(240, 190, 61, 25))
        self.spinBox_3 = QSpinBox(editRoom)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(240, 220, 61, 25))
        self.textEdit = QTextEdit(editRoom)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(240, 280, 161, 61))
        self.textEdit_2 = QTextEdit(editRoom)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(240, 380, 161, 61))
        self.radioButton = QRadioButton(editRoom)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(190, 90, 91, 22))
        self.radioButton.setStyleSheet(u"color: #000000;color: #000000;")
        self.label_6 = QLabel(editRoom)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 220, 121, 21))
        self.label_6.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_3 = QLabel(editRoom)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 130, 101, 21))
        self.label_3.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_9 = QLabel(editRoom)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 350, 121, 21))
        self.label_9.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.cancelButton = QPushButton(editRoom)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(180, 470, 111, 31))
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
        self.editButton = QPushButton(editRoom)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(60, 470, 111, 31))
        self.editButton.setStyleSheet(u"QPushButton {\n"
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
        self.deleteButton = QPushButton(editRoom)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(300, 470, 111, 31))
        self.deleteButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #410000;\n"
"	color: #fff;\n"
"	padding: 0px 5px;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 5px;\n"
"	transition: background-color 0.3s, color 0.3s;\n"
"	font-size: 12px;\n"
"	font-family: Roobert\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #a80000;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #df0000;\n"
"	border: 3px solid #000000;\n"
"}")
        self.label_11 = QLabel(editRoom)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 130, 101, 21))
        self.label_11.setStyleSheet(u"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")

        self.retranslateUi(editRoom)

        QMetaObject.connectSlotsByName(editRoom)
    # setupUi

    def retranslateUi(self, editRoom):
        editRoom.setWindowTitle(QCoreApplication.translate("editRoom", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u043d\u043d\u044f", None))
        self.label.setText(QCoreApplication.translate("editRoom", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_10.setText(QCoreApplication.translate("editRoom", u"\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u0437\u0440\u0443\u0447\u043d\u043e\u0441\u0442\u0456:", None))
        self.label_5.setText(QCoreApplication.translate("editRoom", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u043c\u0456\u0441\u0446\u044c:", None))
        self.label_8.setText(QCoreApplication.translate("editRoom", u"\u041f\u043e\u0431\u0443\u0442\u043e\u0432\u0430 \u0442\u0435\u0445\u043d\u0456\u043a\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("editRoom", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u043a\u0456\u043c\u043d\u0430\u0442:", None))
        self.radioButton_2.setText(QCoreApplication.translate("editRoom", u"\u041b\u044e\u043a\u0441", None))
        self.label_7.setText(QCoreApplication.translate("editRoom", u"\u041f\u043b\u043e\u0449\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("editRoom", u"\u0422\u0438\u043f:", None))
        self.radioButton.setText(QCoreApplication.translate("editRoom", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.label_6.setText(QCoreApplication.translate("editRoom", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0432\u0456\u043a\u043e\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("editRoom", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_9.setText(QCoreApplication.translate("editRoom", u"\u0426\u0456\u043d\u0430/\u0434\u0435\u043d\u044c:", None))
        self.cancelButton.setText(QCoreApplication.translate("editRoom", u"\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438", None))
        self.editButton.setText(QCoreApplication.translate("editRoom", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438 \u0434\u0430\u043d\u0456", None))
        self.deleteButton.setText(QCoreApplication.translate("editRoom", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_11.setText("")
    # retranslateUi

