import time
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
            print(f'{self.dinosaur.name}, the dinosaur, is the winner!')
        else:
            print(f'{self.robot.name}, the robot, is the winner!')





# Instance game
game1 = Battlefield(Robot('Arnold', 100, Weapon('Sawed-off Shotgun', 20)), Dinosaur('Sue', 100, 20))

# Run game instance
game1.run_game()
