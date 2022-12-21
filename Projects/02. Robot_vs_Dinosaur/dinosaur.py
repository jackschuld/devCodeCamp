class Dinosaur:
    
    def __init__ (self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    
    def attack(self, robot):
        print(f'\n{self.name}\'s turn!\n')
        print(f'TARGET:\n{robot.name}\'s health: {robot.health}\n')
        input(f'Press enter to have {self.name} attack {robot.name}')
        robot.health -= self.attack_power
        print(f'{robot.name}\'s health is now {robot.health}\n')