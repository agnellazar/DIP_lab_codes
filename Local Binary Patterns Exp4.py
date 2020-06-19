#Written by Agnel Lazar Alappat
import cv2
import numpy as np

def bin2dec(L):                                         # function to calculate decimal equilvalent
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
cv2.imshow("Original image",img)
m=img.shape[0]
n=img.shape[1]
## Padding
img_p=np.zeros((m+2,n+2))
img_p[0,:]=0
img_p[m+1,:]=0
img_p[:,0]=0
img_p[:,n+1]
img_p[1:m+1,1:n+1]=img
##print(img_p)

## creating new matrix
img_re=np.zeros((img_p.shape))
for  i in range(1,m+1):
    for j in range(1,n+1):
        num=list()
        temp1=img_p[i,j]
        a=i
        b=j
        b+=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        a-=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        b-=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        b-=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        a-=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
            a-=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        b+=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        b+=1
        if (temp1<img_p[a,b]):
            num.append(0)
        else:
            num.append(1)
        img_re[i,j]=bin2dec(num[::1])
        
cv2.imshow("reconstructed image",img_re/255)
print(np.max(img_re))

