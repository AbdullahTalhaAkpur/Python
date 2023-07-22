# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:48:30 2023

@author: Abdullah
"""

import calendar

print("Bir yıl girin: ")
yy = input() #yıl değerini alan komut
print("\nBir ay girin: ")
mm= input()  #ay değerini inputla aldık 

y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m)) #bu kısım takvimde olduğu gibi ay ve yılı en üst kısma yazmamızı print ettik