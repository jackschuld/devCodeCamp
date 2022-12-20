from random import randint
from battlefield import Battlefield
from battlefield_3s import Battlefield_3s
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from weapon import Weapon


# Instance players

# Robots
arnold = Robot('Arnold', randint(110, 136), [Weapon('Punch', randint(20, 36)), Weapon('Sawed-off Shotgun', randint(15, 41)), Weapon('Grenade', randint(5, 46))])
r2_d2 = Robot('R2-D2', randint(60, 101), [Weapon('Tazer', randint(15, 31)), Weapon('Flamethrower', randint(25, 41)), Weapon('Round Saw', randint(10, 26))], "It is estimated this droid has an impressively large kill count of 1,000,253 ~ https://may4bewithyou.com/how-many-kills-does-r2d2-have/")
bender = Robot('Bender', randint(90, 121), [Weapon('Bend', randint(20, 36)), Weapon('Flame Burp', randint(25, 41)), Weapon('Self-Destruct', randint(75, 91), -150)])
robots = Fleet([arnold, r2_d2, bender])

# Dinosaurs
sue = Dinosaur('Sue', randint(90, 131), randint(15, 31))
godzilla = Dinosaur('Godzilla', randint(110, 201), randint(20, 51))
barney = Dinosaur('Barney', randint(50, 101), randint(0, 21))
dinosaurs = Herd([sue, godzilla, barney])


# Instance games
game1 = Battlefield(arnold, sue)
game2 = Battlefield_3s(robots, dinosaurs)


# Run game instance
game1.run_game()
game2.run_game()