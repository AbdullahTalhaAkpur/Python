# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 01:45:01 2023

@author: Abdullah
"""

vize_notu = float(input("Vize notunu gir:"))

final_notu = float(input("Final notunu gir: "))

vize_notu = vize_notu * 0.4
final_notu = final_notu * 0.6
ortalama = vize_notu + final_notu

print("Ortalamanız: {}".format(ortalama) )

if ortalama >= 55:
    print("Geçtiniz")
    
else : 
   print("Kaldınız")