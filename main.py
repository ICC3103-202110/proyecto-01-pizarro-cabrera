from player import Player
from duke import Duke
from console import Console
from deck import Deck
from assasin import Assasin
from duke import Duke
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa

class Game:
    NUMBER_OF_PLAYERS = 0
    __players = []
    __board = None
    __current_player = None
    __deck = Deck([])
    duke = Duke("Duke")
    assasin = Assasin("Assasin")
    ambassador = Ambassador("Ambassador")
    captain = Captain("Captain")
    contessa = Contessa("Contessa")

    @classmethod
    def play(cls):
        cls.__set_number_of_players()
        cls.__set_players()
        cls.__deck.build_deck(cls.duke,cls.assasin,cls.ambassador,cls.captain,cls.contessa)
        cls.__distribute_cards()
        Console.print_options()


    @classmethod
    def __set_players(cls):
        for i in range(1, cls.NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                'Please enter player\'s {} name: ', [i]
            )
            cls.__players.append(Player(name, i))
        cls.__current_player = cls.__players[1]

    @classmethod
    def __set_number_of_players(cls):
        while cls.NUMBER_OF_PLAYERS>4 or cls.NUMBER_OF_PLAYERS<3:
            number = Console.get_int_input(
                "How many players wish to play(Min=3,Max=4): "
            )
            cls.NUMBER_OF_PLAYERS = number

    @classmethod
    def __search_deck(cls):
        for i in cls.__deck.cardlist:
            print(i)

    @classmethod
    def __distribute_cards(cls):
        for i in range(len(cls.__players)):
            cls.__players[i].cards.append(cls.__deck.draw_card())
            cls.__players[i].cards.append(cls.__deck.draw_card())






if __name__ == "__main__":
    Game.play()