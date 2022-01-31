class Sale:
    def __init__(self,manufacturer,model,price,quantity,date_of_purchase,discount):
        self.__manufacturer=manufacturer
        self.__model = model
        self.__price = price
        self.__quantity = quantity
        self.__date_of_purchase = date_of_purchase
        self.__discount = discount

#--------Getters--------#
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
    def date_of_purchase(self):
        return self.__date_of_purchase

    @property
    def discount(self):
        return self.__discount

    @property
    def as_table_value(self):
        return f"'{self.manufacturer}', '{self.model}', '{self.price}', '{self.quantity}','{self.date_of_purchase}','{self.discount}'"

    @property
    def parameters(self) -> dict:
        return {"manufacturer": self.manufacturer,
                "model": self.model,
                "price": self.price,
                "quantity": self.quantity,
                "date_of_purchase": self.date_of_purchase,
                "discount": self.discount}

#-----------------------------------#
    def setQuantity(self,quantity):
        self.__quantity = quantity





