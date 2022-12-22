from player import Player


class Human(Player):

    def __init__(self, name):
        super().__init__(name)
    

    def set_selection(self):
        selection = ''
        while selection not in self.gestures:
            print(f'\n{self.name}\'s turn!')
            for gesture in self.gestures:
                print(f'- ' + gesture)
            selection = input(f'\n{self.name} - Type out the option from above that you want to select: ').title()
        self.selection = selection
        input('\n[ Press Enter to Continue ]')
        print('\n')