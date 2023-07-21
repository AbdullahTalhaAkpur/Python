# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:01:45 2023

@author: Abdullah
"""

#Boş liste oluştur
todoList = []

#listeye eklenen fonksiyon
def addTask(todoList):
    task = input("Yapılacak görevi girin: ")
    todoList.append(task)
    print("Görev başarıyla eklendi ")
    
#listedeki görevleri gösteren fonksiyon
def showTask(todoList):
    print("Yapılacak Görevler:")
    for task in todoList:
        print("-", + task)
        
#Silmek istediğiniz görevi yazan fonksiyon
def deleteTask(todoList):
    task = input("Silmek istediğiniz görevi girin: ")
    if task in todoList:
       todoList.remove(task)
       print("Görev başarıyla silindi")
    else:
        print("Görev bulunamadı")
        
while True:
   print("\nTo-Do List Uygulaması")
   print("1. Görev Ekle")
   print("2. Görevleri Göster")
   print("3. Görev Sil")
   print("4. Çıkış")
   choice = input("Seçiminiz (1/2/3/4): ")
   break
   
if choice == "1":
        addTask(todoList)
elif choice == "2":
        showTask(todoList)
elif choice == "3":
        deleteTask(todoList)
elif choice == "4":
   print("Uygulamadan çıkılıyor...")
 
else:
   print("Geçersiz seçim. Lütfen tekrar deneyin.")