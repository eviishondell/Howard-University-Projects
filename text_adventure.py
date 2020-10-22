# Here are all of the strings, exactly as you will need them.
# What, you thought I was going to make you type all that??
CHEST_LOCKED = "The chest is locked!"
CLOSE_DOOR = "The door closes."
DOOR_CLOSED = "The door is closed."
DOOR_DESC_CLOSED = "The door is made of heavy oak, but is unlocked."
DOOR_DESC_OPEN = "The open door is made of heavy oak"
HALL_DESC = "You enter a long stone hallway, lit by torches. To the North is a room with a fireplace and a chest. To the east is a room with a key on a table. To the west is a dark cell."
KEY_DESC = "You enter a sparse room with a small wooden table."
KEY_DESC_WITH_KEY = KEY_DESC + " There is a small golden key on the table."
KEY_GET = "You pick up the key. It is gold-colored and weighs a lot."
LOOK_CHEST = "The chest is large and made of oak."
LOOK_FIRE = "The fire is roaring."
LOOK_KEY = "The key is made of gold."
OPEN_DOOR = "The door opens."
SORRY = "Sorry."
START_DESC = "You are in a cold, dark, stone room. There is a large oak door to the East."
TREASURE_ROOM_DESC = "You enter a lavish living space. There is a roaring fire in a fireplace, and an enormous wooden chest."
WIN = "You have retrieved the treasure! You win."

# Here are some handy constants for recognizing your locations.
ROOM_HALL = "hall"
ROOM_KEY = "key"
ROOM_START = "start"
ROOM_TREASURE = "treasure"
# And some variables. You may need to add some more here.
door_open = False
location = ROOM_START
won = False
has_key = False

# Start by printing the first room description.
print(START_DESC)


# Now we loop until the user finds the treasure!
while not won:
    command = input("> ")

    if command == "quit":
        break # This breaks the loop and ends the game.

    if location == ROOM_START:
        if command == "open door" and not door_open:
            print(OPEN_DOOR)
            door_open = True
        elif command == "close door" and door_open:
            print(CLOSE_DOOR)
            door_open = False
        elif command == "look at door":
            if door_open:
                print(DOOR_DESC_OPEN)
            else:
                print(DOOR_DESC_CLOSED)
        elif command == "go east":
            if door_open:
                print(HALL_DESC)
                location = ROOM_HALL
            else:
                print(DOOR_CLOSED)
        else:
            print(SORRY)
                  

    elif location == ROOM_HALL:
        if command == "go north":
            print(TREASURE_ROOM_DESC)
            location = ROOM_TREASURE
        elif command == "go east":
            if has_key == False:
                print(KEY_DESC_WITH_KEY)
                location = ROOM_KEY
            else:
                print(KEY_DESC)
                location = ROOM_KEY
            location = ROOM_KEY
        elif command == "go west":
            print(START_DESC)
            location = ROOM_START
        else:
            print(SORRY)
        
        
    elif location == ROOM_KEY:
        if command == "look at key" and has_key == False:
            print(LOOK_KEY)
            #location = ROOM_HALL
        elif command == "get key" and has_key == False:
            print(KEY_GET)
            has_key = True
        elif command == "go west":
            print(HALL_DESC)
            location = ROOM_HALL
        elif command == "get key" and has_key == True:
            print(SORRY)
        
        
    elif location == ROOM_TREASURE:
        if command == "look at fire":
            print(LOOK_FIRE)
        elif command == "look at chest":
            print(LOOK_CHEST)
        elif command == "go south":
            print(HALL_DESC)
            location = ROOM_HALL
        elif command == "open chest":
            if has_key == False:
                print(CHEST_LOCKED)
            elif has_key == True:
                print(WIN)
                won = True
        else:
            print(SORRY)
    


        
        
        
        
        
        
        
