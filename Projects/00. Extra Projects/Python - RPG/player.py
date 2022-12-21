from random import randint


class Player:
    def __init__(self, name, is_ai=True):
        self.name = name
        self.is_ai = is_ai
        self.enemy = None
        self.health = 100
        self.attacks = None


    def assign_enemy(self, enemy):
        self.enemy = enemy
    

    def assign_attacks(self):
        if self.name == 'Hercules':
            self.attacks = '''Select from the options below:
                        1. Sword Stike - swing sword at enemy
                        2. Wrestle - pin enemy to ground if enemy is weak enough
                        3. Lion's Pelt - take almost up to 50%% off future hits by enemy'''
        elif self.name == 'Hydra':
            self.attacks = '''Select from the options below:
                        1. Poison Bite - bite and poison enemy
                        2. Breath Fire - breathe fire at enemy
                        3. Regenerate Head - regain 30 health if health is less than 70'''


    def select_attack(self):
        print(f'{self.name}\'s turn!')
        print(self.attacks)
        if self.is_ai:
            attack_num = randint(1, 4)
            print(f'Select your attack here: {attack_num}')
        else:
            attack_num = input('Select your attack here: ')
        return attack_num
        

    def attack(selected_attack_num):
        pass