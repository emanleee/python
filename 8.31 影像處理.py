# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
FLOOR(4.5)+FLOOR(-4.5)
• CEIL(4.5) + CEIL(-4.5)
• 20 ∗ ARCTAN 1/7  + 8 ∗ ARCTAN 3/79
'''


import numpy as np

b=np.floor(4.5)
c=np.floor(-4.5)
d=b+c
print(d)


e=np.ceil(4.5)
f=np.ceil(-4.5)
g=e+f


h=np.arctan(1/7)
i=np.arctan(3/79)
j=(20*h+8*i)
print(j)


k=0
for ii in range(1,2000):
    k=k+(1/(ii*ii)) 
ll=(6*k)**0.5
print(ll)



aa=[[1,2],[3,4]]
bb=[[0,4],[1,1]]
cc=np.matmul(aa,bb)
print(cc)



x=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.mean(x))
print(np.std(x))
print(np.max(x))
print(x[x<4])

y=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.mean(y))
print(np.std(y))
print(y[y>6])
print(y.sum(axis=0))
print(y.sum(axis=1))

#黑白視窗
import cv2 
img1=np.zeros([512,512],dtype="uint8")
img2=np.ones([512,512],dtype="float32")
cv2.imshow("test1",img1) 
cv2.imshow("test2",img2) 
cv2.waitKey()

#黑白格子
import numpy as np
import cv2 
img=np.zeros([500,500],dtype="uint8")
for i in range(5):
    for j in range(5):
        if((i+j)%2==1):
            for k in range(100):
                for l in range(100):
                    img[i*100+k,j*100+l]=255
cv2.imshow("test",img) 
cv2.waitKey()        



img=np.zeros([500,500],dtype="float32")
for m in range(500):
    for n in range(500):
        





