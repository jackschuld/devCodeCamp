class Robot:
    
    def __init__ (self, name, health, active_weapons):
        self.name = name
        self.health = health
        self.active_weapons = active_weapons
    
    # Method works the same on dinosaur.py
    def attack(self, dinosaur):
        print('\nRobot\'s turn!\n')
        # Displays enemies health
        print(f'{dinosaur.name}\'s health: {dinosaur.health}')
        # Assign weapon selection from the select method
        selection = self.select(dinosaur)
        # Apply selection to enemy's health
        dinosaur.health -= self.active_weapons[int(selection) - 1].attack_power
        print(f'{dinosaur.name}\'s health is now {dinosaur.health}\n')
    

    def select(self, dinosaur):
        selection = '0'
        # Will loop until the player enters a valid selection (1-3)
        while int(selection) < 1 or int(selection) > len(self.active_weapons):
            count = 1
            for weapon in self.active_weapons:
                print(str(count) + ') ' + weapon.name)
                count += 1
            selection = input(f'Enter the number of the attack you want {self.name} to use against {dinosaur.name}: ')
        return selection