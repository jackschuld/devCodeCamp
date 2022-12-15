from player import Player
from attacks import Attacks


def start_game():
    input('# # # HERCULES VS HYDRA # # #')
    characters = ['Hercules', 'Hydra']
    player = instantiate(display_options(characters), characters, False)
    enemy = instantiate(display_options(characters), characters)
    player.assign_enemy(enemy)
    enemy = player.enemy
    enemy.assign_enemy(player)
    player.select_attack()

    
def display_options(options):
    i = 1
    print('Select from the options below:')
    for option in options:
        print(f'{i}) {option}')
        i += 1
    return select_option(len(options))


def select_option(num_of_options):
    selection = ''
    num_of_options = [str(i) for i in range(1, num_of_options+1)]
    while selection not in num_of_options:
        selection = input('Enter the number coorelated to your selection above: ')
    return int(selection)

    
def instantiate(selection_num, characters, is_ai=True):
    player = Player(characters.pop(selection_num-1), is_ai)
    return player

start_game()