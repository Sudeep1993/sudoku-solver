# src/gui.py
import tkinter as tk
from tkinter import messagebox, ttk
import os
import sys
import cv2


# Add the parent directory to the path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.grid_extractor import capture_and_crop, extract_sudoku
from src.ocr_processor import extract_numbers, save_debug_cells
from src.solver import solve_sudoku, is_valid_sudoku

def display_grid(entries, grid, original_grid):
    """
    Update the GUI to display the current state of the Sudoku grid.
    
    Args:
        entries (list): 2D list of tkinter Entry widgets
        grid (list): 2D list representing the current Sudoku grid
        original_grid (list): 2D list representing the original Sudoku grid
    """
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            if grid[i][j] != 0:
                entries[i][j].insert(0, str(grid[i][j]))
                # Set color based on whether it was an original value or solved value
                if original_grid[i][j] != 0:
                    entries[i][j].config(fg="black")  # Original values in black
                else:
                    entries[i][j].config(fg="red")    # Solved values in red

def capture_and_extract_handler(grid, original_grid, entries):
    """
    Handle the capture and extract button click event.
    
    Args:
        grid (list): 2D list representing the current Sudoku grid
        original_grid (list): 2D list representing the original Sudoku grid
        entries (list): 2D list of tkinter Entry widgets
    """
    image_path = capture_and_crop()
    if image_path:
        extracted_image = extract_sudoku(image_path)
        if extracted_image is not None:
            # Save the extracted grid for debugging
            debug_dir = os.path.join(os.path.dirname(image_path), "debug")
            os.makedirs(debug_dir, exist_ok=True)
            debug_path = os.path.join(debug_dir, "extracted_grid.png")
            cv2.imwrite(debug_path, extracted_image)
            
            # Extract numbers from the grid
            extracted_grid = extract_numbers(extracted_image)
            
            # Update the grid
            for i in range(9):
                for j in range(9):
                    grid[i][j] = extracted_grid[i][j]
                    original_grid[i][j] = extracted_grid[i][j]
            
            # Update the display
            display_grid(entries, grid, original_grid)
            
            # Show message to check for mistakes
            messagebox.showinfo("Extraction Complete", "Check manually for any mistakes in Sudoku values.")

def solve_and_display_handler(grid, original_grid, entries):
    """
    Handle the solve button click event.
    
    Args:
        grid (list): 2D list representing the current Sudoku grid
        original_grid (list): 2D list representing the original Sudoku grid
        entries (list): 2D list of tkinter Entry widgets
    """
    # Update grid from current entries
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            grid[i][j] = int(value) if value.isdigit() else 0
            original_grid[i][j] = grid[i][j]  # Update original grid to reflect manual edits
    
    # Check if the current state is valid
    if not is_valid_sudoku(grid):
        messagebox.showerror("Error", "Current Sudoku state is invalid. Please check your input.")
        return
    
    # Try to solve the puzzle
    puzzle_copy = [row[:] for row in grid]  # Make a copy to avoid modifying the original in case of failure
    if solve_sudoku(puzzle_copy):
        grid[:] = puzzle_copy[:]  # Update the grid with the solution
        display_grid(entries, grid, original_grid)
        messagebox.showinfo("Success", "Sudoku Solved!")
    else:
        messagebox.showerror("Error", "No solution exists for this puzzle.")

def clear_grid_handler(grid, original_grid, entries):
    """
    Handle the clear button click event.
    
    Args:
        grid (list): 2D list representing the current Sudoku grid
        original_grid (list): 2D list representing the original Sudoku grid
        entries (list): 2D list of tkinter Entry widgets
    """
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
            original_grid[i][j] = 0
    
    display_grid(entries, grid, original_grid)

def create_gui(grid, original_grid, entries):
    """
    Create the GUI for the Sudoku Solver.
    
    Args:
        grid (list): 2D list representing the current Sudoku grid
        original_grid (list): 2D list representing the original Sudoku grid
        entries (list): Reference to store the Entry widgets
    """
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("600x700")
    
    # Set app icon if available
    icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "images", "icon.png")
    if os.path.exists(icon_path):
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(False, icon)
    
    # Main frame
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Title and instructions
    title_label = tk.Label(main_frame, text="Sudoku Solver", font=("Arial", 24, "bold"))
    title_label.pack(pady=(0, 10))
    
    instructions = tk.Label(main_frame, text="Capture a Sudoku puzzle, check the values, and solve it automatically.",
                           font=("Arial", 10))
    instructions.pack(pady=(0, 20))
    
    # Create a frame for the Sudoku grid with thicker borders for 3x3 boxes
    grid_frame = tk.Frame(main_frame, bd=2, relief=tk.SUNKEN)
    grid_frame.pack(padx=10, pady=10)
    
    # Create subframes for each 3x3 box
    box_frames = [[tk.Frame(grid_frame, bd=2, relief=tk.RAISED) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            box_frames[i][j].grid(row=i, column=j, padx=3, pady=3)
    
    # Create entries inside the appropriate 3x3 box frames
    for i in range(9):
        row_entries = []
        for j in range(9):
            box_i, box_j = i // 3, j // 3
            entry = tk.Entry(box_frames[box_i][box_j], width=2, font=('Arial', 18), 
                           justify='center', bd=1)
            entry.grid(row=i % 3, column=j % 3, padx=1, pady=1)
            row_entries.append(entry)
        entries.append(row_entries)
    
    # Button frame
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=20)
    
    # Style for buttons
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 10))
    
    # Buttons with better styling
    capture_btn = ttk.Button(button_frame, text="Capture & Extract", 
                           command=lambda: capture_and_extract_handler(grid, original_grid, entries))
    capture_btn.grid(row=0, column=0, padx=5)
    
    solve_btn = ttk.Button(button_frame, text="Solve", 
                         command=lambda: solve_and_display_handler(grid, original_grid, entries))
    solve_btn.grid(row=0, column=1, padx=5)
    
    clear_btn = ttk.Button(button_frame, text="Clear", 
                         command=lambda: clear_grid_handler(grid, original_grid, entries))
    clear_btn.grid(row=0, column=2, padx=5)
    
    # Add color legend
    legend_frame = tk.Frame(main_frame)
    legend_frame.pack(pady=10)
    
    tk.Label(legend_frame, text="Original values:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
    tk.Label(legend_frame, text="1", fg="black", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5)
    
    tk.Label(legend_frame, text="Solved values:", font=("Arial", 10)).grid(row=0, column=2, padx=5)
    tk.Label(legend_frame, text="1", fg="red", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=5)
    
    # Status bar
    status_frame = tk.Frame(main_frame)
    status_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)
    
    status_label = tk.Label(status_frame, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(fill=tk.X)
    
    # Footer
    footer = tk.Label(root, text="Sudoku Solver v1.0 | © 2025", font=("Arial", 8), fg="gray")
    footer.pack(side=tk.BOTTOM, pady=5)
    
    root.mainloop()
