import time
from random import randint
from human import Human
from ai import Ai


class Gui:

    def __init__(self):
        self.players = []


    # Goes through gui methods to run the game
    def run_game(self):
        self.welcome()
        self.instructions()
        self.create_player()
        self.vs_human_or_ai()
        self.play()
        self.game_over()


    # Displays welcome message
    def welcome(self):
        self.new_section()
        print('''                       Welcome to RPSLS!
                
                Rock, Paper, Scissors, Lizard, Spock!

            ''')


    # Seperates sections of the game in the terminal. Optionally, add a title to the section.
    def new_section(self, title='', pause_time=1):
        print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
        time.sleep(pause_time)
        print(title.upper())
        time.sleep(pause_time)
    

    # Instructions for the game
    def instructions(self):
        self.new_section('instructions', 2)
        print('''
Rules:
    - Two ways to play:
        1. against an ai
        2. against a friend
    - Take turns entering 'Rock', 'Paper', 'Scissors', 'Lizard', or 'Spock'.
    - If your selection wins against the opponent's, you earn a point.
    - Play to the best of 3 (ie. first to win 2 rounds wins the game).
    
Determine Winner:
    - Rock > Scissors
    - Scissors > Paper
    - Paper > Rock
    - Rock > Lizard
    - Paper > Spock
    - Scissors > Lizard
    - Lizard > Spock
    - Lizard > Paper
    - Spock > Scissors
    - Spock > Rock
        ''')
        input('[ Press Enter to Continue ]')
    

    # Returns a yes or no response from the user
    def yes_or_no(self, question):
        answer = ''
        while answer != 'Y' and answer != 'N':
            print(question)
            answer = input("Enter 'y' to approve or 'n' to not: ").upper()
        return answer


    # Goes through steps to create a Human
    def create_player(self):
        self.new_section('generate Human')
        self.enter_name()
    

    # Will create the Human class after the user successfully enters their name
    def enter_name(self):
        player_name = input('\nEnter your name: ')
        if self.yes_or_no(f'Your name is {player_name} - Is that correct? ') == 'N':
            player_name = self.enter_name()
        # Adding Human to the players list in the gui
        self.players += [Human(player_name)]


    # Select human or generate ai
    def vs_human_or_ai(self):
        self.new_section()
        if self.yes_or_no('Create another Human? ') == 'Y':
            self.create_player()
        else:
            self.gen_bot()

    
    # Generates bot name and adds to self.players
    def gen_bot(self):
        gen_bot_name = 'bot#' + str(randint(0, 1001)) 
        self.players += [Ai(gen_bot_name)]
    

    # Runs main part of game until there is a winner
    def play(self):
        self.new_section('start game')
        round_counter = 1
        while self.players[0].wins < 2 and self.players[1].wins < 2:
            self.new_section('Round ' + str(round_counter))
            self.get_selections()
            self.compare_selections()
            self.scoreboard()
            round_counter += 1
            
    
    def get_selections(self):
        self.players[0].set_selection()
        time.sleep(1)
        self.players[1].set_selection()
        print(f'{self.players[0].selection} vs {self.players[1].selection}')
        time.sleep(1)
    

    # Compares selections to give a player a point or detect a draw
    def compare_selections(self):

        # If same selections, then do not add any points
        if self.players[0].selection == self.players[1].selection:
            print('Draw!\nGo again\n')

        # If player 2's selection is in player 1's selection's value (ie. a list of winning options for the selection), then player 1 wins
        elif self.players[1].selection in self.players[0].gestures[self.players[0].selection]:
            print(f'{self.players[0].name} wins this round!')
            self.players[0].wins += 1

        # If not the same and not in player 1's selection's value list, then player 2 must be the winner
        else:
            print(f'{self.players[1].name} wins this round!')
            self.players[1].wins += 1
        


    def scoreboard(self):
        self.new_section('scoreboard')
        print('Points:')
        for player in self.players:
            print(f'{player.name} - {player.wins}')
        input('\n[ Press Enter to Continue ]')

    
    def game_over(self):
        self.new_section('winner')
        if self.players[0].wins > 1:
            print(f'Congrats {self.players[0].name}! You won RPSLS best of 3!\n')
        else:
            print(f'Congrats {self.players[1].name}! You won RPSLS best of 3!\n')
