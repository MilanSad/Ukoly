size = 6
board = [[0 for x in range(size)] for _ in range(size)]

x_pozition = (int(input("Enter start pozition row (1 -6):  "))) -1
y_pozition = (int(input("Enter start pozition column(1-6):  "))) - 1

board[x_pozition][y_pozition] = 1

"""if move(x_pozition, y_pozition, board, move_count=1):
    print("Solution:")
    print_board(board)
else:
    print("No solution"""


def move(x_pozition, y_pozition, board, move_count):
    if move_count == len(board) * len(board[0]):
        return True

    valid_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 1], [-1, -1]]

    for move in valid_moves:

        x_new = x_pozition + move[0]
        y_new = y_pozition + move[1]

        if valid_stay(x_new, y_new, board):
            board[x_new][x_new] = move_count + 1
            if move(x_new, y_new, board, move_count + 1):
                return True
            board[x_new][y_new] = 0

    return False


print(board)
print()
for i in board:
    for j in i:
        print(j, end=" ")
    print()


print(len(board) * len(board[0]))

valid_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 1], [-1, -1]]
x_poz = 1
y_poz = 1
for moves in valid_moves:
    x_new = x_poz + moves[0]
    y_new = y_poz + moves[1]
    print(x_new, y_new)

    print()

print(len(board))
print(len(board[0]))
move_x = 7
move_y = 3
if 0 <= move_x <= len(board) and 0 <= move_y <= len(board[0]) and board[move_x][move_y] == 0:
    print("yes")