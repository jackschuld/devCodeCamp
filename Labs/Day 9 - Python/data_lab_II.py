#(USE FOR TASK 1)from refactor_lab_II import destinations, restaurants, transportations, entertainments

### TASK 1: A List of Destination Dictionaries ###

# Rework your destinations list into individual dictionaries for each destination. 
# Since each destination offers unique restaurants, modes of transportation and entertainment, 
# we want the destination dictionaries to store their own lists for each.
# 1) Create one dictionary for each destination in the destinations list in data.py
def create_dict(location_string, restaurants_list, transportations_list, entertainments_list):
    return {
        'Location': location_string,
        'Restaurants': restaurants_list,
        'Transportations': transportations_list,
        'Entertainments': entertainments_list
    }

# Uncomment for TASK 1:
# chicago = create_dict(destinations[0], restaurants, transportations, entertainments)
# milwaukee = create_dict(destinations[1], restaurants, transportations, entertainments)
# cleveland = create_dict(destinations[2], restaurants, transportations, entertainments)


# 2) Each dictionary must have the following keys:
# Location (string)
# Restaurants (list)
# Transportations (list)
# Entertainments (list)

# print(chicago)
# print(milwaukee)
# print(cleveland)

# 3) Using your original lists for restaurants, transportations and entertainments, populate each dictionary’s list to be unique and add some new options.
chicago_restaurants = ['Lou Malnati\'s', 'Harry Caray\'s', 'Portillo\'s']
chicago_transportations = ['The L', 'Train']
chicago_entertainments = ['Go to a Game (Bulls/Blackhawks/Bears/Cubs/Sox)', 'Lollapalooza', 'The Second City']

milwaukee_restaurants = ['Points East Pub', 'Zocalo Food Park', 'Sobelman\'s', 'Guadalajara']
milwaukee_transportations = ['The Hop', 'Walk']
milwaukee_entertainments = ['Go to a Game (Bucks/Brewers)', 'Summer Fest', 'Brewery Tour']

cleveland_restaurants = ['Margaritaville', 'Saucy Brew Works', 'TownHall']
cleveland_transportations = ['Trolley', 'Walk']
cleveland_entertainments = ['Go to a Game (Browns/Guardians/Cavaliers)', 'Rock & Roll Hall of Fame', 'West Side Market']

# Uncomment for TASK 2:
destinations = ['Chicago', 'Milwaukee', 'Cleveland']
chicago = create_dict(destinations[0], chicago_restaurants, chicago_transportations, chicago_entertainments)
milwaukee = create_dict(destinations[1], milwaukee_restaurants, milwaukee_transportations, milwaukee_entertainments)
cleveland = create_dict(destinations[2], cleveland_restaurants, cleveland_transportations, cleveland_entertainments)

# print(chicago)
# print(milwaukee)
# print(cleveland)


### TASK 2: Refactor The Random Generator ###
# 1) Switch to your refactor.py file. 
# 2) Refamiliarize yourself and identify which functions will need to be refactored in order to randomly generate trip options from the newly organized data. (You may have to create new code/functions for this!)
# 3) Refactor your code to handle the new data format, without changing how the program runs in the terminal.
#       a. The random selections for restaurants, transportations & entertainments must come from the nested lists of the randomly selected destination dictionary.
# 4) Once your code has been refactored to utilize the data from data.py, remove the original four lists from refactor.py

def gen_destination(destination_key):
    if destination_key == destinations[0]:
        return chicago
    elif destination_key == destinations[1]:
        return milwaukee
    elif destination_key == destinations[2]:
        return cleveland
    


### TASK 3: New Data ##
# Management called and wants to include the climate with each destination.
# Add a climate field to each destination dictionary that describes its climate (temperate, tropical, etc)
# Refactor your code to include the climate alongside the destination name, wherever it’s printed in the terminal.
objects = [chicago, milwaukee, cleveland]
for object in objects:
    object['Climate'] = 'humid continental'



### TASK 4: Accessing Dictionary Values with Variables ###
# Create a new module for storing dictionary keys.
# Create a variable for each key of a destination dictionary
# Import the entire keys module into your refactored module (do not individually import each key variable from the module)
# Use the key variables from that module to access the values from the destination dictionaries instead of hard-coded strings.




### BONUS: Nested Data ###
# We must now offer hotel options for each destination!
# Add a list of hotel dictionaries to each destination dictionary (at least three hotels for each destination)
# A hotel dictionary must contain the following fields:
# Name
# Phone
# Location (dictionary with the following fields)
# Address
# City
# State
# Zip Code
# Update the refactored code to include a randomly selected hotel (only by name)
# Upon user confirmation of their trip, display the hotel address and phone number.
