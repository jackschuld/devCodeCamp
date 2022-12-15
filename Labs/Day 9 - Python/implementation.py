import math

# Task 1: Dictionary, Set and Tuple

# 1
# Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists and print that month to the console. 
# HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.

tuple_months = ('Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
pi_as_index = round(math.pi)
print(tuple_months[pi_as_index])



# 2
# Store five fruits or vegetables.
# Add two of your favorite fruits and two of your favorite vegetables to the collection.
# Iterate over the collection and print each one to the console. 

set_fruits_n_veggies = {'apples', 'lettuce', 'grapefruit', 'carrots', 'pomegranates'}
count = 2
while count > 0:
    set_fruits_n_veggies.add(input('Enter a favorite fruit: '))
    set_fruits_n_veggies.add(input('Enter a favorite vegetable: '))
    count -= 1
for item in set_fruits_n_veggies:
    print(item)



# 3
# Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. The profile should consist of the following information:
# First Name
# Last Name
# Email Address
# Phone Number

dict_user_profile = {
    'First Name': 'Amy',
    'Last Name': 'Wong',
    'Email Address': 'awong@marslink.web',
    'Phone Number': '800-AMY-WONG'
}

for key in dict_user_profile:
    print(f'{key}: {dict_user_profile[key]}')