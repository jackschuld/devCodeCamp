class Robot:
    
    def __init__ (self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    

    def attack(self, dinosaur):
        print('\nRobot\'s turn!')
        input(f'Press enter to have the robot attack {dinosaur.name}')
        dinosaur.health -= self.attack_power.attack_power
        print(f'{dinosaur.name}\'s health is now {dinosaur.health}')