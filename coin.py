class Coin:

    #Constructor
    def __init__(self, coin):
        self.__coin = []

    #Getters and Setters
    
    @property
    def deck(self):
        return self.__coin