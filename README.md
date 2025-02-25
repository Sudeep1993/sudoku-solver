# Sudoku Solver

A Python application that automatically captures, processes, and solves Sudoku puzzles. The application uses computer vision to detect Sudoku grids from screenshots, OCR to extract numbers, and a backtracking algorithm to solve puzzles.

## Features

- Screen capture and image cropping functionality
- Automatic Sudoku grid detection and extraction
- OCR-based number recognition
- Efficient Sudoku solving algorithm
- User-friendly GUI with color coding for original vs. solved values
- Manual editing capabilities for OCR correction

## Preview

![Sudoku Solver Screenshot]([https://github.com/yourusername/sudoku-solver/raw/main/docs/images/ScreenRecord.mp4](https://github.com/Sudeep1993/sudoku-solver/blob/main/docs/images/ScreenRecord))

## Installation

### Prerequisites

- Python 3.7+
- Required libraries: OpenCV, NumPy, PyAutoGUI, Pytesseract, Pillow

### Dependencies Installation

```bash
pip install -r requirements.txt
```

### Tesseract OCR Setup

This application uses Tesseract OCR for digit recognition. You need to install it separately:

#### Windows
1. Download and install Tesseract from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Add the Tesseract installation directory to your system PATH

#### macOS
```bash
brew install tesseract
```

#### Linux
```bash
sudo apt install tesseract-ocr
```

## Usage

1. Run the application:
```bash
python sudoku_solver.py
```

2. Click the "Capture & Extract" button to take a screenshot
3. Select the Sudoku grid region by dragging with your mouse
4. Check and correct any digits that were incorrectly recognized
5. Click "Solve" to solve the Sudoku puzzle

## How It Works

### Capture and Extraction
- Takes a screenshot of your screen
- Allows you to select the Sudoku grid
- Uses contour detection to identify and extract the grid
- Applies perspective transformation to obtain a straight view

### Number Recognition
- Divides the grid into 81 cells
- Uses Tesseract OCR to recognize digits in each cell
- Fills the Sudoku grid with recognized numbers

### Solving Algorithm
- Implements a backtracking algorithm to solve the Sudoku puzzle
- Checks for valid placements of digits according to Sudoku rules
- Finds a complete, valid solution if one exists

## Project Structure

```
sudoku-solver/
├── src/
│   ├── __init__.py
│   ├── sudoku_solver.py     # Main application file
│   ├── grid_extractor.py    # Image processing and grid extraction
│   ├── ocr_processor.py     # OCR and number recognition
│   ├── solver.py            # Sudoku solving algorithm
│   └── gui.py               # GUI implementation
├── tests/
├── docs/
│   ├── images/
│   │   └── ScreenRecord.mp4
│   └── usage_guide.md
├── examples/
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV for image processing
- Tesseract OCR for digit recognition
- All contributors who have helped improve this project
