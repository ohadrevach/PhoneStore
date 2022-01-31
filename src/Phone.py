class Phone:
    def __init__(self, manufacturer, model, price, quantity, IMEI, warranty):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price
        self.__quantity = quantity
        self.__IMEI = IMEI
        self.__warranty = warranty

# --------Getters--------#
    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def model(self):
        return self.__model

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def IMEI(self):
        return self.__IMEI

    @property
    def warranty(self):
        return self.__warranty

    @property
    def as_table_value(self):
        return f"'{self.manufacturer}', '{self.model}', '{self.price}', '{self.quantity}', '{self.IMEI}', '{self.warranty}'"

    @property
    def parameters(self) -> dict:
        return {'manufacturer': self.manufacturer, 'price': self.price, 'model':self.model, 'quantity': self.quantity, 'IMEI': self.IMEI, 'warranty': self.warranty}

# -----------------------------------#
    def setQuantity(self, quantity):
        self.__quantity = quantity






