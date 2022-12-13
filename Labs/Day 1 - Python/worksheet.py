# Task 1: Age
age = 26
print(f'I am {age} years old')

# Task 2: First Name
first_name = input('Enter your first name: ')

# Task 3: Last Name
last_name = input('Enter your last name: ')

# Task 4: Full Name
full_name = first_name + ' ' + last_name
print(f'My first name is {first_name} and my last name is {last_name}, which means my full name is {full_name}')

# Task 5: Temperature Converter
fahrenheit = input('Enter a temperature in Fahrenheit: ')
celsius = (int(fahrenheit) - 32) * 5/9
print(f'{fahrenheit} degrees Fahrenheit is {celsius} degress Celsius')

# Task 5a: Function
def f_to_c_converter(temp):
    temp = (int(temp) - 32) * 5/9
    return temp

celsius = f_to_c_converter(fahrenheit)
print(f'{fahrenheit} degrees Fahrenheit is {celsius} degress Celsius')
