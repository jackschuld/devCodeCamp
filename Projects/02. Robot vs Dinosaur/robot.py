class Robot:
    
    def __init__ (self, name, health, active_weapons, about=None):
        self.name = name
        self.health = health
        self.active_weapons = active_weapons
        self.about = about
    
    # Method works the same on dinosaur.py
    def attack(self, dinosaur):
        print(f'\n{self.name}\'s turn!\n')
        # Displays enemies health
        print(f'TARGET:\n{dinosaur.name}\'s health: {dinosaur.health}\n')
        print('ATTACKS:')
        # Assign weapon selection from the select method
        selection = self.select(dinosaur)
        # Apply selection to enemy's health
        dinosaur.health -= self.active_weapons[int(selection)-1].attack_power
        self.health += self.active_weapons[int(selection)-1].affect_to_self
        print(f'\n{dinosaur.name}\'s health is now {dinosaur.health}\n')
    

    def select(self, dinosaur):
        selection = 0
        # Will loop until the player enters a valid selection (1-3)
        while selection < 1 or selection > len(self.active_weapons):
            count = 1
            for weapon in self.active_weapons:
                print(str(count) + ') ' + weapon.name)
                count += 1
            selection = input(f'Enter the number of the attack above you want {self.name} to use against {dinosaur.name}: ')
            try:
                selection = int(selection)
            except ValueError:
                selection = 0
                print(f'Enter a number 1-{len(self.active_weapons)}\n')
        return selection