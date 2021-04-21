from duke import Duke
from assasin import Assasin
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa
import random

class Deck:

    #Constructor
    def __init__(self, cardlist):
        self.__cardlist = []

    #Getters and Setters
    @property
    def cardlist(self):
        return __cardlist

    @cardlist.setter
    def cardlist(self):
        return __cardlist

    #Methods
    def build_deck(self,duke,assasin,ambassador,captain,contessa):
        for i in range(3):
            self.__cardlist.append(duke.name)
        for i in range(3):
            self.__cardlist.append(assasin.name)
        for i in range(3):
            self.__cardlist.append(ambassador.name)
        for i in range(3):
            self.__cardlist.append(captain.name)
        for i in range(3):
            self.__cardlist.append(contessa.name)
        random.shuffle(self.__cardlist)



    def draw_card(self):
        return __cardlist.pop(__cardlist[len(__cardlist)])
 
    

