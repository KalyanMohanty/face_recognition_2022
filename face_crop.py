# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:11:28 2022

@author: kalya_kl8c3da
"""

# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow.keras.utils import to_categorical, plot_model
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras import models,layers
# from tensorflow.keras.layers import BatchNormalization
# from tensorflow.keras.callbacks import EarlyStopping
# from tensorflow.keras.layers import LeakyReLU


# names = os.listdir("C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/")
# print("Name of the Fruits and Category \n", names[0:6])
# # Name of the Fruits and Category 
# #  ['fresh bananas', 'fresh oranges', 'rotten apples', 'fresh apples', 'rotten bananas', 'rotten oranges']
# images = []
# x = []
# y = []
# face_cascade = cv2.CascadeClassifier('C:/Users/kalya_kl8c3da/Downloads/facedata/haarcascade_frontalface_alt2.xml')

# for folder in names:
#   files = os.listdir("C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/"+folder)
#   for file in files:
#       image_path = os.path.join("C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/"+folder+"/", file)
#       img = cv2.imread(image_path)
#       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#       # print(img)
#     # img = image.load_img("C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/"+folder+"/"+file,target_size=(200,200))
#     # images.append(img)
#     # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     # img = image.img_to_array(img)
#     # x.append(img)
#     # y.append(names.index(folder))


# #import the library opencv
# import cv2
# #globbing utility.
# import glob
# #select the path
# #I have provided my path from my local computer, please change it accordingly
# path = "C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/Mithali Raj/*.*"
# # face_cascade = cv2.CascadeClassifier('C:/Users/kalya_kl8c3da/Downloads/facedata/haarcascade_frontalface_alt2.xml')
# for file in glob.glob(path):
#     image_read = cv2.imread(file)
#     # conversion numpy array into rgb image to show
#     gray = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
#     # c = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
#     face_cascade = cv2.CascadeClassifier('C:/Users/kalya_kl8c3da/Downloads/facedata/haarcascade_frontalface_alt2.xml')
#     face_cascade.detectMultiScale(gray)
    
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # cv2.imwrite('C:/Users/kalya_kl8c3da/Downloads/facedata/colorimage/*.*', c)
    # cv2.imshow('Color image', c)
    # wait for 1 second
    # cv2.waitKey(0)
    # destroy the window
    # cv2.destroyAllWindows()


# import cv2

# # Read the input image
# img = cv2.imread('C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/abhishek bachan face/Image_2.jpg')

# # Convert into grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Load the cascade
# face_cascade = cv2.CascadeClassifier('C:/Users/kalya_kl8c3da/Downloads/facedata/haarcascade_frontalcatface.xml')

# # Detect faces
# # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# faces=face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5)
# # Draw rectangle around the faces and crop the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
#     faces = img[y:y + h, x:x + w]
#     cv2.imshow("face",faces)
#     # cv2.imwrite('face.jpg', faces)
#     k = cv2.waitKey(30) & 0xff
#     if k==27:
#         break

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()