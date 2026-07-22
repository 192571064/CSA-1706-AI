# Create board
board = []

for i in range(8):
    row = []
    for j in range(8):
        row.append("*")
    board.append(row)


def queen(row):

    # All queens placed
    if row == 8:
        return

    # Check every column
    for col in range(8):

        safe = 1

        # Check same column
        for i in range(row):
            if board[i][col] == "Q":
                safe = 0

        # Check left diagonal
        i = row
        j = col

        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                safe = 0
            i = i - 1
            j = j - 1

        # Check right diagonal
        i = row
        j = col

        while i >= 0 and j < 8:
            if board[i][j] == "Q":
                safe = 0
            i = i - 1
            j = j + 1

        # Safe place found
        if safe == 1:

            board[row][col] = "Q"

            queen(row + 1)

            # Stop if solution completed
            count = 0

            for r in range(8):
                for c in range(8):
                    if board[r][c] == "Q":
                        count = count + 1

            if count == 8:
                return

            # Backtracking
            board[row][col] = "*"


queen(0)

print("Final Board\n")

for i in range(8):
    for j in range(8):
        print(board[i][j], end=" ")
    print()
