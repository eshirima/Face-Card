import cv2
import numpy as np

def drawProfile(userProfile, frame, highLight):
    for user in userProfile:
        font = cv2.FONT_HERSHEY_SIMPLEX
        name = user["name"]
        age = str(user["age"])
        email = user["email"]
        x = user["x"]
        y = user["y"]
        w = user["w"]
        h = user["h"]
        
        height, width, channels = frame.shape        
        if w >= 400 :
            font_n = 3
            font_r = 2
            if x + w + 400 > width :
                horizontal = x - w - 300
                colorRegion = frame[y:y+h, horizontal:- 300]
            else:
                horizontal = x + w
                colorRegion = frame[y:y+h, horizontal:horizontal + 300]
        if w >= 200 and w < 400 :
            font_n = 2
            font_r = 1
            if x + w + 300 > width :
                horizontal = x - w - 200
                colorRegion = frame[y:y+h, horizontal:- 200]
            else:
                horizontal = x + w
                colorRegion = frame[y:y+h, horizontal:horizontal + 200]
        if w < 200 :
            font_n = 1
            font_r = 1
            if x + w + 200 > width :
                horizontal = x - w - 100
                colorRegion = frame[y:y+h, horizontal:- 100]
            else:
                horizontal = x + w
                colorRegion = frame[y:y+h, horizontal:horizontal + 100]
                
        colorMean = cv2.mean(colorRegion)
        color = colorMean[:3]
        color = tuple(np.subtract((255,255,255), color))
        if highLight == True:
            color = (0, 100, 255)
        
        cv2.putText(frame, name, (x + w,y+h/5), font, font_n, color, 2)
        cv2.putText(frame, "Age: " + age, (x + w,y+2*h/5), font, font_r, color, 2)
        cv2.putText(frame, email, (x + w,y+3*h/5), font, font_r, color, 2)