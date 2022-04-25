# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:31:53 2022

@author: kalya_kl8c3da
"""

import os
import cv2
import json
import numpy as np
from tensorflow.keras.models import load_model

# Import OpenCV2 for image processing
# import cv2
# import os


# vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
faceCascade  = cv2.CascadeClassifier('C:/ProgramData/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
model_path = 'C:/Users/kalya_kl8c3da/Documents/GitHub/face_recognition_2022/keras_model/facemoedl_KBS_RGB.h5'

video_capture = cv2.VideoCapture(0)
names = ['Banaja Rout', 'Saurabh Rout', 'Kalyan Mohanty']
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    model = load_model(model_path)
    img = cv2.resize(frame,(100, 100))
    img = np.reshape(img,[1,100, 100,3])
    classes = model.predict(img)
    normalized_classes = classes//1
    
    j = 0
    index_no = []
    while True: 
        if normalized_classes[0][j] == 1.0:
            index = j
            person_name = {
              'Model prediction':{
                  'ID': index,
                  'Name':names[j]
                        }
              }
            
            json_object = json.dumps(person_name, indent =4)
            print(json_object)
        j = j +1
        if j == 3:
            break
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()