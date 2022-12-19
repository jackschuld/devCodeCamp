import time
from random import randint
from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon


class Battlefield:
    
    def __init__ (self, robot, dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur
    

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        time.sleep(1)
        print('############################################## ROBOT ################################################\n')
        time.sleep(1)
        print('################################################ VS #################################################\n')
        time.sleep(1)
        print('############################################# DINOSAUR ##############################################')
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

########################################################################################################
''')
        time.sleep(1)




    def battle_phase(self):
        turn = 0
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if turn % 2 == 0:
                self.dinosaur.attack(self.robot)
            else:
                self.robot.attack(self.dinosaur)
            turn += 1


    def display_winner(self):
        if self.dinosaur.health > 0:
            print(f'{self.dinosaur.name}, the dinosaur, is the winner with {self.dinosaur.health} remaining!')
        else:
            print(f'{self.robot.name}, the robot, is the winner with {self.robot.health} remaining!')




# Instance game
game1 = Battlefield(Robot('Arnold', randint(80, 121), Weapon('Sawed-off Shotgun', randint(10, 41))), Dinosaur('Sue', randint(90, 131), randint(5, 31)))

# Run game instance
game1.run_game()
