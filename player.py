from card import Card

class Player:

    #Constructor
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        self.__coins = 0
        self.__cards = []
        self.__censored_cards = []

    #Getters and Setters

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        return self.__cards

    @property
    def censored_cards(self):
        return self.__censored_cards

    @censored_cards.setter
    def censored_cards(self, censored_cards):
        return self.__censored_cards

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, coins):
        if coins >= 0:
            self.__coins = coins
        else:
            self.__coins = 0

    #Methods
    def add_coin(self):
        self.__coins += 1

    def substract_coin(self):
        self.__coins -= 1

