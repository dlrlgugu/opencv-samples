import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners = np.int0(corners)

for c in corners:
    x,y=c.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('Cornor',img)
