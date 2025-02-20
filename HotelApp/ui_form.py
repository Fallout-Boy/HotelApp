# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(814, 481)
        icon = QIcon()
        icon.addFile(u"../images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        main.setWindowIcon(icon)
        main.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 9):
            self.tableWidget.setRowCount(9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem27)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(370, 45, 361, 366))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	background-color: gray;\n"
"    border: 1px solid #ccc;\n"
"    font-family: Inter,sans-serif;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #aa55ff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: darkgray;\n"
"	color: black;\n"
"    padding: 4px;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setIconSize(QSize(10, 10))
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.CustomDashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 50, 160, 22))
        self.label_6.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 100, 160, 22))
        self.label_8.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 125, 160, 22))
        self.label_9.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 150, 160, 22))
        self.label_10.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 175, 160, 21))
        self.label_11.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 75, 160, 21))
        self.label_7.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 200, 160, 22))
        self.label_12.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 225, 160, 42))
        self.label_13.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 270, 160, 32))
        self.label_14.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 305, 160, 21))
        self.label_15.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 330, 160, 42))
        self.label_16.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(320, 20, 31, 24))
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../images/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(40, 390, 111, 31))
        self.editButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #111;\n"
"	border-radius: 8px;\n"
"	padding: 0px 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #ffdeda;\n"
"	font-size: 14px;\n"
"	font-family: Inter,sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #ffaaff;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #aaaa00;\n"
"	border: 2px solid #154360;\n"
"}")
        self.bookButton = QPushButton(self.centralwidget)
        self.bookButton.setObjectName(u"bookButton")
        self.bookButton.setGeometry(QRect(195, 390, 111, 31))
        self.bookButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #111;\n"
"	border-radius: 8px;\n"
"	padding: 0px 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #ffdeda;\n"
"	font-size: 14px;\n"
"	font-family: Inter,sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #ffaaff;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #aaaa00;\n"
"	border: 2px solid #154360;\n"
"}")
        self.addRoomButton = QPushButton(self.centralwidget)
        self.addRoomButton.setObjectName(u"addRoomButton")
        self.addRoomButton.setGeometry(QRect(490, 430, 121, 41))
        self.addRoomButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #111;\n"
"	border-radius: 8px;\n"
"	padding: 0px 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: #ffdeda;\n"
"	font-size: 14px;\n"
"	font-family: Inter,sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #ffaaff;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #aaaa00;\n"
"	border: 2px solid #154360;\n"
"}")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(200, 270, 145, 32))
        self.label_25.setStyleSheet(u"color: #000000;\n"
"font-size: 14px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_25.setWordWrap(True)
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(200, 305, 145, 21))
        self.label_26.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_26.setWordWrap(True)
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(200, 330, 145, 42))
        self.label_27.setStyleSheet(u"color: #000000;\n"
"font-size: 14px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_27.setWordWrap(True)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(200, 75, 145, 21))
        self.label_18.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(200, 50, 145, 22))
        self.label_17.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(200, 125, 145, 22))
        self.label_20.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(200, 150, 145, 22))
        self.label_21.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(200, 100, 145, 22))
        self.label_19.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_19.setTextFormat(Qt.AutoText)
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(200, 175, 145, 21))
        self.label_22.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(200, 200, 145, 22))
        self.label_23.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(200, 225, 145, 42))
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setStyleSheet(u"color: #000000;\n"
"font-size: 14px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setScaledContents(False)
        self.label_24.setWordWrap(True)
        self.closeButton_2 = QPushButton(self.centralwidget)
        self.closeButton_2.setObjectName(u"closeButton_2")
        self.closeButton_2.setGeometry(QRect(730, 20, 31, 24))
        self.closeButton_2.setAutoFillBackground(False)
        self.closeButton_2.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}")
        self.closeButton_2.setIcon(icon1)
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(389, 20, 321, 22))
        self.label_28.setStyleSheet(u"color: #000000;\n"
"font-size: 16px;\n"
"text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);\n"
"transition: all 0.3s ease;")
        self.label_28.setTextFormat(Qt.AutoText)
        main.setCentralWidget(self.centralwidget)
        self.dockWidget1 = QDockWidget(main)
        self.dockWidget1.setObjectName(u"dockWidget1")
        self.dockWidget1.setEnabled(True)
        self.dockWidget1.setStyleSheet(u"background-color: rgb(59, 59, 88);")
        self.dockWidget1.setFloating(False)
        self.dockWidget1.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidget1.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.menuButton = QPushButton(self.dockWidgetContents_4)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setEnabled(True)
        self.menuButton.setGeometry(QRect(-2, 0, 41, 41))
        self.menuButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"../images/menu_close2.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u"../images/menu.png", QSize(), QIcon.Selected, QIcon.Off)
        icon2.addFile(u"../images/menu_close2.png", QSize(), QIcon.Selected, QIcon.On)
        self.menuButton.setIcon(icon2)
        self.menuButton.setIconSize(QSize(24, 24))
        self.menuButton.setFlat(True)
        self.menuButton_1 = QPushButton(self.dockWidgetContents_4)
        self.menuButton_1.setObjectName(u"menuButton_1")
        self.menuButton_1.setEnabled(True)
        self.menuButton_1.setGeometry(QRect(0, 50, 201, 31))
        self.menuButton_1.setLayoutDirection(Qt.LeftToRight)
        self.menuButton_1.setAutoFillBackground(False)
        self.menuButton_1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(52, 52, 156);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #1f618d;\n"
"	border: 2px solid #154360;\n"
"}")
        self.menuButton_1.setIconSize(QSize(24, 24))
        self.menuButton_1.setCheckable(False)
        self.menuButton_1.setChecked(False)
        self.menuButton_1.setAutoDefault(False)
        self.menuButton_1.setFlat(False)
        self.menuButton_2 = QPushButton(self.dockWidgetContents_4)
        self.menuButton_2.setObjectName(u"menuButton_2")
        self.menuButton_2.setEnabled(True)
        self.menuButton_2.setGeometry(QRect(0, 100, 201, 31))
        self.menuButton_2.setLayoutDirection(Qt.LeftToRight)
        self.menuButton_2.setAutoFillBackground(False)
        self.menuButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(52, 52, 156);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #1f618d;\n"
"	border: 2px solid #154360;\n"
"}")
        self.menuButton_2.setIconSize(QSize(24, 24))
        self.menuButton_2.setCheckable(False)
        self.menuButton_2.setChecked(False)
        self.menuButton_2.setAutoDefault(False)
        self.menuButton_2.setFlat(False)
        self.menuButton_3 = QPushButton(self.dockWidgetContents_4)
        self.menuButton_3.setObjectName(u"menuButton_3")
        self.menuButton_3.setEnabled(True)
        self.menuButton_3.setGeometry(QRect(0, 150, 201, 31))
        self.menuButton_3.setLayoutDirection(Qt.LeftToRight)
        self.menuButton_3.setAutoFillBackground(False)
        self.menuButton_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(52, 52, 156);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #1f618d;\n"
"	border: 2px solid #154360;\n"
"}")
        self.menuButton_3.setIconSize(QSize(24, 24))
        self.menuButton_3.setCheckable(False)
        self.menuButton_3.setChecked(False)
        self.menuButton_3.setAutoDefault(False)
        self.menuButton_3.setFlat(False)
        self.menuButton_4 = QPushButton(self.dockWidgetContents_4)
        self.menuButton_4.setObjectName(u"menuButton_4")
        self.menuButton_4.setEnabled(True)
        self.menuButton_4.setGeometry(QRect(0, 200, 201, 31))
        self.menuButton_4.setLayoutDirection(Qt.LeftToRight)
        self.menuButton_4.setAutoFillBackground(False)
        self.menuButton_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(52, 52, 156);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #1f618d;\n"
"	border: 2px solid #154360;\n"
"}")
        self.menuButton_4.setIconSize(QSize(24, 24))
        self.menuButton_4.setCheckable(False)
        self.menuButton_4.setChecked(False)
        self.menuButton_4.setAutoDefault(False)
        self.menuButton_4.setFlat(False)
        self.menuButton_5 = QPushButton(self.dockWidgetContents_4)
        self.menuButton_5.setObjectName(u"menuButton_5")
        self.menuButton_5.setEnabled(True)
        self.menuButton_5.setGeometry(QRect(0, 250, 201, 31))
        self.menuButton_5.setLayoutDirection(Qt.LeftToRight)
        self.menuButton_5.setAutoFillBackground(False)
        self.menuButton_5.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #2980b9;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(52, 52, 156);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #1f618d;\n"
"	border: 2px solid #154360;\n"
"}")
        self.menuButton_5.setIconSize(QSize(24, 24))
        self.menuButton_5.setCheckable(False)
        self.menuButton_5.setChecked(False)
        self.menuButton_5.setAutoDefault(False)
        self.menuButton_5.setFlat(False)
        self.dockWidget1.setWidget(self.dockWidgetContents_4)
        main.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget1)

        self.retranslateUi(main)

        self.menuButton_1.setDefault(False)
        self.menuButton_2.setDefault(False)
        self.menuButton_3.setDefault(False)
        self.menuButton_4.setDefault(False)
        self.menuButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f \u043d\u043e\u043c\u0435\u0440\u0430\u043c\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main", u"01", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main", u"02", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main", u"03", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main", u"04", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main", u"05", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main", u"06", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main", u"07", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main", u"08", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main", u"09", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("main", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("main", u"1", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("main", u"2", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("main", u"3", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("main", u"4", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("main", u"5", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("main", u"6", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("main", u"7", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("main", u"8", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("main", u"9", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_6.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_7.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.closeButton.setText("")
        self.editButton.setText(QCoreApplication.translate("main", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438", None))
        self.bookButton.setText(QCoreApplication.translate("main", u"\u0417\u0430\u0431\u0440\u043e\u043d\u044e\u0432\u0430\u0442\u0438", None))
        self.addRoomButton.setText(QCoreApplication.translate("main", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_25.setText("")
        self.label_26.setText("")
        self.label_27.setText("")
        self.label_18.setText("")
        self.label_17.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_19.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.closeButton_2.setText("")
        self.label_28.setText("")
        self.menuButton.setText("")
        self.menuButton_1.setText(QCoreApplication.translate("main", u"\u041f\u043e\u0448\u0443\u043a \u0432\u0456\u043b\u044c\u043d\u0438\u0445 \u043d\u043e\u043c\u0435\u0440\u0456\u0432", None))
#if QT_CONFIG(shortcut)
        self.menuButton_1.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.menuButton_2.setText(QCoreApplication.translate("main", u"    \u041f\u043e\u0448\u0443\u043a \u043d\u043e\u043c\u0435\u0440\u0456\u0432 \u0437\u0430 \u0432\u0430\u0440\u0442\u0456\u0441\u0442\u044e", None))
#if QT_CONFIG(shortcut)
        self.menuButton_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.menuButton_3.setText(QCoreApplication.translate("main", u"\u0412\u0438\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f \u043a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0430", None))
#if QT_CONFIG(shortcut)
        self.menuButton_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.menuButton_4.setText(QCoreApplication.translate("main", u"\u041a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0456 (>2 \u043d\u043e\u043c\u0435\u0440\u0438)", None))
#if QT_CONFIG(shortcut)
        self.menuButton_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.menuButton_5.setText(QCoreApplication.translate("main", u"\u041d\u0430\u0439\u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u0456\u0448\u0438\u0439 \u043d\u043e\u043c\u0435\u0440", None))
#if QT_CONFIG(shortcut)
        self.menuButton_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

