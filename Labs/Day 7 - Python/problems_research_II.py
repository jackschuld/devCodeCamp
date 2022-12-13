# Task 1: Reverse a String
# Write code that takes a string as input and returns the string reversed
# i.e. “Hello” will be returned as “olleH”

def reverse_string(string):
    new_string = ''
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    return new_string

# Task 1 print
# print(reverse_string('Jack'))



# Task 2: Capitalize a Letter

# Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

def capitalize_strings(string):
    return string.title()

# Task 2 print
#  print(capitalize_strings("hello world, i am jack."))


# Task 3: Palindrome
# A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
# Write code that takes a user input and checks to see if it is a Palindrome and reports the result

def is_palindrome(string):
    string_reversed = reverse_string(string)
    print(f'Original => {string}')
    print(f'Reversed => {string_reversed}') 
    print(f'Checking if {string} is a Palindrome...')
    if string_reversed == string:
        return True
    return False


# Task 3 print
# print(is_palindrome('car'))
# print(is_palindrome('madam'))


# Bonus Challenge
# Task 4 : Compress a string of characters
# For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

def compress_chars(string):
    index = 0
    compressed = ''
    while index != len(string):
        count = 1
        while index < len(string) - 1 and string[index] == string[index + 1]:
            # Add 1 to index so we can skip through repeats of letter on outer while loop
                index += 1
            # Add 1 to count to add up the amount of the same character
                count += 1
    # Add count and single letter to compressed string
        compressed += str(count) + str(string[index])
        index += 1
    return compressed

# Task 4 print
# print(compress_chars('aaabbc'))
# print(compress_chars('jjjsssssiieeeeeeeeehffjjjj'))

        