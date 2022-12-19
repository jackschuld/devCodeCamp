# TASK 1: Happy Numbers

def is_happy_number(num):
    comp = 0
    # Convert num to a list
    num_to_list = [int(i) for i in str(num)]
    # Traverse list, squaring each digit
    for i in range(len(num_to_list) - 1):
        num_to_list[i] = num_to_list[i] ** 2
        # Then, we add the squared digit to comp
        comp += num_to_list[i]
    if num == comp:
        return False
    elif comp == 1:
        return True
    # If the comp isn't equal to num or to 1, then run again using the comp as the num
    return is_happy_number(comp)


# Task 1 prints
# print(is_happy_number(4))
# print(is_happy_number(13))



# TASK 2: Prime Numbers

def prime_printer_range(start, end):
    # The outer loop creates a list of numbers to loop through
    for num in range(start, end+1):
        # The inner loop checks if num is divisible by any other number than 1 and itself
        for i in range(2, num+1):
            if num == i:
                print(num)
            elif num % i == 0:
                break
        
            
# Task 2 print
# prime_printer_range(1, 100)



# TASK 3: Fibonacci

# Enter number to start from and how many iterations
def fibonacci(start, count):
        prev = 0
        curr = start
        if start == 0:
            start = 1
        while count != 0:
            print(curr)
            start += prev
            prev = curr
            curr = start
            count -= 1


# Task 3 print
# fibonacci(0, 8)
# fibonacci(10, 6)
