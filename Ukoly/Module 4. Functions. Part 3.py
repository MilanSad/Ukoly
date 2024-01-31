
print("---------------Task 1 ---------------")
"""
Task 1
Write a recursive function for finding the greatest common
divisor of two integers.
"""
# Tady jsem si dal, pul soboty jsem se trápil... chatGPT mi dal ještě lepší, ale vygoogloval jsem tento výpočet 
"""def number_find(num1,num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 == num2:
        return num1
    elif num1 > num2:
        return number_find((num1 - num2), num2)
    elif num1 < num2:
        return number_find((num2 - num1), num1)
    
print(number_find(36,48))
"""
print("---------------Task 2 ---------------")
"""Task 2
Develop a game of Bulls and Cows. The program chooses
a four-digit number, and the player has to guess it. After
the user enters a number, the program reports how many digits of
the number are guessed (bulls), and how many digits are guessed
and stand in the right place (cows). After guessing the number,
print the number of user’s attempts. Use recursion in your game.
"""
"""
import random 

number = (random.randrange(1000,10000))
print (number)

attempts = 0
number = str(number)

def guess_number_input():
  while True:
    guess_number = input(("Insert your number (4 digit):"))
    if guess_number.isdigit() and len(guess_number) == 4:
      return guess_number
    else:
      print("Insert 4 digit number!")

def search_number(number, guess_number):
    j = 0
    bulls = 0
    cows = 0
    for i in guess_number:
        if i in number:
            bulls += 1
    for i in guess_number:
        if i == number[j]:
           cows +=1
        j += 1
    print (f"Bulls: {bulls} Cow: {cows}")
    if cows != 4:
        global attempts
        attempts += 1
        search_number(number, guess_number_input(),)
    return attempts

guess_number_input()
search_number(number, guess_number_input())  
print(f"Great, you have {attempts} attempts")
"""

print("---------------Task 2 ---------------")
"""
Task 3
There are an 8×8 chessboard and a knight. The program
should request the coordinates of the square from the user
and put the knight there. The program’s objective is to find
the knight’s path that allows it to go through the entire chessboard
while stepping on each square only once. (Since the process
of finding a path for initial squares can take a long time,
we recommend you to begin with a 6×6 chessboard). Use
recursion in your game.

"""


def start_square(size):
    board = [[0 for x in range(size)] for _ in range(size)]
    x_position = int(input("Enter start position row (1 -6):  ")) - 1
    y_position = int(input("Enter start position column(1-6):  ")) - 1
    board[x_position][y_position] = 1

    if move(x_position, y_position, board, move_count=1):
        print("Solution:")
        print_board(board)
    else:
        print("No solution")


def move(x_pos, y_pos, board, move_count):
    if move_count == len(board) * len(board[0]):
        return True

    valid_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

    for moves in valid_moves:
        x_new = x_pos + moves[0]
        y_new = y_pos + moves[1]
        if not valid_stay(x_new, y_new, board):
            continue

        board[x_new][y_new] = move_count + 1
        if move(x_new, y_new, board, move_count + 1):
            return True
        board[x_new][y_new] = 0

    return False


def valid_stay(move_x, move_y, board):
    if 0 <= move_x < len(board) and 0 <= move_y < len(board[0]):
        if board[move_x][move_y] == 0:
            return True


def print_board(board):
    for i in board:
        for j in i:
            if j < 10:
                print(f" {j}", end=" ")
            else:
                print(j, end=" ")
        print()


size_board = 6
start_square(size_board)

