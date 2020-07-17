from room import Room
from player import Player
from item import Item
import time


# Declare all the rooms



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions={
    'w': 'north',
    's':  'south',
    'a':  'west',
    'd':  'east'
}

items={
    'Sword': Item('Sword','A sharp sword that can be use to cut down the monster'),
    'Shield': Item('Shield', 'If you don\'t like to attack the monster, you can defend yourself'),
}

# Generate some items in each rooms:

room['outside'].add_items(items['Sword'])
room['foyer'].add_items(items['Shield'])

def start_game():
    name=input('Enter your name here: ')
    player_1=Player(name,room['outside'])
    print(f'''
    Welcome to Treasure Hunting,{name}! Here is the rule :
        Press w,s,d,a,q to go north,south,east,west or to q to quit
        Once inside a room, you can pick up a drop an item by enter
        take [item] or drop [item] or skip to skip''')
    time.sleep(2)
    while True:
        print(f'''
                    You\'re in {player_1.location.name}.
        {player_1.location.description}\n 
        ''')
        player_1.location.show_items()
        action=input(f'Pick up or drop off item: ').split(' ')
        if len(action) == 2:
            player_1.action(action[0],items[action[1]])
        else:
            pass
        cmd=input('If you are ready, let go to a different room, or press i to check your bag: ')
        if cmd in directions:
            if (player_1.location.n_to==None and cmd=='w' or 
            player_1.location.s_to==None and cmd=='s' or 
            player_1.location.w_to==None and cmd=='a' or 
            player_1.location.e_to==None and cmd=='d'):
                print (f'Sorry! You can\'t go {directions[cmd]} from here')
                time.sleep(1)
                continue
            else:
                player_1.change_location(cmd)
                continue
        elif cmd == 'q':
            print('Thank you for playing. Goodbye!!')
            quit()
        elif cmd == 'i':
            player_1.show_items()
            time.sleep(2)
            continue
        else:
            print('Please enter a valid direction')
            continue

start_game()

