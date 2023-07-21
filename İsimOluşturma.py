# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:39:15 2023

@author: Abdullah
"""

import random 

def generate_name():
   first_names = ["Mehmet","Abdullah","Hikmet","Taha","Can"]
   last_names  = ["Akpur","Kandemir","Çevik","Aslan","Demir"]
   
   unique_first_name = random.sample(first_names, 1)[0]
   unique_last_name  = random.sample(last_names,  1)[0] 
   
   return "{} {}".format(unique_first_name, unique_last_name)


for i in range(5):
    print(generate_name())