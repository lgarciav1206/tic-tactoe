def tic_tac_toe():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def table():
        print("        |       |     ")
        print("   ", a[1], " | ", a[2], " | ", a[3])
        print("________|_______|_______")
        print("        |       |     ")
        print("   ", a[4], " | ", a[5], " | ", a[6])
        print("________|_______|_______")
        print("        |       |     ")
        print("   ", a[7], " | ", a[8], " | ", a[9])
        print("        |       |     ")

    def X1():
        b = input("Player 1 Choose Square: ")
        if b == "1": a[1] = "X"
        elif b == "2": a[2] = "X"
        elif b == "3": a[3] = "X"
        elif b == "4": a[4] = "X"
        elif b == "5": a[5] = "X"
        elif b == "6": a[6] = "X"
        elif b == "7": a[7] = "X"
        elif b == "8": a[8] = "X"
        elif b == "9": a[9] = "X"
        else: print("INVALID ENTRY, enter number: ")
        table()

    def X2():
        b = input("Player 2 Choose Square: ")
        if b == "1": a[1] = "X"
        elif b == "2": a[2] = "X"
        elif b == "3": a[3] = "X"
        elif b == "4": a[4] = "X"
        elif b == "5": a[5] = "X"
        elif b == "6": a[6] = "X"
        elif b == "7": a[7] = "X"
        elif b == "8": a[8] = "X"
        elif b == "9": a[9] = "X"
        else: print("INVALID ENTRY, enter number: ")
        table()

    def O1():
        b = input("Player 1 Choose Square: ")
        if b == "1": a[1] = "O"
        elif b == "2": a[2] = "O"
        elif b == "3": a[3] = "O"
        elif b == "4": a[4] = "O"
        elif b == "5": a[5] = "O"
        elif b == "6": a[6] = "O"
        elif b == "7": a[7] = "O"
        elif b == "8": a[8] = "O"
        elif b == "9": a[9] = "O"
        else: print("INVALID ENTRY, enter number: ")
        table()

    def O2():
        b = input("Player 2 Choose Square: ")
        if b == "1": a[1] = "O"
        elif b == "2": a[2] = "O"
        elif b == "3": a[3] = "O"
        elif b == "4": a[4] = "O"
        elif b == "5": a[5] = "O"
        elif b == "6": a[6] = "O"
        elif b == "7": a[7] = "O"
        elif b == "8": a[8] = "O"
        elif b == "9": a[9] = "O"
        else: print("INVALID ENTRY, enter number: ")
        table()

    table()
    while True:
        p1 = input("player 1 choose: 1 for X or 2 for 0: ")
        p2 = input("player 2 choose: 1 for X or 2 for 0: ")
        if p1 == p2:
            print("INVALID ENTRY, both players chose the same option")
        elif p1 == "1" and p2 == "2" or p1 == "2" and p2 == "1":
            break
        else:
            print("INVALID ENTRY, Choose 1 or 2")

    def mark1(p1):
        while True:
            if p1 == "1": X1()
            elif p1 == "2": O1()
            if a[1] == a[2] == a[3] or a[1] == a[4] == a[7] or a[1] == a[5] == a[9] or a[5] == a[2] == a[8] or a[3] == a[5] == a[7] or a[3] == a[6] == a[9] or a[4] == a[5] == a[6]:
                print("PLAYER 1 WIN'S!!")
                break

    def mark2(p2):
        while True:
            if p2 == "1": X2()
            elif p2 == "2": O2()
            if a[1] == a[2] == a[3] or a[1] == a[4] == a[7] or a[1] == a[5] == a[9] or a[5] == a[2] == a[8] or a[3] == a[5] == a[7] or a[3] == a[6] == a[9] or a[4] == a[5] == a[6]:
                print("PLAYER 2 WIN'S!!")
                break

    mark1(p1)
    mark2(p2)

    restart = input("Do you want to play again, choose Yes or No: ")
    if restart == "yes" or restart == "Yes":
        tic_tac_toe()
    elif restart == "no" or restart == "No":
        print("Thanks for playing!")
    else:
        restart = input("INVALID ENTRY, choose Yes or No: ")
        if restart == "yes" or restart == "Yes":
            tic_tac_toe()
        elif restart == "no" or restart == "No":
            print("Thanks for playing!")


tic_tac_toe()
