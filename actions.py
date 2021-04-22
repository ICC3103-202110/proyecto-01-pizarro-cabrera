from player import Player

class Actions:

    @staticmethod
    def income(player):
        player.add_coin()

    @staticmethod
    def foreign_aid(player):
        for i in range(2):
            player.add_coin

    @staticmethod
    def coup(player):
        for i in range(7):
            player.substract_coin()

    @staticmethod
    def tax(player):
        for i in range(3):
            player.add_coin()

    @staticmethod
    def assasinate(player):
        for i in range(3):
            player.substract_coin()