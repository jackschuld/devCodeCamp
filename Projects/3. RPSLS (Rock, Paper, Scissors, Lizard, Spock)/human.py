from player import Player


class Human(Player):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age