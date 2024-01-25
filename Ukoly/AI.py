def find_path(board, row, col):
    if row < 0 or row >= 6 or col < 0 or col >= 6 or board[row][col] != 0:
        return False

    # Mark the current square as visited
    board[row][col] = 1

    # Check for valid moves from the current square
    valid_moves = [(row + 2, col + 1), (row + 2, col - 1), (row + 1, col + 2), (row + 1, col - 2), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col + 2), (row - 1, col - 2)]
    for move in valid_moves:
        if find_path(board, move[0], move[1]):
            # If a valid path is found, return True
            return True

    # No valid path found from the current square
    board[row][col] = 0
    return False

def print_board(board):
    for row in range(6):
        for col in range(6):
            print(board[row][col], end=" ")
        print()

# Initialize the chessboard with all squares as 0 (unvisited)
board = [[0 for col in range(6)] for row in range(6)]

# Get the starting coordinates from the user
row = int(input("Enter the row index of the starting square: "))
col = int(input("Enter the column index of the starting square: "))

# Find a path for the knight starting from the given coordinates
if find_path(board, row, col):
    print("A valid knight's path has been found:")
    print_board(board)
else:
    print("No valid knight's path could be found.")
