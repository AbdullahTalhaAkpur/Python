# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:36:02 2023

@author: Abdullah
"""

sayi = int(input("Sayi : "))

faktoriyel = 1

if sayi < 0 :
    print("Negatif sayıların faktoriyeli hesaplanamaz")
elif sayi == 0:
    print("Sonuc : 1")
else:
    for i in range(1, sayi + 1) :
        faktoriyel = faktoriyel * i
    print("Sonuç : ",faktoriyel)