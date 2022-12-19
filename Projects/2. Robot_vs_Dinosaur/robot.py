class Robot:
    
    def __init__ (self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = active_weapon
    
    # Displays enemies health and has user click enter to have the enemy attacked. Method works the same on dinosaur.py
    def attack(self, dinosaur):
        print('\nRobot\'s turn!\n')
        print(f'{dinosaur.name}\'s health: {dinosaur.health}')
        input(f'Press enter to have the robot attack {dinosaur.name}')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name}\'s health is now {dinosaur.health}\n')