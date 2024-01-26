# Import necessary libraries
import cv2
import numpy as np
import os
import urllib.request

# Function to apply Gaussian blur to an image
def apply_blur(img, k):
    return cv2.GaussianBlur(img, (k, k), sigmaX=1000,sigmaY=1000)

# Function to pixelate a specific region in an image
def pixelate_region(image, startX, startY, endX, endY):
    roi = image[startY:endY, startX:endX]
    # image[startY:endY, startX:endX] = cv2.resize(roi, (1, 1), interpolation=cv2.INTER_NEAREST)

    
    image[startY:endY, startX:endX]= apply_blur(image[startY:endY,startX:endX],5)

# Function to pixelate the face in an image
def pixelate_face(image, blocks=5):
    # Load Haarcascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Pixelate each detected face
    for (x, y, w, h) in faces:
        pixelate_region(image, x, y, x + w, y + h)

# Function to download the Haarcascade file if not exists
def download_haarcascade_file():
    url = 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml'
    filename = 'haarcascade_frontalface_default.xml'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded successfully.")

if __name__ == "__main__":
    # Download Haarcascade file if not exists
    download_haarcascade_file()

    # Load the Haarcascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Capture video stream and apply pixelation to detected faces
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Apply pixelation to detected faces
        pixelate_face(frame)

        # Display the result
        cv2.imshow('Pixelated Faces', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
