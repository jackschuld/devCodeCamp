class Robot:
    
    def __init___ (self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack = attack_power
    

    def attack(self, dinosaur):
        input(f'Press enter to attack {dinosaur.name}, the dinosaur')
        dinosaur.health -= self.attack