class Coin:

    #Constants
    singleCoin= 1

    #Constructor
    def __init__(self, quantity):
        self.__quantity = quantity

    #Getters and Setters
    
    @property
    def quantity(self):
        return self.__quantity

    #Methods

    def add_coin(self):
        self.__quantity += singleCoin

    def substract_coin(self):
        self.__quantity -= singleCoin


    