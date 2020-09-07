# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:29:52 2020

@author: PC234
"""
import numpy as np
import cv2

img=cv2.imread("asd.jpg",-1)#-1圖片原始資料載入  0為黑白圖片
cv2.imshow("img",img)
cv2.waitKey()


cv2.imwrite("test.bmp",img)
cv2.imwrite("test.jpg",img)
a=cv2.imread("test.bmp")
b=cv2.imread("test.jpg")



# import numpy as np
import cv2

img=cv2.imread("asd.jpg",-1)#-1圖片原始資料載入  0為黑白圖片
cv2.imshow("img",img)
cv2.waitKey()

#彩色圖片由B(0)>G(1)>R(2)三個圖層所建立
img_B=np.zeros([352,512,3],dtype="uint8") #建立黑圖 長寬與原本圖片大小一樣,3是宣告為三維圖層
img_G=np.zeros([352,512,3],dtype="uint8")
img_R=np.zeros([352,512,3],dtype="uint8")
img_B[:,:,0]=img[:,:,0] #將img_B這個新圖層的第0層(藍色圖層)等於原始圖片的第0層，導入圖片
                        #(與原始圖哪一層沒關西，顏色是img_B給的，重點是要原圖
img_G[:,:,1]=img[:,:,1]
img_R[:,:,2]=img[:,:,2]
cv2.imshow("img_B",img_B)#顯示圖片
cv2.imshow("img_G",img_G)
cv2.imshow("img_R",img_R)
cv2.waitKey()            #暫留視窗



global img

def onMouse(event,x,y,flags,param):
    x,y=y,x
    if img.ndim !=3:
        print("(x,y)=%d,%d"%(x,y),end=" ")
        print("Gray-Level=%3d:" % img[x,y])
    else:
        print("(x,y)=%d,%d"%(x,y),end=" ")
        print("R,G,B=(%3d,%3d,%3d)"%(img[x,y,2],img[x,y,1],img[x,y,0]))
        
img=cv2.imread("asd.jpg",-1)
cv2.namedWindow("onMouse")
cv2.setMouseCallback("onMouse",onMouse)
cv2.imshow("onMouse",img)
cv2.waitKey()



import numpy as np
import cv2

cap=cv2.VideoCapture('video.avi')
while(cap.isOpened()):
    ret,frame=cap.read()
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





import numpy as np
import cv2
import time

# 讀取預先建立好的Haar Cascade 模型
face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_eye.xml')

sTime = time.time()
# 讀取圖檔並轉成黑白圖(供haar cascade使用)
img = cv2.imread('qwe.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#偵測臉部
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#對於每一個找到的臉部
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # 在臉的範圍之內搜尋眼睛的位置
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
eTime = time.time()

# 輸出並結束程式
print("執行完畢，費時"+str(eTime-sTime)+"秒")
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
















