def treasure_island_game():
    print("Welcome to the treasure island game!")
    print("Your mission is to find the treasure!")

    a=input("You are at cross road, where do you want to go? Type 'left' or 'right'\n")
    if a=='left':
        b=input("You are come at the lake, There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across?\n")
        if b=='wait':
            c=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
            if c=='yellow':
                print("Congratulations!You got the treasure, you won the game!")
            elif c=='red':
                print("You selected the wrong door, you come into the fire lake, and you will be die in few minutes, you lose the game!")
            elif c=='blue':
                print("You selected the wrong door, you killed by the zoombie, you lose the game!")
            else:
                print("Sorry! you entered the wrong door name!")
        elif b=='swim':
            print("Oops! this water is ruined by the all harmfull chemicals and it will affect to my body and i will be die in few minutes, you lose the game!")
        else:
            print("Sorry! you entered the wrong option!")
    elif a=='right':
        print("Oops! you selected the wrong direction, you will be killed, you lose the game!")
    else:
        print("Sorry! you entered the wrong direction!")
treasure_island_game()
