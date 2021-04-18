class Card:

    #Constructor
    def __init__(self, name):
        self.__name = name
        self.discovered = False
        self.hidden = True


    #Getters and Setters
    
    @property
    def name(self):
        return self.__name

    @property
    def discovered(self):
        return self.discovered

    @property
    def hidden(self):
        return self.hidden

    @discovered.setter
    def discovered(self, discovered):
        self.__discovered = discovered

    @hidden.setter
    def hidden(self, hidden):
        self.__hidden = hidden

    #Methods

    def action():
        pass


