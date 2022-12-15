from refactor_lab_II import destinations, restaurants, transportations, entertainments

### TASK 1: A List of Destination Dictionaries ###

# Rework your destinations list into individual dictionaries for each destination. 
# Since each destination offers unique restaurants, modes of transportation and entertainment, 
# we want the destination dictionaries to store their own lists for each.
# 1) Create one dictionary for each destination in the destinations list in data.py
def create_dict(location_string, restaurants_list, transportations_list, entertainments_list):
    return {
        'Location': location_string,
        'Restaurants': restaurants_list,
        'Transportation': transportations_list,
        'Entertainment': entertainments_list
    }


chicago = create_dict(destinations[0], restaurants, transportations, entertainments)
milwaukee = create_dict(destinations[1], restaurants, transportations, entertainments)
cleveland = create_dict(destinations[2], restaurants, transportations, entertainments)


# 2) Each dictionary must have the following keys:
# Location (string)
# Restaurants (list)
# Transportations (list)
# Entertainments (list)
print(chicago)
print(milwaukee)
print(cleveland)

# 3) Using your original lists for restaurants, transportations and entertainments, populate each dictionary’s list to be unique and add some new options.
chicago_restaurants = ['Lou Malnati\'s', 'Harry Caray\'s', 'Portillo\'s']
chicago_transportations = ['The L', 'Train']
chicago_entertainments = ['Bulls/Blackhawks/Bears/Cubs/Sox Game', 'Lollapalooza', 'The Second City']

milwaukee_restaurants = ['Points East Pub', 'Zocalo Food Park', 'Sobelman\'s', 'Guadalajara']
milwaukee_transportations = ['The Hop', 'Walk']
milwaukee_entertainments = ['Bucks/Brewers Game', 'Summer Fest', 'Brewery Tour']

cleveland_restaurants = ['Margaritaville', 'Saucy Brew Works', 'TownHall']
cleveland_transportations = ['Trolley', 'Walk']
cleveland_entertainments = ['Rock & Roll Hall of Fame', 'Browns/Guardians/Cavaliers Game', 'West Side Market']

chicago = create_dict(destinations[0], chicago_restaurants + restaurants, chicago_transportations + transportations, chicago_entertainments + entertainments)
milwaukee = create_dict(destinations[1], milwaukee_restaurants + restaurants, milwaukee_transportations + transportations, milwaukee_entertainments + entertainments)
cleveland = create_dict(destinations[2], cleveland_restaurants + restaurants, cleveland_transportations + transportations, cleveland_entertainments + entertainments)

print(chicago)
print(milwaukee)
print(cleveland)