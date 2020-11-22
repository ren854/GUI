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
    headers = {'cookie': 'EAll_Ph_Url=GoogleBot',
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
#print(b)




#全部產品網址
def LAPD(m):
    Lativ_APD=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
            url = "https://www.lativ.com.tw/Detail/" + m[i][j]["Col"][1]["Sn"]
            #print(url)
            Lativ_APD.append(url)
    return Lativ_APD    
 

#將json存成csv檔
def cloth(m):
    if not os.path.isdir('.//output'):  #檢查是否已經有了
        os.mkdir('.//output')
    with open('.//output//Lativ.csv', 'a' , encoding = 'utf-8-sig' , newline = '') as csvfile:
            w = csv.writer(csvfile)
            filednames=(['名稱','價格','網址'])
            w = csv.DictWriter(csvfile,fieldnames=filednames)
            w.writeheader()
            sleep(0.7)
            for i in range(len(m)):                
                for j in range(len(m[i])):
                    w.writerow({'名稱':m[i][j]['Name'],
                                '價格':m[i][j]['Price'],
                                '網址':"https://www.lativ.com.tw/Detail/" + m[i][j]["Col"][1]["Sn"]})


#將需要圖片網址存成List
def APU(m,pg):
    All_Ph_Url=[]
    #s = []
    #m = mai(s)
    for i in range(0,pg):
        #print(bb[i])
        response = requests.get(LAPD(m)[i])
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup.prettify())  #輸出排版後的HTML內容
        result = soup.find_all("img")
        #print(result[0])
        aa=[]
        for j in result:
            #print(j.get('data-original'))
            aa.append(j.get('data-original'))
        All_Ph_Url.append(aa)
        print("讀取中...")
    return All_Ph_Url
################## 這裡pg輸入太大 資料要讀比較多 會跑很久 所以 抓圖也會跑很久 ###################

#抓圖
def get_html_ph(m,pg):
    print("開始抓圖")
    aaa=APU(m,pg)
    for i in range(0,pg):
            print("再來再來")
            #print(APU[i][j])
            path = ".//output/" + "No." + str(i+1)
            #print(path)
            title = path
            if not os.path.isdir(title):  #檢查是否已經有了
                os.mkdir(title) #沒有的用標題建立資料夾
                for j in range(3,10):
                    url_1 = aaa[i][j] ####直接Call APU() 會跑很慢 所以設定成aaa 慢的原因不明###
                    filepath_1 =  title + '/' + str(j-2) + '.jpg'
                    print(filepath_1)
                    if not os.path.isfile(filepath_1): #檢查是否下載過圖片，沒有就下載
                        wget.download(url_1,filepath_1)

if __name__== "__main__":

    s = str(input("要抓哪種類型的衣服呢?"))    
        
    print("開始讀取資料")

    m=mai(s)

    print("最大圖片數量為"+ str(len(LAPD())))

    pg = int(input("請輸入要抓的圖片數量"))
    
#APU(pg)
#get_html_ph(pg)


''' 消除非法字元 暫時用不到
def text_cleanup(text):
    new =""
    for i in text:
        if i not in'\?.!/;:"*<>|':
            new += i
    return new

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
