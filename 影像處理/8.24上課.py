# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Student():
    
    def __init__(self,ssid,t,w):
        self.__sid=ssid
        self.__tall=160           #預設值 
        self.__weight=60          #預設值
        
    def Tall(self,t):
        self.__tall=t
        
    def Weight(self,w):
        self.__weight=w
        
    def getTall(self):
        return self.__tall/100
        
    def setTall(self,t):
        if (t<250 and t>120):
            self.__tall=t
        else:
            print("error")
        
        
    def toofat(self):
        if Student.bmi(self.__tall,self.__weight)>25:
            return True
        else:
            return False
        
    def bmi(t,w):
        return(w/((t/100)**2))
        
    def __str__(self):
       s = '{}, tall = {}, weight = {}. Is he too fat? {}'.format(self.sid,
            self.__tall, self.__weight, self.toofat())       
       return (s)
   
    def __repr__(self):
       return self.__str__()
              
    tall = property(getTall, setTall)     
  
s1 = Student('S101', 170, 60)

print (s1)    
s1 = Student('S101', 170, 60)       
print (s1.toofat())

s1.weight = 2000
s1.toofat()

s2 = Student('S102', 170, 60)       
print (s1.toofat())
print(s1.getTall())
s1.tall = 280
s1.setTall(280)


#測驗題


a=input("輸入一串數字").split()
n=list(reversed(a))
m=" ".join(n)
print(m)


'''
設計一個學生成績單的類別，裡面可以放學生的學號，姓名，各科的名稱與成績。
* 可以透過 s.getAverage() 回傳所有科目的平均。
* 可以透過 s.getScore(‘Math’) 回傳數學的成績，依此類推。
* 可以透過 s.setScore(‘Math’, 100) 設定數學的成績，依此類推。
* print (s) 時，會印出所有學生的資訊
'''

class GradeBook():
    
   def __init__(self, sid):
       self.__sid = sid
       self.__grade = dict()
              
   def setScore(self, sub, score):
       if score >= 0 and score <= 100:
          self.__grade[sub] = score
       else:
           print ('!!!!! Error !!!!!') 
       
   def getScore(self, sub):
       if self.__grade[sub] != None:
           return self.__grade[sub]
       else:
           print ('!!!! no such subject !!!!!')
   
   def getAverage(self):
       tot = sum(self.__grade.values())
       avg = tot/len(self.__grade.values())
       return avg

       
   def __str__(self):
       s = 'Student {}'.format(self.__sid)
       for sub, score in self.__grade.items():
          s += '\n {}: {}'.format(sub, score) 
       return (s)
   
   def __repr__(self):
       return self.__str__()
                
s1 = GradeBook('S101')
s1.setScore('Math', 100)
s1.setScore('Eng', 98)
print (s1.getScore('Math'))
print (s1.getAverage())

print (s1)



#延遲 sleep

import time                         # 導入模組time
print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))

t1 = time.time()
for i in range(10000):
    for j in range(1000):
        k = i * j
t2 = time.time()
print (t2-t1)
        

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
for fruit in fruits:
    print(fruit)
    #time.sleep(1)                   # 暫停1秒

import time                         # 導入模組time
print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))
t1 = time.time()
for i in range(10000):
    for j in range(1000):
        k = i * j
t2 = time.time()
print (t2-t1)
        

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
for fruit in fruits:
    print(fruit)
    #time.sleep(1)                   # 暫停1秒

print(time.asctime())               # 列出目前系統時間 
xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
time.sleep(1)       # 暫停1秒
print("月 ", xtime[1])
time.sleep(1)       # 暫停1秒
print("日 ", xtime[2])
time.sleep(1)       # 暫停1秒
print("時 ", xtime[3])
time.sleep(1)       # 暫停1秒
print("分 ", xtime[4])
time.sleep(1)       # 暫停1秒
print("秒 ", xtime[5])
time.sleep(1)       # 暫停1秒
print("星期幾   ", xtime[6])
time.sleep(1)       # 暫停1秒
print("第幾天   ", xtime[7])
time.sleep(1)       # 暫停1秒
print("夏令時間 ", xtime[8])

import sys

print("目前Python版本是: ", sys.version)
print("目前Python版本是: ", sys.version_info)



      # ch15_3.py 
def division(x, y):
    try:                        # try - except指令
        ans =  x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    else:
        return ans              # 傳回正確的執行結果

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division(6, 3))           # 列出6/3


# ch15_4.py

fn = 'app.txt'               # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    print(data)                 # 輸出變數data相當於輸出檔案





b=1
for a in range(1,101):
    c=1                #當c=1寫在外面 下一次迴圈時c還是上一個值沒歸回1
    p=a+1              #p改成a會有微小的誤差???為甚麼
    for o in range(1,p):
            c=c*o
    b=b+(1/c)
    if a%10==0:
        print("經過第{:3d}次計算後的結果為{}".format(a,b))
print("最終答案為",b)


#階乘
n=int(input("輸入n值:"))
n=n+1
s=1
for i in range(1,n):
    s=s*i
    print('第',i,'次'," ",s)
print(s)


    









