# src/solver.py

def is_valid(board, row, col, num):
    """
    Check if placing a number at the specified position is valid according to Sudoku rules.
    
    Args:
        board (list): 2D list representing the Sudoku grid
        row (int): Row index
        col (int): Column index
        num (int): Number to check
        
    Returns:
        bool: True if the placement is valid, False otherwise
    """
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using a backtracking algorithm.
    
    Args:
        board (list): 2D list representing the Sudoku grid
        
    Returns:
        bool: True if a solution was found, False otherwise
    """
    # Find an empty cell
    empty_cell = find_empty_cell(board)
    
    # If no empty cell is found, the puzzle is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Try placing digits 1-9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the digit if valid
            board[row][col] = num
            
            # Recursively solve the rest of the puzzle
            if solve_sudoku(board):
                return True
            
            # If placing the digit doesn't lead to a solution, backtrack
            board[row][col] = 0
    
    # No solution found with any digit
    return False

def find_empty_cell(board):
    """
    Find an empty cell in the Sudoku grid.
    
    Args:
        board (list): 2D list representing the Sudoku grid
        
    Returns:
        tuple: (row, col) of the empty cell, or None if no empty cell is found
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid_sudoku(board):
    """
    Check if the current state of the Sudoku grid is valid.
    
    Args:
        board (list): 2D list representing the Sudoku grid
        
    Returns:
        bool: True if the grid is valid, False otherwise
    """
    # Check rows
    for row in range(9):
        if not is_valid_group([board[row][col] for col in range(9)]):
            return False
    
    # Check columns
    for col in range(9):
        if not is_valid_group([board[row][col] for row in range(9)]):
            return False
    
    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    box.append(board[row][col])
            if not is_valid_group(box):
                return False
    
    return True

def is_valid_group(group):
    """
    Check if a group (row, column, or box) contains no duplicate non-zero digits.
    
    Args:
        group (list): List of digits in a group
        
    Returns:
        bool: True if the group is valid, False otherwise
    """
    # Filter out zeros (empty cells)
    digits = [digit for digit in group if digit != 0]
    # Check for duplicates
    return len(digits) == len(set(digits))
