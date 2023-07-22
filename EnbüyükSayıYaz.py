# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:51:41 2023

@author: Abdullah
"""

sayi1 = int(input("1. Sayı : "))
sayi2 = int(input("2. Sayı : "))
sayi3 = int(input("3. Sayı : "))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBüyük = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBüyük = sayi2
else:
    enBüyük = sayi3

print("En Büyük : ", enBüyük)      