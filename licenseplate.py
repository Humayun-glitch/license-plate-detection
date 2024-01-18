import cv2
import pytesseract
import os
import re

harcascade = "licenseplate.xml"

# Load Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

# Create the "licensePlates" folder if it doesn't exist
output_folder = "licensePlates"
os.makedirs(output_folder, exist_ok=True)

# Open the "demo.txt" file for writing
output_file_path = "demo.txt"
output_file = open(output_file_path, 'w')

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            aspect_ratio = w / h
            if aspect_ratio < 1 or aspect_ratio > 4:  # Check aspect ratio
                continue

            img_roi = img[y: y + h, x:x + w]

            # Convert the image to grayscale
            gray_img = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)

            # Apply adaptive thresholding
            gray_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

            # Use OCR to extract text from the image
            text = pytesseract.image_to_string(gray_img)

            # Filter out false positives
            if not re.match(r'^[A-Za-z0-9]+$', text):  # Check if text contains only alphanumeric characters
                continue

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "License Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            # Save the image to the "licensePlates" folder
            cv2.imwrite(os.path.join(output_folder, "carPictures" + str(count) + ".jpg"), img_roi)

            # Print the extracted text (optional)
            print("Detected License Plate:", text)

            # Write the extracted text to the "demo.txt" file
            output_file.write(f"Frame {count} - Detected License Plate: {text}\n")

            count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the output file
output_file.close()

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
