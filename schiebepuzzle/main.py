# Schiebepuzzle 4x4 Feld

def print_board(board):
    for row in board:
        print(" | ".join(f"{num:2}" if num != 0 else "  " for num in row))
        print("-" * 20)
def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    return None
def is_solved(board):
    expected = 1
    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                return board[i][j] == 0
            if board[i][j] != expected:
                return False
            expected += 1
    return True
def move_tile(board, direction):
    empty_i, empty_j = find_empty(board)
    if direction == 'w' and empty_i < 3:  # Up
        board[empty_i][empty_j], board[empty_i + 1][empty_j] = board[empty_i + 1][empty_j], board[empty_i][empty_j]
    elif direction == 's' and empty_i > 0:  # Down
        board[empty_i][empty_j], board[empty_i - 1][empty_j] = board[empty_i - 1][empty_j], board[empty_i][empty_j]
    elif direction == 'a' and empty_j < 3:  # Left
        board[empty_i][empty_j], board[empty_i][empty_j + 1] = board[empty_i][empty_j + 1], board[empty_i][empty_j]
    elif direction == 'd' and empty_j > 0:  # Right
        board[empty_i][empty_j], board[empty_i][empty_j - 1] = board[empty_i][empty_j - 1], board[empty_i][empty_j]
def main():
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 15]
    ]
    while True:
        print_board(board)
        if is_solved(board):
            print("Congratulations! You've solved the puzzle!")
            break
        move = input("Bewegung(w/a/s/d): ").strip().lower()
        if move == 'exit':
            print("Fertig")
            break
        if move in ['w', 'a', 's', 'd']:
            move_tile(board, move)
        else:
            print("Ungueltig benutzte 'w', 'a', 's', or 'd'.")
if __name__ == "__main__":
    main()