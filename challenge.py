from player import Player
from deck import Deck

class Challenge:

    @staticmethod
    def challenge(players,i,j):
        card = ""
        if players[i].action in players[i].cards:
            print(players[i].name+" has the "+players[i].action+" card!")
            print(players[j].name+" loses the challenge!")
            print(str(players[j].cards))
            card = input("Select an influence you wish to lose: ")
            print(card)
            if "HIDDEN" in players[j].censored_cards:
                n = players[j].censored_cards.index("HIDDEN")
                print(n)
                players[j].set_censored_card(n,card)

        else:
            print(players[i].name+" doesn't have the "+players[i].action+" card!")
            print(players[i].name+" loses the challenge!")
            print(players[i].name+"'s cards:")
            print(str(players[i].cards))
            card = input("Select an influence you wish to lose(ex: Duke): ")
            print(card)
            if "HIDDEN" in players[i].censored_cards:
                n = players[i].censored_cards.index("HIDDEN")
                print(n)
                players[i].set_censored_card(n,card)
            
                

