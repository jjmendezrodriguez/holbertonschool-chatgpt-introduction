#!/usr/bin/env python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check horizontal lines
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check vertical lines
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 2:
                return value
            else:
                print("Input out of bounds. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and not is_full(board):
        print_board(board)
        print("Player " + player + "'s turn.")
        row = get_int_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_int_input("Enter column (0, 1, or 2) for player " + player + ": ")
        if board[row][col] == " ":
            board[row][col] = player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if check_winner(board):
        print("Player " + ("O" if player == "X" else "X") + " wins!")
    else:
        print("The game is a tie!")

tic_tac_toe()
