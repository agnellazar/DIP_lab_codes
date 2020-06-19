#Written by Agnel Lazar Alappat
import cv2
import numpy as np
img=[[1,2, 6,7],[3,5,8,13],[4,9,12,14],[10,11,15,16]]
print("Input sequence")
print(img)
img=np.array(img)
m,n=img.shape

i=0
j=1
swipe=1
i_off=1
j_off=-1
lin=[]
lin.append(img[0,0])
for loop_count in range(14):
##        print(img[i,j],i,j,swipe,"j_off"+str(j_off)+"  i_off"+ str(i_off))
##        print()
        lin.append(img[i,j])
        if((j==0 or  i==m-1)and swipe==0):
            if(i==m-1):
                j=j+1
            else:
                i+=1
            j_off=1
            i_off=-1
            swipe=1
        elif((i==0 or  j==n-1) and swipe==0):
            if(j==n-1):
                i=i+1
            else:
                j+=1
            j_off=-1
            i_off=1
            swipe=1
        else:
            i+=i_off
            j+=j_off
            swipe=0

print("Output sequence")        
print(lin)

if len(img.ravel())<len(lin):
	print("Compression Ratio is:", len(lin)/len(img.ravel()))
else:
	print("Negative compression Ratio")
