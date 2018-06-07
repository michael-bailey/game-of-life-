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

def computer():
    counters = 12
    turn = "player"
    pastCount = 0

    while counters > 0:
        print("------")
        print("number of counters remaining",counters)
        print("------")
        if turn == "player":
            count = int(input("enter a number to take : "))

            counters = counters - count
            turn = "computer"

        elif turn == "computer":
            print("computer takes",(4 - count))
            counters = counters - (4 - count)
            turn = "player"
    
    if turn == "player":
        print("computer wins")
        print()
    if turn == "computer":
            print("my algorithm is wrong")

def players():
    counters = 12
    turn = "player1"

    while counters > 0:
        print("------")
        print("number of counters remaining",counters)
        print("------")
        if turn == "player1":
            count = int(input("player1 enter a number to take : "))

            counters = counters - count
            turn = "player2"

        elif turn == "player2":
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
    print()
            

option = 0
try:

    while option != 4:
        option = Menu()
        if option == 1:
            computer()
        if option == 2:
            players()
        if option == 3:
            helpBook()
except:
    print()
    print("##################")
    print("# ending program #")
    print("##################")