# Sudoku Solver Usage Guide

This guide provides detailed instructions on how to use the Sudoku Solver application effectively.

## Getting Started

After installing the application, you can launch it by running:

```bash
python -m src.sudoku_solver
```

Or if you installed it via pip:

```bash
sudoku-solver
```

## Capturing a Sudoku Puzzle

1. Launch the Sudoku Solver application.
2. Click the "Capture & Extract" button.
3. Your screen will freeze, and a crosshair cursor will appear.
4. Click and drag to select the region containing the Sudoku puzzle.
5. Press Enter to confirm your selection.

**Tips for better capture:**
- Ensure good lighting to improve OCR accuracy
- Make sure the puzzle is visible and clear on your screen
- Try to capture only the puzzle grid, excluding surrounding elements

## Correcting OCR Results

After capturing, the application will attempt to recognize the numbers in the grid. However, OCR is not always perfect, so you may need to correct some values:

1. Check each recognized digit in the grid.
2. If a number is incorrect, click on the cell and type the correct number.
3. If a cell should be empty but contains a number, delete the content.

## Solving the Puzzle

Once you've verified that all the numbers are correct:

1. Click the "Solve" button.
2. The application will attempt to solve the Sudoku puzzle.
3. If successful, the solution will be displayed with:
   - Original numbers in black
   - Solved numbers in red
4. A success message will appear when the puzzle is solved.

## Troubleshooting

### Common Issues

**OCR Recognition Problems**
- Make sure the captured image is clear and well-lit
- Try adjusting your screen brightness
- Use puzzles with clear, standard fonts for better recognition

**No Solution Found**
- Check if you've entered the puzzle correctly
- Verify that there are no duplicate numbers in rows, columns, or 3x3 boxes
- Make sure the puzzle is valid and has a solution

**Extraction Fails**
- Try capturing a cleaner view of the puzzle
- Ensure the grid lines are visible
- Make sure the grid has a good contrast against its background

### Debugging

If you encounter persistent issues, the application creates debug files in the `images/debug` directory:
- `extracted_grid.png`: Shows the extracted and normalized grid
- `cell_X_Y_orig.png`: Shows the original cell at position (X,Y)
- `cell_X_Y_proc.png`: Shows the processed cell used for OCR

## Advanced Usage

### Manual Entry

Instead of capturing a puzzle, you can manually enter one:

1. Launch the application
2. Click on each cell and type the numbers
3. Click "Solve" to find the solution

### Clearing the Grid

To start fresh:

1. Click the "Clear" button to reset the grid
2. All cells will be emptied, and you can begin again

## Performance Considerations

- The application uses a backtracking algorithm which works well for most puzzles
- Very difficult puzzles might take longer to solve
- OCR accuracy depends on image quality and digit clarity
