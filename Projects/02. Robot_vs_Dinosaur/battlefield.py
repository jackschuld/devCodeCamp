import time
from random import randint

class Battlefield:
    
    def __init__ (self, robot, dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur
    

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        self.display_credits()
    

    # Displays an introduction screen on the terminal with keyboard art of a dinosaur vs a robot
    def display_welcome(self):
        time.sleep(1)
        print('############################################## ROBOT ##################################################\n')
        time.sleep(1)
        print('################################################ VS ###################################################\n')
        time.sleep(1)
        print('############################################# DINOSAUR ################################################')
        time.sleep(1)
        print('''                   
               ,  ;:._.-`''.                                                       ______
             ;.;'.;`       _ `.                                                  <((((((\\\\\\
              ',;`        ( \ ,`-.                                               /      . }\\
           `:.`,          (_/ ;\  `-.                                            ;--..--._|}
            ';:               / `.   `-._                     (\                 '--/\--'  )
          `;.;'               `-,/ .     `-.                   \\\                | '-'  :'|
          ';;'               _    `^`       `.                  \\\               . -==- .-|
         ';;             ,'-' `--._          ;                   \\\               \.__.'   \--._
':      `;;        ,;     `.    ':`,,.__,,_ /                    [\\\          __.--|       //  _/'--.
 `;`:;;:`         ,; '.    ;,      ';';':';;`                    \ \\\       .'-._ ('-----'/ __/      \\
              .,; '    '-._ `':.;                                 \ \\\     /   __>|      | '--.       |
            .:; `          '._ `';;,         \\\      //  //===     \ \\\   |   \   |     /    /       /
          ;:` `    :'`'       ',__.)          \\\    //   \\\         \ '\ /     \  |     |  _/       /
        `;:;:.,...;'`'                         \\\  //      \\\        \  \       \ |     | /        /
      ';. '`'::'`''  .'`'                       \\\//    ===//         \  \      \       /
    ,'   `';;:,..::;`'`'                 
, .;`      `'::''`                  
       
        DINOSAUR                                                                   ROBOT
''')
        time.sleep(1)
        print('########################################################################################################')
        time.sleep(1)



    # Will switch between the dinosaur and robot to take turns
    def battle_phase(self):
        # Randomly assign who goes first
        turn = randint(1, 2)
        # While both are alive
        while self.robot.health > 0 and self.dinosaur.health > 0:
            time.sleep(1)
            # Dinosaur goes on even numbers, Robot on odds
            if turn % 2 == 0:
                self.dinosaur.attack(self.robot)
            else:
                self.robot.attack(self.dinosaur)
            turn += 1


    def display_winner(self):
        time.sleep(1)
        if self.dinosaur.health > 0:
            print(f'{self.dinosaur.name}, the dinosaur, is the winner with {self.dinosaur.health} remaining health!\n\n')
        elif self.robot.health > 0:
            print(f'{self.robot.name}, the robot, is the winner with {self.robot.health} remaining health!\n\n')
        else:
            print('No survivors!')
        time.sleep(1)
    

    def display_credits(self):
        print('[GAME OVER]\n')
        time.sleep(1)
        print('########################################################################################################')
        print('https://www.asciiart.eu/animals/reptiles/dinosaurs - art by Joan Stark')
        print('https://ascii.co.uk/art/terminator - artist unknown')

