import cv2
import numpy as np

def dec2bin(num):
    L=[0,0,0,0,0,0,0,0]
    temp=0
    while(num!=0):
        L[temp]=int(num%2)
        num=int(num/2)
        temp+=1
    return L[::-1]

def bin2dec(L):
    L=L[::-1]
    num=0
    pow_2=0
    for k in L:
        num=num+k*(2**pow_2)
##        print(num,k,pow_2)
        pow_2+=1
    return num


    
img=cv2.imread("lena.jpeg")
img=img[:,:,1]
img_mat=np.zeros((img.shape[0],img.shape[1],8))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_mat[i,j,:]=dec2bin(img[i,j])

name=[0,1,2,3,4,5,6,7,8]
for k in range(8):
    cv2.imshow(str(name[k]),img_mat[:,:,k])
    
img_mat[:,:,4]=0
img_re=np.zeros((img.shape))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_re[i,j]=bin2dec(img_mat[i,j,:])
print(img)
print(img_re)
cv2.imshow("Re con",img_re/255)
cv2.imshow("original",img)
