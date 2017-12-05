# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:52:51 2017

@author: xILENCE
"""

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detection(img_gray, frame):
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        roi_gray = img_gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 8)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roi_color, (xe, ye), (xe+we, ye+he), (0,255,0), 2)
        for (xs, ys, ws, hs) in smiles:
            cv2.rectangle(roi_color, (xs, ys), (xs+ws, ys+hs), (0,0,255), 2)
    return frame

video_capture = cv2.VideoCapture(0)

    
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plot = detection(gray, frame)
    cv2.imshow('video', plot)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()       
        
