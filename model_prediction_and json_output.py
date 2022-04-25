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

    fruit_names = ['Fresh apple', 'Rotten orange', 'Fresh banana','Rotten banana','Rotten apple', 'Fresh orange' ]
    model = load_model(path_to_model)

    img = cv2.imread(path_to_image)
    
    img = cv2.resize(img,(50, 50))
    img = np.reshape(img,[1, 50, 50,3])
    classes = model.predict(img)
    l = []
    for i in range(len(classes[0])):
        l.append(int(classes[0][i]*100))
    
    for i in range(len(l)):
        try:
            if l[i] > 90:
                caleb_name = {
                  'Model prediction':{
                      'Id': i,
                      'Name':fruit_names[i],
                      'Confidence': l[i]
                            }
                  }
                json_object = json.dumps(caleb_name, indent =4)
                print(json_object)
        
        except:
            if l[i] > 50 or l[i] < 90:
                caleb_name = {
                  'Model prediction':{
                      'Id': i,
                      'Name':fruit_names[i],
                      'Confidence': l[i]
                            }
                  }
                json_object = json.dumps(caleb_name, indent =4)
                print(json_object)
            elif l[i] < 50:
                print('No Face Matched')
    # print(k) 
                return json_object

image_path = 'C:/Users/kalya_kl8c3da/Downloads/banaja4.png'
model_path = 'C:/Users/kalya_kl8c3da/Downloads/fruit_model_v1.h5'
print(model_pred(model_path, image_path))
