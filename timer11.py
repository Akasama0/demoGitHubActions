from tkinter import *

root = 0

class Win1():
    
    time_dict = {}
    list_num = [1]
    list_count = 1
    win2 = 0

    def __init__(self):
        self.list = self.list_num

    def creat1(self,master):
        
        self.master = Tk()
        v = StringVar(value = self.list)
        self.lb = Listbox(
        self.master, listvariable=v,
        selectmode='single', height=4)
        self.lb.event_add("<<lb>>","<ButtonRelease>")
        self.lb.bind(
         '<<lb>>',          #リストボックスが選択されたら
        self.win2)   #関数を実行する
        self.lb.grid(row=0, column=0)

        self.button2 = Button(self.master,text="追加",command=self.add)
        self.button2.grid(row=1,column=0)

        print(self.win2)

        self.master.mainloop()
    
    def add(self):
        self.list_count += 1
        self.list.append(self.list_count)
        v = StringVar(value = self.list)
        self.lb = Listbox(
        self.master, listvariable=v,
        selectmode='single', height=4)
        self.lb.event_add("<<lb>>","<ButtonRelease>")   #バーチャルイベントの設定。たいした意味はない
        self.lb.bind(
         '<<lb>>',          #リストボックスが選択されたら
        self.win2)   #関数を実行する
        self.lb.grid(row=0, column=0)




    def win2(self,event):      
        self.list_lb = self.lb.curselection()
        if len(self.list_lb) != 1:
            return
        else:    
            self.app = Win2()  #インスタス化
            lb_name = self.lb.get(self.lb.curselection())  #タプルが代入される?なんか動作が安定しない
            self.master.after(100,self.app.creat2,lb_name) 
        
class Win2():
    const_num = 1
    def __init__(self):
        if self.const_num == 1:
            self.win2 = Toplevel()
            self.win2.destroy()
            Win2.const_num +=1
            print(Win2.const_num)
        else:
            return

    def creat2(self,listbox_name):
        self.listbox_name = listbox_name
        if Win1.win2 == 0 or self.win2.winfo_exists() != 1:
            self.win2 = Toplevel()    #サブウィンドウ
            Win1.win2 = 1
        self.time = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,]
        v = StringVar(value=self.time)
        
        self.listbox1 = Listbox(
        self.win2,listvariable=v,
        selectmode="single",height=4)
        self.listbox1.event_add("<<listbox1>>","<ButtonRelease>")
        self.listbox1.bind("<<listbox1>>",self.listbox1_cha)
        self.listbox1.grid(row=2,column=0)
        
        self.label1 = Label(self.win2,text="hour")
        self.label1.grid(row=0,column=0)
        
        self.listbox2 = Listbox(
        self.win2,listvariable=v,
        selectmode="single",height=4)
        self.listbox2.event_add("<<listbox1>>","<ButtonRelease>")
        self.listbox2.bind("<<listbox1>>",self.listbox2_cha)
        self.listbox2.grid(row=2,column=1)
        
        self.label2 = Label(self.win2,text="min")
        self.label2.grid(row=0,column=1)

        self.listbox3 = Listbox(
        self.win2,listvariable=v,
        selectmode="single",height=4)
        self.listbox3.event_add("<<listbox1>>","<ButtonRelease>")
        self.listbox3.bind("<<listbox1>>",self.listbox3_cha)
        self.listbox3.grid(row=2,column=2)
        
        self.label3 = Label(self.win2,text="sec")
        self.label3.grid(row=0,column=2)

        self.label4 = Label(self.win2,text=0)
        self.label4.grid(row=1,column=0)

        self.label5 = Label(self.win2,text=0)
        self.label5.grid(row=1,column=1)

        self.label6 = Label(self.win2,text=0)
        self.label6.grid(row=1,column=2)

        self.button1 = Button(self.win2,text="決定",command=self.back)
        self.button1.grid(row=3,column=0)

        self.hour = 0
        self.min = 0
        self.sec = 0
        self.time_mount = (self.hour,self.min,self.sec)

        self.win2.mainloop()

    def listbox1_cha(self,event):
        self.lis1 = self.listbox1.curselection()
        
        if len(self.lis1) != 1:
            return
        else:
            self.label4.config(text=self.listbox1.get(self.listbox1.curselection()))
            self.hour = self.listbox1.get(self.listbox1.curselection())
            self.time_mount = (self.hour,self.min,self.sec)
            Win1.time_dict[self.listbox_name] = self.time_mount
            print(self.time_mount)

    def listbox2_cha(self,event):
        self.lis2 = self.listbox2.curselection()
        
        if len(self.lis2) != 1:
            return
        else:
            self.label5.config(text=self.listbox2.get(self.listbox2.curselection()))
            self.min = self.listbox2.get(self.listbox2.curselection())
            self.time_mount = (self.hour,self.min,self.sec)
            Win1.time_dict[self.listbox_name] = self.time_mount
            print(self.time_mount)

    def listbox3_cha(self,event):
        self.lis3 = self.listbox3.curselection()
        
        if len(self.lis3) != 1:
            return
        else:
            self.label6.config(text=self.listbox3.get(self.listbox3.curselection()))
            self.sec = self.listbox3.get(self.listbox3.curselection())
            self.time_mount = (self.hour,self.min,self.sec)
            Win1.time_dict[self.listbox_name] = self.time_mount
            print(self.time_mount)

    def back(self):
        self.win2.destroy()
    

window = Win1()
window.creat1(root)