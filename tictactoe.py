board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def game():
    count = 0
    x = 1
    y = 2
    print_board()
    while count < 9:
        if count % 2 == 0:
            p = int(input(f"Select one of the free Fields on the Board, player {x} \n"))
        else:
            p = int(input(f"Select one of the free Fields on the Board, player {y} \n"))
        if p < 9:
            if board[p] == "-" and count % 2 == 0:#player1
                board[p] = "O"
                print_board()
                count += 1
                if checkwin():
                     print("P1 won")
                     break
            elif board[p] == "-" and count % 2 == 1: #player2
                board[p] = "X"
                print_board()
                count += 1
                if checkwin():
                     print("P2 won")
                     break
        else:
            p = input("That field is taken or does not exist, try again \n")
    if count == 9:
         print("Looks like a draw")
def print_board():
    for i in range(0, 9, 3):  
        print(board[i], board[i+1], board[i+2])

def checkwin():
     for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == "O":  # Check row win for "O"
            return True
        if board[i] == board[i+1] == board[i+2] == "X":  # Check row win for "X"
            return True
    
    # Check columns
     for i in range(3):
        if board[i] == board[i+3] == board[i+6] == "O":  # Check column win for "O"
            return True
        if board[i] == board[i+3] == board[i+6] == "X":  # Check column win for "X"
            return True

    # Check diagonals
     if board[0] == board[4] == board[8] == "O":  # Check diagonal win for "O"
        return True
     if board[0] == board[4] == board[8] == "X":  # Check diagonal win for "X"
        return True
     if board[2] == board[4] == board[6] == "O":  # Check diagonal win for "O"
        return True
     if board[2] == board[4] == board[6] == "X":  # Check diagonal win for "X"
        return True

     return False
    

game()
        



