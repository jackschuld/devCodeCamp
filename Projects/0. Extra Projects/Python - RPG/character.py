class Character:
    def __init__(self, name, hp, attacks, comp=True):
        self.name = name
        self.health = 100
        self.hp = hp
        self.attacks = attacks
        self.comp = comp
    
