import random

# TASK 1: Screenshot Favorite Number

favorite_number = 4


# TASK 2: Generate a Random Number

def distance_from_randnum_to_num(num):
    randnum = random.randint(0, 10)
    return abs(num - randnum)

task2 = distance_from_randnum_to_num(favorite_number)

# print(task2)


# TASK 3: Repeat Code with Loop

def comp_rand_guess_num(num):
    randnum = None
    guesses = 0
    while randnum != num:
        randnum = random.randint(0, 10)
        guesses += 1
    return f"It took the computer {guesses} random guesses to guess the number\n" if guesses > 1 else f"It took the computer 1 random guess to guess the number"

task3 = comp_rand_guess_num(favorite_number)

# print(task3)


# TASK 4: 