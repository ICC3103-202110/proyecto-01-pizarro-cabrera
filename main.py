from player import Player
from duke import Duke
from console import Console


class Game:
    MAX_NUMBER_OF_PLAYERS = 4
    __players = []
    __board = None
    __current_player = None 

    @classmethod
    def play(cls):
        cls.__set_players()

    @classmethod
    def __set_players(cls):
        for i in range(1, cls.MAX_NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                'Please enter player\'s {} name: ', [i]
            )
            cls.__players.append(Player(name, i))
        cls.__current_player = cls.__players[0]



if __name__ == "__main__":
    Game.play()