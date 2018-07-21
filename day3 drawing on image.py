import numpy as np
import cv2

img = cv2.imread('img.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,255,0),15)#BGR ,000 -> black

cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(500,500),55,(0,0,255),-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'TEXT TEST',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitkey(0)
cv2.deatroyAllWindows()
