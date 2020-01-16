import cv2
import numpy as np
import matplotlib
img_raw=cv2.imread("lena.jpeg")
img2=img_raw[:,:,0]
cv2.imshow('image',img2)
print(img2.shape)
