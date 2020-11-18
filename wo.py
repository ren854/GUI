# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:04:59 2020

@author: candy
"""

import requests
from bs4 import BeautifulSoup

def mai():
    r=requests.get("https://www.lativ.com.tw/WOMEN")
    soup=BeautifulSoup(r.text,"html.parser")
    sel=soup.select("div.container_48 a")
    print(sel)

def ttext(sel):
    for s in sel:
        print(s.text)
        
        
    
    import csv
    
    
    with open('clothes.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
      
      writer = csv.writer(csvfile,delimiter=' ')
    
      
      for s in sel:
         writer.writerow(s.text)

  