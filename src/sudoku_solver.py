# src/sudoku_solver.py
import tkinter as tk
from tkinter import messagebox
import os
import sys

# Add the parent directory to the path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.grid_extractor import capture_and_crop, extract_sudoku
from src.ocr_processor import extract_numbers
from src.solver import solve_sudoku
from src.gui import create_gui

def main():
    # Initialize global variables
    grid = [[0] * 9 for _ in range(9)]
    original_grid = [[0] * 9 for _ in range(9)]
    entries = []
    
    # Start the application
    create_gui(grid, original_grid, entries)

if __name__ == "__main__":
    main()
