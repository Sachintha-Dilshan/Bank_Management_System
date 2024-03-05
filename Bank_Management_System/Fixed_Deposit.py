from tkinter import *
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
from Get_Personal_Info import GetPersonalInfo
from Cash_Deposit import CashDeposit

class FixedDepositPage1(GetPersonalInfo):
    def __init__(self,main_frame,accountNumber,date,balance):
        self.mainTitle="Smart FD Application"
        self.balance=balance
        super().__init__(main_frame,accountNumber,date)
       
    def next(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        obj=FixedDepositPage2(self.main_frame,self.frame,self.accountNumber,self.title,self.name,self.balance)
        
class FixedDepositPage2:
    def __init__(self,main_frame,frame,accountNumber,title,name,balance):
        self.main_frame=main_frame
        self.frame=frame
        self.accountNumber=accountNumber
        self.title=title
        self.name=name
        self.balance=balance
        lbl1=Label(self.frame,text="Deposit Informations",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=5)
        lblAmountInFigure = Label(self.frame, text="Amount in Figure", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=10,y=40)
        lblRs1 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=200,y=40)                     
        self.txtamountInFigure = Entry(self.frame, font=("times new roman", 15), bg="lightgray", width=15)
        self.txtamountInFigure.place(x=250, y=40)

        lblAmountInWords = Label(self.frame, text="Amount in Words", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=10,y=70)
        lblRs2 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=200,y=70)                     
        self.txtamountInWords = Entry(self.frame, font=("times new roman", 15), bg="lightgray", width=30)
        self.txtamountInWords.place(x=250, y=70)
        lblNote=Label(self.frame,text="*Minimum deposit value should be Rs.25000.00",font=("times new roman",12),fg="red",bg="white",width=50).place(x=10,y=100)
        lblTerm = Label(self.frame, text="Term of Deposit", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=10,y=130)
        self.cmbTerm = ttk.Combobox(self.frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbTerm['values'] = ("Select","01 Month","02 Months","03 Months","06 Months","12 Months","24 Months","36 Months","48 Months","60 Months")
        self.cmbTerm.place(x=250, y=130, width=115)
        self.cmbTerm.current(0)
        bntRate=Button(self.frame,text="Rate",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.changeRate,cursor="hand2",borderwidth=5).place(x=400,y=130)
       
        self.lblRate=Label(self.frame,text="",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.lblRate.place(x=500,y=130)
        ############################################################################################################################################## 
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar()  
        lbl2=Label(self.frame,text="Funds Availability",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=180)
        self.check1 = Checkbutton(self.frame, text="From Account", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var1,command=self.check)
        self.check1.place(x=10, y=215)
        self.check2 = Checkbutton(self.frame, text="Other", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var2,command=self.check)
        self.check2.place(x=350, y=215)
        ##############################################################################################################################################
        lbl3=Label(self.frame,text="Maturity Instructions & Interest Payment",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=265)
        lblRenewelOption = Label(self.frame, text="Interest Payment", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=10,y=305)
        self.check3= Checkbutton(self.frame, text="Renewel with Interest", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var3,command=self.check)
        self.check3.place(x=350, y=330)
        self.check4 = Checkbutton(self.frame, text="Transfer Interest to Account", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var4,command=self.check)
        self.check4.place(x=10, y=330)
        ##################################################################################################################################################
        lbl4=Label(self.frame,text="If interest to be transfered to an account, please indicate whether \ninterest payment is tobe made monthly or at maturity",font=("times new roman",15,"bold"),bg="white",justify=LEFT).place(x=10,y=370)
        self.check5= Checkbutton(self.frame, text="Monthly", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var5,command=self.check)
        self.check5.place(x=350, y=420)
        self.check6 = Checkbutton(self.frame, text="At Maturity", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var6,command=self.check)
        self.check6.place(x=10, y=420)
        self.update_clock()
        bntSubmit=Button(self.frame,text="Submit",font=("times new roman",15,"bold"),bg="red",fg="white",command=self.submit,cursor="hand2",borderwidth=5).place(x=480,y=450)
    def check(self):
        if self.var1.get()==1:
            self.check2.configure(state=DISABLED)
        elif self.var2.get()==1:
            self.check1.configure(state=DISABLED)
        else:
            self.check1.configure(state=NORMAL)
            self.check2.configure(state=NORMAL)
        if self.var3.get()==1:
            self.check4.configure(state=DISABLED)
        elif self.var4.get()==1:
            self.check3.configure(state=DISABLED)
        else:
            self.check3.configure(state=NORMAL)
            self.check4.configure(state=NORMAL)
        if self.var5.get()==1:
            self.check6.configure(state=DISABLED)
        elif self.var6.get()==1:
            self.check5.configure(state=DISABLED)
        else:
            self.check5.configure(state=NORMAL)
            self.check6.configure(state=NORMAL)
    def getStockInfo(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)            
            lastTransaction=stockDetails[-1]
            self.currentStock=lastTransaction[3] 
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")
    def submit(self):
        if self.txtamountInFigure.get()=="":
            messagebox.showerror("Submit FD Application", "Please fill the amount in figure")
        elif self.txtamountInWords.get()=="":
            messagebox.showerror("Submit FD Application", "Please fill the amount in words")
        elif self.cmbTerm.get()=="Select":
            messagebox.showerror("Submit FD Application", "Please select the deposit period")
        elif self.var1.get()==0 and self.var2.get()==0:
            messagebox.showerror("Submit FD Application", "Please select a option")
        elif self.var3.get()==0 and self.var4.get()==0:
            messagebox.showerror("Submit FD Application", "Please select a option")
        elif self.var5.get()==0 and self.var6.get()==0:
            messagebox.showerror("Submit FD Application", "Please select a option")
        else:
            if self.var1.get()==1:
                option1="From Account"
            elif self.var2.get()==1:
                option1="Other"
            if self.var3.get()==1:
                option2="Transfer Interest to Account"
            elif self.var4.get()==1:
                option2="Renewel With Interest"
            if self.var5.get()==1:
                option3="At Maturity"
            elif self.var6.get()==1:
                option3="Monthly"
            if int(self.txtamountInFigure.get())>=25000:
                refNumber=id(self.txtamountInFigure.get())
                updatedBalance=int(self.balance)-int(self.txtamountInFigure.get())
                if option1=="From Account":
                    with open("Passbook.txt", 'a') as file:
                        file.write(str(self.accountNumber) + "|" + str(self.date_now) +"|" + str(self.time_now) + "|" + ("-"+str(self.txtamountInFigure.get())) + "|" + str(updatedBalance) + "\n")
                    with open("FD_Details.txt",'a') as file1:
                        file1.write(str(self.accountNumber)+"|"+str(refNumber)+"|"+str(self.title+"."+self.name)+"|"+str(self.txtamountInFigure.get())+"|"+str(self.txtamountInWords.get())+"|"+str(self.cmbTerm.get())+"|"+str(option1)+"|"+str(option2)+"|"+str(option3)+"\n")
                    messagebox.showinfo("Fixed Deposit","Succeffully Deposited "+"Rs."+str(self.txtamountInWords.get())+"\n"+"Reference Number:"+str(refNumber))
                    messagebox.showinfo("Withdrawal Money", "Your A/C:" + str(self.accountNumber)+" Successfully Debited Rs: "+str(self.txtamountInFigure.get()))
                    for widgets in self.frame.winfo_children():
                        widgets.destroy()
                    from User_Interface import AccountDetailsView
                    obj1=AccountDetailsView(self.main_frame,self.accountNumber)
                elif option1=="Other":
                    depositDetails=[self.txtamountInWords.get(),self.cmbTerm.get(),option1,option2,option3]
                    obj=OtherDeposit(self.main_frame,self.balance,self.accountNumber,self.date_now,self.time_now,self.title,self.name,refNumber,updatedBalance,self.txtamountInFigure.get(),depositDetails)
            else:
                messagebox.showerror("Fixed Deposit","Minimum Deposit Amount Shold be Rs.25000.00")
               
    def changeRate(self):
        x=self.cmbTerm.get()
        y=self.lblRate
        if x=="01 Month":
            y.configure(text="4%")
        elif x=="02 Months":
            y.configure(text="4%")
        elif x=="03 Months":
            y.configure(text="4.25%")
        elif x=="06 Months":
            y.configure(text="4.75%")
        elif x=="12 Months":
            y.configure(text="5.40%")
        elif x=="24 Months":
            y.configure(text="5.50%")
        elif x=="36 Months":
            y.configure(text="5.85%")
        elif x=="48 Months":
            y.configure(text="6.05%")
        elif x=="60 Months":
            y.configure(text="6.25%")
        else:
            y.configure(text="")
class OtherDeposit(CashDeposit):
    def __init__(self,root1,balance,accountNumber,date,time,title,accountHolderName,refNumber,updatedBalance,depositAmount,depositDetails):
        self.mainTitle="Loan Application"
        self.refNumber=refNumber
        self.updatedBAlance=updatedBalance
        self.depositAmount=depositAmount
        self.depositDetails=depositDetails
        super().__init__(root1,balance,accountNumber,date,time,title,accountHolderName)
    def deposit(self):
        if int(self.depositAmount)<=int(self.total):
            UpdatedStock=int(self.total)+int(self.currentStock)
            with open("Money_Stock.txt",'a') as file2:
                file2.write( str(self.date) +"|"+str(self.time)+ "|" + ("+"+str(self.depositAmount)) + "|" + str(UpdatedStock) + "\n")       
            with open("FD_Details.txt",'a') as file:
                file.write(str(self.accountNumber)+"|"+str(self.refNumber)+"|"+str(self.title+"."+self.name)+"|"+str(self.depositAmount)+"|"+str(self.depositDetails[0])+"|"+str(self.depositDetails[1])+"|"+str()+"|"+str(self.depositDetails[2])+"|"+str(self.depositDetails[3])+"\n")
            messagebox.showinfo("Fixed Deposit","Succeffully Deposited "+"Rs."+str(self.depositAmount)+"\n"+"Reference Number:"+str(self.refNumber))
            from User_Interface import AccountDetailsView
            for widgets in self.root2.winfo_children():
                    widgets.destroy()
            obj1=AccountDetailsView(self.frame,self.accountNumber)
        else:
            messagebox.showerror("Fixed Deposit","FD amount and total isn't match")
            self.clear()

                 





