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

def mai(s):
    headers = {'cookie': 'ECC=GoogleBot',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                }
    s = str(s)
        
    aa=[]
    for p in range(5):   
        url ="https://www.lativ.com.tw/Search/DataList?keyword={}&ec=0&t=0&page={}&category=ALL&cacheID=36182".format(s,p)
        res = requests.get(url,headers=headers)
        data = json.loads(res.text)
        
    for i in range(len(data)):
        print(str(data[i]['Name'])+str(data[i]['Price']))
        aa.append(data)
    
    return data

    


def cloth(aa):
    with open('a.csv', 'a' , encoding = 'utf-8-sig' , newline = '') as csvfile:
        w = csv.writer(csvfile)
        filednames=(['名稱','價格','圖1'])
        w = csv.DictWriter(csvfile,fieldnames=filednames)
        w.writeheader()
        sleep(0.7)                    
        for i in range(len(aa)):
            for j in range(len(aa[i])):
                w.writerow({'名稱':aa[i][j]['Name'],
                            '價格':aa[i][j]['Price'],
                            '圖1':"https://s2.lativ.com.tw" + aa[i][j]['Image']})
        return aa


def text_cleanup(text):
    new =""
    for i in text:
        if i not in'\?.!/;:"*<>|':
            new += i
    return new



def get_ph(aa):
    for i in range(len(aa)):
        for j in range(len(aa[i])):
                url_1 = "https://s2.lativ.com.tw" + aa[i][j]['Image']
                path =  aa[i][j]['Name']
                title = text_cleanup(path)
                filepath_1 =  title + '/' + "1" + '.jpg'
                if not os.path.isdir(title):  #檢查是否已經有了
                    os.mkdir(title) #沒有的用標題建立資料夾
                    
                    if not os.path.isfile(filepath_1): #檢查是否下載過圖片，沒有就下載
                        wget.download(url_1,filepath_1)
                        
    return aa


                        