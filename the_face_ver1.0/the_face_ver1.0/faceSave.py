username = "Cheng Zhang"

'''
The file used to save capture from video and save in 

usage
don't forgot to change the globel variable username
press a to pause
press s to save ; press any other k not to save

'''


import numpy as np
import cv2, os


camera_index = 0
faceLibPath = "./lib"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


##########################

cap = cv2.VideoCapture(camera_index)
faces = []
count = 0
doSave = False
file_index = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if (count == 5) :
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        count = 0
        if (doSave):
            confirm = cv2.waitKey(10000000)
            if (confirm != ord('s') ):
                doSave = False
                continue
                
            doSave = False
            filename = ""
            while(True):
                filename = os.path.join(faceLibPath, username + "." + str(file_index) + ".jpg")
                if (os.path.isfile(filename) ):
                    file_index += 1
                else:
                    break;
            for (x,y,w,h) in faces:
                print filename
                cv2.imwrite(filename, frame[y:(y+h), x:(x+w)])
    count += 1
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    input = cv2.waitKey(30)
    if (input == ord('a') and len(faces) == 1):
        doSave = True
    cv2.imshow('FaceCap',frame)
    
    
    





