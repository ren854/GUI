import requests
import json
from time import sleep
import csv
import os
import wget

headers = {'cookie': 'ECC=GoogleBot',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

#將所有產品的網址存成一個list
def prods_list(serch,p):
    list1=[]
    for num in range(1,p):
        page_url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page={}&sort=sale/dc'.format(serch,num)
#print(page_url) #所有頁面網址
        sleep(0.7)        
        res1 = requests.get(page_url,headers=headers)
        data1 = json.loads(res1.text)
#print(data1) #頁面的內容
        webdata = data1['prods']
        list1.append(webdata)
    return list1   

#ts=prods_list(serch,p)
#print(ts)
 


#把需要的資訊存入CSV
def csv_1():
    with open('a.csv', 'a' , encoding = 'utf-8-sig' , newline = '') as csvfile:
            w = csv.writer(csvfile)
            filednames=(['名稱','網路價','網址','圖1','圖2'])
            w = csv.DictWriter(csvfile,fieldnames=filednames)
            w.writeheader()
            sleep(0.7)                    
            for i in range(len(ts)):
                for j in range(len(ts[i])):
                    w.writerow({'名稱':ts[i][j]['name'],
                                '網路價':ts[i][j]['price'],
                                '網址':"https://24h.pchome.com.tw/prod/" + ts[i][j]['Id'],
                                '圖1':"http://d.ecimg.tw/" + ts[i][j]['picB'],
                                '圖2':"http://d.ecimg.tw/" + ts[i][j]['picS']})
                
#ts[i][j][Key]
#csv_1()
'''
#網址 = https://24h.pchome.com.tw/prod/ + 'Id'
#圖片 = http://d.ecimg.tw/ + 'picS'
#圖片 = http://d.ecimg.tw/ + 'picB'    
'''

#清除非法字元
def text_cleanup(text):
    new =""
    for i in text:
        if i not in'\?.!/;:"*<>|':
            new += i
    return new


#自動創建資料夾 抓取圖片
def get_ph():
    for i in range(len(ts)):
        for j in range(len(ts[i])):
                url_1 = "http://d.ecimg.tw/" + ts[i][j]['picB']
                url_2 = "http://d.ecimg.tw/" + ts[i][j]['picS']
                path =  ts[i][j]['name']
                title = text_cleanup(path)
                filepath_1 =  title + '/' + "1" + '.jpg'
                filepath_2 =  title + '/' + "2" + '.jpg'
                if not os.path.isdir(title):  #檢查是否已經有了
                    os.mkdir(title) #沒有的用標題建立資料夾
                   
#url_1='http://d.ecimg.tw//items/DCAS4LA900AKITX/000001_1585012989.jpg'
#url_2='http://d.ecimg.tw//items/DCAS4LA900AKITX/000002_1599619807.jpg'

#將圖片下載下來
                    if not os.path.isfile(filepath_1): #檢查是否下載過圖片，沒有就下載
                        wget.download(url_1,filepath_1)
                    if not os.path.isfile(filepath_2): #檢查是否下載過圖片，沒有就下載    
                        wget.download(url_2,filepath_2)
                    sleep(0.7)
                    print("圖片要滿出來啦 >_<")
#get_ph()

def get_max_pages(serch):
    serch=str(serch)

    url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page=1&sort=sale/dc".format(serch)
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)
    #讀取網頁資訊
    #print(data['totalPage']) 頁數數量

    Tp = data['totalPage']+1

    return Tp
    
def i_cant_understand(serch,p):############我看不懂##################################################
    ts=prods_list(serch,p)
    return ts

if __name__== "__main__":
    
    serch = str(input("想抓點什麼呢? "))

    url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page=1&sort=sale/dc".format(serch)
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)
    #讀取網頁資訊
    #print(data['totalPage']) 頁數數量

    Tp = data['totalPage']+1


    #輸入條件
    print("最大頁數為 " + str(Tp))
    p = int(input("請輸入 < " + str(Tp) + " 的數字"))
    print("開始讀取資料")  
    ts=prods_list(serch,p)

