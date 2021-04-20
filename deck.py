from duke import Duke
from assasin import Assasin
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa
import random

class Deck:

    #Constructor
    def __init__(self, cardlist):
        self.cardlist = []

    #Getters and Setters
    @property
    def cardlist(self):
        return cardlist

    @cardlist.setter
    def cardlist(self):
        return cardlist

    #Methods

    def build_deck(self):
        for i in range(3):
            cardlist.append(Duke())
        for i in range(3):
            cardlist.append(Assasin())
        for i in range(3):
            cardlist.append(Ambassador())
        for i in range(3):
            cardlist.append(Captain())
        for i in range(3):
            cardlist.append(Contessa())
        random.shuffle(cardlist)

    def draw_card(self):
        return __cardlist.pop(cardlist[len(cardlist)])
        
    

