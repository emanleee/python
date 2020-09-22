# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:35:33 2020

@author: user
"""
word='1 99 30 70 50'
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
    

def List2word(List):
    word=''
    for i in range(len(List)):
        word+=str(List[i])
        word+=' '
    return word

import time
import socket
HOST = '140.134.210.141'
PORT = 48763


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
Output=[]


i=0
while True:
    
    conn, addr = server.accept() #連接客戶端
    constart=time.time()  #紀錄執行到現在時間
    clientMessage = str(conn.recv(1024), encoding='utf-8')#1024位元,用utf-8解碼
    conend=time.time()    #記錄執行到現在時間
        
    
    
    i=i+1
    print('這是第',i,"次 clientMessage:", clientMessage)
    Output=sorted(wordtolist(clientMessage))
    serverMessage = List2word(Output)
    serverMessage2 = 'toooooo late'
    
    print(conend-constart)#顯示連接後到收到訊息的時間
    if conend-constart>5:
        
        conn.sendall(serverMessage2.encode())
    else:
        conn.sendall(serverMessage.encode()) #加密為二進制
    conn.close()