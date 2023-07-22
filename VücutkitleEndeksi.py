# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 01:12:50 2023

@author: Abdullah
"""

weight = float(input("Enter your weight: "))
height = int(input("Enter your height(cm):"))
vki = weight / ((height/100)**2)
print("Vücut kitle indexin {}".format(round(vki,2)))
print("Durumunuz:")

if vki <=18.5:
    print("Zayıf")
    print("{} kilogram almanız gerekiyor".format(round(18.5*((height/100)**2)-weight,2)))
elif vki <=24.9:
    print("Normal")
elif vki<=29.9:
    print("Fazla kilolu")
    print("{} kilogram vermeniz gerekiyor".format(round(weight-24.9*((height / 100) ** 2)),2))
elif vki<=39.9:
    print("Obez")
    print("{} kilogram vermeniz gerekiyor".format(round(weight - 24.9 * ((height / 100) ** 2)), 2))
else:
    print("Aşırı obez")
    print("{} kilogram vermeniz gerekiyor".format(round(weight - 24.9 * ((height / 100) ** 2)), 2))