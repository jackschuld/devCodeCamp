class Dinosaur:
    
    def __init__ (self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    
    def attack(self, robot):
        input(f'Press enter to attack {robot.name}, the robot')
        robot.health -= self.attack