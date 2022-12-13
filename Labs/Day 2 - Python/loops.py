# Task 1: Five Hellos
for i in range(5):
    print('Hello')

# Task 2: Counting
for i in range(11):
    print(i)

# Task 3: Counting Backwards
for i in range(10, -1, -1):
    print(i)

# Task 4: Prompted Output
for n in range(int(input("Enter number of times \'devCodeCamp\' will print: "))):
    print('devCodeCamp')

# Task 5: Packers Split-Up
for c in 'Packers':
    print(c)

# Task 6: CHALLENGE - Fizz Buzz
for n in range(101):
    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)

# Task 7: Five Hellos (again):
count = 0
while count < 5:
    print('Hello')
    count += 1

# Task 8: Validation:
password = 'password123!'
correct_input = False
while correct_input == 0:
    if input('Enter password: ') == password:
        correct_input = True
        print('User Validated')