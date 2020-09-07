# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#自主上機考前練習 


#8/23

#習題7.16進階

def gcd(a,b):
    d=[]
    for i in range(1,min(a,b)+1):
       if a%i==0 and b%i==0 :
          d.append(i)
          j=i
          l=a*b/j
    return d,j,l



a,b=eval(input("輸入兩個數求最大公因數和最小公倍數:\n "))
e,k,m=gcd(a,b)
print("({},{})的公因數有:{}\n最大公因數是:{}\n兩者的最小公倍數是:{}".format(a,b,e,k,m))
    

#習題 9-1

months={'一月':'January','二月':'February','三月':'March','四月':'April','五月':'May','六月':'June','七月':'July',
        '八月':'August','九月':'September','十月':'October','十一月':'November','十二月':'December'}
mon_ch=input("幾月?:")
if mon_ch in list(months.keys()):
    print(months[mon_ch])
else:
     print("打月份拉幹")
    
#習題9-10

abc = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
listabc=list(abc)
abc3=listabc[:3]
abc3plus=listabc[3:]
abbc=abc3plus+abc3
abclist=dict(zip(abbc,abc))

cgpass=[]
passcode=input("密碼為:")
for i in list(passcode):
    k=abclist[i]
    cgpass.append(k)
    
cgpasstext=''.join(cgpass)
print("更變後的密碼為:\n",cgpasstext)


#第十章
#10-1.10-4.10-5.10