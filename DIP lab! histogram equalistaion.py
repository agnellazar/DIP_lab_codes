import cv2
import numpy as np
import matplotlib

img= np.array([[52	,55	,61	,59	,79,	61,76,	61],
[62	,59	,55	,104	,94	,85,	59,	71],
[63,	65	,66,	113	,144,	104	,63	,72],
[64	,70	,70	,126	,154	,109	,71	,69],
[67	,73	,68	,106	,122	,88	,68	,68],
[68	,79	,60	,70	,77	,66	,58	,75],
[69	,85	,64	,58	,55	,61	,65	,83],
[70	,87	,69	,68	,65	,73	,78	,90]])

##img=cv2.imread("lena.jpeg")
##img=img[:,:,1]
m=img.shape[0]
n=img.shape[1]
L=list()
for i in range(m):
    for j in range(n):
        L.append(img[i,j])
unique_pix=list(set(L))
unique_pix.sort()

l_cdf=list()
temp=0
for k in unique_pix:
    for i in range(m):
        for j in range(n):
            if(k==img[i,j]) :
                temp+=1
    l_cdf.append(temp)

new_pix=list()
unique_pix=np.array(unique_pix)
cdf_min=np.min(unique_pix)
for k in l_cdf:
    temp=255*(k-1)/(m*n-1)
    new_pix.append(round(temp))

img_final=np.zeros((m,n))
for  k in range(len(unique_pix)):
    for i in range(m):
        for j in range(n):
            if(unique_pix[k]==img[i,j]):
                img_final[i,j]=new_pix[k]

##img2=img
##img=np.array(img)
##img_final2=cv2.resize(img2,(800,800),interpolation=cv2.INTER_AREA)
##cv2.imshow('final image',img_final2/255)
                
img3=np.zeros((m,n))
for i in range(m):
    for j in range(n):
        img3[i,j]=img[i,j]
img_final2=cv2.resize(img3,(800,800),interpolation=cv2.INTER_AREA)
cv2.imshow('Original Image',img_final2/255)

img_final2=cv2.resize(img_final,(800,800),interpolation=cv2.INTER_AREA)
cv2.imshow('Final Image',img_final2/255)

