# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sudoku-solver",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Sudoku solver with OCR capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sudoku-solver",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "pytesseract>=0.3.0",
        "pyautogui>=0.9.0",
        "pillow>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "sudoku-solver=src.sudoku_solver:main",
        ],
    },
)
