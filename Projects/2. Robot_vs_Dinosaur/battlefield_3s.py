import time
from random import randint

class Battlefield_3s:
    
    def __init__ (self, robots, dinosaurs):
        self.robots = robots
        self.dinosaurs = dinosaurs
    

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        self.display_credits()
    

    # Displays an introduction screen on the terminal with keyboard art of a dinosaur vs a robot
    def display_welcome(self):
        time.sleep(1)
        print('############################################## ROBOTS #################################################\n')
        time.sleep(1)
        print('################################################ VS ###################################################\n')
        time.sleep(1)
        print('############################################# DINOSAURS ###############################################')
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
        print('########################################################################################################')



    # Will switch between the dinosaurs and robots to take turns
    def battle_phase(self):
        # Randomly assign who goes first
        turn = randint(0, 1)
        fleet = self.robots.fleet
        herd = self.dinosaurs.herd

        while len(fleet) > 0 and len(herd) > 0:
            time.sleep(1)
            # Dinosaur goes on even numbers, Robot on odds
            turn_index_fleet = turn % len(fleet)
            turn_index_herd = turn % len(herd)
            if turn % 2 == 0:
                herd[turn_index_herd].attack(fleet[turn_index_fleet])
                if fleet[turn_index_fleet].health < 1:
                    print(f'KO - {fleet[turn_index_fleet].name}')
                    fleet.pop(turn_index_fleet)
            else:
                fleet[turn_index_fleet].attack(herd[turn_index_herd])
                if herd[turn_index_herd].health < 1:
                    print(f'KO - {herd[turn_index_herd].name}')
                    herd.pop(turn_index_herd)
                if fleet[turn_index_fleet].health < 1:
                    print(f'KO - {fleet[turn_index_fleet].name}')
                    fleet.pop(turn_index_fleet)
            turn += 1
            print('########################################################################################################')


    def display_winner(self):
        time.sleep(1)
        if len(self.dinosaurs.herd) > 0:
            print(f'The dinosaurs are the winner with {len(self.dinosaurs.herd)} remaining!\n\n')
        elif len(self.robots.fleet) > 0:
            print(f'The robots are the winner with {len(self.robots.fleet)} remaining!\n\n')
        time.sleep(1)


    def display_credits(self):
        print('[GAME OVER]\n')
        time.sleep(1)
        print('########################################################################################################')
        print('https://www.asciiart.eu/animals/reptiles/dinosaurs - art by Joan Stark')
        print('https://ascii.co.uk/art/terminator - artist unknown')

