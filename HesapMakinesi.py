# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:10:03 2023

@author: Abdullah
"""

def topla(x,y):
    return x + y

def cikar(x,y):
    return x - y

def carp(x,y):
    return x * y

def bol(x,y):
    return x / y

print("İşlemi seç")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Yapmak istediğin işlem: ")

sayi1 = float(input("İlk sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print(sayi1,"+",sayi2,"=", topla(sayi1,sayi2))

elif secim == '2':
    print(sayi1,"-",sayi2,"=",cikar(sayi1,sayi2))
    
elif secim == '3':
    print(sayi1,"*",sayi2,"=", carp(sayi1,sayi2))

elif secim == '4':
    print(sayi1,"/",sayi2,"=", bol(sayi1,sayi2))    