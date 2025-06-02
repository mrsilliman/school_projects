# Mary Silliman
# FORAGE FINDS - TEXT GAME

# dictionary linking a room to other rooms
# dictionary linking an item to a specific room
rooms = {
    'Hive': {'East': 'Pond', 'item': 'None'},       # start
    'Pond': {'North': 'Helianthus', 'South': 'Lupine', 'East': 'Rock', 'West': 'Hive', 'item': 'Water'},
    'Helianthus': {'East': 'Tree', 'South': 'Pond', 'item': 'Pollen'},
    'Tree': {'West': 'Helianthus', 'item': 'Propolis'},
    'Rock': {'West': 'Pond', 'North': 'Solidago', 'item': 'Dancing shoes'},
    'Solidago': {'South': 'Rock', 'item': 'Dr. Arach'},     # villain
    'Lupine': {'North': 'Pond', 'East': 'Fireweed', 'item': 'Nectar'},
    'Fireweed': {'West': 'Lupine', 'item': 'Striped jacket'}
}

# initialize item inventory
inventory = []

# calls game instructions and movement between rooms
def main():
    show_instructions()
    move_locations()

# instructions for the game
def show_instructions():
   print(f'*** Forage Finds Adventure Game ***\n')
   print(f'Collect 6 items to win the game, or be eaten by the evil spider, Dr. Arach.')
   print(f'Move commands: North, South, East, West')
   print(f'Add to Inventory: get \'item name\'\n')

# move between connected rooms
# call item retrieval
def move_locations():
    # set start location as hive
    location = 'Hive'
    print(f'You are starting at the {location}')
    print(f'Inventory: {inventory}')
    print(f'-' * 20)

    # prompt user to move between rooms (N, S, E, W)
    direction = input('Enter direction to move between locations (North, South, East, West): ')

    # loop until all six items are collected
    while len(inventory) < 7:
        if location in rooms and direction in rooms[location]:
            location = rooms[location][direction]       # set new location
            print(f'You are at the {location}\n')       # print new location
            retrieve_items(location)
        else:
            print(f'Invalid direction. Try again\n')    # invalid entry if entry doesn't match dictionary

        direction = input('Enter direction to move between locations (North, South, East, West): ')

# retrieve items in each room and store them in the inventory
def retrieve_items(location):
    item = rooms[location]['item']

    if item == 'Dr. Arach' and (len(inventory) < 6):        # encountering the villain before all items are collected
        print(f'NOM NOM! Dr. Arach attacks! GAME OVER! You lose!')      # notify player of loss and exit the game
        exit()
    elif item in inventory:                                 # cannot collect the same items more than once
        print(f'Item has already been retrieved!\n')
    elif item == 'None':
        print(f'There are no items here to collect\n')      # no items are found at the start position (Hive)
    else:
        print(f'Inventory: {inventory}')
        print(f'You see {item}')

        print(f'-' * 20)
        invalid_item_selection = True           # account for incorrect entries
        while invalid_item_selection:           # item selection by player must contain item name
            decision = input('Enter your move (get \'item name\'):\n')
            if item in decision:                # a correct item selection get appended to the inventory
                print(f'{item} retrieved!\n')
                inventory.append(item)
                invalid_item_selection = False
                if len(inventory) == 6:         # all items are collected, notify player of win and exit the game
                    print(f'Congrats! YOU WIN! You have collected all the items and avoided Dr. Arach!')
                    exit()
            else:
                print(f'Invalid answer!\n')

if __name__=="__main__":
    main()