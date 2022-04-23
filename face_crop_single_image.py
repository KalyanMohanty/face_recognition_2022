# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:02:48 2022

@author: kalya_kl8c3da
"""

# Import OpenCV2 for image processing
import cv2
import os

# vid_cam = cv2.VideoCapture(0)
image_frame = cv2.imread('C:/Users/kalya_kl8c3da/Downloads/facedata/shah rukh khan face/Image_3.jpg')
# image_frame = cv2.cvtColor(image_frame, cv2.COLOR_RGB2GRAY)
# gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('C:/ProgramData/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# Capture video frame
# Convert frame to grayscale

# Detect frames of different sizes, list of faces rectangles
faces = face_detector.detectMultiScale(image_frame, 1.3, 5)

# Loops for each faces
for (x,y,w,h) in faces:
    # Crop the image frame into rectangle
    cv2.rectangle(image_frame, (x,y), (x+w,y+h), (0, 0, 0), 0)
    # Save the captured image into the datasets folder
    cv2.imwrite("C:/Users/kalya_kl8c3da/Downloads/facedata/test.jpg", image_frame[y:y+h,x:x+w])

    # Display the video frame, with bounded rectangle on the person's face
    # cv2.imshow('frame', image_frame)
