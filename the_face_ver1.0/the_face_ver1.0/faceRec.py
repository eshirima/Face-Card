import numpy as np
import cv2, os
from thresholdBar import TrackBar
from get_profile import getProfile
from drawText import drawProfile
from distutils.command.config import config
from get_parse_profile import getParseProfile

camera_index = 0
faceLibPath = "./lib"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
updateFrequency = 5   # >= 1

################################################

facebookProfile = getParseProfile()
namelist = []

def getRecognizer():
    image_paths = [os.path.join(faceLibPath, f) for f in os.listdir(faceLibPath) if f[0]!='.']
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        print image_path
        name = os.path.split(image_path)[1].split(".")[0]
        
        if (name == "Barack Obama"):
            imageOld = cv2.imread(image_path,1)
            image = cv2.imread(image_path,0)
            faces = face_cascade.detectMultiScale(image, 1.4, 5)
            for (x,y,w,h) in faces:
                cv2.imshow("Adding faces to training set...", imageOld[y:y+h, x:x+w])
                images.append(image[y:y+h, x:x+w])
                if (not name in namelist):
                    namelist.append(name)
                labels.append(namelist.index(name))
        else:
            imageOld = cv2.imread(image_path,1)
            image = cv2.imread(image_path,0)
            cv2.imshow("Adding faces to training set...", imageOld)
            images.append(image)
            if (not name in namelist):
                namelist.append(name)
            labels.append(namelist.index(name))
        cv2.waitKey(50)
        
    cv2.destroyAllWindows()
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.train(images, np.array(labels) )
    return recognizer

def main():
    cap = cv2.VideoCapture(camera_index)
    faces = []
    count = 0
    doRecognize = False
    ifShowProfile = False
    highlightText = False
    userProfile = []
    
    recognizer = getRecognizer()
    trackbar = TrackBar(101,10,150,30,70,120)
    
    while(True):
        # Detect Threshold
        detectThreshold = float(trackbar.getDetectThreshold() ) / 100
        #print detectThreshold
        # Recognize Threshold
        recognizeThreshold = trackbar.getRecognizeThreshold()
        # Capture frame-by-frame
        ret, frame = cap.read()
        if (count == updateFrequency) :
        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, detectThreshold, 5)
            count = 0
            
            if (doRecognize):
                userProfile = []
                for i,(x,y,w,h) in enumerate(faces):
                    predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])
                    if (conf < recognizeThreshold):
                        print "faces["+str(i)+']',namelist[predicted],conf
                        for it in facebookProfile:
                            if (it["name"] == namelist[predicted]):
                                tmp = it
                                tmp['x'] = x
                                tmp['y'] = y
                                tmp['w'] = w
                                tmp['h'] = h
                                userProfile.append(tmp)
                    else:
                        print "faces["+str(i)+']',"Unknown",conf
            
                
        count += 1
        
        for i,(x,y,w,h) in enumerate(faces):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            
        if (ifShowProfile):
            drawProfile(userProfile,frame,highlightText)
    
        # Display the resulting frame
        inputChar = cv2.waitKey(50)
        if (inputChar == ord('z') ):
            doRecognize = True
        if (inputChar == ord('x') ):
            doRecognize = False
            ifShowProfile = False
        if (inputChar == ord('c') and doRecognize):
            ifShowProfile = True
        if (inputChar == ord('v') ):
            ifShowProfile = False
        if (inputChar == ord('d') ):
            highlightText = True
        if (inputChar == ord('f') ):
            highlightText = False
        
        cv2.imshow('Face Recognization',frame)

if __name__ == "__main__":
    main()
    
    
    
    