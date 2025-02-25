# src/ocr_processor.py
import cv2
import pytesseract
import os
import platform

def setup_tesseract():
    """
    Configure Tesseract OCR based on the operating system.
    """
    system_name = platform.system()
    if system_name == "Windows":
        # Check for common installation paths
        tesseract_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        ]
        
        for path in tesseract_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                break
    # For macOS and Linux, Tesseract should be in the PATH already

def extract_numbers(image):
    """
    Extract numbers from the Sudoku grid image using OCR.
    
    Args:
        image (numpy.ndarray): Normalized image of the Sudoku grid
        
    Returns:
        list: 2D list representing the Sudoku grid with recognized numbers
    """
    setup_tesseract()
    
    cell_size = 50  # Assuming the grid is 450x450 pixels and has 9x9 cells
    grid = []
    
    for i in range(9):
        row = []
        for j in range(9):
            # Calculate cell position
            x, y = j * cell_size, i * cell_size
            
            # Extract cell with some margin to avoid grid lines
            cell = image[int(y+0.1*cell_size):int(y+0.9*cell_size), 
                         int(x+0.1*cell_size):int(x+0.9*cell_size)]
            
            # Rotate for better OCR recognition
            cell = cv2.flip(cv2.rotate(cell, cv2.ROTATE_90_CLOCKWISE), 1)
            
            # Recognize digit
            try:
                digit = pytesseract.image_to_string(
                    cell, 
                    config='--psm 10 digits'
                ).strip()
                
                row.append(int(digit) if digit.isdigit() else 0)
            except Exception:
                row.append(0)  # If OCR fails, assume empty cell
                
        grid.append(row)
    
    # Transpose the grid to match the visual representation
    return list(map(list, zip(*grid)))

def save_debug_cells(image, output_dir="debug_cells"):
    """
    Save individual cells as images for debugging OCR issues.
    
    Args:
        image (numpy.ndarray): Normalized image of the Sudoku grid
        output_dir (str): Directory to save the cell images
    """
    os.makedirs(output_dir, exist_ok=True)
    cell_size = 50
    
    for i in range(9):
        for j in range(9):
            x, y = j * cell_size, i * cell_size
            cell = image[int(y+0.1*cell_size):int(y+0.9*cell_size), 
                         int(x+0.1*cell_size):int(x+0.9*cell_size)]
            
            # Save both original and processed cell
            cv2.imwrite(f"{output_dir}/cell_{i}_{j}_orig.png", cell)
            
            # Save processed cell
            processed = cv2.flip(cv2.rotate(cell, cv2.ROTATE_90_CLOCKWISE), 1)
            cv2.imwrite(f"{output_dir}/cell_{i}_{j}_proc.png", processed)
