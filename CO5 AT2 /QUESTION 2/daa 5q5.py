def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n):
    if row == n:
        return True

    if board[row] != -1:
        return solve(board, row + 1, n)

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False

n = 8
board = [-1] * n
board[0] = 0
board[2] = 4

if solve(board, 0, n):

    print("Solution Found")

    for i in range(n):
        print("Row", i, "Column", board[i])

else:
    print("No Solution Exists")
