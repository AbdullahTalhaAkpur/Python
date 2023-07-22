# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:43:34 2023

@author: Abdullah
"""

NewMaas = 0
maas = input("Maaş Gir : ")
zam = input("Zam Oranı(%) : ")

yeniMaas = int(maas) + (int(maas)* int(zam)/100)
print("Zamlı Maaş :", yeniMaas)