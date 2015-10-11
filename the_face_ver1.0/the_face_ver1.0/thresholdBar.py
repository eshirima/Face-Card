import numpy as np
import cv2

class TrackBar:
    windowName = "Control"
    trackName = "ONE"
    secTrackName = "TWO"
    min = 0
    begin = 0
    
    def __init__(self,mini,mid,maxi,start,mild,end):
        def doNothing(x):
            pass
        if maxi - mini <= 0 | end - start <= 0:
            print "Check mini-max & end start values!, <= 0"
        #print mini, mid, maxi, start , mild , end
        cv2.namedWindow(self.windowName, 0)
        cv2.resizeWindow(self.windowName, 400,50)
        cv2.createTrackbar(self.trackName,self.windowName,mid,maxi - mini,doNothing)
        cv2.createTrackbar(self.secTrackName,self.windowName,mild,end - start,doNothing)
        self.min = mini
        self.begin = start
        
    def getDetectThreshold(self):
        cv2.waitKey(1)
        return self.min + cv2.getTrackbarPos(self.trackName, self.windowName)
    
    
    def getRecognizeThreshold(self):
        cv2.waitKey(1)
        return self.begin + cv2.getTrackbarPos(self.secTrackName, self.windowName)
    

#FIRST IS THE WINDOW NAME
#SECOND IS THE TRACK NAME

if __name__ == "__main__":
    index_num = 0;

    cap = cv2.VideoCapture(index_num)
    faces = [[400,200,400,400]]
    count = 0
    
    dect_trackBar = TrackBar(5,0,10,3,2,5)
    while(True):
        # Capture frame-by-frame
        r = dect_trackBar.getDetectThreshold()
        s = dect_trackBar.getRecognizeThreshold()
        print r, " = ", s
        
        
        
        
        
        
        
