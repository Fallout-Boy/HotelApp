import sys
import sqlite3
import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
from PySide6.QtCore import QPropertyAnimation, QRect, Qt, QDate
from PySide6.QtGui import QColor

from ui_form import Ui_main
from ui_addRoom import Ui_addRoom
from ui_editRoom import Ui_editRoom
from ui_bookRoom import Ui_bookRoom
from ui_unbookRoom import Ui_unbookRoom
from ui_info import Ui_info
from ui_error import Ui_error
from ui_question import Ui_question
from ui_menu1 import Ui_menu1
from ui_menu2 import Ui_menu2
from ui_result import Ui_result

from room import Room

class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)

        # Заборона змінення розмірів головного вікна
        self.setFixedSize(814, 481)
        self.setWindowFlags(Qt.Window)

        # Налаштування меню
        self.hideMenuButtons()
        self.ui.menuButton.setCheckable(True)

        # Змінна, яка відповідає за стан меню
        self.isOpened = False

        # Змінна, яка відповідає за вибраний номер
        self.selectedNumber = ""

        # Змінна для вспливаючого вікна питання
        self.isConfirmed = False

        # Змінна для визначення типу пошуку
        self.isSearchOfFree = None

        # Визначення сьогоднішнього дня
        self.today = datetime.date.today()

        # Сигнали для слотів головного вікна
        self.ui.menuButton.clicked.connect(self.openCloseMenu)
        self.ui.closeButton.clicked.connect(self.clearLabels)
        self.ui.addRoomButton.clicked.connect(self.openWindowAddRoom)
        self.ui.editButton.clicked.connect(self.openWindowEditRoom)
        self.ui.bookButton.clicked.connect(self.openWindowBookRoom)
        self.ui.menuButton_1.clicked.connect(self.openSearchWindow)
        self.ui.menuButton_2.clicked.connect(self.openSearch2Window)
        self.ui.menuButton_3.clicked.connect(self.openResult1)
        self.ui.menuButton_4.clicked.connect(self.openResult2)
        self.ui.menuButton_5.clicked.connect(self.openResult3)
        self.ui.closeButton_2.clicked.connect(self.cancelSearch)

        self.ui.closeButton.hide()
        self.ui.bookButton.hide()
        self.ui.editButton.hide()
        self.ui.closeButton_2.hide()

        # Створення вікна додавання нового номера
        self.windowAddRoom = QDialog()
        self.addRoom_ui = Ui_addRoom()
        self.addRoom_ui.setupUi(self.windowAddRoom)

        # Сигнали для слотів цього вікна
        self.addRoom_ui.addButton.clicked.connect(self.addButtonAction)
        self.addRoom_ui.cancelButton.clicked.connect(self.closeAddRoomWindow)
        self.addRoom_ui.radioButton.clicked.connect(self.toggleTextEditState)
        self.addRoom_ui.radioButton_2.clicked.connect(self.toggleTextEditState)

        self.addRoom_ui.textEdit_2.setReadOnly(True)

        # Створення вікна редагування номера
        self.windowEditRoom = QDialog()
        self.editRoom_ui = Ui_editRoom()
        self.editRoom_ui.setupUi(self.windowEditRoom)

        # Сигнали для слотів цього вікна
        self.editRoom_ui.editButton.clicked.connect(self.editButtonAction)
        self.editRoom_ui.cancelButton.clicked.connect(self.closeEditRoomWindow)
        self.editRoom_ui.deleteButton.clicked.connect(self.deleteButtonAction)

        # Створення вікна бронювання номера
        self.windowBookRoom = QDialog()
        self.bookRoom_ui = Ui_bookRoom()
        self.bookRoom_ui.setupUi(self.windowBookRoom)

        # Сигнали для слотів цього вікна
        self.bookRoom_ui.cancelButton.clicked.connect(self.closeBookRoomWindow)
        self.bookRoom_ui.bookButton.clicked.connect(self.bookButtonAction)
        self.bookRoom_ui.unbookButton.clicked.connect(self.openWindowUnbookRoom)

        # Створення вікна розбронювання номера
        self.windowUnbookRoom = QDialog()
        self.unbookRoom_ui = Ui_unbookRoom()
        self.unbookRoom_ui.setupUi(self.windowUnbookRoom)

        # Сигнали для слотів цього вікна
        self.unbookRoom_ui.cancelButton.clicked.connect(self.closeUnbookRoomWindow)
        self.unbookRoom_ui.unbookButton.clicked.connect(self.unbookButtonAction)

        # Створення вспливаючого вікна інформація
        self.windowMessageInfo = QDialog()
        self.messageInfo_ui = Ui_info()
        self.messageInfo_ui.setupUi(self.windowMessageInfo)

        # Сигнали для слотів цього вікна
        self.messageInfo_ui.button.clicked.connect(self.closeInfoWindow)

        # Створення вспливаючого вікна помилка
        self.windowMessageError = QDialog()
        self.messageError_ui = Ui_error()
        self.messageError_ui.setupUi(self.windowMessageError)

        # Сигнали для слотів цього вікна
        self.messageError_ui.button.clicked.connect(self.closeErrorWindow)

        # Створення вспливаючого вікна питання
        self.windowQuestion = QDialog()
        self.question_ui = Ui_question()
        self.question_ui.setupUi(self.windowQuestion)

        # Сигнали для слотів цього вікна
        self.question_ui.buttonYes.clicked.connect(self.continueAction)
        self.question_ui.buttonNo.clicked.connect(self.closeQuestionWindow)

        # Створення вікна пошук вільних номерів на вказані дати
        self.windowMenu1 = QDialog()
        self.menu1_ui = Ui_menu1()
        self.menu1_ui.setupUi(self.windowMenu1)

        # Сигнали для слотів цього вікна
        self.menu1_ui.searchButton.clicked.connect(self.searchAction)

        # Створення вікна пошук номерів за вказаним діапазоном вартості
        self.windowMenu2 = QDialog()
        self.menu2_ui = Ui_menu2()
        self.menu2_ui.setupUi(self.windowMenu2)

        # Сигнали для слотів цього вікна
        self.menu2_ui.searchButton.clicked.connect(self.searchAction_2)

        # Створення вікна результату
        self.windowResult = QDialog()
        self.result_ui = Ui_result()
        self.result_ui.setupUi(self.windowResult)

        # Сигнали для слотів цього вікна
        self.result_ui.button.clicked.connect(self.closeResult)

        # Анімація
        self.animation = QPropertyAnimation(self.ui.dockWidget1, b"geometry")
        self.animation.setDuration(300)

        # База даних
        try:
            self.db = sqlite3.connect('myDataBase.db')
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)
        self.cursor = self.db.cursor()

        # Словник, який відповідає за items в таблиці
        self.items = {}

        # Отримання даних користувачів з бази даних
        self.cursor.execute("SELECT * FROM Users")
        self.userData = self.cursor.fetchall()

        # Отримання даних про номери з бази даних
        self.cursor.execute("SELECT * FROM HotelRooms")
        self.data = self.cursor.fetchall()

        # Інформація з бази даних
        self.rooms = []
        for row_data in self.data:
            db_data = []
            for i in range(len(row_data)):
                db_data.append(row_data[i])
            # Об'єкт класу Room
            room = Room(*db_data)
            self.rooms.append(room)

        # Таблиця
        # Добавлення існуючих номерів
        for room in self.rooms:
            num = room.number
            col = (num % 100) - 1
            row = (num // 100) - 1
            item = QTableWidgetItem(room.lux)

            # Перевірка чи номер зараз заброньований
            date_ranges = room.bookingDates.split()
            roomColor = QColor(100, 255, 100)
            for date_range_str in date_ranges:
                if room.bookingDates == "":
                    continue
                start_date_str, end_date_str = date_range_str.split("-")
                start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").date()
                end_date = datetime.datetime.strptime(end_date_str, "%d.%m.%Y").date()

                # Алгоритм знищення дат, які вже минули, з інформації про номери
                if self.today > end_date:
                    dates = room.bookingDates.split()
                    persons = room.host.split(', ')
                    persons = [i for i in persons if i != ""]
                    for i in reversed(range(len(dates))):
                        if dates[i] == date_range_str:
                            del dates[i]
                            del persons[i]
                    dates = ' '.join(dates)
                    persons = ', '.join(persons)
                    self.cursor.execute(f"""UPDATE HotelRooms SET
                        bookingDate = '{dates}',
                        hostName = '{persons}'
                        WHERE number = {room.number}
                    """)

                    self.db.commit()
                    self.cursor.execute("SELECT * FROM HotelRooms")
                    self.data = self.cursor.fetchall()

                    room.editValues(bookingDates=dates, host=persons)

                if start_date <= self.today <= end_date:
                    roomColor = QColor(255, 100, 100)
                    break

            # Встановлення відповідного кольору іtem
            item.setBackground(roomColor)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)

            # Перевірка чи достатньо у таблиці стовпців
            if self.ui.tableWidget.columnCount() < col + 1:
                self.ui.tableWidget.setColumnCount(col + 1)

            self.ui.tableWidget.setItem(row, col, item)
            self.items[(row, col)] = item


        # Відстеження події нажаття на таблицю
        self.ui.tableWidget.itemClicked.connect(self.on_item_clicked)

    def __del__(self):
        # Завершення роботи з базою даних при виході з програми
        if hasattr(self, 'db'):
            self.db.commit()
            self.db.close()

    # Функція відкриття і закриття меню
    def openCloseMenu(self):
        if self.isOpened:
            self.isOpened = False
            self.animation.setStartValue(self.ui.dockWidget1.geometry())
            self.animation.setEndValue(QRect(0, 0, 0, self.ui.dockWidget1.height()))
            self.animation.start()

            self.ui.menuButton.setChecked(False)

            self.hideMenuButtons()

        elif not self.isOpened:
            self.isOpened = True
            self.animation.setStartValue(QRect(0, 0, 0, self.ui.dockWidget1.height()))
            self.animation.setEndValue(QRect(0, 0, 200, self.ui.dockWidget1.height()))
            self.animation.start()

            self.ui.menuButton.setChecked(True)

            self.showMenuButtons()

    # Функція приховання кнопок меню
    def hideMenuButtons(self):
        self.ui.menuButton_1.hide()
        self.ui.menuButton_2.hide()
        self.ui.menuButton_3.hide()
        self.ui.menuButton_4.hide()
        self.ui.menuButton_5.hide()

    # Функція показу кнопок меню
    def showMenuButtons(self):
        self.ui.menuButton_1.show()
        self.ui.menuButton_2.show()
        self.ui.menuButton_3.show()
        self.ui.menuButton_4.show()
        self.ui.menuButton_5.show()

    # Функція при нажатті на item в таблиці
    def on_item_clicked(self, item):
        if item.text() != "":
            self.fillLabels()
            self.ui.closeButton.show()

            self.ui.bookButton.show()
            self.ui.editButton.show()

        row = item.row() + 1
        column = item.column() + 1

        if column > 9:
            self.selectedNumber = str(row) + str(column)
        else:
            self.selectedNumber = str(row) + "0" + str(column)

        # Показ інформації про номер
        for room in self.rooms:
            if int(self.selectedNumber) == room.number:
                date_ranges = room.bookingDates.split()
                status = "Вільний"
                for date_range_str in date_ranges:
                    if room.bookingDates == "":
                        continue
                    start_date_str, end_date_str = date_range_str.split("-")
                    start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").date()
                    end_date = datetime.datetime.strptime(end_date_str, "%d.%m.%Y").date()

                    if start_date <= self.today <= end_date:
                        status = "Зайнятий"
                        break


                self.ui.label_17.setText(str(room.number))
                self.ui.label_18.setText(status)
                self.ui.label_19.setText(room.lux)
                self.ui.label_20.setText(str(room.roomQuantity))
                self.ui.label_21.setText(str(room.seatQuantity))
                self.ui.label_22.setText(str(room.windowQuantity))
                self.ui.label_23.setText(str(room.square))
                self.ui.label_24.setText(room.householdAppliances)
                self.ui.label_25.setText(room.bookingDates)
                self.ui.label_26.setText(str(room.price))
                self.ui.label_27.setText(room.additionalAmenities)
                break

    def fillLabels(self):
        self.ui.label_6.setText("Номер:")
        self.ui.label_7.setText("Статус:")
        self.ui.label_8.setText("Тип:")
        self.ui.label_9.setText("Кількість кімнат:")
        self.ui.label_10.setText("Кількість місць:")
        self.ui.label_11.setText("Кількість вікон:")
        self.ui.label_12.setText("Площа:")
        self.ui.label_13.setText("Побутова техніка:")
        self.ui.label_14.setText("Дата бронювання:")
        self.ui.label_15.setText("Вартість:")
        self.ui.label_16.setText("Додаткові зручності:")

    def clearLabels(self):
        self.ui.label_6.setText("")
        self.ui.label_7.setText("")
        self.ui.label_8.setText("")
        self.ui.label_9.setText("")
        self.ui.label_10.setText("")
        self.ui.label_11.setText("")
        self.ui.label_12.setText("")
        self.ui.label_13.setText("")
        self.ui.label_14.setText("")
        self.ui.label_15.setText("")
        self.ui.label_16.setText("")
        self.ui.label_17.setText("")
        self.ui.label_18.setText("")
        self.ui.label_19.setText("")
        self.ui.label_20.setText("")
        self.ui.label_21.setText("")
        self.ui.label_22.setText("")
        self.ui.label_23.setText("")
        self.ui.label_24.setText("")
        self.ui.label_25.setText("")
        self.ui.label_26.setText("")
        self.ui.label_27.setText("")
        self.ui.closeButton.hide()
        self.ui.bookButton.hide()
        self.ui.editButton.hide()

    # Функція відкриття вікна додавання номеру
    def openWindowAddRoom(self):
        self.clearAddRoomWindow()
        self.windowAddRoom.exec()

    # Функція відкриття вікна редагування номеру
    def openWindowEditRoom(self):
        selected_room = None
        for room in self.rooms:
            if room.number == int(self.selectedNumber):
                selected_room = room
                break

        if selected_room:
            if selected_room.lux == "Номер":
                self.editRoom_ui.radioButton.setChecked(True)
            elif selected_room.lux == "Люкс":
                self.editRoom_ui.radioButton_2.setChecked(True)

            self.editRoom_ui.label_11.setText(str(selected_room.number))
            self.editRoom_ui.spinBox.setValue(selected_room.roomQuantity)
            self.editRoom_ui.spinBox_2.setValue(selected_room.seatQuantity)
            self.editRoom_ui.spinBox_3.setValue(selected_room.windowQuantity)
            self.editRoom_ui.doubleSpinBox.setValue(selected_room.square)
            self.editRoom_ui.textEdit.setPlainText(selected_room.householdAppliances)
            self.editRoom_ui.doubleSpinBox_2.setValue(selected_room.price)
            self.editRoom_ui.textEdit_2.setPlainText(selected_room.additionalAmenities)

        self.windowEditRoom.exec()

    # Функція відкриття вікна бронювання номера
    def openWindowBookRoom(self):
        selected_room = None
        for room in self.rooms:
            if room.number == int(self.selectedNumber):
                selected_room = room
                break

        if selected_room:
            self.bookRoom_ui.label.setText(f"Бронювання номера {selected_room.number}")
            if selected_room.bookingDates != "":
                self.bookRoom_ui.label_2.setText(f"Заброньовані дати: {selected_room.bookingDates}")
            else:
                self.bookRoom_ui.label_2.setText("У номера немає заброньованих дат")

        self.bookRoom_ui.dateEdit.setDate(QDate())
        self.bookRoom_ui.dateEdit_2.setDate(QDate())
        self.bookRoom_ui.textEdit.clear()
        self.windowBookRoom.exec()


    # Функція відкриття вікна розбронювання номера
    def openWindowUnbookRoom(self):
        selected_room = None
        for room in self.rooms:
            if room.number == int(self.selectedNumber):
                selected_room = room
                break

        self.unbookRoom_ui.comboBox.clear()
        if selected_room:
            date_ranges = selected_room.bookingDates.split()
            for date_range in date_ranges:
                self.unbookRoom_ui.comboBox.addItem(date_range)

        self.windowUnbookRoom.exec()


    # Функція відкриття вікна пошуку по датах
    def openSearchWindow(self):
        self.isSearchOfFree = True
        self.menu1_ui.dateEdit.setDate(QDate())
        self.menu1_ui.dateEdit_2.setDate(QDate())
        self.openCloseMenu()
        self.windowMenu1.exec()

    # Функція відкриття вікна пошуку по вартості
    def openSearch2Window(self):
        self.openCloseMenu()
        self.windowMenu2.exec()

    # Функція відкриття вікна результату визначення гостя, який проживає в готелі найдовше
    def openResult1(self):
        res = {}
        for users in self.userData:
            date_ranges = users[2].split()
            for date_range_str in date_ranges:
                start_date_str, end_date_str = date_range_str.split("-")
                start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").date()
                end_date = datetime.datetime.strptime(end_date_str, "%d.%m.%Y").date()
                if start_date <= self.today <= end_date:
                    res[users[0]] = (self.today - start_date).days
        max_value = None
        max_key = None

        for key, value in res.items():
            if max_value is None or value > max_value:
                max_key = key
                max_value = value

        self.result_ui.label.setText(f"Користувач, який проживає в готелі найдовше: {max_key}\n\n"\
                                     f"Кількість прожитих днів: {max_value}")

        self.openCloseMenu()
        self.windowResult.exec()

    # Функція відкриття вікна результату визначення гостей, які забронювали більше 2 номерів
    def openResult2(self):
        resText = "Користувачі, які забронювали більше 2 номерів: "
        isHere = False
        for users in self.userData:
            rooms = users[1].split()
            count = 0
            for i in rooms:
                count += 1
            if count > 2:
                resText += f"{users[0]}"
                if isHere:
                    resText += ", "
                isHere = True
        if not isHere:
            resText += '-'
        self.result_ui.label.setText(resText)
        self.openCloseMenu()
        self.windowResult.exec()

    # Функція відкриття вікна пошуку найпопулярнішого номеру
    def openResult3(self):
        self.isSearchOfFree = False
        self.menu1_ui.label.setText("Знаходження найпопулярнішого номеру в заданому діапазоні")
        self.openCloseMenu()
        self.windowMenu1.exec()

    # Функція скасування результатів пошуку
    def cancelSearch(self):
        for room in self.rooms:
            date_ranges = room.bookingDates.split()
            roomColor = QColor(100, 255, 100)
            num = room.number
            col = (num % 100) - 1
            row = (num // 100) - 1
            for date_range_str in date_ranges:
                if room.bookingDates == "":
                    continue
                start_date_str, end_date_str = date_range_str.split("-")
                start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").date()
                end_date = datetime.datetime.strptime(end_date_str, "%d.%m.%Y").date()

                if start_date <= self.today <= end_date:
                    roomColor = QColor(255, 100, 100)
                    break
            item = self.items.get((row, col))
            item.setBackground(roomColor)
        self.ui.closeButton_2.hide()
        self.ui.label_28.setText("")

    # Функція для додавання номеру
    def addButtonAction(self):
        numberValue = self.addRoom_ui.spinBox.value()
        # Перевірка чи вибраний тип
        if self.addRoom_ui.radioButton.isChecked() or self.addRoom_ui.radioButton_2.isChecked():
            if 100 < numberValue < 1000:
                if self.addRoom_ui.spinBox_2.value() > 0:
                    if self.addRoom_ui.spinBox_3.value() > 0:
                        if self.addRoom_ui.spinBox_4.value() > 0:
                            if 10 < self.addRoom_ui.doubleSpinBox.value():
                                if self.addRoom_ui.textEdit.toPlainText():
                                    if 1000 <= self.addRoom_ui.doubleSpinBox_2.value():
                                        isSameNumber = any(room.number == numberValue for room in self.rooms)

                                        if not isSameNumber:
                                            type = "Номер"
                                            if self.addRoom_ui.radioButton_2.isChecked():
                                                type = "Люкс"
                                            self.cursor.execute(f"""INSERT INTO HotelRooms VALUES (
                                                {numberValue},
                                                '{type}',
                                                {self.addRoom_ui.spinBox_2.value()},
                                                {self.addRoom_ui.spinBox_3.value()},
                                                {self.addRoom_ui.spinBox_4.value()},
                                                {self.addRoom_ui.doubleSpinBox.value()},
                                                '{self.addRoom_ui.textEdit.toPlainText()}',
                                                '',
                                                {self.addRoom_ui.doubleSpinBox_2.value()},
                                                '{self.addRoom_ui.textEdit_2.toPlainText()}',
                                                ''
                                                )""")
                                            self.db.commit()

                                            room = Room(numberValue, type, self.addRoom_ui.spinBox_2.value(), self.addRoom_ui.spinBox_3.value(),
                                            self.addRoom_ui.spinBox_4.value(), self.addRoom_ui.doubleSpinBox.value(), self.addRoom_ui.textEdit.toPlainText(),
                                            '', self.addRoom_ui.doubleSpinBox_2.value(), self.addRoom_ui.textEdit_2.toPlainText(), '')
                                            self.rooms.append(room)

                                            middle_digit = (numberValue % 1000) // 100
                                            if middle_digit:
                                                col = numberValue % 100 - 1
                                            else:
                                                col = numberValue % 10 - 1
                                            row = self.addRoom_ui.spinBox.value() // 100 - 1
                                            item = QTableWidgetItem(type)
                                            item.setBackground(QColor(100, 255, 100))
                                            if self.ui.tableWidget.columnCount() < col + 1:
                                                self.ui.tableWidget.setColumnCount(col + 1)
                                            self.ui.tableWidget.setItem(row, col, item)

                                            self.cursor.execute("SELECT * FROM HotelRooms")
                                            self.data = self.cursor.fetchall()

                                            self.windowAddRoom.close()

                                            self.messageInfo_ui.label.setText("Номер успішно додано!")
                                            self.windowMessageInfo.exec()
                                        else:
                                            self.messageError_ui.label.setText(f"Номер {numberValue} вже існує!")
                                            self.windowMessageError.exec()
                                    else:
                                        self.messageError_ui.label.setText("Ціна повинна бути не менша за 1000!")
                                        self.windowMessageError.exec()
                                else:
                                    self.messageError_ui.label.setText("Номер повинен містити побутову техніку!")
                                    self.windowMessageError.exec()
                            else:
                                self.messageError_ui.label.setText("Площа повинна бути більша за 10!")
                                self.windowMessageError.exec()
                        else:
                            self.messageError_ui.label.setText("Кількість вікон не може бути рівна 0!")
                            self.windowMessageError.exec()
                    else:
                        self.messageError_ui.label.setText("Кількість місць не може бути рівна 0!")
                        self.windowMessageError.exec()
                else:
                    self.messageError_ui.label.setText("Кількість кімнат не може бути рівна 0!")
                    self.windowMessageError.exec()
            else:
                self.messageError_ui.label.setText("Номер повинен бути більший за 100 і менший за 1000!")
                self.windowMessageError.exec()
        else:
            self.messageError_ui.label.setText("Тип не вибрано!")
            self.windowMessageError.exec()

    # Функція для редагування номеру
    def editButtonAction(self):
        if self.editRoom_ui.radioButton.isChecked() or self.editRoom_ui.radioButton_2.isChecked():
            if 100 < int(self.editRoom_ui.label_11.text()) < 1000:
                if self.editRoom_ui.spinBox.value() > 0:
                    if self.editRoom_ui.spinBox_2.value() > 0:
                        if self.editRoom_ui.spinBox_3.value() > 0:
                            if 10 < self.editRoom_ui.doubleSpinBox.value():
                                if self.editRoom_ui.textEdit.toPlainText():
                                    if 1000 <= self.editRoom_ui.doubleSpinBox_2.value():
                                        type = "Номер"
                                        if self.editRoom_ui.radioButton_2.isChecked():
                                            type = "Люкс"
                                        num = int(self.selectedNumber)
                                        self.cursor.execute(f"""UPDATE HotelRooms SET
                                            type = '{type}',
                                            roomsQuantity = {self.editRoom_ui.spinBox.value()},
                                            seatsQuantity = {self.editRoom_ui.spinBox_2.value()},
                                            windowsQuantity = {self.editRoom_ui.spinBox_3.value()},
                                            square = {self.editRoom_ui.doubleSpinBox.value()},
                                            householdAppliances = '{self.editRoom_ui.textEdit.toPlainText()}',
                                            dayPrice = {self.editRoom_ui.doubleSpinBox_2.value()},
                                            additionalAmenities = '{self.editRoom_ui.textEdit_2.toPlainText()}'
                                            WHERE number = {num}
                                            """)
                                        self.db.commit()

                                        room = self.getRoom(num)
                                        if room:
                                            room.editValues(num, type, self.editRoom_ui.spinBox.value(), self.editRoom_ui.spinBox_2.value(),
                                            self.editRoom_ui.spinBox_3.value(), self.editRoom_ui.doubleSpinBox.value(), self.editRoom_ui.textEdit.toPlainText(),
                                            room.bookingDates, self.editRoom_ui.doubleSpinBox_2.value(), self.editRoom_ui.textEdit_2.toPlainText())

                                        self.cursor.execute("SELECT * FROM HotelRooms")
                                        self.data = self.cursor.fetchall()

                                        self.windowEditRoom.close()

                                        self.messageInfo_ui.label.setText("Дані про номер успішно оновлено!")
                                        self.windowMessageInfo.exec()

                                        self.clearLabels()
                                    else:
                                        self.messageError_ui.label.setText("Ціна повинна бути не менша за 1000!")
                                        self.windowMessageError.exec()
                                else:
                                    self.messageError_ui.label.setText("Номер повинен містити побутову техніку!")
                                    self.windowMessageError.exec()
                            else:
                                self.messageError_ui.label.setText("Площа повинна бути більша за 10!")
                                self.windowMessageError.exec()
                        else:
                            self.messageError_ui.label.setText("Кількість вікон не може бути рівна 0!")
                            self.windowMessageError.exec()
                    else:
                        self.messageError_ui.label.setText("Кількість місць не може бути рівна 0!")
                        self.windowMessageError.exec()
                else:
                    self.messageError_ui.label.setText("Кількість кімнат не може бути рівна 0!")
                    self.windowMessageError.exec()
            else:
                self.messageError_ui.label.setText("Номер повинен бути більший за 100 і менший за 1000!")
                self.windowMessageError.exec()
        else:
            self.messageError_ui.label.setText("Тип не вибрано!")
            self.windowMessageError.exec()


    # Функція для видалення номеру
    def deleteButtonAction(self):
        self.isConfirmed = False
        self.question_ui.label.setText(f"Ви впевнені, що хочете видалити номер {self.selectedNumber}?")
        self.windowQuestion.exec()
        if self.isConfirmed:
            self.cursor.execute(f"DELETE FROM HotelRooms WHERE number = {self.selectedNumber}")
            self.db.commit()

            self.cursor.execute("SELECT * FROM HotelRooms")
            self.data = self.cursor.fetchall()

            # Знаходження індексу номера в self.rooms і видалення його
            index_to_remove = None
            for index, room in enumerate(self.rooms):
                if room.number == int(self.selectedNumber):
                    index_to_remove = index
                    break

            # Видалення номера зі списку self.rooms
            if index_to_remove is not None:
                del self.rooms[index_to_remove]

            col = (int(self.selectedNumber) % 100) - 1
            row = (int(self.selectedNumber) // 100) - 1
            item = self.ui.tableWidget.takeItem(row, col)
            if item is not None:
                del item

            self.clearLabels()
            self.closeEditRoomWindow()

            self.messageInfo_ui.label.setText(f"Номер {self.selectedNumber} успішно видалено!")
            self.windowMessageInfo.exec()

        self.isConfimed = False

    # Функція для бронювання номеру
    def bookButtonAction(self):
        start_date = self.bookRoom_ui.dateEdit.date()
        end_date = self.bookRoom_ui.dateEdit_2.date()

        for room in self.rooms:
            if room.number == int(self.selectedNumber):
                if start_date >= self.today and end_date < datetime.date(2030, 12, 30) and end_date >= start_date:
                    date_ranges = room.bookingDates.split()
                    error = False
                    for date_range_str in date_ranges:
                        sd_str, ed_str = date_range_str.split("-")
                        sd = datetime.datetime.strptime(sd_str, "%d.%m.%Y").date()
                        ed = datetime.datetime.strptime(ed_str, "%d.%m.%Y").date()

                        if start_date <= sd <= end_date or start_date <= ed <= end_date or sd <= start_date <= end_date <= ed:
                            error = True
                            self.messageError_ui.label.setText("Дата, вказана вами, накладається на існуючу дату бронювання!")
                            self.windowMessageError.exec()
                            break
                    if not error:
                        resDate = start_date.toString("dd.MM.yyyy") + "-" + end_date.toString("dd.MM.yyyy")
                        if room.bookingDates != "":
                            resDate = " " + resDate
                        resDate = room.bookingDates + resDate
                        resHost = self.bookRoom_ui.textEdit.toPlainText()
                        if resHost:
                            if room.host != "":
                                resHost = ", " + resHost
                            resHost = room.host + resHost
                            num = room.number
                            self.cursor.execute(f"""UPDATE HotelRooms SET
                                    bookingDate = '{resDate}',
                                    hostName = '{resHost}'
                                    WHERE number = {num}
                                """)

                            room = self.getRoom(num)
                            if room:
                                room.editValues(bookingDates=resDate, host=resHost)

                            isInList = False
                            rooms = str(room.number)
                            resDate = start_date.toString("dd.MM.yyyy") + "-" + end_date.toString("dd.MM.yyyy")
                            resHost = self.bookRoom_ui.textEdit.toPlainText()
                            for users in self.userData:
                                if resHost == users[0]:
                                    if users[2] != "":
                                        resDate = " " + resDate
                                    if users[1] != "":
                                        rooms = " " + rooms
                                    isInList = True
                                    rooms = users[1] + rooms
                                    resDate = users[2] + resDate
                                    break
                            if isInList:
                                self.cursor.execute(f"""UPDATE Users SET
                                    rooms = '{rooms}',
                                    dates = '{resDate}'
                                    WHERE name = '{resHost}'
                                """)
                            else:
                                rooms = str(room.number)
                                self.cursor.execute(f"""INSERT INTO Users VALUES (
                                    '{resHost}',
                                    {rooms},
                                    '{resDate}'
                                )""")

                            self.db.commit()
                            self.cursor.execute("SELECT * FROM HotelRooms")
                            self.data = self.cursor.fetchall()
                            self.cursor.execute("SELECT * FROM Users")
                            self.userData = self.cursor.fetchall()

                            self.closeBookRoomWindow()

                            self.messageInfo_ui.label.setText("Номер успішно заброньовано!")
                            self.windowMessageInfo.exec()

                            self.clearLabels()

                            if start_date == self.today:
                                col = (room.number % 100) - 1
                                row = (room.number // 100) - 1
                                item = self.items.get((row, col))
                                item.setBackground(QColor(255, 100, 100))
                        else:
                            self.messageError_ui.label.setText("Власника не вказано!")
                            self.windowMessageError.exec()
                else:
                    self.messageError_ui.label.setText("Дату вказано неправильно!")
                    self.windowMessageError.exec()

    # Функція для розбронювання номеру
    def unbookButtonAction(self):
        self.isConfirmed = False
        self.question_ui.label.setText("Ви впевнені, що хочете скасувати бронь на вибрану дату?")
        self.windowQuestion.exec()
        if self.isConfirmed:
            selected_item = self.unbookRoom_ui.comboBox.currentText()
            if selected_item:
                for room in self.rooms:
                    if room.number == int(self.selectedNumber):
                        dates = room.bookingDates.split()
                        persons = room.host.split(', ')
                        persons = [i for i in persons if i != ""]
                        selectedPerson = ""
                        for i in range(len(dates)):
                            if dates[i] == selected_item:
                                del dates[i]
                                selectedPerson = persons[i]
                                del persons[i]
                                break
                        dates = ' '.join(dates)
                        persons = ', '.join(persons)
                        num = room.number
                        self.cursor.execute(f"""UPDATE HotelRooms SET
                            bookingDate = '{dates}',
                            hostName = '{persons}'
                            WHERE number = {num}
                        """)

                        room = self.getRoom(num)
                        if room:
                            room.editValues(bookingDates=dates, host=persons)

                        for users in self.userData:
                            if users[0] == selectedPerson:
                                dates = users[2].split()
                                rooms = users[1].split()
                                for i in range(len(dates)):
                                    if dates[i] == selected_item:
                                        del dates[i]
                                        del rooms[i]
                                        break
                                dates = ' '.join(dates)
                                rooms = ' '.join(rooms)
                                self.cursor.execute(f"""UPDATE Users SET
                                    rooms = '{rooms}',
                                    dates = '{dates}'
                                    WHERE name = '{selectedPerson}'
                                """)

                        self.db.commit()

                        self.cursor.execute("SELECT * FROM HotelRooms")
                        self.data = self.cursor.fetchall()

                        self.cursor.execute("SELECT * FROM Users")
                        self.userData = self.cursor.fetchall()

                        self.closeUnbookRoomWindow()

                        self.messageInfo_ui.label.setText("Бронь успішно скасовано!")
                        self.windowMessageInfo.exec()

                        self.clearLabels()
                        self.closeBookRoomWindow()
            else:
                self.messageError_ui.label.setText("Дату не вибрано!")
                self.windowMessageError.exec()
        for room in self.rooms:
            if room.number == int(self.selectedNumber):
                if room.bookingDates != "":
                    self.bookRoom_ui.label_2.setText(f"Заброньовані дати: {room.bookingDates}")
                else:
                    self.bookRoom_ui.label_2.setText("У номера немає заброньованих дат")

                date_ranges = room.bookingDates.split()
                roomColor = QColor(100, 255, 100)
                for date_range_str in date_ranges:
                    if room.bookingDates == "":
                        continue
                    start_date_str, end_date_str = date_range_str.split("-")
                    start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").date()
                    end_date = datetime.datetime.strptime(end_date_str, "%d.%m.%Y").date()
                    if start_date <= self.today <= end_date:
                        roomColor = QColor(255, 100, 100)
                        break
                col = (room.number % 100) - 1
                row = (room.number // 100) - 1
                item = self.items.get((row, col))
                item.setBackground(roomColor)

        self.bookRoom_ui.dateEdit.setDate(QDate())
        self.bookRoom_ui.dateEdit_2.setDate(QDate())
        self.bookRoom_ui.textEdit.clear()


    # Функція для radiobutton
    def toggleTextEditState(self):
        if self.addRoom_ui.radioButton.isChecked():
            self.addRoom_ui.textEdit_2.setReadOnly(True)
        elif self.addRoom_ui.radioButton_2.isChecked():
            self.addRoom_ui.textEdit_2.setReadOnly(False)

    # Функція очищення вікна додавання номеру
    def clearAddRoomWindow(self):
        self.addRoom_ui.spinBox.setValue(0)
        self.addRoom_ui.spinBox_2.setValue(0)
        self.addRoom_ui.spinBox_3.setValue(0)
        self.addRoom_ui.spinBox_4.setValue(0)
        self.addRoom_ui.doubleSpinBox.setValue(0)
        self.addRoom_ui.doubleSpinBox_2.setValue(0)
        self.addRoom_ui.textEdit.clear()
        self.addRoom_ui.textEdit_2.clear()

    # Функція підтвердження дії
    def continueAction(self):
        self.isConfirmed = True
        self.windowQuestion.close()

    # Функція для пошуку за датою
    def searchAction(self):
        error = False
        start_date = self.menu1_ui.dateEdit.date()
        end_date = self.menu1_ui.dateEdit_2.date()
        popularity = {}
        for room in self.rooms:
            if start_date >= self.today and end_date < datetime.date(2030, 12, 30) and end_date >= start_date:
                date_ranges = room.bookingDates.split()
                if self.isSearchOfFree:
                    isFree = all(
                        start_date > datetime.datetime.strptime(end, "%d.%m.%Y").date() or
                        end_date < datetime.datetime.strptime(start, "%d.%m.%Y").date()
                        for start, end in (date_range_str.split("-") for date_range_str in date_ranges)
                    )
                    num = int(room.number)
                    col = (num % 100) - 1
                    row = (num // 100) - 1
                    if isFree:
                        item = self.items.get((row, col))
                        item.setBackground(QColor(255, 215, 0))
                    else:
                        item = self.items.get((row, col))
                        item.setBackground(QColor(192, 192, 192))
                else:
                    count = 0
                    for date_range_str in date_ranges:
                        sd_str, ed_str = date_range_str.split("-")
                        sd = datetime.datetime.strptime(sd_str, "%d.%m.%Y").date()
                        ed = datetime.datetime.strptime(ed_str, "%d.%m.%Y").date()
                        if start_date <= sd <= end_date or start_date <= ed <= end_date or sd <= start_date <= end_date <= ed:
                            count += 1
                    popularity[room.number] = count
            else:
                self.messageError_ui.label.setText("Дату вказано неправильно!")
                self.windowMessageError.exec()
                error = True
                break

        if not error:
            if self.isSearchOfFree:
                self.windowMenu1.close()
                self.ui.closeButton_2.show()
                start_date = start_date.toString("dd.MM.yyyy")
                end_date = end_date.toString("dd.MM.yyyy")
                self.ui.label_28.setText(f"Вибрана дата {start_date}-{end_date}")
            else:
                max_value = None
                max_key = None

                for key, value in popularity.items():
                    if max_value is None or value > max_value:
                        max_key = key
                        max_value = value
                if max_value:
                    self.result_ui.label.setText(f"Найпопулярніший номер: {max_key}\n\nКількість гостей: {max_value}")
                else:
                    self.result_ui.label.setText("У вибраному діапазоні жоден номер не має жодного клієнта")
                self.windowResult.exec()
                self.windowMenu1.close()

    # Функція для пошуку за вартістю
    def searchAction_2(self):
        valueFrom = self.menu2_ui.doubleSpinBox.value()
        valueTo = self.menu2_ui.doubleSpinBox_2.value()
        for room in self.rooms:
            num = int(room.number)
            col = (num % 100) - 1
            row = (num // 100) - 1
            if valueFrom <= room.price <= valueTo:
                item = self.items.get((row, col))
                item.setBackground(QColor(255, 215, 0))
            else:
                item = self.items.get((row, col))
                item.setBackground(QColor(192, 192, 192))
        self.windowMenu2.close()
        self.ui.closeButton_2.show()
        self.ui.label_28.setText(f"Вибраний діапазон вартості {valueFrom}-{valueTo}")

    # Функція отримання номеру зі списку номерів за відповідним номером
    def getRoom(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    # Функції закриття вікон
    def closeAddRoomWindow(self):
        self.windowAddRoom.close()

    def closeEditRoomWindow(self):
        self.windowEditRoom.close()

    def closeBookRoomWindow(self):
        self.windowBookRoom.close()

    def closeUnbookRoomWindow(self):
        self.windowUnbookRoom.close()

    def closeInfoWindow(self):
        self.windowMessageInfo.close()

    def closeErrorWindow(self):
        self.windowMessageError.close()

    def closeQuestionWindow(self):
        self.windowQuestion.close()

    def closeResult(self):
        self.windowResult.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec())
