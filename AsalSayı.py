# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:52:17 2023

@author: Abdullah
"""

sayi = int(input("Sayı giriniz  : "))
asalmi = True
for x in range(2, sayi):
    if (sayi % x) == 0:
        asalmi = False
        break
    
if asalmi == True:
    print("ASAL")
else:
    print("ASAL DEĞİL")    