# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print("48763")   
print(ord("李"))                           #顯示出"李"這個字的ANSI編碼
x=97                                  
print(chr(x))                              #顯示出ANSI編碼下 x=97時代表的字元
for a in range (ord("李"),ord("李")+100):  #顯示出'李'以及這之後100個字的ANSI編碼
    print(chr(a),end=" ")
    print(chr(a).encode('utf-8'))          #列出這些字元的utf-8編碼
    
    
    #exercise 
    #計算兩點間音速從月球到地球的時間 
speed=1225
dist=384400
a=dist/speed
b=int(a/24)
c=round(a%24,3)
print(b,"天 ",c,"小時")

    #exercise
    #輸入點並計算兩點間距離
x1=int(input("x1=?"))
x2=int(input("x2=?"))
y1=int(input("y1=?"))
y2=int(input("y2=?"))

dist=((x1-x2)**2+(y1-y2)**2)**0.5
print("兩點間的距離是",dist)


#使用eval(解析數字並使用','隔開帶入變數)
#改變分隔用的字符可使用split(" ")改變

x1,y1,x2,y2=eval(input("輸入x1,y1,x2,y2用,隔開"))
dist=((x1-x2)**2+(y1-y2)**2)**0.5
print("({:4d},{:4d})和({:4d},{:4d})的距離是{:5.1f}".format(x1,y1,x2,y2,dist))
#.format是將變數依序帶入矩陣 ()中寫出要帶入哪些變數 
# d: decimal; f: float


#使用open()開啟檔案 #右邊的視窗路徑必須與檔案一致

f=open(file="abc.txt",mode="r") #mode開啟後模式為 r(read):讀取，a:換行並寫入，w:覆寫
aline=f.readline()              #讀取一行檔案中的文字
x1,y1,x2,y2=eval(aline)         #將讀取的數字輸入變數中
print("({:4d},{:4d})和({:4d},{:4d})的距離是{:5.1f}".format(x1,y1,x2,y2,dist))
f.close()                       #最重要的一行;讀取完記得關閉檔案


    #exercise練習寫出華氏與攝氏溫度之間的轉換

a=int(input("華氏溫度="))
float(b) #浮點數
b=(a-32)*5/9
print("攝氏溫度為",b)

c=int(input("攝氏溫度="))
d=(c*9/5)+32
float(d)
print("華氏溫度為",d)


#開啟檔案並讀取複數行字元並列出

gg=open(file="zxc.txt",mode="r")
aline1=gg.readline().replace('\n', '') #讀取一行並且刪掉換行(\n)然後用空格(' ')取代
aline2=gg.readline()                   #再讀取一行
aline3=gg.readline().replace('\n', '') #讀取第三行
aline4=gg.readline()                   #讀取第四行
a,b,c=eval(aline2)  #將第2行的變數代入
d,e,f=eval(aline4)
p=(a+b+c)/3
q=(d+e+f)/3
print("{:3s}的國英數成績為:{:4d},{:4d},{:4d} 平均為:{:5.1f}".format(aline1,a,b,c,p))
#平均為浮點數要用f表示 #.1表示取到小數一位
print("{:3s}的國英數成績為:{:4d},{:4d},{:4d} 平均為:{:5.1f}".format(aline3,d,e,f,q))
gg.close()


#使用if與elif

print("幫我撐十秒")
second=int(input("幾秒了"))
if (second>=10):
    print("48763")
elif (second<10):
    print("gg")


#使用連續if與elif判別條件

b,a=eval(input("安安你好多高幾歲"))
tall=(a>=180)
young=(b>=20 and b<30) #設定變數條件 符合為1(ture) 不符為0(false)
if(young and tall):
    print("打籃球拉幹")
elif (tall and not young):
    print("去打排球")
elif(young and not tall):
        print("打棒球")
elif not (tall and young ): #也可寫成 elif (not tall and not young):
            money=int(input("哩五幾某?年收多少?"))
if(money<1000000):
   print("去睡覺")
elif(money>=1000000):
    print("來打高爾夫球")
    

#8/6 Exercise 1
#練習讀出並排列出檔案中字元
        #張三 100,20,50
        #李四 90,50,100
#string.split(' ')

qq=open(file="zxc.txt",mode='r')
aline1=qq.readline()
aline2=qq.readline()
name,grade=aline1.split(' ')#從空白處將名字與分數分別變成兩個變數
name2,grade2=aline2.split(' ')
a,b,c=eval(grade)
d,e,f=eval(grade2)
p=(a+b+c)/3
q=(d+e+f)/3
print("{:3s}的國英數成績為:{:4d},{:4d},{:4d}平均為:{:5.1f}".format(name,a,b,c,p))
print("{:3s}的國英數成績為:{:4d},{:4d},{:4d}平均為:{:5.1f}".format(name2,d,e,f,q))
qq.close()


#8/6 Exercise 2

tall,kg=eval(input("身高體重?"))
mtall=tall/100
bmi=round(kg/(mtall**2),2)
print("你的bmi是:",bmi)
normal=(bmi>=18.5 and bmi<=24)
thin=(bmi<18.5)
fat=(bmi>24)
if (normal and bmi>=20 and bmi<=22):
    print("hen棒喔 你是正常人")
elif(bmi>22 and bmi<24):
    print("有一點點ㄈ喔")    
elif(bmi>18.5 and bmi<20):
    print("有一點點瘦喔")    
elif (fat):
    print("去減肥啦幹")
elif (thin):
    print("記得多ㄘ一點")
    

#8/10上課
    
    
    #判斷分數 修改程式
g = int(input('your grade'))
if (g >= 90):
      print ('excellent')
elif  g >= 60:
   print ('pass')
   print ('good')
elif g>= 50:
   print ('almost pass')
else:
   print ('fail')
   print ('not good')
print ('end of report')


#判斷輸入的點是否在園內
a,b=eval(input("輸入座標 用點隔開:"))
r=20
if (a**2+b**2>r**2):
    print("你在圓外")
elif (a**2+b**2<=r**2):
    print("你在圓內")
    
    #自主練習
    #1.假設今天是星期日，請輸入天數days，本程式可以回應days天後是星期幾
aday = int(input('幾天後'))
if (aday%7<1):
    print("今天禮拜天")
elif (aday%7<2):
    print("今天禮拜一")
elif (aday%7<3):
    print("今天禮拜二")
elif (aday%7<4):
    print("今天禮拜三")
elif (aday%7<5):
    print("今天禮拜四")
elif (aday%7<6):
    print("今天禮拜五")
    
    
    #假設麥當勞打工每週領一次薪資，工作基本時薪是150元，其它規則如下：
    #小於40小時(週)，每小時是基本時薪的0.8倍。
    #等於40小時(週)，每小時是基本時薪。
    #大於40至50(含)小時(週)，每小時是基本時薪的1.2倍。
    #大於50小時(週)，每小時是基本時薪的1.6倍。
    #請輸入工作時數，然後可以計算週薪。
hour=int(input("你這禮拜工作多久:"))
if (hour<40):
    print("這禮拜的薪水有:",hour*150*0.8)
elif(hour!=40):
     print("這禮拜的薪水有:",hour*150)
elif(hour <=50 ):
     print("這禮拜的薪水有:",hour*150*1.2)
elif(hour >50 ):
     print("這禮拜的薪水有:",hour*150*1.6)     


#串列(序列)
    
    
list=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
grades=['分數',list,list2]
grades[1][3]+grades[2][8]
list[1:5]
list[-1]


#打包多於數字給某一變數
a,b,*c=1,2,3,4,5
print(a,b,c)


#給定亂數
grades = [0]*12                   #序列為12個0
import random as r                #輸入亂數模組用r作為代稱
for i in range(12):               #for迴圈 將變數i執行12次
    grades[i] = r.randint(0,100)  #序列的第i位依次數隨機生成0~100之間的實數並帶入
grades.sort()                     #將序列依大小排序
 
gg=[1,2,3,4,5,6]
del gg[0:6:2]                    #刪除gg這個序列中第0個開始到第6個結尾，間隔2


#in的用法
season = '春 夏 秋 冬'
season = season.split(' ')  #用空格把season變為有4個元素的序列

m = input('What is your favorite season? ')
if (m in season):
    print ('asfdasf')
else:
    print ('error')    

#一般寫法
season = '春 夏 秋 冬' 
season = season.split(' ') #用空格把season變為有4個元素的序列
m = eval(input('Month= ? '))
if (m <= 3 and m >= 1):
    s = season[0]
elif (m <= 6 and m >= 4):
    s = season[1]
elif (m <= 9 and m >= 7):
    s = season[2]
elif (m <= 12 and m >= 10):
    s = season[3]
else:
    s = 'Error'
print (s)


#簡單物件導向

ball=input("你喜歡打羽球嗎?YES or NO:")
word=ball.lower().strip()
if (word in ['yes','y']):
    print("蚌ㄛ")
elif (word in ['no','n']):
    print("乾")
    #lower( )：將字串轉成小寫字。(6-2-1節)
    #upper( )：將字串轉成大寫字。(6-2-1節)
    #title( )：將字串轉成第一個字母大寫，其它是小寫。(6-2-1節)
    #rstrip( )：刪除字串尾端多餘的空白。(6-2-2節)
    #lstrip( )：刪除字串開始端多餘的空白。(6-2-2節)
    #strip( )：刪除字串頭尾兩邊多餘的空白。(6-2-2節)
    #center( )：字串在指定寬度置中對齊。(6-2-3節)
    #rjust( ) ：字串在指定寬度靠右對齊。(6-2-3節)
    #ljust( )：字串在指定寬度靠左對齊。(6-2-3節)


#成績列表

ooo=open(file="st.txt",mode='r')
st=[]
aline1=ooo.readline().split(' ')
st.append(aline1)
aline2=ooo.readline().split(' ')
st.append(aline2)
aline3=ooo.readline().split(' ')
st.append(aline3)
aline4=ooo.readline().split(' ')
st.append(aline4)

st[0][1]=int(st[0][1])
st[0][2]=int(st[0][2])
st[0][3]=int(st[0][3])

st[1][1]=int(st[1][1])
st[1][2]=int(st[1][2])
st[1][3]=int(st[1][3])

st[2][1]=int(st[2][1])
st[2][2]=int(st[2][2])
st[2][3]=int(st[2][3])

st[3][1]=int(st[3][1])
st[3][2]=int(st[3][2])
st[3][3]=int(st[3][3])
ooo.close()
    
    
#簡易加密
love='i love python'
love_str=list(love)
x=love_str[:]
for i in range(len(love_str)):
    x[i]=chr(ord(love_str[i])+1)
    
    love_en=''.join(x)
    
    
    #for迴圈加法
total=0
for i in range(1,11):
    total=total+i
    
    #
total=0
for i in range(1,101,2):
    total=total+1
    print(i,total)
    
    #用index找某自在字串中的位置
    love='i love python'.split(' ')
print(love.index('love'))    
    

    #印個三角形
for i in range(5):
      i=i+1
      print('*'*i)
    
    
    #印個倒三角形
a=6
for i in range(5):
    a=a-1
    print('*'*a)
    
    
    #找字
ppp=open(file="asd.txt",mode='r')
aline1=ppp.readline()
a=list(aline1)
for i in range(len(a)):
    if ( "風" not in a):
        print("done")
    elif( "風" in a):
        print(a.index('風'))
    g=a.index('風')
    del a[g]
    
        
    #請用 for 迴圈印出三個人的成績，及平均
names = ['james', 'nick', 'jonathan']
eng = [12,23,90]
math=[100,99,98]
phy=[54,66,88]

for i in range(len(names)):
    n, e, m, p = names[i], eng[i], math[i], phy[i]
    av = round((e+m+p)/3, 2)
    grade_str = '{}: {}, {}, {}, 平均={}'.format(n, e, m, p, av)
    print (grade_str)
    
    #請用 for 迴圈印出三個人的成績，及平均與三科的 平均成績
names = ['james', 'nick', 'jonathan']
eng = [12,23,90]
math=[100,99,98]
phy=[54,66,88]
eeng=0
mmath=0
pphy=0
for i in range(len(names)):
    n, e, m, p = names[i], eng[i], math[i], phy[i]
    av = round((e+m+p)/3, 2)
    eeng=(eeng+eng[i])/
    mmath=(mmath+math[i])/
    pphy=(pphy+phy[i])/
    grade_str = '{}: {}, {}, {}, 平均={}，各科平均;英文:{:4.1f}數學:{:4.1f}物理:{:4.1f}'.format(n, e, m, p, av,eeng,mmath,pphy)
    print (grade_str)
    
    
    
# 一個個打的方法
eng_av = round(sum(eng)/len(eng),2)
math_av = round(sum(math)/len(math),2)
phy_av = round(sum(phy)/len(phy),2)
print ('Eng average: ', eng_av)
print ('Math average: ', phy_av)
print ('Phy average: ', phy_av)

# 利用迴圈的做法，更棒
subject = 'eng math phy'.split(' ')
g =[eng, math, phy]
for i in range(len(subject)):
    sub, av = subject[i], round(sum(g[i])/len(g[i]),2)
    print ('{} average: {}'.format(sub.title(), av))



    
    
    
    