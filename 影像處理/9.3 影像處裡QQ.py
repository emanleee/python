# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:33:06 2020

@author: PC234
"""

import numpy as np
import cv2

a=np.array([80,97,89,65,90])
y=np.zeros([700,700,3],dtype="uint8")#全黑整數 ,3 三個維度
print(a.mean(),a.std())#平均值
b=np.array([50,77,100,91,20])
print(b.mean(),b.std())
c=np.array([78,60,56,75,79])
print(c.mean(),c.std())

cv2.rectangle(y,(100,699),(200,int(699-7*a.mean())),(0,0,255),-1)
cv2.line(y,(150,int(699-7*a.mean()+7*a.std()/2)),
         (150,int(699-7*a.mean()-7*a.std()/2)),(255,255,255),4)

cv2.rectangle(y,(300,699),(400,int(699-7*b.mean())),(0,255,0),-1)
cv2.line(y,(350,int(699-7*b.mean()+7*b.std()/2)),
         (350,int(699-7*b.mean()-7*b.std()/2)),(255,255,255),4)

cv2.rectangle(y,(500,699),(600,int(699-7*c.mean())),(255,0,0),-1)
cv2.line(y,(550,int(699-7*c.mean()+7*c.std()/2)),
         (550,int(699-7*c.mean()-7*c.std()/2)),(255,255,255),4)

cv2.imshow("img",y)
cv2.waitKey();