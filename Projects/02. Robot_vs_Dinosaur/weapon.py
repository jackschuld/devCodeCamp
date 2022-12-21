class Weapon:
    
    def __init__ (self, name, attack_power, affect_to_self=0):
        self.name = name
        self.attack_power = attack_power
        self.affect_to_self = affect_to_self
    