import random
import time
import inspect

answer = 1
inventory = []
altar = []
rCode = str(random.randint(1000,9999))
n = 0
red = "Off"
blue = "Off"
green = "Off"
inventory = []

def win():
    print("****************************************************************************")
    time.sleep(1)
    print("""Congratulations, brave adventurer, you have made it to the end of the game alive.
          \nYou will forever be remembered as one of the greats of your era, all people soon shall know the tale of""", name,
          """ the Great and how they overcame the many challenges in their way to earn the ultimate prize:\nFreedom!\n\n\n""")
    time.sleep(1)
    print("Adventure : A Text Based Game\n")
    print("""Credits:
Story by iAlphaRaptor
Coded by iAlphaRaptor in Python 3.6.5""")
    time.sleep(1)
    print("Thank you for playing.")
    input()

def timeGet():
    global clock_time
    answer = input("Change to what?\n")
    if answer == "save":
        progress.save(input("What would you like the save to be called?\n"), inspect.stack()[0][3], inventory)
    elif len(answer) == 4:
        hour = answer[0]
        minute = answer[2] + answer[3]
        hour = int(hour)
        minute = int(minute)
        if hour > 12 or minute > 60:
            print("Invalid time!")
            timeGet()
        hour = str(hour)
        minute = str(minute)
        clock_time = hour + ":" + minute
    elif len(answer) == 5:
        hour = answer[0] + answer[1]
        minute = answer[3] + answer[4]
        hour = int(hour)
        minute = int(minute)
        if hour > 12 or minute > 60:
            print("Invalid time!")
            timeGet()
        hour = str(hour)
        minute = str(minute)
        clock_time = hour + ":" + minute
    else:
        print("Invalid time!")
        timeGet()

def king():
    global clock_time
    print("You can see a large stone statue of what looks like a King from ages past.")
    if "Charm" in inventory:
        print("In the foot of the statue is a clock similar to the one in the silver charm.")
    else:
        print("In the foot of the statue is a clock decorated with silver.")
    time.sleep(3)
    print("According to this clock it is midnight but the hands are not moving.")
    print("There is a small cog which looks like it would change the time on the clock.")
    answer = input("Change the time or Go Back?\n").lower()
    if answer == "change time" or answer == "time" or answer == "change":
        timeGet()
        time.sleep(1)
        if clock_time == "6:59":
            print("The clock hands begin to move again and the clock starts to chime.\nAs the seventh note reverberates around the room, your vision slowly fades into darkness.")
            time.sleep(1)
            win()
        else:
            print("The clock now reads", clock_time, ".")
            king()
    elif answer == "go back":
        endFight()
    else:
        print("You cannot do that at the moment.")
        king()



def diamondBanner():
    print("You can see nothing of interest about this banner.")
    banners()

def blueBanners():
    print("You can see that all of the banners look the same.")
    time.sleep(0.76)
    print("Then you notice a word sewn in gold on the blue background.")
    time.sleep(1)
    print("...")
    time.sleep(0.5)
    print("Adventure")
    time.sleep(0.5)
    print("...")
    time.sleep(0.85)
    banners()

def throneSit():
    print("The moment you sit down, a voice with no obvious source bellows, \n\"What is The Word?\"")
    answer = input().lower()
    if answer == "adventure":
        print("As soon as you mention The Word, the door which you previously came through swings open.")
        print("You go through it and find yourself in a massive, lavishly decorated room.")
        king()
    else:
        print("Again, the voice shouts, \"Who dares sit where the Great King sat without knowing The Word?\"")
        time.sleep(1)
        print("As soon as you hear the final word, a strange blue gas rises from the floor and you begin to feel sleepy...")
        death()

def charm():
    print("The charm is made of pure silver and has a small clock in the centre. The time reads 6:59 but neither of the hands are moving.")
    time.sleep(0.5)
    answer = input("Add charm to inventory?\n").lower()
    if answer == "yes":
        print("Adding charm to inventory...")
        time.sleep(1)
        inventory.append("Charm")
        throne()
    elif answer == "no":
        print("Come back later when you would like to collect the charm.")
        throne()
    else:
        print("Invalid Answer.")
        charm()

def banners():
    print("All of the banners look the same - blue with a lion's head in the middle.")
    time.sleep(0.5)
    print("However, there is one which shows a sparkling diamond on a silver and gold checked background.")
    answer = input("Type 1 to inspect the blue banners.\nType 2 to inspect the diamond banner.\nType 3 to go back.\n")
    if answer == "1":
        blueBanners()
    elif answer == "2":
        diamondBanner()
    elif answer == "3":
        endFight()
    else:
        print("You cannot do that at the moment.")
        banners()

def throne():
    print("You can see a throne which is covered in cobwebs and clearly has not been sat in for a long time.")
    if "Charm" not in inventory:
        print("There is a small silver charm on the arm of the throne.")
        answer = input("Sit down or Take Charm or Go Back?\n").lower()
    else:
        answer = input("Sit down or Go Back?\n").lower()
    if answer == "go back":
        endFight()
    elif answer == "sit down":
        throneSit()
    elif answer == "take charm" or answer == "charm":
        charm()
    else:
        print("You cannot do that at the moment.")
        throne()

def endFight():
    print("You are in what appears to be a throne room with a large gold throne at one end and many colourful banners on the wall.\nThere is a locked door next to you.")
    answer = input("Look at Throne or Banners?\n").lower()
    if answer == "look at throne" or answer == "throne":
        throne()
    elif answer == "look at banners" or answer == "look at banner" or answer == "banner" or answer == "banners":
        banners()
    elif answer == "look at door" or answer == "door" or answer == "inspect door":
        print("The door cannot be opened.")
        endFight()
    else:
        print("You cannot do that at the moment.")
        endFight()

def buttonCheck():
    global red, green, blue
    if red == "On" and blue == "On" and green == "Off":
        time.sleep(0.5)
        print("The room changes before your very eyes.\nWalls moving, colours changing until you end up in another room.")
        endFight()

def blueChange():
    global blue
    if blue == "Off":
        print("Click")
        time.sleep(0.5)
        blue = "On"
        buttonCheck()
        endGame()
    else:
        print("Click")
        time.sleep(0.5)
        blue = "Off"
        buttonCheck()
        endGame()

def redChange():
    global red
    if red == "Off":
        print("Click")
        time.sleep(0.5)
        red = "On"
        buttonCheck()
        endGame()
    else:
        print("Click")
        time.sleep(0.5)
        red = "Off"
        buttonCheck()
        endGame()

def greenChange():
    global green
    if green == "Off":
        print("Click")
        time.sleep(0.5)
        green = "On"
        buttonCheck()
        endGame()
    else:
        print("Click")
        time.sleep(0.5)
        green = "Off"
        buttonCheck()
        endGame()

def endGame():
    global green, blue, red
    if red == "Off" and blue == "Off" and green == "Off":
        print("You are in a large room with three buttons on the wall: Red, Green and Blue.")
    answer = input("").lower()
    if answer == "push red button" or answer == "press red button" or answer == "red" or answer == "press red" or answer == "push red" or answer == "red button":
        redChange()
    elif answer == "push green button" or answer == "press green button" or answer == "green" or answer == "press green" or answer == "push green" or answer == "green button":
        greenChange()
    elif answer == "push blue button" or answer == "press blue button" or answer == "blue" or answer == "press blue" or answer == "push blue" or answer == "blue button":
        blueChange()
    elif answer == "inventory":
        check()
        endGame()
    else:
        print("Pardon?")
        endGame()


def death():
    answer = input("Unlucky, brave adventurer.\nWould you like to try again?\n").lower()
    if answer == "yes":
        welcome()
    elif answer == "no":
        print("Well then, I hope to see you again soon.")
    else:
        print("Pardon?")
        death()

def dungeonWin():
    print("Where the troll once stood, a Gold Key now lies, glittering.")
    answer = input("Pick it up?\n").lower()
    if answer == "yes":
        inventory.append("Gold Key")
        print("Adding Gold Key to inventory..")
        time.sleep(0.5)
        print("You ascend the stairs once again and end up back in the outbuilding.")
        time.sleep(0.5)
        outbuilding()
    elif answer == "no":
        answer = input("Are you sure you want to leave the Gold Key?\n").lower()
        if answer == "yes":
            print("You ascend the stairs once again and end up back in the outbuilding.")
            outbuilding()
        elif answer == "no":
            inventory.append("Gold Key")
            print("Adding Gold Key to inventory..")
            time.sleep(0.5)
            print("You ascend the stairs once again and end up back in the outbuilding.")
            outbuilding()
        else:
            print("Invalid Action")
            dungeonWin()
    else:
        print("Invalid Action")
        dungeonWin()

def death():
    print("GAME OVER")
    answer = input("Try again?\n").lower()
    if answer == "yes":
        welcome()
    else:
        print("Goodbye then, brave adventurer, I hope to see you again soon.")

def dungeonFight():
    print("As the last stone enters the altar, the whole table sinks into the ground and a large, ugly troll drops down from a previously unseen hole in the ceiling, brandishing a bloody axe.")
    print("The troll is blocking all exits but the one leading north.")
    answer = input("Fight or Run Away?\n").lower()
    if answer == "fight":
        if "Sword" in inventory:
            print("Your elvish-made sword begins to glow brightly as it guides your hand toward the troll's neck.\nThe instant the troll dies, its body is enshrouded in black smoke and, as the smoke clears, you can see the troll has disappeared.")
            time.sleep(1)
            dungeonWin()
        else:
            print("Your punch connects with the troll's jaw and stuns him, he stumbles backwards and drops his axe.")
            answer = input("Attack or Run Away?\n").lower()
            if answer == "attack":
                chance = random.randint(1,3)
                if chance == 1:
                    print("The troll recovers from his daze and swings his head-sized fist into your temple, the world fades into darkness...")
                    time.sleep(1.5)
                    death()
                else:
                    print("Your next attack takes the troll off guard and he crumples to the floor, dead.\nThe instant the troll dies, its body is enshrouded in black smoke and, as the smoke clears, you can see the troll has disappeared.")
                    time.sleep(1)
                    dungeonWin()
            elif answer == "run away":
                print("The troll recovers from his daze and swings his head-sized fist into your temple, the world fades into darkness...")
                time.sleep(1.5)
                death()
            else:
                print("Pardon?")
                print("The troll take advantage of your hesitation and swings his head-sized fist into your temple.")
                time.sleep(0.5)
                print("The world fades into darkness...")
                time.sleep(0.5)
                death()
    elif answer == "run away":
        print("With surprising speed, the troll jumps into your path and swiftly decapitates you.")
        death()
    else:
        print("You cannot do that at the moment")
        dungeonFight()

def room6():
    print("You are in what looks like an abandoned armorey.")
    if "Sword" in inventory:
        answer = input("An exit leads off to the north.\n").lower()
    else:
        print("In a dusty, glass case you see a bronze shield and an elvish sword.")
        answer = input("Pick them up?\n").lower()
        if answer == "yes":
            inventory.append("Shield")
            inventory.append("Sword")
        else:
            print("Come back later when you would.")
        answer = input("An exit leads off to the north.\n").lower()
    if answer == "go north":
        intersection9()
    elif answer == "go east":
        wall()
        room6()
    elif answer == "go south":
        wall()
        room6()
    elif answer == "go west":
        wall()
        room6()
    else:
        direction()
        room6()

def room5():
    print("You are in a plain room with a single electric light hanging from the bare ceiling.\nYou can see nothing of interest about the room")
    answer = input("An exit leads off to the north.\n").lower()
    if answer == "go north":
            intersection28()
    elif answer == "go east":
        wall()
        room5()
    elif answer == "go south":
        wall()
        room5()
    elif answer == "go west":
        wall()
        room5()
    elif answer == "mjw":
        if "Sapphire" in inventory or "Sapphire" in altar:
            n = 0
        else:
            inventory.append("Sapphire")
        if "Ruby" in inventory or "Ruby" in altar:
            n = 0
        else:
            inventory.append("Ruby")
        if "Diamond" in inventory or "Diamond" in altar:
            n = 0
        else:
            inventory.append("Diamond")
        if "Emerald" in inventory or "Emerald" in altar:
            n = 0
        else:
            inventory.append("Emerald")
        print("Congratulations! You have found the Easter Egg.\nAll gems have been instantly added to your inventory.")
        time.sleep(2)
        room5()
    else:
        direction()
        room5()

def room4():
    print("You are in an expensive looking room, a chandelier hangs from the ceiling.")
    if "Diamond" in inventory or "Diamond" in altar:
        answer = input("Exits lead off to the west and to the south.\n").lower()
    else:
        print("Hanging from the bottom of the chandelier is a massive diamond.")
        answer = input("Take it?\n").lower()
        if answer == "yes":
            inventory.append("Diamond")
        else:
            print("Come back later when you would.")
        answer = input("Exits lead off to the west and to the south.\n").lower()
    if answer == "go north":
        wall()
        room4()
    elif answer == "go east":
        wall()
        room4()
    elif answer == "go south":
        intersection23()
    elif answer == "go west":
        intersection25()
    else:
        direction()
        room4()

def room3():
    print("You are in a dark cave with strange markings covering the walls.")
    if "Ruby" in inventory or "Ruby" in altar:
        answer = input("An exit leads off to the north.\n").lower()
    else:
        print("You stand on something which, on inspection, appears to be a polished ruby.")
        answer = input("Pick it up?\n").lower()
        if answer == "yes":
            inventory.append("Ruby")
        else:
            print("Come back later when you would.")
        answer = input("An exit leads off to the north.\n").lower()
    if answer == "go north":
        intersection22()
    elif answer == "go east":
        wall()
        room3()
    elif answer == "go south":
        wall()
        room3()
    elif answer == "go west":
        wall()
        room3()
    else:
        direction()
        room3()

def room2():
    print("You are in a large room with a vaulted ceiling.")
    if "Emerald" in inventory or "Emerald" in altar:
        answer = input("Exits lead off to the north and to the west.\n").lower()
    else:
        print("In the wall, you see something flash green.")
        answer = input("It turns out to be a large expensive-looking emerald.\nTake it?\n").lower()
        if answer == "yes":
            inventory.append("Emerald")
        else:
            print("Come back later when you would.")
        answer = input("Exits lead off to the north and to the west.\n").lower()
    if answer == "go north":
        intersection11()
    elif answer == "go east":
        wall()
        room2()
    elif answer == "go south":
        wall()
        room2()
    elif answer == "go west":
        intersection12()
    else:
        direction()
        room2()

def room1():
    print("You are in a small room lit by a single flaming torch.")
    if "Sapphire" in inventory or "Sapphire" in altar:
        answer = input("Exits lead off in all directions.\n").lower()
    else:
        print("On the floor, you see something flicker blue.")
        answer = input("It turns out to be a small sapphire.\nPick it up?\n").lower()
        if answer == "yes":
            inventory.append("Sapphire")
        else:
            print("Come back later when you would.")
        answer = input("Exits lead off in all directions.\n").lower()
    if answer == "go north":
        intersection2()
    elif answer == "go east":
        intersection10()
    elif answer == "go south":
        intersection17()
    elif answer == "go west":
        centerMaze()
    else:
        direction()
        room1()

def centerMaze():
    global n
    print("You are back in the center of the maze.")
    time.sleep(1)
    if "Sapphire" in inventory:
        answer = input("Place the sapphire in its slot on the altar?\n").lower()
        if answer == "yes":
            altar.append("Sapphire")
            inventory.remove("Sapphire")
            time.sleep(1)
        elif answer == "no":
            print("Come back later when you would.")
            time.sleep(1)
    if "Ruby" in inventory:
        answer = input("Place the ruby in its slot in the altar?\n").lower()
        if answer == "yes":
            altar.append("Ruby")
            inventory.remove("Ruby")
            time.sleep(1)
        elif answer == "no":
            print("Come back later when you would.")
            time.sleep(1)
    if "Diamond" in inventory:
        answer = input("Place the diamond in its slot in the altar?\n").lower()
        if answer == "yes":
            altar.append("Diamond")
            inventory.remove("Diamond")
            time.sleep(1)
        elif answer == "no":
            print("Come back later when you would.")
            time.sleep(1)
    if "Emerald" in inventory:
        answer = input("Place the emerald in its slot in the altar?\n").lower()
        if answer == "yes":
            altar.append("Emerald")
            inventory.remove("Emerald")
            time.sleep(1)
        elif answer == "no":
            print("Come back later when you would.")
            time.sleep(1)
    if len(altar) == 0:
        print("There is currently nothing in the altar.")
    elif len(altar) < 4:
        print("Gemstones in the altar:")
        for i in range(0, len(altar)):
            print(altar[n])
            n += 1
            time.sleep(0.5)
        n = 0
        time.sleep(1)
    else:
        dungeonFight()
    answer = input("Exits lead off in all directions.\n").lower()
    if answer == "go north":
        intersection1()
    elif answer == "go south":
        intersection18()
    elif answer == "go east":
        room1()
    elif answer == "go west":
        intersection3()
    else:
        direction()
        centerMaze()

def intersection28():
    intText()
    answer = input("")
    if answer == "go north":
        intersection27()
    elif answer == "go east":
        intersection21()
    elif answer == "go south":
        room5()
    elif answer == "go west":
        wall()
        intersection28()
    else:
        direction()
        intersection28()

def intersection27():
    intText()
    answer = input("")
    if answer == "go north":
        intersection23()
    elif answer == "go east":
        intersection22()
    elif answer == "go south":
        intersection28()
    elif answer == "go west":
        intersection26()
    else:
        direction()
        intersection27()

def intersection26():
    intText()
    answer = input("")
    if answer == "go north":
        intersection24()
    elif answer == "go east":
        intersection27()
    elif answer == "go south":
        wall()
        intersection26()
    elif answer == "go west":
        wall()
        intersection26()
    else:
        direction()
        intersection26()

def intersection25():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection25()
    elif answer == "go east":
        room4()
    elif answer == "go south":
        intersection24()
    elif answer == "go west":
        wall()
        intersection25()
    else:
        direction()
        intersection25()

def intersection24():
    intText()
    answer = input("")
    if answer == "go north":
        intersection25()
    elif answer == "go east":
        intersection23()
    elif answer == "go south":
        intersection26()
    elif answer == "go west":
        wall()
        intersection24()
    else:
        direction()
        intersection24()

def intersection23():
    intText()
    answer = input("")
    if answer == "go north":
        room4()
    elif answer == "go east":
        intersection4()
    elif answer == "go south":
        intersection27()
    elif answer == "go west":
        intersection24()
    else:
        direction()
        intersection23()

def intersection22():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection22()
    elif answer == "go east":
        intersection3()
    elif answer == "go south":
        room3()
    elif answer == "go west":
        intersection27()
    else:
        direction()
        intersection22()

def intersection21():
    intText()
    answer = input("")
    if answer == "go north":
        intersection3()
    elif answer == "go east":
        intersection18()
    elif answer == "go south":
        intersection20()
    elif answer == "go west":
        intersection28()
    else:
        direction()
        intersection21()

def intersection20():
    intText()
    answer = input("")
    if answer == "go north":
        intersection21()
    elif answer == "go east":
        intersection19()
    elif answer == "go south":
        wall()
        intersection20()
    elif answer == "go west":
        wall()
        intersection20()
    else:
        direction()
        intersection20()

def intersection19():
    intText()
    answer = input("")
    if answer == "go north":
        intersection18()
    elif answer == "go east":
        intersection16()
    elif answer == "go south":
        wall()
        intersection19()
    elif answer == "go west":
        intersection20()
    else:
        direction()
        intersection19()

def intersection18():
    intText()
    answer = input("")
    if answer == "go north":
        centerMaze()
    elif answer == "go east":
        intersection17()
    elif answer == "go south":
        intersection19()
    elif answer == "go west":
        intersection21()
    else:
        direction()
        intersection21()

def intersection17():
    intText()
    answer = input("")
    if answer == "go north":
        room1()
    elif answer == "go east":
        wall()
        intersection17()
    elif answer == "go south":
        intersection16()
    elif answer == "go west":
        intersection18()
    else:
        direction()
        intersection17()

def intersection16():
    intText()
    answer = input("")
    if answer == "go north":
        intersection17()
    elif answer == "go east":
        intersection15()
    elif answer == "go south":
        wall()
        intersection16()
    elif answer == "go west":
        intersection19()
    else:
        direction()
        intersection16()

def intersection15():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection13()
    elif answer == "go east":
        wall()
        intersection15()
    elif answer == "go south":
        intersection15()
    elif answer == "go west":
        intersection16()
    else:
        direction()
        intersection15()

def intersection13():
    intText()
    answer = input("")
    if answer == "go north":
        intersection12()
    elif answer == "go east":
        wall()
        intersection13()
    elif answer == "go south":
        intersection15()
    elif answer == "go west":
        wall()
        intersection13()
    else:
        direction()
        intersection13()

def intersection12():
    intText()
    answer = input("")
    if answer == "go north":
        intersection10()
    elif answer == "go east":
        room2()
    elif answer == "go south":
        intersection13()
    elif answer == "go west":
        wall()
        intersection12()
    else:
        direction()
        intersection12()

def intersection11():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection11()
    elif answer == "go east":
        wall()
        intersection11()
    elif answer == "go south":
        room2()
    elif answer == "go west":
        intersection10()
    else:
        direction()
        intersection11()

def intersection10():
    intText()
    answer = input("")
    if answer == "go north":
        intersection7()
    elif answer == "go east":
        intersection11()
    elif answer == "go south":
        intersection12()
    elif answer == "go west":
        room1()
    else:
        direction()
        intersection10()

def intersection9():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection9()
    elif answer == "go east":
        wall()
        intersection9()
    elif answer == "go south":
        room6()
    elif answer == "go west":
        intersection8()
    else:
        direction()
        intersection9()

def intersection8():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection8()
    elif answer == "go east":
        intersection9()
    elif answer == "go south":
        intersection7()
    elif answer == "go west":
        wall()
        intersection8()
    else:
        direction()
        intersection8()

def intersection7():
    intText()
    answer = input("")
    if answer == "go north":
        intersection8()
    elif answer == "go east":
        intersection6()
    elif answer == "go south":
        intersection10()
    elif answer == "go west":
        wall()
        intersection7()
    else:
        direction()
        intersection7()

def intersection6():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection6()
    elif answer == "go east":
        intersection7()
    elif answer == "go south":
        intersection2()
    elif answer == "go west":
        intersection5()
    else:
        direction()
        intersection6()

def intersection5():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection5()
    elif answer == "go east":
        wall()
        intersection6()
    elif answer == "go south":
        intersection4()
    elif answer == "go west":
        wall()
        intersection5()
    else:
        direction()
        intersection5()

def intersection4():
    intText()
    answer = input("")
    if answer == "go north":
        intersection5()
    elif answer == "go east":
        wall()
        intersection4()
    elif answer == "go south":
        intersection3()
    elif answer == "go west":
        intersection23()
    else:
        direction()
        intersection4()

def intersection3():
    intText()
    answer = input("")
    if answer == "go north":
        intersection4()
    elif answer == "go east":
        centerMaze()
    elif answer == "go south":
        intersection21()
    elif answer == "go west":
        intersection22()
    else:
        direction()
        intersection3()

def intersection2():
    intText()
    answer = input("")
    if answer == "go north":
        intersection6()
    elif answer == "go east":
        wall()
        intersection2()
    elif answer == "go south":
        room1()
    elif answer == "go west":
        intersection1()
    else:
        direction()
        intersection2()

def intersection1():
    intText()
    answer = input("")
    if answer == "go north":
        wall()
        intersection1()
    elif answer == "go east":
        intersection2()
    elif answer == "go south":
        centerMaze()
    elif answer == "go west":
        wall()
        intersection1()
    else:
        direction()
        intersection1()

def intText():
    print("You are deep in the maze.\nEverything looks the same")

def direction():
    print("You cannot go in that direction.")

def wall():
    print("There is a wall in the way.")
    time.sleep(0.5)

def mazeCenter1():
    print("You descend a flight of stairs until you reach a large round room.\nIn the center is what appears to be an altar with four gem shaped holes in the top.\nOn the side a sign reads:\nWelcome to the Middle of the Maze.")
    time.sleep(2.5)
    print("You hear the door slam shut behind you, and, after inspection, you can see no way of opening it for now.")
    print("There are exits leading off in all directions from this room.")
    time.sleep(1)
    print("\nNote: From now you will not be prompted when moving.\nSimply type 'go' and then the direction you would like to go in (North, East, South, West).")
    answer = input("You will be told if there is something blocking your path.\n").lower()
    if answer == "go north":
        intersection1()
    elif answer == "go south":
        intersection18()
    elif answer == "go east":
        room1()
    elif answer == "go west":
        intersection3()
    else:
        direction()
        centerMaze()

def check():
    global n
    if len(inventory) == 0:
        print("There is nothing in your inventory yet.")
        time.sleep(1)
    else:
        print("The items currently in your inventory are:")
        for i in range(0, len(inventory)):
            print(inventory[n])
            n += 1
            time.sleep(0.1)
        time.sleep(1.5)
        n = 0

def paintings():
    print("Type 1 for the painting of the old man.")
    print("Type 2 for the painting of the fruit.")
    print("Type 3 for the painting of the jewels.")
    answer = input("Type 4 to go back.\n")
    if answer == "1":
        print("You lift the painting off the wall to reveal a locked safe.")
        if "Silver Key" in inventory:
            answer = input("Use Silver Key to unlock the safe?\n")
            if answer == "yes":
                print("The safe is empty apart from a dead fly.")
                time.sleep(1)
                paintings()
            else:
                print("Come back later when you would like to unlock the safe.")
                time.sleep(1)
                paintings()
        else:
            print("This safe needs the Silver Key to be unlocked.\nCome back later when you have the Silver Key.")
            time.sleep(1)
            paintings()
    elif answer == "2":
        print("You can see nothing of interest about this painting.")
        time.sleep(2)
        paintings()
    elif answer == "3":
        print("The painting lifts off the wall to show a locked safe.")
        if "Bronze Key" in inventory:
            answer = input("Unlock with the Bronze Key?\n")
            if answer == "yes":
                print("You can just make out four numbers scratched into the wall of the safe...")
                time.sleep(1)
                print("...",rCode[0],"...")
                time.sleep(1)
                print("...",rCode[1],"...")
                time.sleep(1)
                print("...",rCode[2],"...")
                time.sleep(1)
                print("...",rCode[3],"...")
                time.sleep(1.5)
                paintings()
            else:
                print("Come back later when you would like to unlock the safe.")
                time.sleep(1)
                paintings()
        else:
            print("This safe requires the Bronze Key to be unlocked.\nCome back later when you have the Bronze Key.")
            time.sleep(1)
            paintings()
    elif answer == "4":
        insideHouse()
    elif answer == "inventory":
        check()
        paintings()
    else:
        print("Invalid Action.")
        paintings()

def toolbox():
    global count
    print("The toolbox appears to have two compartments.")
    answer = input("Compartment 1 or 2 or Go Back?\n").lower()
    if answer == "compartment 1" or answer == "1":
        print("This compartment is empty...")
        time.sleep(1)
        toolbox()
    elif answer == "compartment 2" or answer == "2":
        if "Silver Key" in inventory:
            print("This compartment is empty")
        else:
            print("You find a key. It is the Silver Key.")
            answer = input("Pick up key?\n").lower()
            if answer == "yes":
                print("Adding Silver Key to inventory...")
                time.sleep(0.5)
                inventory.append("Silver Key")
                toolbox()
            elif answer == "no":
                toolbox()
    elif answer == "go back":
        outbuilding()
    elif answer == "inventory":
        check()
        toolbox()
    else:
        print("Invalid Action.")
        toolbox()
    outbuilding()

def codeRetry():
    print("Incorrect code.")
    answer = input("Try again or Go Back?\n").lower()
    if answer == "go back":
        outbuilding()
    elif answer == "try again":
        codeDoorLock()
    elif answer == "inventory":
        check()
        codeRetry()
    else:
        print("Invalid Action.")
        codeRetry()

def codeDoorLock():
    print("The door is locked with a code lock.")
    code = input("Please enter the code.\n")
    if code == rCode:
        print("Access granted")
        print("Entering the dungeon...")
        time.sleep(1)
        mazeCenter1()
    else:
        codeRetry()

def outbuilding():
    answer = input("Inside the outbuilding, there is a large toolbox on top of a rotten wooden workbench.\nNext to the bench is a white door.\nOpen Door or Inspect Toolbox or Go Back?\n").lower()
    if answer == "open door":
        codeDoorLock()
    elif answer == "inspect toolbox":
        toolbox()
    elif answer == "go back":
        garden()
    elif answer == "inventory":
        check()
        outbuilding()
    else:
        print("Invalid Action.")
        outbuilding()

def vegPatchT():
    if "Gold Key" in inventory:
        answer = input("The grating is locked.\nUnlock with the Gold Key?\n").lower()
        if answer == "yes":
            print("You climb down the ladder into the darkness...")
            time.sleep(2)
            endGame()
        elif answer == "no":
            print("Come back later when you would like to unlcok the grating.")
            time.sleep(0.5)
            garden()
        elif answer == "inventory":
            check()
            vegPatchT()
        else:
            vegPatchT()
    else:
        print("The grating is still locked and you do not have the Gold Key.\nCome back later when you have the key...")
        time.sleep(1)
        garden()

def vegPatch():
    global vegPatchSearch
    if "Bronze Key" not in inventory:
        answer = input("Searching through the weed-filled soil, you see something glint in the sunlight. It turns out to be an ornate key.\nIt is the Bronze Key.\nKeep Key or Discard Key?\n").lower()
        if answer == "keep key":
            print("Adding Bronze Key to inventory...")
            time.sleep(0.5)
            inventory.append("Bronze Key")
        elif answer == "discard key":
            garden()
        elif answer == "inventory":
            check()
            vegPatch()
        else:
            print("Invalid action.")
            vegPatch()
        print("Then you unearth a metal grating, through which you can see a ladder leading into darkness.\nThe grating is locked.")
        print("The Gold Key is required to unlock the grating. Come back later when you have it.")
        time.sleep(2)
        garden()
    else:
        vegPatchT()

def main():
    answer = input("Enter House or Enter Garden?\n").lower()
    if answer == "enter house":
        insideHouse()
    elif answer == "enter garden":
        garden()
    elif answer == "inventory":
        check()
        main()
    else:
        print("Invalid action.")
        main()

def insideHouse():
    print("There are few furnishings in the house. A large wooden table fills the floor space and three paintings adorn the walls.\nOne depicts an old man, the other a large bowl of fruit and the final one a treasure chest filled with precious jewels.")
    answer = input("Inspect Table or Inspect Paintings or Go Back?\n").lower()
    if answer == "inspect table":
        print("There is nothing special about the table.")
        time.sleep(1)
        insideHouse()
    elif answer == "inspect paintings":
        paintings()
    elif answer == "go back":
        main()
    elif answer == "inventory":
        check()
        insideHouse()
    else:
        print("Invalid Action.")
        insideHouse()


def garden():
    answer = input("You are in a small garden with a vegetable patch as well as a rundown outbuilding.\nSearch Veg Patch or Enter Outbuilding or Go Back?\n").lower()
    if answer == "go back":
        main()
    elif answer == "enter outbuilding":
        outbuilding()
    elif answer == "search veg patch":
        vegPatch()
    elif answer == "inventory":
        check()
        garden()
    else:
        print("Invalid action.")
        garden()

def seeHouse():
    print("In your hand, you hold a letter which reads:\n")
    time.sleep(1)
    print("""Welcome to Adventure!
Created by iAlphaRaptor
Throughout this game, you will find many challenges and puzzles.
You must complete all these challenges and make your way to the End Room.
There, you will find the Final Test which will test your strength, intellingence and speed.

Good Luck!""")
    time.sleep(2)
    print("You can see a one-roomed shack with a small garden next to it.")
    answer = input("Enter house or Enter Garden?\n")
    if answer == "enter house":
        insideHouse()
    elif answer == "enter garden":
        garden()
    elif answer == "inventory":
        check()
        main()
    else:
        print("Invalid action.")
        seeHouse()



def loadError():
    print("There is an error with the load function in the progress module.")
    print("Uh Oh!")

seeHouse()
