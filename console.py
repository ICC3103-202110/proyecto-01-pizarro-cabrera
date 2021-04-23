from player import Player
class Console:

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))

    @staticmethod
    def get_int_input(message):
        return int(input(message))

    @staticmethod
    def print_options(player_name,cards,player_coins):
        print("ACTIONS:    "+player_name+"'s Cards: "+str(cards)+"")
        print("General Actions:    "+player_name+"'s Coins: "+str(player_coins)+"")
        print("1. Income")
        print("2. Foreign Aid")
        print("3. Coup")
        print("Card Actions:")
        print("4. Tax")
        print("5. Assasinate")
        print("6. Exchange")
        print("7. Steal")

    @staticmethod
    def print_table(players,call,player_number):
        print("TABLE:")
        for i in range(len(players)):
            print(players[i].name+"'s cards: "+str(players[i].censored_cards))
        print("React to the call: "+str(call))
        print("1. Counteract")
        print("2. Challenge")
        print("3. pass")
    




