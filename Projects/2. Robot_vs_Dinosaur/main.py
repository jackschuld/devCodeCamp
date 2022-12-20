from battlefield import Battlefield
from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
from random import randint


# Instance game
game1 = Battlefield(Robot('Arnold', randint(80, 126), [Weapon('Punch', randint(16, 26)), Weapon('Sawed-off Shotgun', randint(10, 36)), Weapon('Grenade', randint(5, 46))]), Dinosaur('Sue', randint(90, 131), randint(15, 31)))

# Run game instance
game1.run_game()