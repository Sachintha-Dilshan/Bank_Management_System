from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Fixed_Deposit import FixedDepositPage1
from  datetime import datetime
from Change_Rates import ChangeRates
from Update_Money_Stock import UpdateMoneyStock
from Search import Search


class Admin:
    def __init__(self,root2):
        self.root2=root2
        self.root2.title("Admin Login")
        self.root2.state("zoomed")
        frame1=Frame(self.root2,bg="lightgreen",height=100)
        frame1.pack(fill=X)
        btnDashBoard=Button(self.root2,text="Dash Board",font=("times new roman",15,"bold"),bg="green",fg="white",command=self.getStatusView,cursor="hand2",borderwidth=5).place(x=1360,y=105)
        self.lblDateNow=Label(frame1,text="",font=("times new roman",30,"bold"),bg="lightgreen")
        self.lblDateNow.place(x=1150,y=10)
        self.lblTimeNow=Label(frame1,text="",font=("times new roman",30,"bold"),bg="lightgreen")
        self.lblTimeNow.place(x=900,y=10)
        btnLogOut=Button(frame1, text="Log Out",font=("times new roman",20,"bold"),bg="red",fg="white",cursor="hand2",command=self.logOut,borderwidth=5).place(x=1380,y=10)
        lbl1=Label(frame1,text="Welcome",font=("times new roman",20,"bold"),bg="lightgreen").place(x=10,y=5)
        lblname=Label(frame1,text=("Admin Section"),font=("times new roman",20,"bold"),bg="lightgreen").place(x=10,y=50)
        btn3=Button(self.root2, text="Search",font=("times new roman",30,"bold"),fg="white",bg="green",cursor="hand2",width="18",command=self.search,borderwidth=5).place(x=10,y=300)
        btn4=Button(self.root2, text="Update Money Stock",font=("times new roman",30,"bold"),fg="white",bg="green",cursor="hand2",width="18",command=self.updateMoneyStock,borderwidth=5).place(x=10,y=450)
        self.frame2=Frame(self.root2,bg="lightgray")
        self.frame2.place(x=480, y=150, width=1000, height=600)  
        self.update_clock()
        self.today=self.date_now
        self.time=self.time_now
        obj=Status(self.frame2)
        self.root2.mainloop()    
    
    def fixedDeposit(self):
        #self.getClientInfo()
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=FixedDepositPage1(self.frame2,self.accountNumber,self.today)   
    def search(self):
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=Search(self.frame2,self.date_now)
    def updateMoneyStock(self):
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=UpdateMoneyStock(self.frame2)
    def getStatusView(self):
        obj=Status(self.frame2)
    
    def logOut(self):
        self.root2.destroy()
        from Login_Page import Login
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")
        self.lblDateNow.config(text=self.date_now)
        self.lblTimeNow.config(text=self.time_now)
        self.lblTimeNow.after(1000,self.update_clock)

class Status:          
    def __init__(self,main_frame):
        self.main_frame=main_frame
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        accountHoldersDetails=self.getAccountHolderDetails()
        pendingLoansDetails=self.getLoanDetails()
        depositDetails=self.getDepositDetails()
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        lblTitle=Label(frame,text="Status",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=10)
        lbl1=Label(frame,font=("times new roman",20,"bold"),text="Number of Pending Loans    :",bg="white").place(x=20,y=60)
        lbl2=Label(frame,font=("times new roman",20,"bold"),text=str(len(pendingLoansDetails)),bg="white",fg="red").place(x=400,y=60)
        lbl3=Label(frame,font=("times new roman",20,"bold"),text="Number of Fixed Deposits    :",bg="white").place(x=20,y=100)
        lbl4=Label(frame,font=("times new roman",20,"bold"),text=str(len(self.depositDetails)),bg="white",fg="red").place(x=400,y=100)
        lbl5=Label(frame,font=("times new roman",20,"bold"),text="Number of Account Holders :",bg="white").place(x=20,y=140)
        lbl6=Label(frame,font=("times new roman",20,"bold"),text=str(len(accountHoldersDetails)),bg="white",fg="red").place(x=400,y=140)
        btn7=Button(frame,text="View",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.loanDetailsView,cursor="hand2",borderwidth=5).place(x=500,y=60)
        btn8=Button(frame,text="View",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.FDDetailsView,cursor="hand2",borderwidth=5).place(x=500,y=100)
        btn9=Button(frame,text="View",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.accountDetailsView,cursor="hand2",borderwidth=5).place(x=500,y=140)
        lblTitle1=Label(frame,text="Money Stock",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=180)
        lblMoneyStock=Label(frame,font=("times new roman",20,"bold"),text="Current Stock Amount",bg="white",fg="gray").place(x=20,y=210)
        self.getStockInfo()
        txtMoneyStock=Entry(frame,font=("times new roman",30),justify=CENTER,bg="lightgray")
        txtMoneyStock.place(x=100,y=260)
        txtMoneyStock.insert(0,("Rs."+self.currentStock+".00"))
        txtMoneyStock.configure(state=DISABLED)
        txtMoneyStock.insert(0,"Hello")
        lblTitle2=Label(frame,text="Current Rates",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=320)
        self.cmbLoanType = ttk.Combobox(frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbLoanType['values'] = ("Select","Saving Account","Personal Loan","Home Loan","Education Loan")
        self.cmbLoanType.place(x=60, y=380)
        self.cmbLoanType.current(0)
        self.lblLoanRate=Label(frame,text="Rate",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.lblLoanRate.place(x=400,y=380)
        bntRate=Button(frame,text="Rate",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.changeRate,cursor="hand2",borderwidth=5).place(x=300,y=380)
        btnUpdateRate=Button(frame,text="Update rates",font=("times new roman",20,"bold"),fg="white",bg="red",command=self.updateRate,cursor="hand2",borderwidth=5)
        btnUpdateRate.place(x=220,y=450)

    def updateRate(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        obj=ChangeRates(self.main_frame)  
    
    def changeRate(self):
        self.getRates()
        if self.cmbLoanType.get()=="Select":
            messagebox.showerror("Update Rates","Please Select a type")
            self.lblLoanRate.configure(text="Rate")
        elif self.cmbLoanType.get()=="Saving Account":
            self.lblLoanRate.configure(text=(self.Rate[0]+"%"))
        elif self.cmbLoanType.get()=="Personal Loan":
            self.lblLoanRate.configure(text=(self.Rate[1]+"%"))
        elif self.cmbLoanType.get()=="Home Loan":
            self.lblLoanRate.configure(text=(self.Rate[2]+"%"))
        elif self.cmbLoanType.get()=="Education Loan":
            self.lblLoanRate.configure(text=(self.Rate[3]+"%")) 

    def getRates(self):
        self.Rate=[]
        self.Type=[]
        with open("Rates.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                self.Rate.append(split[1])
                self.Type.append(split[0])
  
    def getLoanDetails(self):
        self.LoanDetails=[]
        with open("Loan_details.txt", "r") as file:
            for line in file:
                split=line.strip().split("|")
                self.LoanDetails.append(split)
        return self.LoanDetails
    def getAccountHolderDetails(self):
        self.accountHolderDetails=[]
        with open("Personal_Details.txt", "r") as file:
            for line in file:
                split=line.strip().split("|")
                self.accountHolderDetails.append(split)
        return self.accountHolderDetails
    def getDepositDetails(self):
        self.depositDetails=[]
        with open("FD_details.txt", "r") as file:
            for line in file:
                split=line.strip().split("|")
                self.depositDetails.append(split)
        return self.depositDetails
    def getStockInfo(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)
            if len(stockDetails)==0:
                self.currentStock="0"
            else:               
                lastTransaction=stockDetails[-1]
                self.currentStock=lastTransaction[3]

    def accountDetailsView(self):
        root=Tk()
        root.geometry("840x600+280+80")
        root.resizable(False,False)
        root.title("Account Holders")
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        canvas=Canvas(main_frame)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        scrollBar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
        scrollBar.pack(side=LEFT,fill=Y)
        canvas.configure(yscrollcommand=scrollBar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        self.FRAME=Frame(canvas)
        canvas.create_window((0,0),window=self.FRAME,anchor="nw")
        self.update_clock() 
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=6)
        Label(self.FRAME,text="Account Number",font=("times new roman",15)).grid(column=0,row=7)
        Label(self.FRAME,text="Name",font=("times new roman",15)).grid(column=1,row=7)
        Label(self.FRAME,text="ID No",font=("times new roman",15)).grid(column=2,row=7)
        Label(self.FRAME,text="Contact No",font=("times new roman",15)).grid(column=3,row=7)
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=8)
        accountHoldersDetails=self.getAccountHolderDetails()  
        y=0
        for i in accountHoldersDetails:
            Label(self.FRAME,text=str(i[0]),font=("times new roman",15)).grid(column=0,row=9+2*y)
            Label(self.FRAME,text=(str(i[1])+"."+str(i[3])),font=("times new roman",15)).grid(column=1,row=9+2*y)
            Label(self.FRAME,text=str(i[4]),font=("times new roman",15)).grid(column=2,row=9+2*y)
            Label(self.FRAME,text=str(i[13]),font=("times new roman",15)).grid(column=3,row=9+2*y)
            for x in range(4):
                Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=x,row=10+2*y)         
            y+=1
        root.mainloop()
    def loanDetailsView(self):
        root=Tk()
        root.geometry("840x600+280+80")
        root.resizable(False,False)
        root.title("Loan Details")
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        canvas=Canvas(main_frame)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        scrollBar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
        scrollBar.pack(side=LEFT,fill=Y)
        canvas.configure(yscrollcommand=scrollBar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        self.FRAME=Frame(canvas)
        canvas.create_window((0,0),window=self.FRAME,anchor="nw")
        self.update_clock() 
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=6)
        Label(self.FRAME,text="Account Number",font=("times new roman",15)).grid(column=0,row=7)
        Label(self.FRAME,text="Name",font=("times new roman",15)).grid(column=1,row=7)
        Label(self.FRAME,text="Loan Type",font=("times new roman",15)).grid(column=2,row=7)
        Label(self.FRAME,text="Loan Amount",font=("times new roman",15)).grid(column=3,row=7)
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=8)
        loanDetails=self.getLoanDetails()
        y=0
        for i in loanDetails:
            Label(self.FRAME,text=str(i[0]),font=("times new roman",15)).grid(column=0,row=9+2*y)
            Label(self.FRAME,text=(str(i[1])+"."+str(i[2])),font=("times new roman",15)).grid(column=1,row=9+2*y)
            Label(self.FRAME,text=str(i[9]),font=("times new roman",15)).grid(column=2,row=9+2*y)
            Label(self.FRAME,text=str(i[10]),font=("times new roman",15)).grid(column=3,row=9+2*y)
            for x in range(4):
                Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=x,row=10+2*y)         
            y+=1
        root.mainloop()
    def FDDetailsView(self):
        root=Tk()
        root.geometry("840x600+280+80")
        root.resizable(False,False)
        root.title("Loan Details")
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        canvas=Canvas(main_frame)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        scrollBar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
        scrollBar.pack(side=LEFT,fill=Y)
        canvas.configure(yscrollcommand=scrollBar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        self.FRAME=Frame(canvas)
        canvas.create_window((0,0),window=self.FRAME,anchor="nw")
        self.update_clock() 
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=6)
        Label(self.FRAME,text="Account Number",font=("times new roman",15)).grid(column=0,row=7)
        Label(self.FRAME,text="Reference Number",font=("times new roman",15)).grid(column=1,row=7)
        Label(self.FRAME,text="Name",font=("times new roman",15)).grid(column=2,row=7)
        Label(self.FRAME,text="Deposit Amount",font=("times new roman",15)).grid(column=3,row=7)
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=8)
        depositDetails=self.getDepositDetails()
        y=0
        for i in depositDetails:
            Label(self.FRAME,text=str(i[0]),font=("times new roman",15)).grid(column=0,row=9+2*y)
            Label(self.FRAME,text=str(i[1]),font=("times new roman",15)).grid(column=1,row=9+2*y)
            Label(self.FRAME,text=str(i[2]),font=("times new roman",15)).grid(column=2,row=9+2*y)
            Label(self.FRAME,text=str(i[3]),font=("times new roman",15)).grid(column=3,row=9+2*y)
            for x in range(4):
                Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=x,row=10+2*y)         
            y+=1
        root.mainloop()
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")




 




