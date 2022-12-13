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
print(is_happy_number(4))
print(is_happy_number(13))
