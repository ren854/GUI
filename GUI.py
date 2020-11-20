# -------------------------import area-----------------------------
from tkinter import *
import os
import threading
import worm_EX_ver as pchome_ver
import pri as lative_ver
#'''----------------------- subfuntion ----------------------- '''


def find_totalPage_():
    choice_ = [var4.get(), var1.get(), var3.get()]
    key_word=Entry_2.get()
    totalPage=pchome_ver.get_max_pages(key_word)
    Label_4_show.set("輸入想抓取的總頁數(小於{}):".format(totalPage))
    Label_5_show.set('')
    return totalPage

def set_wantpage():
    wp = [var4.get()]
    wantpage=Entry_4.get()
    return wantpage

def download_pic():
    key_word = Entry_2.get()
    wantpage = int(Entry_4.get())
    pchome_ver.prods_list(key_word,wantpage)
    pchome_ver.get_ph()
    Label_5_show.set('')

def pa_():
    site = var2.get()
    key_word = Entry_2.get()
    wantpage = int(Entry_4.get())
    ts = pchome_ver.prods_list(key_word,wantpage)
    if   site == 2 and var5.get() == True and var6.get() == False:
        pchome_ver.csv_1(ts)
    elif site == 2 and var5.get() == False and var6.get() == True:
        pchome_ver.get_ph(ts)
    elif site == 2 and var5.get() == True and var6.get() == True:
        pchome_ver.csv_1(ts)
        pchome_ver.get_ph(ts)
#####################以上已完成######################      
    elif site == 10 and var5.get() == True and var6.get() == False:
        print('pc cccccc')
        lative_ver.cloth(ts)
    elif site == 10 and var5.get() == False and var6.get() == True:
        print('pc p')
        lative_ver.get_ph(ts)
    elif site == 10 and var5.get() == True and var6.get() == True:
        print('pc cp')
        lative_ver.cloth(ts)
        lative_ver.get_ph(ts)
    Label_5_show.set('')
        
####################多線程處理#############
def find_totalPage():
    t1=threading.Thread(target=find_totalPage_)
    Label_5_show.set('搜尋中請稍後')
    t1.start()
def pa():
    t1=threading.Thread(target=pa_)
    Label_5_show.set('下載中請稍後 可至OUTPUT資料夾觀看結果')
    t1.start()
'''
#######################################這東西沒用阿.......
def get_max_pages(serch):
    serch=str(serch)
    #####################################別這樣寫拉用import的方式叫,不然會出bug
    url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page=1&sort=sale/dc".format(serch)
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)
    #讀取網頁資訊
    #print(data['totalPage']) 頁數數量

    Tp = data['totalPage']+1
##################這個return沒人收阿????????????????
    return Tp
###################同上
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
                    
###########################同上--------->我只是放在上面方便看，沒有要叫他們~~~~~~~~~~
'''
#'''------------------------- main() --------------------------'''
    # -------參數宣告-----------------

root = Tk()
root.title("爬蟲蟲")
show = StringVar()
Label_4_show = StringVar()
Label_5_show = StringVar()
Label_4_show.set("輸入想抓取的總頁數:")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

# -------------主邏輯------------------
# -----------參數定義-----------------
        ######-----------按鈕宣告-----------------
Button_EXIT=Button(root,text="EXIT",command=root.destroy)
Button_03=Button(root,text="搜尋",command=find_totalPage)
Button_04=Button(root,text="爬！",command=pa)

Label_1 = Label(root, text="請選擇網站:")
Label_2 = Label(root, text="輸入關鍵字:")
Label_3 = Label(root, text="儲存方式:")
Label_4 = Label(root, textvariable=Label_4_show)
Label_5 = Label(root, textvariable=Label_5_show)

Entry_1 = Entry(root)
Entry_2 = Entry(root)
Entry_3 = Entry(root)
Entry_4 = Entry(root)

result = Label(root, textvariable=show, height=3, width=30)

#result_time = Label(root, textvariable=show_time, height=1)

# -----------按鈕宣告-----------------

Radiobutton1 = Radiobutton(root, text='PChome', variable=var2, value=2)
Radiobutton2 = Radiobutton(root, text='Lativ', variable=var2, value=10)

Checkbutton1 = Checkbutton(root, text="CSV", variable=var5,onvalue = 1, offvalue = 0)
Checkbutton2 = Checkbutton(root, text="PIC", variable=var6,onvalue = 1, offvalue = 0)

# ---------------排版-----------------

Label_1.grid(row=3)
Label_2.grid(row=1)
Label_3.grid(row=2)
Label_4.grid(row=4)
Label_5.grid(row=5,column=1)

Entry_2.grid(row=1, column=1)
Entry_4.grid(row=4, column=1)

Button_EXIT.grid(row=6, column=3)
Button_03.grid(row=1, column=3)
Button_04.grid(row=4, column=3)

# =======
Checkbutton1.grid(row=2, column=1)
Checkbutton2.grid(row=2, column=2)
Radiobutton1.grid(row=3, column=1)
Radiobutton2.grid(row=3, column=2)


root.mainloop()
