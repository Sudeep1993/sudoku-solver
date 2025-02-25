# src/grid_extractor.py
import cv2
import numpy as np
import pyautogui
import platform
from tkinter import messagebox
import os

def capture_and_crop():
    """
    Capture a screenshot and allow the user to crop the Sudoku grid.
    
    Returns:
        str: Path to the saved cropped image or None if capture failed
    """
    system_name = platform.system()
    try:
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        roi = cv2.selectROI("Crop Image", screenshot_cv, showCrosshair=True)
        cv2.destroyWindow("Crop Image")
        if roi != (0, 0, 0, 0):
            x, y, w, h = roi
            cropped_image = screenshot_cv[y:y+h, x:x+w]
            
            # Create images directory if it doesn't exist
            os.makedirs("images", exist_ok=True)
            image_path = os.path.join("images", "sudoku.png")
            
            cv2.imwrite(image_path, cropped_image)
            return image_path
        else:
            messagebox.showerror("Error", "No region selected for cropping.")
            return None
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def preprocess_image(image_path):
    """
    Preprocess the image for contour detection.
    
    Args:
        image_path (str): Path to the image
        
    Returns:
        numpy.ndarray: Preprocessed binary image
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    return cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

def extract_sudoku(image_path):
    """
    Extract and normalize the Sudoku grid from the image.
    
    Args:
        image_path (str): Path to the image containing the Sudoku grid
        
    Returns:
        numpy.ndarray: Extracted and normalized Sudoku grid image or None if extraction failed
    """
    thresh = preprocess_image(image_path)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            pts1 = np.float32([approx[i][0] for i in range(4)])
            pts2 = np.float32([[0, 0], [450, 0], [450, 450], [0, 450]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            return cv2.warpPerspective(cv2.imread(image_path), matrix, (450, 450))
            
    messagebox.showerror("Error", "No Sudoku grid found.")
    return None
