import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #HSV MORE NATURE COLOR. COLOR VALUE.

    lower_red =np.array([150,150,0])    
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv,lower_red,upper_red)# 0 or 1
    result = cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((15,15),np.float32)/255 #average.
    smoothed = cv2.filter2D(result,-1,kernel)
    blur = cv2.GaussianBlur(result,(15,15),0)#gaussian
    median = cv2.medianBlur(result,15)
    bilateral = cv2.bilateralFilter(result,15,75,75)
    #added

    cv2.imshow('frame',frame)
    cv2.imshow('median',median)
    #cv2.imshow('mask',mask)
    cv2.imshow('result',result)

    k=cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
