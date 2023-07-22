# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:06:18 2023

@author: Abdullah
"""


def fibonacci():
    
    num = int(input("Kaç tane fibonnaci sayıları üretmek istersin? "))
    
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib 
 
print(fibonacci())
input()      