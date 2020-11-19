# -------------------------import area-----------------------------
from tkinter import *
import hashlib
import time
import threading
import worm_EX_ver as pchome_ver
#'''----------------------- subfuntion ----------------------- '''


def find_totalPage():
    choice_ = [var2.get(), var1.get(), var3.get()]
    show_time.set(choice_)
    key_word=Entry_2.get()
    totalPage=pchome_ver.get_max_pages(key_word)
    show_time.set(totalPage)
    Label_4_show.set("輸入想抓取的總頁數(小於{}):".format(totalPage))
    return totalPage

def get_max_pages(serch):
    serch=str(serch)

    url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page=1&sort=sale/dc".format(serch)
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)
    #讀取網頁資訊
    #print(data['totalPage']) 頁數數量

    Tp = data['totalPage']+1

    return Tp

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

#'''------------------------- main() --------------------------'''
    # -------參數宣告-----------------

root = Tk()
root.title("爬蟲蟲")
show = StringVar()
Label_4_show = StringVar()
show_time = StringVar()
Label_4_show.set("輸入想抓取的總頁數:")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

#serch = key_word
#serch = choice_
#ts=prods_list(serch,p)

#<<<<<<< Updated upstream
# -------------主邏輯------------------
# -----------參數定義-----------------
#=======
    #####-------------主邏輯------------------
        ######-----------參數定義-----------------
#<<<<<<< HEAD
'''Label_1=Label(root,text="輸入:")
#=======
Label_1=Label(root,text="請選擇網站:")
#>>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Label_2=Label(root,text="輸入關鍵字:")
Label_3=Label(root,text="儲存方式:")
Entry_1=Entry(root)
Entry_2=Entry(root)
Entry_3=Entry(root)

result=Label(root,textvariable=show,height=3,width=30)
result_del=Label(root,textvariable=show_del,height=3)
result_time=Label(root,textvariable=show_time,height=1)'''

        ######-----------按鈕宣告-----------------
#<<<<<<< HEAD
'''Button_01=Button(root,text="sha_1",command=Sub_Test_01)'''
#=======

#>>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Button_EXIT=Button(root,text="EXIT",command=root.destroy)
Button_03=Button(root,text="搜尋",command=find_totalPage)
Button_04=Button(root,text="爬！",command=pchome_ver.get_ph)

#Button_03.grid(sticky = W)
#>>>>>>> Stashed changes


# =======
Label_1 = Label(root, text="請選擇網站:")
# >>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Label_2 = Label(root, text="輸入關鍵字:")
Label_3 = Label(root, text="儲存方式:")
#Label_4 = Label(root, text="輸入想抓取的總頁數(小於){}:")
Label_4 = Label(root, textvariable=Label_4_show)
#.format(find_totalPage.totalPage)
#.format(find_totalPage()

Entry_1 = Entry(root)
Entry_2 = Entry(root)
Entry_3 = Entry(root)
Entry_4 = Entry(root)

result = Label(root, textvariable=show, height=3, width=30)

result_time = Label(root, textvariable=show_time, height=1)

# -----------按鈕宣告-----------------
# <<<<<<< HEAD

# =======

# >>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
'''Button_EXIT = Button(root, text="EXIT", command=root.destroy)
Button_03 = Button(root, text="爬蟲開始", command=find_totalPage)'''

Radiobutton1 = Radiobutton(root, text='PChome', variable=var2, value=2)
Radiobutton2 = Radiobutton(root, text='Lativ', variable=var2, value=10)
Checkbutton1 = Checkbutton(root, text="CSV", variable=var1,command=pchome_ver.csv_1)
Checkbutton2 = Checkbutton(root, text="PIC", variable=var3)

#,command=pchome_ver.csv_1()
#,command=pchome_ver.get_ph()

# ---------------排版-----------------

Label_1.grid(row=3)
Label_2.grid(row=1)
Label_3.grid(row=2)
Label_4.grid(row=4)

Entry_2.grid(row=1, column=1)
#Entry_3.grid(row=4,column=1)
Entry_4.grid(row=4, column=1)



#result_del.grid(row=4, column=1)
#result_time.grid(row=5, column=1)


Button_EXIT.grid(row=6, column=3)
Button_03.grid(row=1, column=3)
Button_04.grid(row=4, column=3)

# =======
Checkbutton1.grid(row=2, column=1)
Checkbutton2.grid(row=2, column=2)
Radiobutton1.grid(row=3, column=1)
Radiobutton2.grid(row=3, column=2)
# >>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91


root.mainloop()
