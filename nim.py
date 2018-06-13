def Menu():
    print("enter an option :")
    print("1. play against computer")
    print("2. play against another person")
    print("3. help (not implemented)")
    print("4. exit")
    print()
    try:
        x = int(input("enter option number : "))
        if x < 1 or x > 4:
            raise ValueError
        return x
    except ValueError as e:
        print("the input wasnt an intager or a valid option please try again")
        print()
        return Menu()

def computer(counter_num, player):
    counters = counter_num
    if player.upper() == "C":
        turn = "computer"
    else:
        turn = "player"
    pastCount = 0

    while counters > 0:
        print("------")
        print("number of counters remaining",counters)
        print("------")
        if turn == "player":
            count = 0
            while not (count < 4 and count > 0):
                count = int(input("enter a number to take : "))

            counters = counters - count
            turn = "computer"

        elif turn == "computer":
            if counters % 4 == 0:
                print("computer takes",(4 - count))
                counters = counters - (4 - count)
                turn = "player"
            else:
                print("computer takes",((counters % 4)))
                counters = counters - (counters % 4) 
                turn = "player"
                
    
    if turn == "player":
        print("computer wins")
        print()
    if turn == "computer":
            print("my algorithm is wrong")

def players(counter_num):
    counters = counter_num
    turn = "player1"

    while counters > 0:
        print("------")
        print("number of counters remaining",counters)
        print("------")
        if turn == "player1":
            count = 0
            while not (count < 4 and count > 0):
                count = int(input("player1 enter a number to take : "))

            counters = counters - count
            turn = "player2"

        elif turn == "player2":
            count = 0
            while not (count < 4 and count > 0):
                count = int(input("player2 enter a number to take : "))

            counters = counters - count
            turn = "player2"
    
    if turn == "player1":
        print("player2 wins wins")
        print()
    if turn == "player2":
        print("player1 wins")
        print()

def helpBook():
    for i in (open("nim-help.txt","r").readlines()):
        print(i)
            

option = 0
try:

    while option != 4:
        option = Menu()
        if option == 1:
            computer(int(input("enter number of counters : ")),input("who starts C or P : "))
        if option == 2:
            players(int(input("enter number of counters : ")))
        if option == 3:
            helpBook()
except Exception as e:
    print()
    print("##################")
    print("# ending program #")
    print("##################")
    print(e.value)