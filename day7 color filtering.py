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

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)

    k=cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
