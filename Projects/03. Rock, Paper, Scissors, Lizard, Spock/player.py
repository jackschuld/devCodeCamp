from random import choice


class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        # Made into dictionary, which has gesture as the key and the values are the gestures the key will beat
        self.gestures = {'Rock': ['Scissors', 'Lizard'], 'Paper': ['Spock', 'Rock'], 'Scissors': ['Paper', 'Lizard'], 'Lizard': ['Paper', 'Spock'], 'Spock': ['Rock', 'Scissors']}
        self.selection = ''
    

    def set_selection(self):
        selection = ''
        print(f'\n{self.name}\'s turn!')
        for gesture in self.gestures:
            print(f'- ' + gesture)
        print(f'\n{self.name} - Type out the option from above that you want to select: ')
        selection = choice([key for key in self.gestures.keys()])
        self.selection = selection
        input('\n[ Press Enter to Continue ]')
        print('\n')



    