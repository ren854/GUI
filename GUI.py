#-------------------------import area-----------------------------
from tkinter import *
import hashlib,time,threading
#'''----------------------- subfuntion ----------------------- '''
def Sub_Test_01():
    data=Entry_1.get()
    Entry_1.delete(0,END)
    if data!="":
        sha1=hashlib.sha1(data.encode('utf-8')).hexdigest()
        show.set(str(data)+"  sha1:\n"+sha1)
    else:
        show.set('你沒有輸入任何東西')

def check_01():
    show_del.set(var2.get())
    #show_time.set(var2.get())

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
 
  
#'''------------------------- main() --------------------------'''
    #######-------參數宣告-----------------
root =Tk()
root.title("mark1_test1")
show=StringVar()
show_del=StringVar()
show_time=StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

    #####-------------主邏輯------------------
        ######-----------參數定義-----------------
<<<<<<< HEAD
Label_1=Label(root,text="輸入:")
=======
Label_1=Label(root,text="請選擇網站:")
>>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Label_2=Label(root,text="輸入關鍵字:")
Label_3=Label(root,text="儲存方式:")
Entry_1=Entry(root)
Entry_2=Entry(root)
Entry_3=Entry(root)

result=Label(root,textvariable=show,height=3,width=30)
result_del=Label(root,textvariable=show_del,height=3)
result_time=Label(root,textvariable=show_time,height=1)

        ######-----------按鈕宣告-----------------
<<<<<<< HEAD
Button_01=Button(root,text="sha_1",command=Sub_Test_01)
=======

>>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91
Button_EXIT=Button(root,text="EXIT",command=root.destroy)
Button_03=Button(root,text="爬蟲開始",command=check_01)

Radiobutton1=Radiobutton(root,text='PChome',variable=var2, value=2)
Radiobutton2=Radiobutton(root,text='衣服',variable=var2, value=10)
Checkbutton1=Checkbutton(root, text="CSV", variable=var1)
Checkbutton2=Checkbutton(root, text="DB", variable=var3)

        ######---------------排版-----------------
<<<<<<< HEAD

Label_2.grid(row=3)
Label_3.grid(row=4)

Entry_2.grid(row=3,column=1)
#Entry_3.grid(row=4,column=1)


result_del.grid(row=6,column=1)
result_time.grid(row=7,column=1)


Button_EXIT.grid(row=8,column=3)
Button_03.grid(row=6,column=3)
=======
Label_1.grid(row=3)
Label_2.grid(row=1)
Label_3.grid(row=2)

Entry_2.grid(row=1,column=1)
#Entry_3.grid(row=4,column=1)


result_del.grid(row=4,column=1)
result_time.grid(row=5,column=1)


Button_EXIT.grid(row=6,column=3)
Button_03.grid(row=4,column=3)
>>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91

#Checkbutton1.grid(row=4,column=1)
#Checkbutton2.grid(row=4,column=2)

<<<<<<< HEAD
Checkbutton1.grid(row=4,column=1)
Checkbutton2.grid(row=4,column=2)
Radiobutton1.grid(row=5,column=1)
Radiobutton2.grid(row=5,column=2)
=======
Checkbutton1.grid(row=2,column=1)
Checkbutton2.grid(row=2,column=2)
Radiobutton1.grid(row=3,column=1)
Radiobutton2.grid(row=3,column=2)
>>>>>>> ff8d9f7f1ca16989e4cc32bb13fe6d8e8da2dd91

root.mainloop()
