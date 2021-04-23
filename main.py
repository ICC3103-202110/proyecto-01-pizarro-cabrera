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
from challenge import Challenge

class Game:
    NUMBER_OF_PLAYERS = 0
    players = []
    reactions = []
    __board = None
    __current_player = None
    __deck = Deck([])
    duke = Duke("Duke")
    assasin = Assasin("Assasin")
    ambassador = Ambassador("Ambassador")
    captain = Captain("Captain")
    contessa = Contessa("Contessa")
    option = False
    win = False

    @classmethod
    def play(cls):
        cls.__set_number_of_players()
        cls.__set_players()
        cls.__deck.build_deck(cls.duke,cls.assasin,cls.ambassador,cls.captain,cls.contessa)
        cls.__fill_censored_cards()
        cls.__distribute_cards()
        cls.__distribute_coins()

        while cls.win != True:
            for i in range(len(cls.players)):
                while cls.option != True:
                    if len(cls.players)==3:
                        Console.print_options3(cls.players,i)
                    if len(cls.players)==4:
                        Console.print_options4(cls.players,i)
                    n = Console.get_int_input("Select an action number, "+cls.players[i].name+" (ex: 1): ")
                    call = cls.__option_selec(n,cls.players[i],cls.option)

                if i == 0:
                    Console.print_table(cls.players,call,1)
                    cls.players[1].set_reaction(Console.get_int_input(cls.players[1].name+" select an option: "))
                    cls.__check_if_challenge(i,1)
                    Console.print_table(cls.players,call,2)
                    cls.players[2].set_reaction(Console.get_int_input(cls.players[2].name+" select an option: "))
                    cls.__check_if_challenge(i,2)
                    if len(cls.players) == 4:
                        Console.print_table(cls.players,call,3)
                        cls.players[3].set_reaction(Console.get_int_input(cls.players[3].name+" select an option: "))
                    cls.__execute_action(call,i)
        
                if i == 1:
                    Console.print_table(cls.players,call,2)
                    cls.players[2].set_reaction(Console.get_int_input(cls.players[2].name+" select an option: "))
                    if len(cls.players) == 4:
                        Console.print_table(cls.players,call,3)
                        cls.players[3].set_reaction(Console.get_int_input(cls.players[3].name+" select an option: "))
                    Console.print_table(cls.players,call,0)
                    cls.players[0].set_reaction(Console.get_int_input(cls.players[0].name+" select an option: "))
                    cls.__execute_action(call,i)

                if i == 2:
                    if len(cls.players) == 4:
                        Console.print_table(cls.players,call,3)
                        cls.players[3].set_reaction(Console.get_int_input(cls.players[3].name+" select an option: "))
                    Console.print_table(cls.players,call,0)
                    cls.players[0].set_reaction(Console.get_int_input(cls.players[0].name+" select an option: "))
                    Console.print_table(cls.players,call,1)
                    cls.players[1].set_reaction(Console.get_int_input(cls.players[1].name+" select an option: "))
                    cls.__execute_action(call,i)

                if len(cls.players) == 4:
                    if i == 3:
                        Console.print_table(cls.players,call,0)
                        cls.players[0].set_reaction(Console.get_int_input(cls.players[0].name+" select an option: "))
                        Console.print_table(cls.players,call,1)
                        cls.players[1].set_reaction(Console.get_int_input(cls.players[1].name+" select an option: "))
                        Console.print_table(cls.players,call,2)
                        cls.players[2].set_reaction(Console.get_int_input(cls.players[2].name+" select an option: "))
                        cls.__execute_action(call,i)

                cls.option = False
            
            if (cls.players[0].censored_cards[0] and cls.players[0].censored_cards[1]) != "HIDDEN":
                cls.win = True


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
                Actions.income(cls.players,i)

    @classmethod
    def __option_selec(cls,n,player,option):
        if n == 1:
            call = "Income"
            cls.option = True
            return call
        if n == 2:
            call = "Foreign Aid"
            cls.option = True
            return call
        if n == 3 and player.coins>=7:
            call = "Coup"
            cls.option = True
            return call
        if n == 4:
            call = "Tax"
            cls.option = True
            player.set_action("Duke")
            return call
        if n == 5 and player.coins>=3:
            call = "Assasinate"
            cls.option = True
            player.set_action("Assasin")
            return call
        if n == 6:
            call = "Exchange"
            cls.option = True
            player.set_action("Ambassador")
            return call
        if n == 7:
            call = "Steal"
            cls.option = True
            player.set_action("Captain")
            return call
        else:
            print("Insuficient funds, try again:")
            call = ""
            return call

    @classmethod
    def __fill_censored_cards(cls):
        for i in range(len(cls.players)):
            cls.players[i].censored_cards.append("HIDDEN")
            cls.players[i].censored_cards.append("HIDDEN")

    @classmethod
    def __check_if_challenge(cls,i,j):
        if cls.players[j].reaction == 2:
            print(cls.players[j].name+" challenged "+cls.players[i].name+"!")
            Challenge.challenge(cls.players,i,j)

    @classmethod
    def __execute_action(cls,call,i):
        if call == "Income":
            Actions.income(cls.players,i)
        if call == "Foreign aid":
            Actions.foreign_aid(cls.players,i)
        if call == "Coup":
            Actions.coup(cls.players,i)
        if call == "Tax":
            Actions.tax(cls.players,i)
        if call == "Assasinate":
            Actions.assasinate(cls.players,i)


if __name__ == "__main__":
    Game.play()