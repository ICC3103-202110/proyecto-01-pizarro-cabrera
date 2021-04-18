class Coin:

    #Constants
    singleCoin= 1

    #Constructor
    def __init__(self, quantity):
        self.__quantity = quantity

    #Getters and Setters
    
    @property
    def coin(self):
        return self.__quantity

    @value.setter
    def quantity(self,quantity)
        if quantity < 0:
            self.__quantity = 0
        else:
            self.__quantity = quantity

    #Methods

    def add_coin(self):
        self.__quantity += singleCoin

    def substract_coin(self):
        self.__quantity -= singleCoin


    