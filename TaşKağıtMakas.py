# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 00:57:38 2023

@author: Abdullah
"""

import random
secenek=["taş","kağıt","makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
print("Taş,Kağıt, Makas oyununa hoş geldiniz. "  "Oyunu bitirmek için r tuşuna basın")
while True:
    secim = input("Taş mı kağıt mı makas mı? ")
    bilgasayar_secim = random.choice(secenek)
    if secim==taş:
        if  bilgasayar_secim==taş:
            print("Bilgisayarın seçimi: Taş  Sonuç: Berabere")
        elif  bilgasayar_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt Kaybettiniz")
        else:
            print("Bilgisayarın seçimi: Makas Sonuç: Kazandınız")
    if secim==kağıt:
        if  bilgasayar_secim==taş:
            print("Bilgisayarın seçimi: Taş Sonuç: Kazandınız")
        elif  bilgasayar_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: Makas Sonuç: Kaybettiniz")
    if secim==makas:
        if  bilgasayar_secim==taş:
            print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
        elif  bilgasayar_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
        else:
            print("Bilgisayarın seçimi: Makas Sonuç: Berabere")
        if secim=='e':
            print("Çıkılıyor...")
            break