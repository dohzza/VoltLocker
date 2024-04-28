import subprocess
import pytesseract
import re
import cv2
import time

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


f = open("/OCRscan.txt", "w")
# Takes a string 'text' as an input and searches for a 9-digit ID number.
# If a match is found it returns the ID number as a string, otherwise it returns none
def extract_id_from_text(text):
    #Pattern defined searching for a 9-digit number
    pattern = r'\b\d{9}\b'

    # Search for the pattern in the text
    match = re.search(pattern, text)

    if match:
        # Extract and return the ID number
        return match.group()
    else:
        return None

# Takes a image file path as input. Reads the image using OpenCV.
# If image successful, it is converted to grayscale and OCR is performed.
# Extracted text is returned.
def read_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read image file")
        return ""

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale image
    text = pytesseract.image_to_string(gray_image)

    return text

# Main of program.
# Reads image text. Extracts ID number if found. Prints ID number or an error if no ID found.
if __name__ == "__main__":
    # Capture image using rpicam-jpeg command-line tool
    image_path = 'ID.jpg'
    subprocess.run(['rpicam-jpeg', '-o', image_path])
    print("ID scanned. Searching for ID number...")

    # Read text from the captured image
    text = read_text_from_image(image_path)

    # Extract ID from the text
    id_number = extract_id_from_text(text)

    # Display the extracted ID number
    if id_number:
        print("Student ID:", id_number)
        
        f.write(id_number)
        time.sleep(1)
        f.close()
    else:
        print("Student ID not seen. Plaese recan ID.")
