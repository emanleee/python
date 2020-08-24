# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:23:46 2020

@author: PC234
"""

#生成鋪克牌列表
def poker():
    n = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
    x = ['Heart', 'Spare', 'Dimand', 'Club']    
    p = []
    for i in x:
        for j in n:
          p.append(i + ':' + j)           
    return p      

print (poker())


#打亂並且發牌
import random
def getPoker13():
    p = poker()
    random.shuffle(p)
    players = []
    players.append(p[0:13])
    players.append(p[13:26])
    players.append(p[26:39])
    players.append(p[39:])
    
    return players


#印出各玩家的持牌
def showPlayers(players):
    for i, p in enumerate(players):
       print ('\n Players '+str(i))
       print (p)
       
       
       


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    