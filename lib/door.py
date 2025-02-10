class Door():
    def __init__(self, colour):
        self.colour = colour

    def open(self, person): #Mock
        return person.open_door()