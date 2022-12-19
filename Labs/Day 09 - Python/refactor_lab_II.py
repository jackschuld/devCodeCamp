from random import choice
from data_lab_II import gen_destination

destinations = ['Chicago', 'Milwaukee', 'Cleveland']
# TASK 1: restaurants = ['Pizza', 'Italian', 'Sushi', 'Seafood', 'Burgers']
# TASK 1: transportations = ['Car', 'Uber/Lyft']
# TASK 1: entertainments = ['Tourist Site', 'Explore Downtown', 'Bars/Clubs']

def gen_lists():
    destination = gen_object(choice(destinations))
    restaurant = choice(destination['Restaurants'])
    tranportation = choice(destination['Transportations'])
    entertainment = choice(destination['Entertainments'])
    destination = destination['Location'] + ' - ' + destination['Climate']


    return f'''
    GENERATED TRIP:
        Destination: {destination}
        Restaurant: {restaurant}
        Transportation: {tranportation}
        Entertainment: {entertainment}
    '''


def select():
    response = ''
    while response.upper() != 'Y':
        print()
        trip = gen_lists()
        print('----------------------------------------------')
        print(trip)
        response = input('Do you accept the generated trip? (y/n): ')
    return f'\n\n\n\n\nYour final generated trip is...\n{trip}\n\n'


def gen_object(selected_destination):
    for destination in destinations:
        if destination == selected_destination:
            return gen_destination(destination)
    


def play_again():
    if input('\n\n\nWould you like to play again? (y/n): ').upper() == 'Y':
        start()
    else:
        print("\n\n\n\n\n\nThanks for playing!!!\n\n\n##### TRIP GENERATOR #####\n\n\n")


def intro():
    print("\n\n### Day Trip Generator ###\n")
    print('There are 4 decisions that need to be made - The destination, restaurant, mode of transport, and entertainment...')
    print('First, we will show you a selection for the destination. Next, you will approve or disapprove the selection...')
    print('After approving the destination, we will display a restaurant, mode of transport, and entertainment for you to approve...')
    print('Once all is approved, we will display the completed trip in the terminal...\n\n')
    input(['PRESS ENTER TO START THE DAY TRIP GENERATOR'])


def start():
    intro()
    print(select())
    play_again()


start()
