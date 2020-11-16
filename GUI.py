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

#'''------------------------- main() --------------------------'''
    # -------參數宣告-----------------

root = Tk()
root.title("mark1_test1")
show = StringVar()
show_del = StringVar()
show_time = StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

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
Button_03=Button(root,text="爬蟲開始",command=find_totalPage)
#Button_03.grid(sticky = W)
#>>>>>>> Stashed changes

# =======
Label_1 = Label(root, text="請選擇網站:")
# >>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Label_2 = Label(root, text="輸入關鍵字:")
Label_3 = Label(root, text="儲存方式:")
Label_4 = Label(root, text="輸入想抓取的總頁數(小於100):")

Entry_1 = Entry(root)
Entry_2 = Entry(root)
Entry_3 = Entry(root)
Entry_4 = Entry(root)

result = Label(root, textvariable=show, height=3, width=30)
result_del = Label(root, textvariable=show_del, height=3)
result_time = Label(root, textvariable=show_time, height=1)

# -----------按鈕宣告-----------------
# <<<<<<< HEAD

# =======

# >>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Button_EXIT = Button(root, text="EXIT", command=root.destroy)
Button_03 = Button(root, text="爬蟲開始", command=find_totalPage)

Radiobutton1 = Radiobutton(root, text='PChome', variable=var2, value=2)
Radiobutton2 = Radiobutton(root, text='衣服', variable=var2, value=10)
Checkbutton1 = Checkbutton(root, text="CSV", variable=var1)
Checkbutton2 = Checkbutton(root, text="DB", variable=var3)

# ---------------排版-----------------

Label_1.grid(row=3)
Label_2.grid(row=1)
Label_3.grid(row=2)
Label_4.grid(row=4)

Entry_2.grid(row=1, column=1)
# Entry_3.grid(row=4,column=1)
Entry_4.grid(row=4, column=1)



result_del.grid(row=4, column=1)
result_time.grid(row=5, column=1)


Button_EXIT.grid(row=6, column=3)
Button_03.grid(row=4, column=3)

# =======
Checkbutton1.grid(row=2, column=1)
Checkbutton2.grid(row=2, column=2)
Radiobutton1.grid(row=3, column=1)
Radiobutton2.grid(row=3, column=2)
# >>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91


root.mainloop()
