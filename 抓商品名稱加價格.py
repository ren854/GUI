# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:38:34 2020

@author: candy
"""

import requests
import json
from time import sleep
import csv
import os
import wget

headers = {'cookie': 'ECC=GoogleBot',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
           }   
url ="https://www.lativ.com.tw/Product/GetNewProductCategoryList?MainCategory=WOMEN&pageIndex=0&cacheID=35976"
res = requests.get(url,headers=headers)
data = json.loads(res.text)

for i in range(len(data)):
    print(str(data[i]['ProductName'])+str(data[i]['Price']))

    
import csv


with open('price.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
  
  writer = csv.writer(csvfile,delimiter=' ')

  
  for i in range(len(data)) :
     writer.writerow(str(data[i]['ProductName'])+str(data[i]['Price']))