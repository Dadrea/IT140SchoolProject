def player_menu():   # Player information and controls
    print('------------------------------------------------------------------------------------------------------\n')
    print('To move to another room type: Go North, Go South, Go East, or Go West')
    print("To add an item to your Inventory: Get 'Item Name'")
    print('To see the menu again type: Menu')
    print('To leave the game type: Exit')
    print('------------------------------------------------------------------------------------------------------\n')


def intro_spiel():   # Basic information about the game and end goal
    print('\n'
          'Welcome brave adventurer!\n'
          'You have made your way to the manor and seek to rid it of the Vampire Lord who now'
          ' taints its grounds.\n'
          'You will have to collect the six items from around the manor to defeat the Lord '
          'of the house.\n'
          'Do you have what it takes to defeat the Lord and save the town?\n'
          '------------------------------------------------------------------------------------------------------')


def moving_rooms(current_room, move, rooms):   # for moving rooms
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, rooms, inventory):   # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of rooms with items
    rooms = {
        'Main Foyer': {'name': 'Main Foyer', 'East': 'Graveyard', 'North': 'Great Hall'},
        'Great Hall': {'name': 'Great Hall', 'South': 'Main Foyer', 'West': 'Dining Room', 'East': 'Kitchen',
                       'North': 'Audience Chamber', 'item': 'Pocket Watch'},
        'Audience Chamber': {'name': 'Audience Chamber', 'South': 'Great Hall', 'East': 'Vampire Lords Private Chamber',
                             'item': 'Old Shield'},
        'Vampire Lords Private Chamber': {'name': 'Vampire Lords Private Chamber', 'west': 'Audience Chamber'},
        'Kitchen': {'name': 'Kitchen', 'West': 'Great Hall', 'North': "Servants' Quarters", 'item': 'Old Mutton'},
        "Servants' Quarters": {'name': "Servants' Quarters", 'South': 'Kitchen', 'item': 'Gold Key'},
        'Graveyard': {'name': 'Graveyard', 'West': 'Main Foyer', 'item': 'Holy Symbol'},
        'Dining Room': {'name': 'Dining Room', 'East': 'Great Hall', 'item': 'Wooden Stake'}
    }

    inventory = []   # list for storing player inventory

    current_room = "Main Foyer"   # starting room

    intro_spiel()   # displays the player introduction

    player_menu()   # displays the player menu

    while True:
        if current_room == 'Vampire Lords Private Chamber':
            #  prints when player wins the game
            if len(inventory) == 6:
                print('\nThe Door slams shut behind you!!!\n')
                print('You have found all of the necessary items!')
                print('Congratulations you have vanquished The Vampire Lord and saved the town!')
                print('Thank you for playing!')
                break
            # prints when the player loses the game
            else:
                print('\nThe Door slams shut behind you!!!\n')
                print('You have failed to find all of the necessary items!')
                print('Your soul has been taken by the Vampire Lord and the town is doomed!')
                print('Thank you for playing!')
                break
        # Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print(inventory)
        # tell the user if there is an item in the room
        if current_room != 'Vampire Lords Private Chamber' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------------------------------------------------------------------------------')
        move = input('Enter your move: ').title().split()
        # User enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = moving_rooms(current_room, move[1], rooms)
            continue
        # User enters a command to get an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, rooms, inventory)
            continue
        elif 'Exit' in move:   # exits the game
            print('Thank you for playing')
            break
        elif 'Menu' in move:   # brings up the player menu when called
            player_menu()
            continue
        else:   # Response if a wrong input is entered
            print('Invalid move, please try another direction')
            continue


main()
