# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:04:42 2022

@author: kalya_kl8c3da
"""

import os
import cv2
import timeit
import matplotlib.pyplot as plt

'''
dataset_path = 'C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/'
path = 'C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/deepika padukone face/'
destination = 'C:/Users/kalya_kl8c3da/Downloads/facedata/shah rukh khan face_copy_test/'
folder = os.listdir(path)

names = []
for file in folder:
    names.append(file)
face_detector = cv2.CascadeClassifier('C:/ProgramData/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
for image_names in range(len(names)):
    img_path = path + names[image_names]
    img = cv2.imread(img_path)
    faces = face_detector.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 0), 0)
        cv2.imwrite(destination + str(names[image_names]) , img[y:y+h,x:x+w])
'''

# dataset_path = 'C:/Users/kalya_kl8c3da/Downloads/facedata/dataset/celebrity_face_dataset/'
dataset_path = 'C:/Users/kalya_kl8c3da/Downloads/facedata/cropped_kalyan_banaja_saurav_color_gray/'
destination = 'C:/Users/kalya_kl8c3da/Downloads/facedata/shah rukh khan face_copy_test/'

def face_extraction(face_dataset_path):
    start = timeit.default_timer()
    folder = os.listdir(face_dataset_path)
    face_detector = cv2.CascadeClassifier('C:/ProgramData/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    
    names = []
    sub_folder_path = []
    # image_pth = []
    sf_images = []
    
    for folder_names in folder:
        names.append(folder_names)
    for file in range(len(names)):
        sub_folder = face_dataset_path + names[file]  + '/'
        sub_folder_path.append(sub_folder)
        for i in range(len(sub_folder_path)):
            sf_img1 = os.listdir(sub_folder_path[i])
            for j in range(len(sf_img1)):
                sf_img = str(sub_folder_path[i])  + str(sf_img1[j]) 
                sf_images.append(sf_img)
    print(sf_images)

    for image_names in range(len(sf_images)):
        img_path =  sf_images[image_names]
        img = cv2.imread(img_path)
        faces = face_detector.detectMultiScale(img, 1.3, 5)
        print(faces)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 0), 0)
            cv2.imwrite(str(sf_images[image_names]) , img[y:y+h,x:x+w])

    stop = timeit.default_timer()
    print('Tptal Time Taken to crop dataset: ', stop - start)
face_extraction(dataset_path)   










#Your statements here




























