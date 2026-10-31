##################################################
# Student Name: Augie Krueger                    #
# Course: CS2                                    #
# Date: September 30, 2026                       #
# Project: Tic Tac Toe                           #
##################################################

import random

board = [
         [" "," "," "],
         [" "," "," "],
         [" "," "," "]
    ]
def display_board(board):
    '''
    Summary: displays the current board

    Paramaters: takes the current board

    Output: prints the current board
    '''
    for row in board:
        print(" | ".join(row))
        print("---------")
def check_winner(board):
    '''
    Summary: checks if a player has three in a row than returns true or false

    Paramaters: current board state

    Output: returns true or false
    '''
    for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":                                                                #checks if any of the columns have three of the same charecter in a row that isnt a space
                return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":                                                                    #checks if any of the rows have threen of the same charecter in a row that isn't a space
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":                                                                        #checks diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":                                                                        #checks diagonal
        return True
def main_game():
    game_mode = input("would you like to play against a friend or a bot. Answer friend for friend, and bot for bot  ")
    if game_mode == "friend":
        curr_player = "x"
        moves_counter = 0
        while True: 
            try:
                if moves_counter == 9:
                    print("tie")
                    break
                elif curr_player == "x":
                    move = int(input("player 1 where would you like to go? answer 1-9:  "))
                    value = move - 1                                                                                            #moves the input from 1-9 to 0-8
                    row = value // 3                                                                                            #sets the row value to the remainder after dividing by three rounded down
                    column = value % 3                                                                                          #sets the column value to remainder after dividing by three
                    if board[row][column] == " ":                                                                               #if the square is empty you can move there otherwise you can't
                        board[row][column] = "x"
                        display_board(board)
                        moves_counter += 1
                        check_winner(board)
                        if check_winner(board) == True:
                                    print(f"{curr_player} won")
                                    break
                        curr_player = "o"
                    elif board[row][colum] == "x" or "o":
                        print("that square is already occupied")
                elif curr_player == "o":
                    move = int(input("player 2 where would you like to go? answer 1-9:  "))
                    value = move - 1
                    row = value // 3
                    column = value % 3
                    if board[row][column] == " ":
                        board[row][column] = "o"
                        display_board(board)
                        moves_counter += 1
                        check_winner(board)
                        if check_winner(board) == True:
                                    print(f"{curr_player} won")
                                    break
                        curr_player = "x"
                    elif board[row][colum] == "x" or "o":
                        print("that square is already occupied")
            except ValueError:
                print("please input a number 1-9")
            except IndexError:
                        print("please input a number 1-9")
    elif game_mode == "bot":
        curr_player = "x"
        moves_counter = 0
        while True: 
            try:
                if moves_counter == 9:
                    print("tie")
                    break
            
                elif curr_player == "x":
                    move = int(input("player 1 where would you like to go? answer 1-9:  "))
                    value = move - 1
                    row = value // 3
                    colum = value % 3 
                    
                    if board[row][colum] == " ":
                        board[row][colum] = "x"
                        display_board(board)
                        moves_counter += 1
                        check_winner(board)
                        if check_winner(board) == True:
                                    print(f"{curr_player} won")
                                    break
                        curr_player = "o"

                    elif board[row][colum] == "x" or "o":
                        print("that square is already occupied")

                elif curr_player == "o":
                    move = random.randint(1,9)
                    value = move - 1
                    row = value // 3
                    colum = value % 3
                    
                    if board[row][colum] == " ":
                        board[row][colum] = "o"
                        display_board(board)
                        moves_counter += 1
                        check_winner(board)
                        if check_winner(board) == True:
                                    print(f"{curr_player} won")
                                    break
                        curr_player = "x"
                    
                    elif board[row][colum] == "x" or "o":
                        pass

            except ValueError:
                print("please input a number 1-9")
            
            except IndexError:
                        print("please input a number 1-9")
    
    
    else:
         print("please answer with friend or bot")

main_game()