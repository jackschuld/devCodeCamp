# importing random to use randrange
import random


# Task 1: Driving Age
legal_driving_age = 16
age = input("Enter your age: ")

if int(age) >= legal_driving_age:
    print('You are legally able to drive')
else:
    print('You are not old enough to drive yet')


# Task 2: Random Number
ran_num = random.randrange(11)
print(ran_num)
if ran_num <= 2:
    print('0 or 1 or 2')
elif ran_num <= 5:
    print('3 or 4 or 5')
elif ran_num <= 8:
    print('6 or 7 or 8')
else:
    print('9 or 10')


# Task 3: NFL Teams
nfl_fav = input('Enter your favorite NFL team: ')
if nfl_fav == 'Bears':
    print('Da Bears!')
elif nfl_fav == 'Vikings':
    print('SKOL')
elif nfl_fav == 'Packers':
    print('Cheesepackers')
elif nfl_fav == 'Lions':
    print('Sorry...')
else:
    print('Nice!')
