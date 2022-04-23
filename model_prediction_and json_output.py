# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:24:47 2022

@author: kalya_kl8c3da
"""

from tensorflow.keras.models import load_model
import cv2
import os
import numpy as np
import json

def model_pred(path_to_model, path_to_image):
    caleb_names =['ranvir kapoor face', 'Ravindra Jadeja', 'varun dhawan wallpaper', 
                  'Sonam Kapoor Ahuja', 'Raveena Tandon', 'shah rukh khan face', 
                  'ram charan wallpaper', 'Smriti Mandhana', 'rani mukharji wallpaper', 
                  'sonu sood wallpaper', 'S. Srisanth', 'slaman khan face', 'Sunil Gavaskar', 
                  'karan johar wallpaper', 'sonu nigam wallpaper', 'deepika padukone face']
    model = load_model(path_to_model)

    img = cv2.imread(path_to_image)
    
    img = cv2.resize(img,(100, 100))
    img = np.reshape(img,[1,100, 100,3])
    classes = model.predict(img)
    normalized_classes = classes//1

    j = 0
    index_no = []
    while True:
        if normalized_classes[0][j] == 1.0:
            index = j
            caleb_name = {
              'Model prediction':{
                  'ID': index,
                  'Name':caleb_names[j]
                        }
              }
            json_object = json.dumps(caleb_name, indent =4)
            print(json_object)
        j = j +1    
        if j == 16:
            break
    for i in classes:
        confidence = (i//1)* 100 
        print(confidence)
image_path = 'C:/Users/kalya_kl8c3da/Downloads/Ranvir_Kapoor (1).jpeg'
model_path = 'C:/Users/kalya_kl8c3da/Downloads/facedata/facemoedl.h5'
print(model_pred(model_path, image_path))
