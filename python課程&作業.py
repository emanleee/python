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
aline1=qq.readline().split(' ')
uig=str(aline1)
aline2=qq.readline()
m,a,b,c=eval(uig)
n,d,e,f=eval(aline2)
print=(a)
p=(a+b+c)/3
q=(d+e+f)/3
print("{:3s}的國英數成績為:{:4d},{:4d},{:4d}平均為:{:5.1f}".format(m,a,b,c,p))
print("李四的國英數成績為:{:4d},{:4d},{:4d}".format(d,e,f),"平均為:",q)
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
    



