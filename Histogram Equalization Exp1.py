#Written by Agnel Lazar Alappat



import cv2                                                          #importing required libraries
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("lena.jpeg")                                 #importing image           
img=img[:,:,1]                                                     #Using only one layer
m=img.shape[0]                                                  #getting dimensions of an image
n=img.shape[1]
L=list()
for i in range(m):
    for j in range(n):
        L.append(img[i,j])                                      #getting id array of image
unique_pix=list(set(L))                                       #getting list of unique elements
unique_pix.sort()                                               # sorting pixels
l_cdf=list()
temp=0
for k in unique_pix:
    for i in range(m):
        for j in range(n):
            if(k==img[i,j]) :                                       #counting the frequency and cdf of each value of pixel
                temp+=1
    l_cdf.append(temp)
new_pix=list()
unique_pix=np.array(unique_pix)
cdf_min=np.min(unique_pix)
for k in l_cdf:
    temp=255*(k-1)/(m*n-1)
    new_pix.append(round(temp))                         #calculating new pixel values

img_final=np.zeros((m,n))               
for  k in range(len(unique_pix)):                   
    for i in range(m):
        for j in range(n):
            if(unique_pix[k]==img[i,j]):                    
                img_final[i,j]=new_pix[k]                     # changing values of each image pixel             
plt.plot(l_cdf)                                                     #ploting histogram
plt.show()
img3=np.zeros((m,n))
for i in range(m):
    for j in range(n):
        img3[i,j]=img[i,j]
img_final2=cv2.resize(img3,(800,800),interpolation=cv2.INTER_AREA)
cv2.imshow('Original Image',img_final2/255)       #showing result

img_final2=cv2.resize(img_final,(800,800),interpolation=cv2.INTER_AREA)
cv2.imshow('Final Image',img_final2/255)          

