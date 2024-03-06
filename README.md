## Automatic License Plate Detection System (Python)

This project implements an automatic license plate detection system using Python libraries OpenCV (cv2) and Tesseract. 

###  Getting Started

**Prerequisites:**

* Python 3.x
* OpenCV library (cv2): `pip install opencv-python`
* PyTesseract library: `pip install pytesseract`
* Tesseract OCR engine: Download and install Tesseract OCR from [https://tesseract-ocr.github.io/tessdoc/Downloads.html](https://tesseract-ocr.github.io/tessdoc/Downloads.html) 
  -  Set the Tesseract path in the code (`pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`) (Replace path with your Tesseract installation directory)

**License Plate Cascade Classifier:**

This project utilizes a pre-trained cascade classifier for license plate detection. You can download a license plate cascade classifier from various online sources or train your own using OpenCV. The code assumes the cascade classifier file is named "licenseplate.xml" and placed in the same directory as the Python script.

### How to Run

1. Clone or download the project repository.
2. Ensure you have the required libraries installed (OpenCV, PyTesseract).
3. Set the Tesseract path in the code if needed.
4. Run the script: `python license_plate_detection.py`

The script will access your webcam by default. Detected license plates will be displayed on the video stream with bounding boxes and labels. Extracted license plate text will be saved to the following locations:

* Images: `licensePlates` folder (created if it doesn't exist)
* Text file: `demo.txt`

5. Press 'q' to quit the program.

### Project Breakdown

The script follows these primary steps:

1. **Video Capture and Preprocessing:** 
  - Initializes video capture using OpenCV.
  - Converts captured frames to grayscale for better license plate detection.

2. **License Plate Detection:**
  - Loads the pre-trained cascade classifier for license plates.
  - Identifies potential license plate regions in the grayscale frame.

3. **Region of Interest (ROI) Processing:**
  - For each detected region:
      - Applies adaptive thresholding to enhance license plate text clarity.
      - Performs OCR using Tesseract to extract text from the image.
      - Filters out potential false positives using regular expressions (alphanumeric check).

4. **Result Display and Storage:**
  - Draws bounding boxes and labels around detected license plates on the video stream.
  - Saves the extracted text to a text file (`demo.txt`).
  - Saves the license plate image for further analysis (optional).

### Additional Notes

* This is a basic implementation and can be further enhanced with functionalities like:
    - License plate recognition across different countries/regions.
    - Integrating the system with a database for real-time verification.
* The accuracy of license plate detection depends on the quality of the training data used for the cascade classifier.

### Contributing

We welcome contributions to this project! Feel free to create a pull request with your improvements or bug fixes.
