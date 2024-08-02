def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col):
    # Base case: If all queens are placed, return True
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            
            if solve_n_queens_util(board, col + 1):
                return True
            
            # If placing queen at board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0
    
    return False

def solve_n_queens():
    board = [[0 for _ in range(4)] for _ in range(4)]
    
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False
    
    print("Solution:")
    for row in board:
        print(" ".join(map(str, row)))
    
    return True

# Solve the 4-Queens problem
solve_n_queens()
