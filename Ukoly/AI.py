def start_square(size):
    board = [[0 for x in range(size)] for _ in range(size)]
    x_position = int(input("Enter start position row (1 - 6):  ")) - 1
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

    valid_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 1], [-1, -1]]

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
    if 0 <= move_x < len(board) and 0 <= move_y < len(board[0]) and board[move_x][move_y] == 0:
        return True

def print_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

size_board = 6
start_square(size_board)