from random import choice

# Intro to game with instructions
def intro():
    print("\n\n### Day Trip Generator ###\n")
    print("\nYou will be asked to enter the categories you need help choicing from and then enter the options you are stuck between...\n")
    print("After, we will pick out of your options and give you the choice to accept or deny our selection...\n")
    input(['PRESS ENTER TO START THE DAY TRIP GENERATOR'])


# Assigns a string and a list of strings to be each key: [values] pair in the selections dictionary
def create_selections_dict(dict):
    cont = ''
    while cont != 'n':
        key = input('Enter a selection category (for instance, \'Destination\' or \'Food\'): ').title()
        values = create_options_list()
        dict[key] = values
        cont = continue_y_or_n('selection category')
    return dict


# Returns the [values] list for the key: [values] pairing
def create_options_list():
    lst = []
    cont = ''
    while cont != 'n':
        lst.append(input('Enter an option for this selection category: '))
        cont = continue_y_or_n('option')
    return lst


# Loops through created dictionary and chooses a random value from each key's value list
def select(dict):
    for key_values in dict.items():
        cont = ''
        while cont != 'y':
            option = choice(key_values[1])
            print(f'\nThe selected {key_values[0]} is {option}...')
            cont = continue_y_or_n(option, False)
            if cont == 'y':
                dict[key_values[0]] = option
            # Checks if length of values list is greater than 1, so we do not accidentally remove all value options
            elif len(key_values[1]) > 1:
                remove_option(option, key_values)
    return dict


# For 'y' or 'n' questions
def continue_y_or_n(selection, add=True, remove=False):
    # If user is adding to the dictionary
    if add:
        return input(f'Do you want to add another {selection} to this category? (y/n): ')
    # If user is removing from the dictionary
    elif remove:
        return input(f'Remove {selection} from choices? (y/n): ')
    # If user is selecting final value per category key in the dictionary
    else:
        return input(f'Do you approve {selection} to be the selection for this category? (y/n): ')


# Removes option from values list if user no longer wants to see it
def remove_option(option, values_list):
    remove = continue_y_or_n(option, False, True)
    if remove == 'y':
        index = values_list[1].index(option)
        dict[values_list[0]].pop(index)


# Asks if player wants to play again
def play_again():
    if input('\nWould you like to play again? (y/n): ') == 'y':
        start()
    else:
        print("\nThanks for playing!\n")


# Starts and runs the functions for the game
def start():
    intro()
    selections = {}
    # Create dictionary with key: [values]
    selections = create_selections_dict(selections)
    # User selects value per key returning key: value pairs
    selections = select(selections)
    print(f'Here is the final selections made for your trip:\n {selections}')
    play_again()


start()