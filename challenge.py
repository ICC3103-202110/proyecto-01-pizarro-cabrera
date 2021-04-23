from player import Player
from deck import Deck

class Challenge:

    @staticmethod
    def challenge(players,i):
        card = ""
        if players[i].action in players[i].cards:
            print(players[i].name+"Has the "+players[i].action+" card!")
                #card = players[i].pop(players[i].cards.index(players[i].action))
                #Deck.__cardlist.append(card)
                #random.shuffle(Deck.__cardlist)

        else:
            print(players[i].name+"doesn't have the "+players[i].action+" card!")
                

