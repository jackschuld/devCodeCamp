class Robot:
    
    def __init__ (self, name, health, active_weapons):
        self.name = name
        self.health = health
        self.active_weapons = active_weapons
    
    # Displays enemies health and has user click enter to have the enemy attacked. Method works the same on dinosaur.py
    def attack(self, dinosaur):
        count = 1
        print('\nRobot\'s turn!\n')
        print(f'{dinosaur.name}\'s health: {dinosaur.health}')
        for weapon in self.active_weapons:
            print(str(count) + ') ' + weapon.name)
            count += 1
        selection = input(f'Enter the number of the attack you want {self.name} to use against {dinosaur.name}: ')
        # TODO base case if selection is not 1-3
        dinosaur.health -= self.active_weapons[int(selection) - 1].attack_power
        print(f'{dinosaur.name}\'s health is now {dinosaur.health}\n')