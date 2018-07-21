import numpy as np
import cv2

img = cv2.imread('img.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,255,0),15)#BGR ,000 -> black

cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(500,500),55,(0,0,255),-1)

cv2.imshow('image',img)
cv2.waitkey(0)
cv2.deatroyAllWindows()
