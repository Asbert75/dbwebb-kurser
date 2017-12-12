#!/usr/bin/env python3

"""
Creating, loading, saving and maintaining rooms and their objects.

For all items/objects, a roomId of -1 means the object/item has been destroyed.
A roomId of 0 means the item has been picked up and is in the players inventory.
A roomId of 1 through 7 points to the Id of the room that the item is currently
located in.

playerLocation points to the Id of the room the player is currently in.
"""

import sqlite3, random

playerLocation = 1
gameFinished = False

wolfBlessing = False
owlBlessing = False
batBlessing = False
spiderBlessing = False


vestibuleQuery = "INSERT INTO Rooms VALUES ('1', 'True', 'the Vestibule', 'You \
can not help but notice the beautiful architecture. Large stone pillars are pla\
ced evenly spaced around the room. You spot a large, distinct, wooden chest in\
 the northeastern corner.', 'Perhaps you can use something found in the room\
 to open the chest. It might contain something useful.')"

hallwayQuery = "INSERT INTO Rooms VALUES ('2', 'False', 'the Hallway', 'The \
Hallway is not quite as grand of a sight as the Vestibule. Parts of the roof \
appears to have caved in over the door. There is a beautiful painting hanging \
from the wall on the west side.', 'There is no way to go through the rocks, \
but perhaps you can somehow climb over them?')"

diningHallQuery = "INSERT INTO Rooms VALUES ('3', 'False', 'Nerzias Dining \
Hall', 'The Dining Hall is a very dark and quite place. There does not seem to \
be anything special in sight.', 'To move forward, the riddle you must beat.')"

towerQuery = "INSERT INTO Rooms VALUES ('4', 'False', 'the Tower', 'The Tower\
 appears to be very barren, there are what appears to be 4 stone statues in the\
 room.', 'Answering the questions will get you forward on your missions. Just \
remember that you are also a specie.')"

antechamberQuery = "INSERT INTO Rooms VALUES ('5', 'False', 'the Lost Antecham\
ber', 'You have entered what appears to be some sort of antechamber. From the \
looks of it, nobody has been here for a long time.', 'Find the door.')"

laboratoryQuery = "INSERT INTO Rooms VALUES ('6', 'False', 'the Alchemists\
 Laboratory', 'It is Nerzia himself, right infront of you!', 'Type forward \
to engage in combat with Nerzia, beat him to unlock the next room.')"

vaultQuery = "INSERT INTO Rooms VALUES ('7', 'False', 'the Keepers Vault', 'The\
 Keepers Vault is the final of the seven. It is THE room, the room in which the\
  Staff of Netherwind lies. A large stone tomb is located in the middle of the \
 otherwise empty room, that must be where the staff lies.', 'To retrieve the \
 staff, simply open the tomb.')"


roomQueries = (vestibuleQuery, hallwayQuery, diningHallQuery, towerQuery, \
antechamberQuery, laboratoryQuery, vaultQuery)


key = "INSERT INTO Objects VALUES ('1', '-1', 'Key', 'A small \
silver key, embellished with a large N made out of gold on the front. It almost\
 looks like it could fit into that door over there...', 'True', 'False', '0', \
'False', 'False', 'False')"

chest = "INSERT INTO Objects VALUES ('2', '1', 'Chest', 'A large, \
distinct wooden chest with beautiful inscriptions on it. Looks like it could \
contain something valueable.', 'False', 'False', '1', 'False', 'False', 'True')"

hammer = "INSERT INTO Objects VALUES ('3', '-1', 'Hammer', 'A robust hammer. \
You could probably use this to smash the chest in.', 'True', 'False', '0', \
'False', 'False', 'False')"

toolbox = "INSERT INTO Objects VALUES ('4', '1', 'Toolbox', 'There are still \
some tools inside.', 'False', 'True', '3', 'False', 'False', 'False')"


ladder = "INSERT INTO Objects VALUES ('5', '2', 'Ladder', \
'An iron ladder, looks tall enough.', 'False', 'False', '0', 'False', \
'True', 'False')"

rope = "INSERT INTO Objects VALUES ('6', '2', 'Rope', 'The rope seem to be \
quite long and sturdy.', 'False', 'False', '0', 'False', 'True', 'False')"

painting = "INSERT INTO Objects VALUES ('7', '0', 'Painting', 'A beautiful \
painting.', 'False', 'False', '0', 'False', 'True', 'False')"


statue1 = "INSERT INTO Objects VALUES ('8', '4', 'Owl', 'A stone statue \
of an owl.', 'False', 'False', '0', 'False', 'False', 'False')"

statue2 = "INSERT INTO Objects VALUES ('9', '4', 'Wolf', 'A stone statue \
of a wolf.', 'False', 'False', '0', 'False', 'False', 'False')"

statue3 = "INSERT INTO Objects VALUES ('10', '4', 'Bat', 'A stone statue \
of a bat.', 'False', 'False', '0', 'False', 'False', 'False')"

statue4 = "INSERT INTO Objects VALUES ('11', '4', 'Spider', 'A stone statue \
of a spider', 'False', 'False', '0', 'False', 'False', 'False')"


tomb = "INSERT INTO Objects VALUES ('12', '7', 'Tomb', 'A large beautiful tomb,\
 it has some foreign inscriptions on it, almost looks like ancient Egyptian.', \
 'False', 'True', '0', 'False', 'False', 'False')"


wardrobe = "INSERT INTO Objects VALUES ('13', '5', 'Wardrobe', 'A beautifully \
self-carved wardrobe made out of wood.', 'False', 'False', '0', 'False', \
'False', 'True')"

painting = "INSERT INTO Objects VALUES ('14', '5', 'Painting', 'A \
large waterpainting.', 'False', 'False', '0', 'False', 'False', 'True')"






itemQueries = (key, chest, hammer, toolbox, ladder, rope, statue1, \
statue2, statue3, statue4, tomb, wardrobe, painting)


def initialize():
    """
    Initializes the game, creating the tables, and inserting the data.
    """

    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    """
    Database Structure:

    Table: Rooms
    id          INTEGER
    unlocked    BOOLEAN
    name        TEXT
    description TEXT
    clue        TEXT

    Table: Objects
    id          INTEGER
    roomId      INTEGER         - -1 = Not Yet Looted, 0 = In Player Inventory
    name        TEXT
    description TEXT
    droppable   BOOLEAN
    lootable    BOOLEAN
    contains    INTEGER
    looted      BOOLEAN
    movable    BOOLEAN
    destroyable BOOLEAN
    """

    dbc.execute("DROP TABLE IF EXISTS Rooms")
    dbc.execute("DROP TABLE IF EXISTS Objects")
    dbc.execute("CREATE TABLE Rooms (id INTEGER, unlocked TEXT, \
name TEXT, description TEXT, clue TEXT)")
    dbc.execute("CREATE TABLE Objects (id INTEGER, \
roomId INTEGER, name TEXT, description TEXT, droppable TEXT, \
lootable TEXT, contains INTEGER, looted TEXT, movable TEXT, \
destroyable TEXT)")

    for query in roomQueries:
        try:
            dbc.execute(query)
        except Exception as err:
            print(err)

    for query in itemQueries:
        try:
            dbc.execute(query)
        except Exception as err:
            print(err)

    connection.commit()
    connection.close()


def bossFight():
    """
    A mini-game where you have to beat a boss to continue
    """
    playerHealth = 100
    bossHealth = 1000

    print("You have been challenged to duel by Nerzia. Beat him to unlock the \
door to the next room.\n")

    while playerHealth > 0 and bossHealth > 0:
        print("It's your turn to strike. What spell do you use?")
        print("Available spells: Fireball, Missiles")
        cast = input("Cast: ")

        if cast.lower() == 'fireball':
            damage = random.randint(150, 250)
            bossHealth = bossHealth - damage

            if bossHealth <= 0:
                print("\nYou won! Passage to the next room has been granted.")
                unlockVault()
            else:
                print("You hit Nerzia for", damage, "damage! He has", bossHealth, \
"health left.\n")

        elif cast.lower() == 'missiles':
            damage = 5*random.randint(25, 75)
            bossHealth = bossHealth - damage

            if bossHealth <= 0:
                print("\nYou won! Passage to the next room has been granted.")
                unlockVault()
            else:
                print("You hit Nerzia for", damage, "damage! He has", bossHealth, \
"health left.\n")
        else:
            print("That is not a valid spellname.\n")

        bossAttack = random.randint(5, 20)
        playerHealth = playerHealth - bossAttack

        if playerHealth <= 0:
            print("You lost. Try again!")
        else:
            print("Nerzia hit you for", bossAttack, "damage. You have", \
playerHealth, "health left.\n")


def wolfEquation():
    """
    Equation for the wolf statue.
    """
    global wolfBlessing

    if wolfBlessing:
        print("You have already been granted this blessing.")
        return

    print("The statue rumbles as it wakes to life. To recieve the wolf's \
blessing, you must first pass its test. Answer the following:")
    print("In a room there are 6 wolfs and 2 spiders. How many legs are there \
in total?")
    answer = input("Answer: ")

    if answer == "40":
        print("You have answered correctly. You have been granted the \
blessing of the Wolf.")
        wolfBlessing = True
    else:
        print("Your answer is incorrect. The statue turns back to stone.")

def owlEquation():
    """
    Equation for the owl statue.
    """
    global owlBlessing

    if owlBlessing:
        print("You have already been granted this blessing.")
        return

    print("The statue rumbles as it wakes to life. To recieve the owl's \
blessing, you must first pass its test. Answer the following:")
    print("If one owl can fly 200 meters vertically up into the sky, how many \
meters up into the sky can two owls fly?")
    answer = input("Answer: ")

    if answer == "200":
        print("You have answered correctly. You have been granted the \
blessing of the Owl.")
        owlBlessing = True
    else:
        print("Your answer is incorrect. The statue turns back to stone.")

def spiderEquation():
    """
    Equation for the spider statue.
    """
    global spiderBlessing

    if spiderBlessing:
        print("You have already been granted this blessing.")
        return

    print("The statue rumbles as it wakes to life. To recieve the wolf's \
blessing, you must first pass its test. Answer the following:")
    print("If 5x-3*2 = 9, what is x^2+3x?")
    answer = input("Answer: ")

    if answer == "18":
        print("You have answered correctly. You have been granted the \
blessing of the Wolf.")
        spiderBlessing = True
    else:
        print("Your answer is incorrect. The statue turns back to stone.")

def batEquation():
    """
    Equation for the bat statue.
    """
    global batBlessing

    if batBlessing:
        print("You have already been granted this blessing.")
        return

    print("The statue rumbles as it wakes to life. To recieve the wolf's \
blessing, you must first pass its test. Answer the following:")
    print("There are currently how many different species in this room?")
    answer = input("Answer: ")

    if answer == "5":
        print("You have answered correctly. You have been granted the \
blessing of the Wolf.")
        batBlessing = True
    else:
        print("Your answer is incorrect. The statue turns back to stone.")


def theRiddler():
    """"
    Plays a game of riddles. Win to move foward in the game.
    """
    q1 = {"Question": "Which two things can you never eat for breakfast?", \
"A": "Milk and Cereal", "B": "Beef and Potatoes", "C": "Lunch and Dinner", \
"Answer": "C"}

    q2 = {"Question": "If it's information you seek, come and see me. If it's \
pairs of letters you need, I have consecutively three. Who am I?", \
"A": "Wikipedia", "B": "A Bookkeeper", "C": "The Alphabet", "Answer": "B"}

    q3 = {"Question": "I only exist where there is light, but I die if light \
is shone upon me.", "A": "A shadow", "B": "The human race", \
"C": "A type of bug", "Answer": "A"}

    q4 = {"Question": "Every night you tell me what to do, and every morning \
I do what I am told. Still you hate me. What am I?", "A": "A cat", \
"B": "An alarm clock", "C": "The law", "Answer": "B"}

    q5 = {"Question": "What is it that no man wants, but no man wants \
to lose?", "A": "A baby", "B": "A woman", "C": "A lawsuit", "Answer": "C"}

    riddles = (q1, q2, q3, q4, q5)

    print("You have been challenged to a game of riddles. Shall you win\
, you will be allowed passage into the next room. You will be presented with a \
riddle and 3 answers. Simply answer with the letter of the answer you think is \
correct, A, B, or C.")

    print("\nThe Riddler says: I will start you off with an easy one.\n")
    input("Press Enter to Continue...")

    incorrectCount = 0
    for riddle in riddles:
        incorrect = True

        while incorrect:
            print(riddle["Question"])
            print("A)", riddle["A"])
            print("B)", riddle["B"])
            print("C)", riddle["C"])

            a = input("Answer: ")
            answer = a.upper()

            if answer == riddle["Answer"]:
                print("\nThe Riddler says: You are correct.\n")
                incorrect = False
            else:
                incorrectCount += 1
                print("\nThe Riddler says: Incorrect! Try again...\n")


    if incorrectCount == 0:
        unlockKitchen()
        print("The Riddler says: Congratulations. You have earned passage to \
the next room.")
    else:
        print("The Riddler says: Looks like you took quite a few too many \
wrong guesses. Feel free to try again.")


def roomInformation():
    """
    Prints room information.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    roomId = playerLocation

    dbc.execute("SELECT description FROM Rooms WHERE id = ?", str(roomId))
    ret = str(dbc.fetchone()[0])

    connection.close()

    return ret


def isUnlocked():
    """
    Checks if the given room (roomId) is unlocked or not.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    loc = str(playerLocation+1)
    dbc.execute("SELECT unlocked FROM Rooms WHERE id = ?", loc)
    res = dbc.fetchone()[0]

    connection.close()

    if res == 'True':
        return True
    else:
        return False


def gameHelp():
    """
    Prints game help.
    """
    print("""\nAvailable commands are:
    q, quit             -   Quit the game.
    fwd, forward        -   Move into the next room (if unlocked).
    ba, backwards       -   Move back to the previous room.
    i, info             -   Prints the room description.
    v, view             -   Prints out anything noteworthy in the room.
    c, clue             -   Prints a clue on how to pass the current room.
    h, help             -   Prints the help menu (current).

    o, object           -   Prints out the objects in the current room.
    s [obj], see [obj]  -   Prints the description of the selected object.
    o [obj], open [obj] -   Open the selected object, if possible.
    k [obj], kick [obj] -   Breaks the selected object, if possible.
    m [obj], move [obj] -   Moves the selected object, if possible.
    """)


def moveForward():
    """
    Moves the player into the next room (if unlocked)
    """
    global playerLocation

    unlockHallway()

    if playerLocation == 4:
        unlockAntechamber()

    unlocked = isUnlocked()

    if playerLocation == 7:
        print("You can't go that way.")
    elif playerLocation == 6 and not unlocked:
        bossFight()
    elif playerLocation == 3 and not unlocked:
        theRiddler()
    elif unlocked:
        playerLocation = playerLocation + 1

        roomImage(playerLocation)
        desc = roomInformation()
        print(desc)
    else:
        print("That door is locked!")


def moveBackwards():
    """
    Moves the player into the next room (if not in room #1)
    """
    global playerLocation

    if playerLocation == 1:
        print("You can't go that way.")
    else:
        playerLocation = playerLocation - 1

        roomImage(playerLocation)
        desc = roomInformation()
        print(desc)


def viewRoom():
    """
    Fetches all the current items in the room by roomID.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("SELECT name, description FROM Objects WHERE roomID = ?", \
    str(playerLocation))

    print("In the current room, you find:")

    items = dbc.fetchall()
    for item in items:
        try:
            print(str(item[0]))
        except Exception as err:
            print(err)

    connection.close()


def clue():
    """
    Displays a clue on how to unlock the next room.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("SELECT clue FROM Rooms WHERE id = ?", str(playerLocation))
    print(dbc.fetchone()[0])

    connection.close()


def seeObject(obj):
    """
    Displays info on the selected object.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    name = obj[0].upper() + obj[1:].lower()

    try:
        dbc.execute("SELECT description, roomId FROM Objects \
WHERE name = (?)", (name,))
        row = dbc.fetchone()
        if row is not None:
            desc = row[0]
            room = row[1]

            if room == playerLocation or room == 0:
                print(desc)
            else:
                print("Object not found.")
        else:
            print("Object not found.")

        connection.close()
    except Exception as err:
        print("Error:", err)


def kickObject(obj):
    """
    Opens the selected object.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    name = obj[0].upper() + obj[1:].lower()

    try:
        dbc.execute("SELECT destroyable, contains, looted, roomId FROM Objects \
WHERE name = (?)", (name,))
        row = dbc.fetchall()

        if len(row) < 1:
            print("Object not found.")
            return

        if row is not None:
            destroyable = row[0][0]
            cId = row[0][1]
            looted = row[0][2]
            room = row[0][3]

            if room is not playerLocation:
                print("Object not found.")
                return

            if destroyable == "True" and looted == "False":
                if name == "Chest":
                    if not playerHasHammer():
                        print("You need something stronger to destroy the \
chest.")
                        return

                dbc.execute("UPDATE Objects SET looted = 'True', roomId = '-1' \
WHERE name = (?)", (name,))
                dbc.execute("UPDATE Objects SET roomId = (?) WHERE id = (?)", \
('0', cId))
                dbc.execute("SELECT name FROM Objects WHERE id = (?)", (cId,))
                item = dbc.fetchone()[0]

                connection.commit()

                print("You destroyed the", name, "and found a", item, "inside!")

            elif destroyable == "False":
                print("You can't destroy that object.")

            elif looted == "True":
                print("Object not found.")
        else:
            print("Object not found.")

        connection.close()
    except Exception as err:
        print("Error:", err)


def openObject(obj):
    """
    Destroys the selected object.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    name = obj[0].upper() + obj[1:].lower()

    if name == "Chest" and playerLocation == 1:
        print("That object is locked.")
    elif name == "Owl" and playerLocation == 4:
        owlEquation()
    elif name == "Spider" and playerLocation == 4:
        spiderEquation()
    elif name == "Bat" and playerLocation == 4:
        batEquation()
    elif name == "Wolf" and playerLocation == 4:
        wolfEquation()
    elif name == "Tomb" and playerLocation == 7:
        global gameFinished
        gameFinished = True

        print("Waleria says: The Staff of Netherwind! So it is true, the \
staff exists. You did it, the staff has been retrieved.")
        print("\nYou have beaten the game. Thank you for playing.")
        input("Press Enter to Quit...")

    else:
        try:
            dbc.execute("SELECT lootable, contains, looted, roomId FROM Objects\
 WHERE name = (?)", (name,))
            row = dbc.fetchall()

            if len(row) < 1:
                print("Object not found.")
                return

            if row is not None:
                openable = row[0][0]
                cId = row[0][1]
                looted = row[0][2]
                room = row[0][3]

                if room is not playerLocation:
                    print("Object not found.")
                    return

                if openable == "True" and looted == "False":
                    dbc.execute("UPDATE Objects SET looted = 'True' WHERE \
name = (?)", (name,))
                    dbc.execute("UPDATE Objects SET roomId = (?) WHERE \
id = (?)", ('0', cId))
                    dbc.execute("SELECT name FROM Objects WHERE id = (?)", \
(cId,))
                    item = dbc.fetchone()[0]

                    connection.commit()

                    print("Opening the", name, "you found a", item)

                elif openable == "False":
                    print("That object cannot be opened.")

                elif looted == "True":
                    print("You have already opened that object.")
                else:
                    print("Object not found.")

            connection.close()
        except Exception as err:
            print("Error:", err)


def moveObject(obj):
    """
    Moves the selected object.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    global playerLocation

    name = obj[0].upper() + obj[1:].lower()

    if playerLocation == 2:
        if name == "Ladder":
            print("You moved the ladder to the cave-in. It wasn't high \
enough to get you past the rumble.")
        elif name == "Rope":
            print("You threw the rope over the rumble and dragged it towards \
you. It seem to have hooked onto something. You're able to move into the next \
room!")
            dbc.execute("UPDATE Rooms SET unlocked = 'True' WHERE id = '3'")
        elif name == "Painting":
            print("Moving the painting, you notice something strange, there \
seem to be some kind of seam behind the painting in the wall. Upon further \
inspection you notice that it's a trapdoor. You choose to enter and follow the \
path. You end up in what appears to be the final chamber, the Keeper's Vault!")
            dbc.execute("UPDATE Rooms SET unlocked = 'True'")

            playerLocation = 7

            input("Press Enter to Continue...")

            roomImage(playerLocation)
            desc = roomInformation()
            print(desc)

    elif playerLocation == 5:
        if  name == "Painting":
            print("Waleria says: There doesn't appear to be anything special behind the \
painting.")
        elif name == "Wardrobe":
            print("Waleria says: There is a hole behind the wardrobe! \
You found the passage to the next room!!")
            unlockLab()

    connection.commit()
    connection.close()


def unlockHallway():
    """
    Checks if the roomId of Key is 0 == Player has acquired Key and can unlock
    the door to the next room.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("SELECT roomId FROM Objects WHERE name = 'Key'")
    itemLoc = dbc.fetchone()

    if itemLoc[0] == 0:
        dbc.execute("UPDATE Rooms SET unlocked = 'True' WHERE id = '2'")
        dbc.execute("UPDATE Objects SET roomId = '-1' WHERE name = 'Key'")
        print("Waleria says: The key was a perfect match. The door to enter \
the next room has been unlocked!")

    connection.commit()
    connection.close()


def unlockKitchen():
    """
    Unlocks the kitchen.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("UPDATE Rooms SET unlocked = 'True' WHERE id = '4'")

    connection.commit()
    connection.close()


def unlockAntechamber():
    """
    Unlocks the Antechamber.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()


    if owlBlessing and wolfBlessing and spiderBlessing and batBlessing:
        dbc.execute("UPDATE Rooms SET unlocked = 'True' WHERE id = '5'")
        print("Waleria says: The door to the next room has been unlocked!")
    else:
        print("Waleria says: You must acquire all 4 blessings before the door \
unlocks.")

    connection.commit()
    connection.close()


def unlockLab():
    """
    Checks if the roomId of Key is 0 == Player has acquired Key and can unlock
    the door to the next room.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("UPDATE Rooms SET unlocked = 'True' WHERE id = '6'")

    connection.commit()
    connection.close()


def unlockVault():
    """
    Checks if the roomId of Key is 0 == Player has acquired Key and can unlock
    the door to the next room.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("UPDATE Rooms SET unlocked = 'True' WHERE id = '7'")

    connection.commit()
    connection.close()


def playerHasHammer():
    """
    Checks if the roomId of Hammer is 0 == Player has acquired Hammer.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("SELECT roomId FROM Objects WHERE name = 'Hammer'")
    itemLoc = dbc.fetchone()[0]

    if itemLoc == 0:
        dbc.execute("UPDATE Objects SET roomId = '-1' WHERE name = 'Hammer'")
        return True
    else:
        return False

    connection.commit()
    connection.close()


def roomImage(location):
    """
    Prints the room image when entering a new room.
    """
    if location == 1:
        print(room1Image)
    elif location == 2:
        print(room2Image)
    elif location == 3:
        print(room3Image)
    elif location == 4:
        print(room4Image)
    elif location == 5:
        print(room5Image)
    elif location == 6:
        print(room6Image)
    elif location == 7:
        print(room7Image)

room1Image = r"""
▬▬▬▬▬▬▬▬▬▬▬___▬▬▬▬▬▬▬▬▬▬▬
▌                     ■ ▐
▌ ●                   ● ▐
▌║   ●             ●    ▐
▌  ●                 ●  ▐
▌    ●             ●    ▐
▌ ●                   ● ▐
▌    ●      o      ●    ▐
▌ ●     ●       ●     ● ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Vestibule.
"""

room2Image = r"""
▬▬▬▬▬▬▬▬▬▬▬___▬▬▬▬▬▬▬▬▬▬▬
▌    │   ●●●●●●●  ______▐
▌    │            │    ║▐
▌    │            │_/ __▐
▌                 │     ▐
▌    │                  ▐
▌║   │            │_  /_▐
▌    │      o     │     ▐
▌    │            │     ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Hallway.
"""

room3Image = r"""
▬▬▬▬▬▬▬▬▬▬▬___▬▬▬▬▬▬▬▬▬▬▬
▌           ?            ▐
▌ ▬▬▬▬              ▬▬▬▬ ▐
▌                        ▐
▌ ▬▬▬▬              ▬▬▬▬ ▐
▌                        ▐
▌ ▬▬▬▬              ▬▬▬▬ ▐
▌           o            ▐
▌ ▬▬▬▬              ▬▬▬▬ ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Dining Hall.
"""

room4Image = r"""
▬▬▬▬▬▬▬▬▬▬▬■■■▬▬▬▬▬▬▬▬▬▬▬
▌                       ▐
▌■                     ■▐
▌                       ▐
▌                       ▐
▌                       ▐
▌■                     ■▐
▌           o           ▐
▌                       ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Tower.
"""

room5Image = r"""
▬▬▬▬▬▬▬▬▬▬▬___▬▬▬▬▬▬▬▬▬▬▬
▌                       ▐
▌    ▌              ▌   ▐
▌                       ▐
▌    ▌              ▌   ▐
▌                       ▐
▌    ▌              ▌   ▐
▌           o           ▐
▌    ▌              ▌   ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Lost Antechamber.
"""

room6Image = r"""
▬▬▬▬▬▬▬▬▬▬▬___▬▬▬▬▬▬▬▬▬▬▬
▌    │      N      ┬   ■▐
▌                 │     ▐
▌    ┬           │      ▐
      │            │    ▐
▌    │             │    ▐
▌   │            │      ▐
▌    │      o    │      ▐
▌     │            │    ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Alchemist's Laboratory.
"""

room7Image = r"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▌         ■■■■■         ▐
▌                       ▐
▌                       ▐
▌                       ▐
▌                       ▐
▌                       ▐
▌           o           ▐
▌                       ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬
You have entered the Keeper's Vault.
"""


def debugObject(obj):
    """
    Prints SQL Info on the named object, used for debugging data.
    """
    connection = sqlite3.connect("game.sqlite")
    dbc = connection.cursor()

    dbc.execute("SELECT * FROM Objects WHERE name = (?)", (obj,))
    info = dbc.fetchall()

    objId = info[0][0]
    objRoomId = info[0][1]
    objName = info[0][2]
    objDesc = info[0][3]
    objDroppable = info[0][4]
    objLootable = info[0][5]
    objContains = info[0][6]
    objLooted = info[0][7]
    objMovable = info[0][8]
    objDestroyable = info[0][9]

    print("Id:", objId)
    print("roomId:", objRoomId)
    print("Name:", objName)
    print("Desc:", objDesc)
    print("Droppable:", objDroppable)
    print("Lootable:", objLootable)
    print("Contains:", objContains)
    print("Looted:", objLooted)
    print("Movable:", objMovable)
    print("Destroyable:", objDestroyable)
