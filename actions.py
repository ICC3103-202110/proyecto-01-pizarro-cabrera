from player import Player

class Actions:

    @staticmethod
    def income(players,i):
        players[i].add_coin()

    @staticmethod
    def foreign_aid(players,i):
        for j in range(2):
            players[i].add_coin

    @staticmethod
    def coup(players,i):
        for j in range(7):
            players[i].substract_coin()
        print("The Action Coup was succesfully commited")
        victim = input("Select a player you wish to coup(ex: playername): ")
        if players[0].name == victim:
            print(victim+"'s cards:")
            print(str(players[0].cards))
            card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
            if "HIDDEN" in players[0].censored_cards:
                n = players[0].censored_cards.index("HIDDEN")

                players[0].set_censored_card(n,card)

        if players[1].name == victim:
            print(victim+"'s cards:")
            print(str(players[1].cards))
            card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
            if "HIDDEN" in players[1].censored_cards:
                n = players[1].censored_cards.index("HIDDEN")

                players[1].set_censored_card(n,card)

        if players[2].name == victim:
            print(victim+"'s cards:")
            print(str(players[2].cards))
            card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
            if "HIDDEN" in players[2].censored_cards:
                n = players[2].censored_cards.index("HIDDEN")

                players[2].set_censored_card(n,card)

        if len(players) == 4:
            if players[3].name == victim:
                print(victim+"'s cards:")
                print(str(players[3].cards))
                card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
                if "HIDDEN" in players[3].censored_cards:
                    n = players[3].censored_cards.index("HIDDEN")

                    players[3].set_censored_card(n,card)

    @staticmethod
    def tax(players,i):
        for j in range(3):
            players[i].add_coin()

    @staticmethod
    def assasinate(players,i):
        card = ""
        for i in range(3):
            players[i].substract_coin()
        print("The Action assasinate was succesfully commited")
        victim = input("Select a player you wish to assasinate(ex: playername): ")
        if players[0].name == victim:
            print(victim+"'s cards:")
            print(str(players[0].cards))
            card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
            if "HIDDEN" in players[0].censored_cards:
                n = players[0].censored_cards.index("HIDDEN")

                players[0].set_censored_card(n,card)

        if players[1].name == victim:
            print(victim+"'s cards:")
            print(str(players[1].cards))
            card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
            if "HIDDEN" in players[1].censored_cards:
                n = players[1].censored_cards.index("HIDDEN")

                players[1].set_censored_card(n,card)

        if players[2].name == victim:
            print(victim+"'s cards:")
            print(str(players[2].cards))
            card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
            if "HIDDEN" in players[2].censored_cards:
                n = players[2].censored_cards.index("HIDDEN")

                players[2].set_censored_card(n,card)

        if len(players) == 4:
            if players[3].name == victim:
                print(victim+"'s cards:")
                print(str(players[3].cards))
                card = input("Wich influence do wish to lose, "+victim+" (ex: Duke): ")
                if "HIDDEN" in players[3].censored_cards:
                    n = players[3].censored_cards.index("HIDDEN")

                    players[3].set_censored_card(n,card)



            