# Lab 2 - Plagiarism Detector

## Author
Jacinta Ngugi

## How to Run
1. Make sure essay1.txt and essay2.txt are in the same folder
2. Run the Python script:
   python plagiarism-detector.py
3. When prompted, type a word to search for

## How it Works
The program reads two essays, finds common words using set intersection,
and calculates plagiarism percentage using the formula:
plagiarism% = (common words / total unique words) x 100
If the result is 50% or more, plagiarism is detected.