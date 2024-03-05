from tkinter import *
from tkinter import messagebox
from datetime import datetime
from Get_Personal_Info import GetPersonalInfo

class ApprobvedLoanPage1(GetPersonalInfo):
    def __init__(self,main_frame,accountNumber,date):
        self.mainTitle="Loan Application"
        super().__init__(main_frame,accountNumber,date)
       
    def next(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        obj=LoanPage2(self.main_frame,self.frame,self.accountNumber)
           
class LoanPage2:
    def __init__(self,main_frame,frame,accountNumber):
        self.main_frame=main_frame
        self.frame=frame
        self.accountNumber=accountNumber
        ################################################################################################################################
        lbl1=Label(self.frame,text="Financial Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=5)
        self.lblOption1 = Label(self.frame, text="Salaried", font=("times new roman", 15),bg="white")
        self.lblOption1.place(x=10, y=40)

        ##################################################################################################################################
        lbl2=Label(self.frame,text="Monthly Income",font=("times new roman",15,"bold"),fg="white",bg="green",width=18).place(x=10,y=90)
        lblBasicSalary = Label(self.frame, text="Basic Salary", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=125)
        lblRs1 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=125)
        self.txtBasicSalary = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtBasicSalary.place(x=300, y=125, width=250)
        
        lblFixedAllowance = Label(self.frame, text="Fixed Allowance", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=155)
        lblRs2 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=155)
        self.txtFixedAllowance = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtFixedAllowance.place(x=300, y=155, width=250)
        
        lblVariableIncome = Label(self.frame, text="Variable Income", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=185)
        lblRs3 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=185)
        self.txtVariableIncome = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtVariableIncome.place(x=300, y=185, width=250)
 
        lblRs4 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=230)
        self.txtTotalIncome = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtTotalIncome.place(x=300, y=230, width=250)
        #####################################################################################################################################
        lb3=Label(self.frame,text="Monthly Expences",font=("times new roman",15,"bold"),fg="white",bg="green",width=18).place(x=10,y=280)
        lbltax = Label(self.frame, text="Payee Tax", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=315)
        lblRs3 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=315)
        self.txtTax = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtTax.place(x=300, y=315, width=250)

        lblLoanRepayments = Label(self.frame, text="Existing Loan Repayments", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=345)
        lblRs3 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=345)
        self.txtLoanRepayments = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtLoanRepayments.place(x=300, y=345, width=250)

        lblRs4 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=390)
        self.txtTotalExpenses = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtTotalExpenses.place(x=300, y=390, width=250)
        bntnext=Button(self.frame,text="NEXT",font=("times new roman",20,"bold"),bg="green",fg="white",command=self.next).place(x=480,y=435)
        self.insertInfo()
 
    def getLoanDetails(self):
        details=[]
        with open("Approved_Loans.txt", "r") as file:
            for line in file:
                split=line.strip().split("|")
                if self.accountNumber in split:
                    details.append(split)
        LoanDetails=details[0]        
        self.title=LoanDetails[1]
        self.name=LoanDetails[2]
        self.option1=LoanDetails[3]
        self.basicSalary=LoanDetails[4]
        self.fixedAllowance=LoanDetails[5]
        self.variableIncome=LoanDetails[6]
        self.tax=LoanDetails[7]
        self.loanRepayment=LoanDetails[8]
        self.loanType=LoanDetails[9]
        self.loanAmountInFigure=LoanDetails[10]
        self.loanAmountInWord=LoanDetails[11]
        self.purpose=LoanDetails[12]
        self.option2=LoanDetails[13]
        self.option3=LoanDetails[14]
        self.page3Details=[self.loanType,self.loanAmountInFigure,self.loanAmountInWord,self.purpose,self.option2,self.option3]
    def insertInfo(self):
        self.getLoanDetails()
        if self.option1=="Salaried":
            self.lblOption1.configure(text="Salaried")
        else:
            self.lblOption1.configure(text="Self Employment")
        self.txtBasicSalary.insert(0,self.basicSalary)
        self.txtFixedAllowance.insert(0,self.fixedAllowance)
        self.txtVariableIncome.insert(0,self.variableIncome)
        self.totalIncome=int(self.basicSalary)+int(self.fixedAllowance)+int(self.variableIncome)
        self.txtTotalIncome.insert(0,self.totalIncome)
        self.txtTax.insert(0,self.tax)
        self.txtLoanRepayments.insert(0,self.loanRepayment)
        self.totalExpenses=int(self.tax)+int(self.loanRepayment)
        self.txtTotalExpenses.insert(0,self.totalExpenses)

        self.txtBasicSalary.configure(state=DISABLED)
        self.txtFixedAllowance.configure(state=DISABLED)
        self.txtVariableIncome.configure(state=DISABLED)
        self.txtTotalIncome.configure(state=DISABLED)
        self.txtTax.configure(state=DISABLED)
        self.txtLoanRepayments.configure(state=DISABLED)
        self.txtTotalExpenses.configure(state=DISABLED)

        

    def next(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        obj=LoanPage3(self.main_frame,self.frame,self.page3Details,self.accountNumber)

class LoanPage3:
    def __init__(self,main_frame,frame,page3Details,accountNumber):
        self.page3Details=page3Details
        self.accountNumber=accountNumber
        self.main_frame=main_frame
        self.frame=frame
        lbl=Label(self.frame,text="Loan Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=5)
        ########################
        self.lblLoanType = Label(self.frame, text="Loan Type", font=("times new roman", 16, "bold"), bg="white", fg="gray")
        self.lblLoanType.place(x=10, y=50)
        ######################################
        lblLoanAmount = Label(self.frame, text="Loan Amount", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=125)
        lblRs1 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=125)
        self.txtLoanAmount = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtLoanAmount.place(x=300, y=125, width=250)
        ##########################################        
        lblRepaymentPeriod = Label(self.frame, text="Repayment Period(Months)", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=155)
        self.txtRepeymentPeriod = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtRepeymentPeriod.place(x=300, y=155, width=250)
        ########################################        
        lblPurpose = Label(self.frame, text="Purpose of The Loan", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=185)
        self.txtPurpose = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtPurpose.place(x=300, y=185, width=250)

        lblOption1 = Label(self.frame, text="Replacement Option", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=235)
        self.lblOption2 = Label(self.frame, text=" ", font=("times new roman", 15),bg="white")
        self.lblOption2.place(x=20, y=275)
 

        lblOption2 = Label(self.frame, text="Availability of Guarantors", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=320)
        self.lblOption3 = Label(self.frame, text="", font=("times new roman", 15),bg="white")
        self.lblOption3.place(x=20, y=360)

        self.insertInfo()


    def insertInfo(self):
        self.lblLoanType.configure(text=("Loan Type:"+self.page3Details[0]))
        self.txtLoanAmount.insert(0,self.page3Details[1])
        self.txtRepeymentPeriod.insert(0,self.page3Details[2])
        self.txtPurpose.insert(0,self.page3Details[3])
        self.lblOption2.configure(text=self.page3Details[4])
        self.lblOption3.configure(text=self.page3Details[5])
        self.txtLoanAmount.configure(state=DISABLED)
        self.txtRepeymentPeriod.configure(state=DISABLED)
        self.txtPurpose.configure(state=DISABLED)
        
    def getStockInfo(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)            
            lastTransaction=stockDetails[-1]
            self.currentStock=lastTransaction[3]
    def getPassbookInfo(self):
        passbookData=[]
        recentActivity=[]
        with open("Passbook.txt", 'r') as file1:
            for line in file1:
                split2 = line.strip().split("|")
                if self.accountNumber in split2:
                    passbookData.append(split2)          
        recentActivity=passbookData[-1]
        self.balance=recentActivity[4] 
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")