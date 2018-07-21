import numpy as np
import cv2

img=cv2.imread('img.jpg',cv2.IMREAD_COLOR)

#img[55,55]=[255,0,0]
px = img[55,55] #pixel of this location.

#print(px)

icon = img[37:111,107:194]
img[0:74,0:87] = icon

img[100:150,100:150] = [0,255,255]
roi = img[100:150,100:150]
#print(roi)

cv2.imshow('img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
