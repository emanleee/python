# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:27:56 2020

@author: Visitor
"""
import cv2
import numpy as np

img=cv2.imread("penguin_noise.png")
ave=cv2.blur(img,(3,3))
med=cv2.medianBlur(img,3)

cv2.imshow("img",img)
cv2.imshow("average_img",ave)
cv2.imshow("medium_img",med)
cv2.waitKey()



def calcAndDrawHist(image, color):
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9* 256);
    
    for h in range(256):
        intensity = int(hist[h]*hpt/maxVal)
        cv2.line(histImg,(h,256), (h,256-intensity), color)
        
    return histImg;

img=cv2.imread("image.jpg",0)
his=calcAndDrawHist(img, (255,255,255))
cv2.imshow("histogram",his)
cv2.waitKey()

eqimg=cv2.equalizeHist(img)
his2=calcAndDrawHist(eqimg, (255,255,255))
cv2.imshow("img",img)
cv2.imshow("eqimg",eqimg)
cv2.imshow("his",his)
cv2.imshow("his2",his2)
cv2.waitKey()


