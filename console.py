from player import Player
class Console:

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))

    @staticmethod
    def get_int_input(message):
        return int(input(message))

    @staticmethod
    def print_options3(players,i):
        print("ACTIONS:            "+players[i].name+"'s Cards: "+str(players[2].cards)+"")
        print("General Actions:    "+players[0].name+"'s Coins: "+str(players[0].coins)+"")
        print("1. Income           "+players[1].name+"'s Coins: "+str(players[1].coins)+"")
        print("2. Foreign Aid      "+players[2].name+"'s Coins: "+str(players[2].coins)+"")
        print("3. Coup")
        print("Card Actions         "+players[0].name+"'s Cards: "+str(players[0].censored_cards)+"")
        print("4. Tax               "+players[1].name+"'s Cards: "+str(players[1].censored_cards)+"")
        print("5. Assasinate        "+players[2].name+"'s Cards: "+str(players[2].censored_cards)+"")
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

    @staticmethod
    def print_react_to_ca(players,counteraction):
        print("TABLE:")
        for i in range(len(players)):
            print(players[i].name+"'s cards: "+str(players[i].censored_cards))
        print("React to the counteraction: ")
        print("1. Challenge")
        print("2. pass")

    @staticmethod
    def print_options4(players,i):
        print("ACTIONS:    "+players[i].name+"'s Cards: "+str(players[i].cards)+"")
        print("General Actions:    "+players[0].name+"'s Coins: "+str(players[0].coins)+"")
        print("1. Income           "+players[1].name+"'s Coins: "+str(players[1].coins)+"")
        print("2. Foreign Aid      "+players[2].name+"'s Coins: "+str(players[2].coins)+"")
        print("3. Coup             "+players[3].name+"'s Coins: "+str(players[3].coins)+"")
        print("Card Actions:        "+players[0].name+"'s Cards: "+str(players[0].censored_cards)+"")
        print("4. Tax               "+players[1].name+"'s Cards: "+str(players[1].censored_cards)+"")
        print("5. Assasinate        "+players[2].name+"'s Cards: "+str(players[2].censored_cards)+"")
        print("6. Exchange          "+players[3].name+"'s Cards: "+str(players[3].censored_cards)+"")
        print("7. Steal")

    @staticmethod
    def print_options2(players,i):
        print("ACTIONS:            "+players[i].name+"'s Cards: "+str(players[2].cards)+"")
        print("General Actions:    "+players[0].name+"'s Coins: "+str(players[0].coins)+"")
        print("1. Income           "+players[1].name+"'s Coins: "+str(players[1].coins)+"")
        print("2. Foreign Aid")
        print("3. Coup")
        print("Card Actions         "+players[0].name+"'s Cards: "+str(players[0].censored_cards)+"")
        print("4. Tax               "+players[1].name+"'s Cards: "+str(players[1].censored_cards)+"")
        print("5. Assasinate")
        print("6. Exchange")
        print("7. Steal")

    

    
    




