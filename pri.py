# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:38:34 2020

@author: candy
"""
import requests
from bs4 import BeautifulSoup
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

        
    db_list=[]
    for p in range(5):   
        url ="https://www.lativ.com.tw/Search/DataList?keyword={}&ec=0&t=0&page={}&category=ALL&cacheID=36182".format(s,p)
        res = requests.get(url,headers=headers)
        data = json.loads(res.text)
        
        for i in range(len(data)):
            db_list.append(data)
    
        return db_list

m=mai("大衣")    
#print(b)



def cloth(m):
    with open('Lativ.csv', 'a' , encoding = 'utf-8-sig' , newline = '') as csvfile:
        w = csv.writer(csvfile)
        filednames=(['名稱','價格','圖1','網址'])
        w = csv.DictWriter(csvfile,fieldnames=filednames)
        w.writeheader()
        sleep(0.7)                    
        for i in range(len(m)):
            for j in range(len(m[i])):
                w.writerow({'名稱':m[i][j]['Name'],
                            '價格':m[i][j]['Price'],
                            '圖1':"https://s2.lativ.com.tw" + m[i][j]['Image'],
                            '網址':"https://www.lativ.com.tw/Detail/" + m[i][j]["Col"][1]["Sn"]})
cloth(m)

def text_cleanup(text):
    new =""
    for i in text:
        if i not in'\?.!/;:"*<>|':
            new += i
    return new


'''
######################################圖片漏抓#####################################
def get_ph(aa):
    for i in range(len(aa)):
        for j in range(len(aa[i])):
                url_1 = "https://s2.lativ.com.tw" + aa[i][j]['Image']
                path =  str(aa[i][j]["Col"][1]["Sn"])
                title = text_cleanup(path)
                filepath_1 =  title + '/' + "1" + '.jpg'
                if not os.path.isdir(title):  #檢查是否已經有了
                    os.mkdir(title) #沒有的用標題建立資料夾
                    
                    if not os.path.isfile(filepath_1): #檢查是否下載過圖片，沒有就下載
                        wget.download(url_1,filepath_1)
                        
get_ph(m)      ####################這個不要
'''




bb=[]
for i in range(len(m)):
    for j in range(len(m[i])):
        url = "https://www.lativ.com.tw/Detail/" + m[i][j]["Col"][1]["Sn"]
        #print(url)
        bb.append(url)
                
cc=[]
for i in range(0,10):
    #print(bb[i])
    response = requests.get(bb[i])
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())  #輸出排版後的HTML內容
    result = soup.find_all("img")
    #print(result[0])
    aa=[]
    for j in result:
        #print(j.get('data-original'))
        aa.append(j.get('data-original'))
    cc.append(aa)



for i in range(0,10):    
    for j in range(3,10):
        #print(i)
        #print(cc[i][j])
        url_1 = cc[i][j]
        path = "No." + str(i+2)
        #print(path)
        title = path
        if not os.path.isdir(title):  #檢查是否已經有了
            os.mkdir(title) #沒有的用標題建立資料夾
            
            filepath_1 =  title + '/' + str(j-2) + '.jpg'        
            if not os.path.isfile(filepath_1): #檢查是否下載過圖片，沒有就下載
                wget.download(url_1,filepath_1)
##############################圖片只會抓一張 應該每個資料夾有7張 迴圈有問題

