import random

def print_board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-----")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-----")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def tictactoe():
    # Initialize game state
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]

    # Choose whether the player or the computer goes first
    choice = input("Would you like to go first? (y/n) ")
    if choice == "y":
        human_player = players[0]
        computer_player = players[1]
    else:
        human_player = players[1]
        computer_player = players[0]
        # Computer plays first move
        row, col = random.randint(0, 2), random.randint(0, 2)
        board[row][col] = computer_player
        current_player = human_player

    # Play game
    while True:
        # Print board
        print_board(board)

        # Get player input or have the computer make a move
        if current_player == human_player:
            while True:
                row = int(input("Enter row (0-2) for " + current_player + ": "))
                col = int(input("Enter column (0-2) for " + current_player + ": "))
                if board[row][col] == " ":
                    break
                else:
                    print("That spot is already taken. Try again.")
        else:
            # Choose a random move for the computer
            while True:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if board[row][col] == " ":
                    break
            print("Computer chooses row " + str(row) + ", column " + str(col) + ".")
        
        # Update board
        board[row][col] = current_player

        # Check for win
        if check_win(board, current_player):
            print_board(board)
            if current_player == human_player:
                print("You win!")
            else:
                print("Computer wins!")
            break

        # Check for tie
        tie = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    tie = False
        if tie:
            print_board(board)
            print("Tie game.")


            # Switch players
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]
    
tictactoe()
