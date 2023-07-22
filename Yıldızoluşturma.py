# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:08:59 2023

@author: Abdullah
"""

sayi = int(input("Kaç yıldız olsun ?"))

yıldız = ""

for x in range(1,sayi + 1):
    yıldız = yıldız + "*"
    print(yıldız)