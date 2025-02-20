class Room:
    def __init__(self, number, lux, roomQuantity, seatQuantity, windowQuantity, square, householdAppliances, bookingDates, price, additionalAmenities, host):
        self.number = number
        self.lux = lux
        self.roomQuantity = roomQuantity
        self.seatQuantity = seatQuantity
        self.windowQuantity = windowQuantity
        self.square = square
        self.householdAppliances = householdAppliances
        self.bookingDates = bookingDates
        self.price = price
        self.additionalAmenities = additionalAmenities
        self.host = host

    def editValues(self, number=None, lux=None, roomQuantity=None, seatQuantity=None, windowQuantity=None,
                     square=None, householdAppliances=None, bookingDates=None, price=None,
                     additionalAmenities=None, host=None):
            self.number = number if number is not None else self.number
            self.lux = lux if lux is not None else self.lux
            self.roomQuantity = roomQuantity if roomQuantity is not None else self.roomQuantity
            self.seatQuantity = seatQuantity if seatQuantity is not None else self.seatQuantity
            self.windowQuantity = windowQuantity if windowQuantity is not None else self.windowQuantity
            self.square = square if square is not None else self.square
            self.householdAppliances = householdAppliances if householdAppliances is not None else self.householdAppliances
            self.bookingDates = bookingDates if bookingDates is not None else self.bookingDates
            self.price = price if price is not None else self.price
            self.additionalAmenities = additionalAmenities if additionalAmenities is not None else self.additionalAmenities
            self.host = host if host is not None else self.host
