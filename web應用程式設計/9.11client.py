# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:48:58 2020

@author: user
"""

# -*- coding: utf-8 -*-
def List2word(List):
    word=''
    for i in range(len(List)):
        word+=str(List[i])
        word+=' '
    return word

def wordtolist(word):
    List=[]
    Wordsave=''
    for i in word:
        if i != " ":
            Wordsave+=i
        else:
            List.append(int(Wordsave))
            Wordsave=""
    return List
    

import socket
import time
import random as r
a=r.randint(1,4) #隨機產生一個1~4的數字

HOST = '140.134.210.141'
PORT = 48763
clientMessage = '19 1 77 20 30 6'
clientMessage1 = "I am Delay QQ"
List=[19,1,77,20,30,6]
word=List2word(List)
#word=19 1 77 20 30 6
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

#延遲時間
tStart = time.time()
time.sleep(a)
tEnd = time.time()
Total_time = tEnd - tStart
print(Total_time)

if Total_time > 5:
    client.sendall(clientMessage1.encode()) #Send message
else:
    client.sendall(clientMessage.encode()) #Send message
serverMessage = str(client.recv(1024), encoding='utf-8')
print('Server List sorted:', serverMessage)

client.close()
