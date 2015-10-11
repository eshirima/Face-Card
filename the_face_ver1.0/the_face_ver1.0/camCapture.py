import numpy as np
import cv2

index_num = 0;

cap = cv2.VideoCapture(index_num)
faces = [[400,200,400,400]]
count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if (count == 5) :
    
        face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.12/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        count = 0
        
    count += 1
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    input = cv2.waitKey(30)
    print "count", count
    print "input", input
    cv2.imshow('FaceCap',frame)