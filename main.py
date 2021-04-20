from player import Player
from duke import Duke
from console import Console
from deck import Deck

class Game:
    NUMBER_OF_PLAYERS = 0
    __players = []
    __board = None
    __current_player = None
    

    @classmethod
    def play(cls):
        cls.__set_number_of_players()
        cls.__set_players()
        
    @classmethod
    def __set_players(cls):
        for i in range(1, cls.NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                'Please enter player\'s {} name: ', [i]
            )
            cls.__players.append(Player(name, i))
        cls.__current_player = cls.__players[0]

    @classmethod
    def __set_number_of_players(cls):
        while cls.NUMBER_OF_PLAYERS>4 or cls.NUMBER_OF_PLAYERS<3:
            number = Console.get_int_input(
                "How many players wish to play(Min=3,Max=4): "
            )
            cls.NUMBER_OF_PLAYERS = number



if __name__ == "__main__":
    Game.play()