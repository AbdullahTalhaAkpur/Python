# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:19:55 2023

@author: Abdullah
"""

#Kenarları verilen dikdörtgenin alanı ve çevresini hesaplama 
#tabiki diğer geometrik cisimler için formüllerini uygulayıp alan ve çevresini bulabilirsiniz

kisa = input("Kısa Kenar : ")
uzun = input("Uzun Kenar : ")

alan = int(kisa)*int(uzun)
cevre = 2*(int(kisa) + int(uzun))

print("Alan : {0}".format(alan))
print("Çevre : {0}".format(cevre))