class Robot:
    
    def __init__ (self, name, health, active_weapons):
        self.name = name
        self.health = health
        self.active_weapons = active_weapons
    
    # Displays enemies health and has user click enter to have the enemy attacked. Method works the same on dinosaur.py
    def attack(self, dinosaur):
        print('\nRobot\'s turn!\n')
        print(f'{dinosaur.name}\'s health: {dinosaur.health}')
        selection = self.select(dinosaur)
        dinosaur.health -= self.active_weapons[int(selection) - 1].attack_power
        print(f'{dinosaur.name}\'s health is now {dinosaur.health}\n')
    

    def select(self, dinosaur):
        selection = '0'
        while int(selection) < 1 or int(selection) > len(self.active_weapons):
            count = 1
            for weapon in self.active_weapons:
                print(str(count) + ') ' + weapon.name)
                count += 1
            selection = input(f'Enter the number of the attack you want {self.name} to use against {dinosaur.name}: ')
        return selection