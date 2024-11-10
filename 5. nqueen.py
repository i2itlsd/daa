def is_safe(board, row, col, n):
    # Check if the column is safe
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
    # Base case: If all queens are placed, return True
    if row == n:
        return True

    # Try placing the queen in each column one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place the queen
            if solve_n_queens(board, row + 1, n):  # Recur to place the next queen
                return True
            # Backtrack: Remove the queen
            board[row] = -1

    return False

def print_solution(board, n):
    # Print the n-Queens board as a matrix
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(" ".join(row))

def n_queens():
    # Take input for the size of the board (n)
    n = int(input("Enter the size of the board (n): "))
    
    if n < 1:
        print("There is no solution for this size.")
        return
    
    board = [-1] * n  # Initialize the board with -1, indicating no queens placed
    # Place the first queen in the first row, first column (for simplicity)
    board[0] = 0
    
    if solve_n_queens(board, 1, n):  # Start placing queens from row 1
        print_solution(board, n)
    else:
        print("Solution does not exist")

# Run the function
n_queens()


'''
Time Complexity: O(n!)
Space Complexity: O(n)

Explanation:

is_safe(board, row, col, n): This function checks if placing a queen at position (row, col) is safe. It checks for conflicts in the same column and diagonals.

solve_n_queens(board, row, n): This is the backtracking function. It attempts to place a queen in each column of the current row. If successful, it proceeds to the next row.

print_solution(board, n): This function prints the solution as a chessboard matrix where 'Q' represents a queen and '.' represents an empty square.

n_queens(n): This is the main function that initializes the board and starts the backtracking process. It places the first queen in the first row and uses backtracking to place the remaining queens.

'''