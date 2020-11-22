# -------------------------import area-----------------------------
from tkinter import *
import os,time
import threading
import worm_EX_ver as pchome_ver
import pri as lative_ver
#'''----------------------- subfuntion ----------------------- '''

#輸入關鍵字，找到搜尋結果的最大頁數
def find_totalPage_():
    global thr
    choice_ = [var4.get(), var1.get(), var3.get()]
    key_word=Entry_2.get()
    site = var2.get()
    if site == 2:
        totalPage=pchome_ver.get_max_pages(key_word)
        Label_4_show.set("輸入想抓取的總頁數(小於{}):".format(totalPage))
        thr=True
        Label_5_show.set('完成')
        return totalPage
    elif site == 10:
        totalPage=lative_ver.mai(key_word)
        thr=True
        Label_5_show.set('此網站不支援此功能')
        return totalPage


def download_pic():
    global thr
    key_word = Entry_2.get()
    wantpage = int(Entry_4.get())
    pchome_ver.prods_list(key_word,wantpage)
    pchome_ver.get_ph()
    thr=True
    Label_5_show.set('完成')

#開始爬蟲
def pa_():
    global thr
    site = var2.get()
    key_word = Entry_2.get()
    wantpage = int(Entry_4.get())
    ts = pchome_ver.prods_list(key_word,wantpage)
    m = lative_ver.mai(key_word)
    #pchome
    if   site == 2 and var5.get() == True and var6.get() == False:
        pchome_ver.csv_1(ts)    #存成csv
    elif site == 2 and var5.get() == False and var6.get() == True:
        pchome_ver.get_ph(ts)   #存成圖片
    elif site == 2 and var5.get() == True and var6.get() == True:
        pchome_ver.csv_1(ts)
        pchome_ver.get_ph(ts)   #存成csv+圖片
    #lative
    elif site == 10 and var5.get() == True and var6.get() == False:
        lative_ver.cloth(m)
    elif site == 10 and var5.get() == False and var6.get() == True:
        lative_ver.get_html_ph(m,wantpage)
    elif site == 10 and var5.get() == True and var6.get() == True:
        lative_ver.cloth(m)
        lative_ver.get_html_ph(m,wantpage)   #同pchome
    thr=True
    Label_5_show.set('完成')
        
####################多線程處理#############
def find_totalPage():
    t1=threading.Thread(target=find_totalPage_)
    t2=threading.Thread(target=act,args=['搜尋中請稍候'])
    Label_5_show.set('搜尋中請稍候')
    t2.start()
    t1.start()
    
def pa():
    t1=threading.Thread(target=pa_)
    t2=threading.Thread(target=act,args=['下載中請稍候'])
    Label_5_show.set('下載中請稍候')
    t2.start()
    t1.start()
    
def act(text):
    global thr
    con=0
    print(thr)
    while thr==False:
        text_=text
        if con%5==0:
            con=con+1
        else:
            for i in range(con%5):    
                text_=text_+'.'
            con=con+1
        Label_5_show.set(text_)
        #print(text_)
        time.sleep(0.1)
    thr=False
        

#'''------------------------- main() --------------------------'''
    # -------參數宣告-----------------
global thr
thr=False
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

Checkbutton1 = Checkbutton(root, text="CSV", variable=var5)
Checkbutton2 = Checkbutton(root, text="PIC", variable=var6)

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
