from tkinter import *
from  datetime import datetime
from tkinter import messagebox

class UpdateMoneyStock:
    def __init__(self,main_frame):
        self.main_frame=main_frame
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)       
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        lblTitle=Label(frame,text="Update Money Stock",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=10)
        lblCurrentStock=Label(frame,font=("times new roman",20,"bold"),text="Current Stock",bg="white",fg="green").place(x=20,y=50)
        self.txtCurrentStock=Entry(frame,font=("times new roman",30,"bold"),justify=CENTER,bg="lightgray")
        self.txtCurrentStock.place(x=120,y=100)
        self.getStock()
        lblTitle1=Label(frame,font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=160)
        lblEnterAmount=Label(frame,font=("times new roman",20,"bold"),text="Update Amount",bg="white",fg="green").place(x=20,y=200)
        lblRs2=Label(frame,font=("times new roman",20,"bold"),text="Rs.",bg="white",fg="gray").place(x=60,y=270)
        self.txtAmount=Entry(frame,font=("times new roman",30,"bold"),justify=CENTER,bg="lightgray")
        self.txtAmount.place(x=120,y=250)
        btnUpdateStock=Button(frame,text="Update",font=("times new roman",20,"bold"),fg="white",bg="red",command=self.updateStock,cursor="hand2",borderwidth=5).place(x=280,y=320)   
    def getStock(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)
        if len(stockDetails)==0:
            self.txtCurrentStock.insert(0,("Rs."+"0"+".00"))
            self.txtCurrentStock.configure(state=DISABLED)
        else:
            lastTransaction=stockDetails[-1]
            currentStock=lastTransaction[3]
            self.txtCurrentStock.insert(0,("Rs."+currentStock+".00"))
            self.txtCurrentStock.configure(state=DISABLED)
    def updateStock(self):
        self.txtCurrentStock.configure(state=NORMAL)
        self.update_clock()
        nowStock=int(self.txtCurrentStock.get())+int(self.txtAmount.get())
        with open("Money_Stock.txt",'a') as file1:
            file1.write(str(self.date_now)+"|"+str(self.time_now)+"|"+str("+"+str(self.txtAmount.get()))+"|"+str(nowStock)+"\n")
        messagebox.showinfo("Stock Update","Money Stock Updated Successfully!")
        for widgets in self.main_frame.winfo_children():
                    widgets.destroy()
        from Manager_Interface import Status
        obj=Status(self.main_frame)
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")