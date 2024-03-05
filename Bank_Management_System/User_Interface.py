from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Cash_Deposit import CashDeposit
from Cash_Withdrawal import Withdrawal
from Loan_Application import LoanPage1
from Fixed_Deposit import FixedDepositPage1
from Fund_Transfer import FundTransfer
from  datetime import datetime


class User:
    def __init__(self,root2,accountNumber):
        self.accountNumber=accountNumber
        self.root2=root2
        self.root2.title("User Login")
        self.root2.state("zoomed")
        self.getClientInfo()
        frame1=Frame(self.root2,bg="lightgreen",height=100)
        frame1.pack(fill=X)
        btnDashBoard=Button(self.root2,text="Dash Board",font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",borderwidth=5,command=self.getAccountDetailsView).place(x=1360,y=105)
        self.lblDateNow=Label(frame1,text="",font=("times new roman",30,"bold"),bg="lightgreen")
        self.lblDateNow.place(x=1150,y=10)
        self.lblTimeNow=Label(frame1,text="",font=("times new roman",30,"bold"),bg="lightgreen")
        self.lblTimeNow.place(x=900,y=10)
        btnLogOut=Button(frame1, text="Log Out",font=("times new roman",20,"bold"),bg="red",fg="white",cursor="hand2",command=self.logOut,borderwidth=5).place(x=1380,y=10)
        lbl1=Label(frame1,text="Welcome",font=("times new roman",20,"bold"),bg="lightgreen").place(x=10,y=5)
        lblname=Label(frame1,text=(self.title+"."+self.name),font=("times new roman",20,"bold"),bg="lightgreen").place(x=10,y=50)
        btn2=Button(self.root2, text="CASH DEPOSIT",font=("times new roman",30,"bold"),cursor="hand2",command=self.getDeposit,width="18",borderwidth=10,fg="white",bg="green").place(x=10,y=150)
        btn3=Button(self.root2, text="CASH WITHDRAWAL",font=("times new roman",30,"bold"),cursor="hand2",command=self.withdrawal,width="18",borderwidth=10,fg="white",bg="green").place(x=10,y=262)
        btn4=Button(self.root2, text="FIXED DEPOSIT",font=("times new roman",30,"bold"),cursor="hand2",command=self.fixedDeposit,width="18",borderwidth=10,fg="white",bg="green").place(x=10,y=374)
        btn5=Button(self.root2, text="APPLY FOR A LOAN",font=("times new roman",30,"bold"),cursor="hand2",command=self.applyForLoan,width="18",borderwidth=10,fg="white",bg="green").place(x=10,y=486)
        btn6=Button(self.root2, text="FUND TRANSFER",font=("times new roman",30,"bold"),cursor="hand2",command=self.fundTrasfer,width="18",borderwidth=10,fg="white",bg="green").place(x=10,y=598)

        self.frame2=Frame(self.root2,bg="lightgray")
        self.frame2.place(x=480, y=150, width=1000, height=600)
        self.update_clock()
        self.today=self.date_now
        self.time=self.time_now
        obj=AccountDetailsView(self.frame2,self.accountNumber)
        self.root2.mainloop()    
 ##################################################################################Deposit Button############################################################################################  
    def getDeposit(self):
        self.getClientInfo()
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj = CashDeposit(self.frame2,self.balance,self.accountNumber,self.today,self.time,self.title,self.name)
  ##################################################################################Withdrawal Button############################################################################################            
    def withdrawal(self):
        self.getClientInfo()
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj1=Withdrawal(self.frame2,self.accountNumber,self.balance,self.today,self.time,self.title,self.name)
 ##################################################################################Fixed Deposit Button############################################################################################  
    def fixedDeposit(self):
        self.getClientInfo()
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=FixedDepositPage1(self.frame2,self.accountNumber,self.today,self.balance)
 ##################################################################################Apply for a Loan Button############################################################################################  
    def applyForLoan(self):
        self.getStockInfo()
        self.getClientInfo()
        AvailableStock=int(self.currentStock)-1000
        messagebox.showinfo("Available Stock",("Available Loan Amount is Rs."+str(AvailableStock)))
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=LoanPage1(self.frame2,self.accountNumber,self.today)
 ########################################################################################Fund Transfer Button#################################################################################
    def fundTrasfer(self):
        self.getClientInfo()
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=FundTransfer(self.frame2,self.balance,self.accountNumber)
 ##################################################################################Log Out Button############################################################################################  
    def logOut(self):
        self.root2.destroy()
        from Login_Page import Login
 ##################################################################################Get Account Details View############################################################################################  
    def getAccountDetailsView(self):
        self.getClientInfo()
        for widgets in self.frame2.winfo_children():
            widgets.destroy()
        obj=AccountDetailsView(self.frame2,self.accountNumber)
 ##################################################################################Get Client Personal Informations and Account Informations############################################################################################    
    def getClientInfo(self):

        accountHolderDetails=[]
        with open("Personal_Details.txt", 'r') as file:
            for line in file:
                split1 = line.strip().split("|")
                if self.accountNumber in split1:
                    accountHolderDetails=split1
        self.title=accountHolderDetails[1]
        self.fullName=accountHolderDetails[2]
        self.name=accountHolderDetails[3]
        self.IDNo=accountHolderDetails[4]
        self.birthYear=accountHolderDetails[5]
        self.birthMonth=accountHolderDetails[6]
        self.birthDate=accountHolderDetails[7]
        self.occupation=accountHolderDetails[8]
        self.addressNo=accountHolderDetails[9]
        self.line1=accountHolderDetails[10]
        self.line2=accountHolderDetails[11]
        self.line3=accountHolderDetails[12]
        self.contactNo=accountHolderDetails[13]
        self.email=accountHolderDetails[14]

        passbookData=[]
        recentActivity=[]
        with open("Passbook.txt", 'r') as file1:
            for line in file1:
                split2 = line.strip().split("|")
                if self.accountNumber in split2:
                    passbookData.append(split2)
                
                        
        recentActivity=passbookData[-1]
        self.balance=recentActivity[4]
 ##################################################################################Bank Available Money Stock############################################################################################  
    def getStockInfo(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)            
            lastTransaction=stockDetails[-1]
            self.currentStock=lastTransaction[3]      
 ##################################################################################Real Time Clock############################################################################################  
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")
        self.lblDateNow.config(text=self.date_now)
        self.lblTimeNow.config(text=self.time_now)
        self.lblTimeNow.after(1000,self.update_clock)
##################################################################################User Interface Details view############################################################################################  
class AccountDetailsView:           
    def __init__(self,main_frame,accountNo):
        self.main_frame=main_frame
        self.accountNumber=accountNo
        self.getClientInfo()
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        lblTitle=Label(frame,text="Account Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=10)
        lbl1=Label(frame,font=("times new roman",20,"bold"),text=(str(self.accountNumber)+"-"+"Saving Account"),bg="white").place(x=140,y=80)
        lbl2=Label(frame,text="Account Balance",font=("times new roman",20,"bold"),fg="white",bg="green",width=36).place(x=10,y=160)
        lbl3=Label(frame,font=("times new roman",30,"bold"),fg="Red",text=("Rs."+str(self.balance)+".00"),bg="white").place(x=220,y=220)
        lblTitle2=Label(frame,text="Current Rates",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=320)
        self.cmbLoanType = ttk.Combobox(frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbLoanType['values'] = ("Select","Saving Account","Personal Loan","Home Loan","Education Loan")
        self.cmbLoanType.place(x=60, y=380)
        self.cmbLoanType.current(0)
        self.lblLoanRate=Label(frame,text="Rate",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.lblLoanRate.place(x=400,y=380)
        bntRate=Button(frame,text="Rate",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.changeRate,cursor="hand2",borderwidth=10).place(x=300,y=380)
        btnAccountSummary=Button(frame,text="Account Summary",font=("times new roman",20,"bold"),fg="white",bg="red",command=self.AccountSummary,cursor="hand2",borderwidth=5)
        btnAccountSummary.place(x=180,y=450)
    
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
    def getClientInfo(self):

        accountHolderDetails=[]
        with open("Personal_Details.txt", 'r') as file:
            for line in file:
                split1 = line.strip().split("|")
                if self.accountNumber in split1:
                    accountHolderDetails=split1
        self.title=accountHolderDetails[1]
        self.fullName=accountHolderDetails[2]
        self.name=accountHolderDetails[3]
        self.IDNo=accountHolderDetails[4]
        self.birthYear=accountHolderDetails[5]
        self.birthMonth=accountHolderDetails[6]
        self.birthDate=accountHolderDetails[7]
        self.occupation=accountHolderDetails[8]
        self.addressNo=accountHolderDetails[9]
        self.line1=accountHolderDetails[10]
        self.line2=accountHolderDetails[11]
        self.line3=accountHolderDetails[12]
        self.contactNo=accountHolderDetails[13]
        self.email=accountHolderDetails[14]


        passbookData=[]
        recentActivity=[]
        with open("Passbook.txt", 'r') as file1:
            for line in file1:
                split2 = line.strip().split("|")
                if self.accountNumber in split2:
                    passbookData.append(split2)                
        recentActivity=passbookData[-1]
        self.balance=recentActivity[4]
     ##################################################################################Account Summary Button############################################################################################  
    def AccountSummary(self):
        obj=BankStatement(self.accountNumber)
##################################################################################Get Transaction Info(Bank Statement)############################################################################################  
class BankStatement:
    def __init__(self,accountNumber):
        root=Tk()
        root.geometry("840x600+280+80")
        root.resizable(False,False)
        root.title("Bank Statement")
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
        self.accountNumber=accountNumber
        self.getAccountSummary()
        root.mainloop()
    
    def getAccountSummary(self):
        self.update_clock()    
        self.getClientInfo()
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=0)
        
        Label(self.FRAME,text=(str(self.title)+"."+str(self.name)+"\n"+str(self.addressNo)+"\n"+str(self.line1)+"\n"+str(self.line2)+"\n"+str(self.line3)+"\n"),font=("times new roman",12,"bold"),justify=LEFT).grid(column=0,row=2)
        Label(self.FRAME,text="            Account Number:",font=("times new roman",15)).grid(column=0,row=5)
        Label(self.FRAME,text=str(self.accountNumber),font=("times new roman",15,"bold")).grid(column=1,row=5)
        Label(self.FRAME,text=(str(self.date_now)+" "+str(self.time_now)),font=("times new roman",15)).grid(column=3,row=5)
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=6)
        Label(self.FRAME,text="Date",font=("times new roman",15)).grid(column=0,row=7)
        Label(self.FRAME,text="Time",font=("times new roman",15)).grid(column=1,row=7)
        Label(self.FRAME,text="Transaction (LKR)",font=("times new roman",15)).grid(column=2,row=7)
        Label(self.FRAME,text="Balance (LKR)",font=("times new roman",15)).grid(column=3,row=7)
        for i in range(4):
            Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=i,row=8)
        passBookData=self.getClientInfo()
        y=0
        for i in passBookData:
            for x in range(4):
                Label(self.FRAME,text=str(i[x+1]),font=("times new roman",15)).grid(column=x,row=9+2*y)
                Label(self.FRAME,text="---------------------------",font=("times new roman",15)).grid(column=x,row=10+2*y)         
            y+=1
            
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")

    def getClientInfo(self):
        accountHolderDetails=[]
        with open("Personal_Details.txt", 'r') as file:
            for line in file:
                split1 = line.strip().split("|")
                if self.accountNumber in split1:
                    accountHolderDetails=split1
        self.title=accountHolderDetails[1]
        self.fullName=accountHolderDetails[2]
        self.name=accountHolderDetails[3]
        self.IDNo=accountHolderDetails[4]
        self.birthYear=accountHolderDetails[5]
        self.birthMonth=accountHolderDetails[6]
        self.birthDate=accountHolderDetails[7]
        self.occupation=accountHolderDetails[8]
        self.addressNo=accountHolderDetails[9]
        self.line1=accountHolderDetails[10]
        self.line2=accountHolderDetails[11]
        self.line3=accountHolderDetails[12]
        self.contactNo=accountHolderDetails[13]
        self.email=accountHolderDetails[14]


        passbookData=[]
        recentActivity=[]
        with open("Passbook.txt", 'r') as file1:
            for line in file1:
                split2 = line.strip().split("|")
                if self.accountNumber in split2:
                    passbookData.append(split2)                
        recentActivity=passbookData[-1]
        self.balance=recentActivity[4]
        return passbookData


 




