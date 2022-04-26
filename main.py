from random import randint

board = [] # creates an array

for x in range(8):
    board.append(["O"] * 8) # *8 is the amount of rows; can be changed to make a bigger game board

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Let's play Battleship!")
print_board(board) # appends the info into the console

def random_row(board):
    return randint(0, len(board) - 1) # chooses a random row on the game board
def random_col(board):
    return randint(0, len(board[0]) - 3) # chooses random column; it is -3 to prevent the ship from having a spot assigned off the gaem board

ship1_row = random_row(board) # utilizes function defined above to choose a randomized row on gameboard
ship1_col = random_col(board) # utilizes function defined above to choose a randomized column on gameboard
ship1_col2 = ship1_col + 1 #chooses a location directly next to the first location
ship1_locat1 = (ship1_row, ship1_col)
ship1_locat2 = (ship1_row, ship1_col2)

battleship1 = False # boolean to determine if half the ship has been sunk or not
battleship2 = False # boolean to see if other half
sunk1 = False# boolean to see if battleship sunk

ship2_row = random_row(board)
ship2_col = random_col(board)
ship2_col2 = ship2_col + 1
ship2_col3 = ship2_col+ 2
ship2_locat = (ship2_row, ship2_col) #portion of ship & its coordinates are assigned to variables
ship2_locat2 = (ship2_row, ship2_col2)
ship2_locat3 = (ship2_row, ship2_col3)

carrier1 = False # check to see if portion of ship is sunk
carrier2 = False
carrier3 = False
sunk2 = False # boolean to determine if the ship has been sunk or not


if ship1_locat1 == ship2_locat or ship1_locat2 == ship2_locat or ship1_locat1 == ship2_locat2 or ship1_locat2 == ship2_locat2 or ship1_locat1 == ship2_locat3 or ship1_locat1 == ship2_locat3:  #rerolls the location of ship one when the locations are exactly the same
    print("Ship location rerolled")
    ship1_row = random_row(board)  # utilizes function defined above to choose a randomized row on gameboard
    ship1_col = random_col(board)  # utilizes function defined above to choose a randomized column on gameboard
    ship1_col2 = ship1_col + 1
    ship1_locat1 = (ship1_row, ship1_col)
    ship1_locat2 = (ship1_row, ship1_col2)

#guess mechanism
for turn in range(99):
    print ("Turn", turn + 1) # the "+1" is so there is no "Turn 0"
    guess_row = int(input("Guess Row: ")) #value is inputted as one coordinate for row
    guess_row -= 1 # to make it less confusing for the user; there is now no confusion about a "Row 0"
    guess_col = int(input("Guess Col: ")) #value for coordinate of column
    guess_col -= 1 # to make it less confusing for the user; there is now no confusion about a "Col 0"

#half ship if statement group 1
    if guess_row == ship1_row and guess_col == ship1_col: # if both coordinates are correct, so and so happens
        if board[guess_row][guess_col] == "*":  # this is to check to see if its been found and the player guesses the same spot
            if guess_row == ship1_row and guess_col == ship1_col:
                print("Don't beat a dead horse!")
                print_board(board)
        else:
            print("Hit!")
            battleship1 = True # indicates half the battleship has been found
            board[guess_row][guess_col] = "*" #different marker to show a correct guess opposed to an incorrect one
            print_board(board)
            if battleship1 == True and battleship2  == True: #if both halves of the ship were found, do this
                print("You sunk my battleship!")
                sunk1 = True # ship has been marked as sunk
            else:
                print("next turn")

#half ship if statement group 2
    elif guess_row == ship1_row and guess_col == ship1_col2: # if both coordinates are correct, so and so happens
        if board[guess_row][guess_col] == "*":  # this is to check to see if its been found and the player guesses the same spot
            if guess_row == ship1_row and guess_col == ship1_col2:
                print("Don't beat a dead horse!")
                print_board(board)
        else:
            print("Hit!")
            battleship2 = True # indicates half the battleship has been found
            board[guess_row][guess_col] = "*" #different marker to show a correct guess opposed to an incorrect one
            print_board(board)
            if battleship1 == True and battleship2  == True: #if both halves of the ship were found, do this
                print("You sunk my battleship!")
                sunk1 = True  # ship has been marked as sunk
            else:
                print("Next Turn!")
#1/3 ship2 if statement
    elif guess_row == ship2_row and guess_col == ship2_col: # if both coordinates are correct, so and so happens
        if board[guess_row][guess_col] == "*":  # this is to check to see if its been found and the player guesses the same spot
            if guess_row == ship2_row and guess_col == ship2_col:
                print("Don't beat a dead horse!")
                print_board(board)
        else:
            print("Hit!")
            carrier1 = True # indicates the carrier has been found
            board[guess_row][guess_col] = "*"
            print_board(board)
            if carrier1 == True and carrier2 == True and carrier3 == True:
                print("You sunk my carrier!")
                sunk2 = True
            else:
                print("Next Turn!")

#2/3 ship2 if statement
    elif guess_row == ship2_row and guess_col == ship2_col2: # if both coordinates are correct, so and so happens
        if board[guess_row][guess_col] == "*":  # this is to check to see if its been found and the player guesses the same spot
            if guess_row == ship2_row and guess_col == ship2_col2:
                print("Don't beat a dead horse!")
                print_board(board)
        else:
            print("Hit!")
            carrier2 = True # indicates the carrier has been found
            board[guess_row][guess_col] = "*"
            print_board(board)
            if carrier1 == True and carrier2 == True and carrier3 == True:
                print("You sunk my carrier!")
                sunk2 = True
            else:
                print("Next Turn!")

 #3/3 ship2 if statement
    elif guess_row == ship2_row and guess_col == ship2_col3: # if both coordinates are correct, so and so happens
        if board[guess_row][guess_col] == "*":  # this is to check to see if its been found and the player guesses the same spot
            if guess_row == ship2_row and guess_col == ship2_col3:
                print("Don't beat a dead horse!")
                print_board(board)
        else:
            print("Hit!")
            carrier3 = True # indicates the carrier has been found
            board[guess_row][guess_col] = "*" #indicates a spot where a hit was acheived
            print_board(board)
            if carrier1 == True and carrier2 == True and carrier3 == True:
                print("You sunk my carrier!")
                sunk2 = True
            else:
                print("Next Turn!")

    else:
        if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 8): #if the player doesn't choose a coordinate on the board
            print("Oops, that's not even in the ocean.")
            print_board(board)
        elif(board[guess_row][guess_col] == "X"): #checks to see if player has already guessed this spot
            print("You guessed that one already.")
            print_board(board) #reprints board
        else:
            print("Haha, you suck!")
            board[guess_row][guess_col] = "X" # when the player guesses incorrectly, it replaces the 'O' with an 'X' to indicate its been guessed
            print_board(board)

    if sunk1 == True and sunk2 == True: #if statement to check if both ships have been found
        print("You Win! It only took you ", turn + 1, " shots to beat me!")
        break
    turn =+ 1 #after guess is made, turn counter adds one.