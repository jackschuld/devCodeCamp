class Robot:
    
    def __init__ (self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    

    def attack(self, dinosaur):
        input(f'Press enter to attack {dinosaur.name}, the dinosaur')
        dinosaur.health -= self.attack