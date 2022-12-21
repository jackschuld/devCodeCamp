from random import choice


def gen_lists():
    destinations = ['Chicago', 'Milwaukee', 'St. Louis', 'Madison', 'Twin Cities']
    restaurants = ['Pizza', 'Italian', 'Sushi', 'Seafood', 'Burgers']
    transportations = ['Car', 'Uber/Lyft', 'Public Transport', 'Walk']
    entertainments = ['Sports Game', 'Live Performance', 'Tourist Site', 'Explore Downtown']
    destination = choice(destinations)
    restaurant = choice(restaurants)
    tranportation = choice(transportations)
    entertainment = choice(entertainments)

    return f'''
    Destination: {destination}
    Restaurant: {restaurant}
    Transportation: {tranportation}
    Entertainment: {entertainment}
    '''


def select():
    response = ''
    while response != 'y':
        trip = gen_lists()
        print(trip)
        response = input('Do you accept the generated trip? (y/n): ')
    return trip


def play_again():
    if input('\nWould you like to play again? (y/n): ') == 'y':
        start()
    else:
        print("\nThanks for playing!\n")


def intro():
    print("\n\n### Day Trip Generator ###\n")
    print('There are 4 decisions that need to be made - The destination, restaurant, mode of transport, and entertainment...')
    print('First, we will show you a selection. Next, you will approve or disapprove the selection...')
    print('Once you approve a selection for all 4 decisions, we will display the completed trip in the terminal...\n\n')
    input(['PRESS ENTER TO START THE DAY TRIP GENERATOR'])


def start():
    intro()
    select()
    play_again()


start()