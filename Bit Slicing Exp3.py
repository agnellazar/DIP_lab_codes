#Written by Agnel Lazar Alappat
import cv2                                                  #importing libraries
import numpy as np

def dec2bin(num):                                       #function to calculate binary equvalent
    L=[0,0,0,0,0,0,0,0]
    temp=0
    while(num!=0):
        L[temp]=int(num%2)
        num=int(num/2)
        temp+=1
    return L[::-1]

def bin2dec(L):                                         # function to calculate decimal equilvalent
    L=L[::-1]
    num=0
    pow_2=0
    for k in L:
        num=num+k*(2**pow_2)
##        print(num,k,pow_2)
        pow_2+=1
    return num


    
img=cv2.imread("lena.jpeg")                     #reading image
img=img[:,:,1]
img_mat=np.zeros((img.shape[0],img.shape[1],8))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_mat[i,j,:]=dec2bin(img[i,j])        #creating 3D matrix of binary images

name=[0,1,2,3,4,5,6,7,8]
for k in range(8):
    cv2.imshow(str(name[k]),img_mat[:,:,k]) #ploting each image
    
img_mat[:,:,7]=0                                    #compressing image
img_re=np.zeros((img.shape))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_re[i,j]=bin2dec(img_mat[i,j,:]) #reconstructing image
print(img)
print(img_re)
cv2.imshow("Re constructed",img_re/255)         #showing results
cv2.imshow("original",img)
