# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 16:43:49 2023

@author: Abdullah
"""

secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız : ")
ogrenci = input("Öğrenci misiniz(E/H) : ")
ucret = 0

#indirimsiz fiyatı için
if secim == '1' :
    ucret = 70 # sinema
elif secim == '2' :
    ucret = 50 # tiyatro

#öğrenci indirimi 
if ogrenci == 'E' or ogrenci == 'e':
    ucret = ucret / 2 #%50    
    
print("Ödemeniz gereken ücret : {}".format(ucret))
