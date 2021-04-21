from card import Card

class Player:

    #Constructor
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.coins = 0
        self.cards = []

    #Getters and Setters

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        for i in range(2):
            cards.append(1)

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, coins):
        if coins >= 0:
            self.__coins = coins
        else:
            self.__coins = 0

