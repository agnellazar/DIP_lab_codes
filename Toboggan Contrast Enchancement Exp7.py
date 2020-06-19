#Written by Agnel Lazar Alappat

import cv2
import numpy as np

T=[[0,0,0,0,0,0],[0,12,14,23,13,0],[0,16,11,21,18,0],[0,21,24,23,12,0],[0,12,21,20,10,0],[0,0,0,0,0,0]]
img0=[[4,4,3,2],[3,7,6,1],[2,7,6,2],[0,1,0,2]]
img_final=np.zeros((4,4))
for i in range(1,5):
    for j in range(1,5):
        l_min=1000
        for m in range(-1,2):
            for n in range(-1,2):
                    if(T[i+m][j+n]<l_min) and T[i+m][j+n]!=0:
                        l_min=T[i+m][j+n]
                        t=img0[m+i-1][j+n-1]
                        img_final[i-1][j-1]=t
                        
print(img_final)
