from random import choice


# VARIABLES

# Selection categories and selection options per category
selections = {
    'Destination': ['Chicago', 'Milwaukee', 'St. Louis', 'Madison', 'Twin Cities'],
    'Restaurant': ['Pizza', 'Italian', 'Sushi', 'Seafood', 'Burgers'],
    'Mode of Transport': ['Car', 'Uber/Lyft', 'Public Transport', 'Walk'],
    'Entertainment': ['Sports Game', 'Live Performance', 'Tourist Site', 'Explore Downtown']
}


# Final selections which will be added then displayed at the end
final_selections = {
    'Destination': '',
    'Restaurant': '',
    'Mode of Transport': '',
    'Entertainment': ''
}


# FUNCTIONS

# Goes through selections and asks user to approve or reselect selection option
def approve_select():
   for key_values in selections.items():
    response = ''
    while response != 'a':
        option = choice(key_values[1])
        print(f'\nThe selected {key_values[0]} is {option}...')
        response = input('Enter \'a\' if you Approve the selection. Enter anything else if you want another selection: ')
        if response == 'a':
            final_selections[key_values[0]] = option


# Communicates instructions to player
def game_intro():
    print("\n\n### Day Trip Generator ###\n")
    print('You are planning a day trip and must make a few decisions...')
    print('There are 4 decisions that need to be made - The destination, restaurant, mode of transport, and entertainment...')
    print('First, we will show you a selection. Next, you will approve or disapprove the selection...')
    print('Once you approve a selection for all 4 decisions, we will display the completed trip in the terminal...\n\n')
    input(['PRESS ENTER TO START THE DAY TRIP GENERATOR'])


# Asks if player wants to play again
def play_again():
    if input('\nWould you like to play again? (y/n): ') == 'y':
        start()
    else:
        print("\nThanks for playing!\n")


# Starts the game
def start():
    game_intro()
    approve_select()
    print(final_selections)
    play_again()


start()