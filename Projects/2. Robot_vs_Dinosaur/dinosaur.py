class Dinosaur:
    
    def __init__ (self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    
    def attack(self, robot):
        print('\nDinosaur\'s turn!\n')
        print(f'{robot.name}\'s health: {robot.health}')
        input(f'Press enter to have the dinosaur attack {robot.name}')
        robot.health -= self.attack_power
        print(f'{robot.name}\'s health is now {robot.health}')