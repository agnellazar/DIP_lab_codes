#Written by Agnel Lazar Alappat
import cv2                                                  #importing libraries
import numpy as np

img=cv2.imread("fruits.jpg")                    #reading image
img_b=img*255
img_b[:,:,1]=0
img_b[:,:,2]=0

img_g=img*255
img_g[:,:,0]=0
img_g[:,:,2]=0

img_r=img*255
img_r[:,:,0]=0
img_r[:,:,1]=0

t=(img_r[:,:,0]/255)
print(t.shape)
# cv2 uses bgr pattern
cv2.imshow("R-plane",img_r)
cv2.imshow("G-plane",img_g)
cv2.imshow("B-plane",img_b)
cv2.imshow("Original Image",img)
