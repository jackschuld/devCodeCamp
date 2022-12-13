# Task 1: String Manipulation

def first_last(string):
    return string[0] + string[-1]

print(first_last('Packers'))


# Task 2: Peanut Butter & Jelly

def zero_to_hundred():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print('peanut butter jelly')
        elif i % 3 == 0:
            print('peanut butter')
        elif i % 5 == 0:
            print('jelly')
        else:
            print(i)

zero_to_hundred()


# Task 3: Word-Letter Indexing

def char_with_index(string):
    final_result = ''
    for i in range(len(string)):
        final_result += string[i] + str(i)
    return final_result

print(char_with_index('World Peace'))


# Task 4: Ingredient Search

def ingredient_search(ingredients):
    ingredient_input = input('What ingredient do you want to search for? ')
    for i in ingredients:
        if i == ingredient_input:
            return i
    y_or_n = input("We could not find that... Would you want to search again? (y/n) ")
    if y_or_n == 'y':
        ingredient_search(ingredients)
    return 'Ingredient not found.'

ingredient_list = ['carrots', 'green onions', 'rice', 'general tso sauce', 'chicken']

print(ingredient_search(ingredient_list))


# Task 5: Reverse a List

def reverse_list(str_list):
    new_str_list = []
    for i in str_list:
        new_str_list.insert(0, i)
    return new_str_list

list_of_strings = ['Vucevic', 'Williams', 'Derozan', 'LaVine', 'Ball']

print(reverse_list(list_of_strings))


# Task 6: Drop Four

def drop_four(names):
    for i in names:
        if len(i) < 5:
            names.pop(names.index(i))
    return names

list_of_names = ['Jack', 'Parson', 'Mia']

print(drop_four(list_of_names))