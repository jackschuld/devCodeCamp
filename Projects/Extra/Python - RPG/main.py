from random import randint
from character import Character

# VARIABLES
hercules = Character('Hercules', 20, {'1': 'Punch', '2': 'Poison Arrow', '3': 'Equip Nemean Lion Pelt', '4': 'Sword Attack'})

hydra = Character('Hydra', 12, {'1': 'Slash', '2': 'Poison Bite', '3': 'Regrow Head', '4': 'Fire Breath'})

players = [hercules, hydra]
turn = 0


# FUNCTIONS
def start_game():
    player_select()
    while hercules.health > 0 and hydra.health > 0:
        print(f'{players[turn].name.upper()}\'S TURN\n')
        if players[turn].comp == False:
            input('SELECT ANY KEY WHEN READY')
        select_attack(players[turn])


def player_select():
    print()
    for p in players:
        print(p.name)
    user = input('SELECT YOUR HERO - ENTER \'Hercules\' OR \'Hydra\': ')
    if user == 'Hercules':
        hercules.comp = False
    elif user == 'Hydra':
        hydra.comp = False
    else:
        print('MUST ENTER EITHER \'Hercules\' OR \'Hydra\'')
        player_select()


def select_attack(player):
    for item, value in player.attacks.items():
        print(item + ': ' + value)
    if player.comp == True:
        print('\nSELECT 1, 2, 3, OR 4 FROM THE OPTIONS ABOVE: ')
        selection = randint(1, 5)
        print(selection)
    else:
        selection = input('\nSELECT 1, 2, 3, OR 4 FROM THE OPTIONS ABOVE: ')
    if selection == '1':
        attack()
    elif selection == '2':
        attack()
    elif selection == '3':
        attack()
    elif selection == '4':
        attack()
    else:
        print('\nINPUT MUST BE ONE OF THE FOLLOW NUMBERS: 1, 2, 3, 4\n')
        select_attack(player)


# Applies affects from selected attack
def attack():
    if turn == 0:
        turn += 1
    else:
        turn = 0



# def ai_attack():
#     if selection == 'a':
#         attack(randint(20, 71))
#     elif selection == 'b':
#         attack(randint(5, 31), 0, True)
#     elif selection == 'c':
#         attack(0, 0, False, 3)
#     elif selection == 'd':
#         attack(randint(50, 61))


# def turn(player):
#         if selection == 'a':
#             attack(randint(20, 71))
#         elif selection == 'b':
#             attack(randint(5, 31), 0, True)
#         elif selection == 'c':
#             attack(0, 0, False, 3)
#         elif selection == 'd':
#             attack(randint(50, 61))

start_game()