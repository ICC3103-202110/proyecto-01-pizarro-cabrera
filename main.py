from player import Player
from duke import Duke
from console import Console
from deck import Deck
from assasin import Assasin
from duke import Duke
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa
from actions import Actions

class Game:
    NUMBER_OF_PLAYERS = 0
    players = []
    __board = None
    __current_player = None
    __deck = Deck([])
    duke = Duke("Duke")
    assasin = Assasin("Assasin")
    ambassador = Ambassador("Ambassador")
    captain = Captain("Captain")
    contessa = Contessa("Contessa")
    option = False

    @classmethod
    def play(cls):
        cls.__set_number_of_players()
        cls.__set_players()
        cls.__deck.build_deck(cls.duke,cls.assasin,cls.ambassador,cls.captain,cls.contessa)
        cls.__fill_censored_cards()
        cls.__distribute_cards()
        cls.__distribute_coins()
        while cls.option != True:
            n = Console.print_options(cls.players[0].name, cls.players[0].cards,cls.players[0].coins)
            call = cls.__option_selec(n,cls.players[0],cls.option)
        reaction = Console.print_table(cls.players,call,1)

        print(cls.players[0].coins)


    @classmethod
    def __set_players(cls):
        for i in range(1, cls.NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                'Please enter player\'s {} name: ', [i]
            )
            cls.players.append(Player(name, i))
        cls.__current_player = cls.players[1]

    @classmethod
    def __set_number_of_players(cls):
        while cls.NUMBER_OF_PLAYERS>4 or cls.NUMBER_OF_PLAYERS<3:
            number = Console.get_int_input(
                "How many players wish to play(Min=3,Max=4): "
            )
            cls.NUMBER_OF_PLAYERS = number

    @classmethod
    def __distribute_cards(cls):
        for i in range(len(cls.players)):
            cls.players[i].cards.append(cls.__deck.draw_card())
            cls.players[i].cards.append(cls.__deck.draw_card())

    @classmethod
    def __distribute_coins(cls):
        for i in range(len(cls.players)):
            for j in range(2):
                Actions.income(cls.players[i])

    @classmethod
    def __option_selec(cls,n,player,option):
        if n == 1:
            call = "Income"
            cls.option = True
        if n == 2:
            call = "Foreign Aid"
            cls.option = True
        if n == 3 and player.coins>=7:
            call = "Coup"
            cls.option = True
        if n == 4:
            call = "Tax"
            cls.option = True
        if n == 5 and player.coins>=3:
            call = "Assasinate"
            cls.option = True
        if n == 6:
            call = "Exchange"
            cls.option = True
        if n == 7:
            call = "Steal"
            cls.option = True
        else:
            print("Insuficient funds, try again:")
        return call

    @classmethod
    def __fill_censored_cards(cls):
        for i in range(len(cls.players)):
            cls.players[i].censored_cards.append("HIDDEN")
            cls.players[i].censored_cards.append("HIDDEN")


if __name__ == "__main__":
    Game.play()