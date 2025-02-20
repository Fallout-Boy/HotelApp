import sqlite3

db = sqlite3.connect('myDataBase.db')

cursor = db.cursor()

cursor.execute("SELECT * FROM HotelRooms")
print(cursor.fetchall())

db.commit()

db.close()

# self.cursor.execute("""CREATE TABLE HotelRooms (
        #    number integer,
        #    type text,
        #    roomsQuantity integer,
        #    seatsQuantity integer,
        #    windowsQuantity integer,
        #    square float,
        #    householdAppliances text,
        #    bookingDate text,
        #    dayPrice float,
        #    additionalAmenities text,
        #    hostName text
        #)""")
# cursor.execute("""CREATE TABLE Users (
#     name text,
#     rooms text,
#     dates text
# )""")
