from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Get_Personal_Info import GetPersonalInfo


class LoanPage1(GetPersonalInfo):
    def __init__(self,main_frame,accountNumber,date):
        self.mainTitle="Loan Application"
        super().__init__(main_frame,accountNumber,date)
        
       
    def next(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        obj=LoanPage2(self.main_frame,self.frame,self.accountNumber,self.title,self.name)
    
        
class LoanPage2:
    def __init__(self,main_frame,frame,accountNumber,title,name):
        self.main_frame=main_frame
        self.frame=frame
        self.accountNumber=accountNumber
        self.title=title
        self.name=name
        ################################################################################################################################
        lbl1=Label(self.frame,text="Financial Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=5)
        self.var1=IntVar()
        self.var2=IntVar()
        self.check1 = Checkbutton(self.frame, text="Salaried", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var1,command=self.check)
        self.check1.place(x=10, y=40)
        self.check2 = Checkbutton(self.frame, text="Self Employed", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var2,command=self.check)
        self.check2.place(x=350, y=40)
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
 
        self.btnIncome = Button(self.frame, text="Total Income", font=("times new roman", 15, "bold"), bg="white", fg="green",command=self.getTotalIncome,cursor="hand2",borderwidth=5)
        self.btnIncome.place(x=10, y=220)
        lblRs4 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=230)
        self.txtTotalIncome = Entry(self.frame, font=("times new roman", 15), bg="lightgray",state=DISABLED)
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

        self.btnExpenses = Button(self.frame, text="Total Expenses", font=("times new roman", 15, "bold"), bg="white", fg="green",command=self.getTotalExpenses,cursor="hand2",borderwidth=5)
        self.btnExpenses.place(x=10, y=380)
        lblRs4 = Label(self.frame, text="Rs.", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=260,y=390)
        self.txtTotalExpenses = Entry(self.frame, font=("times new roman", 15), bg="lightgray",state=DISABLED)
        self.txtTotalExpenses.place(x=300, y=390, width=250)

        
        bntnext=Button(self.frame,text="NEXT",font=("times new roman",20,"bold"),bg="green",fg="white",command=self.next,cursor="hand2",borderwidth=5).place(x=480,y=435)

    def getTotalIncome(self):
        financialDetails=[self.txtBasicSalary.get(),self.txtFixedAllowance.get(),self.txtVariableIncome.get()]  
        if self.btnIncome['text']=="Total Income":
            self.income=[]
            for i in range(3):
                if financialDetails[i]=="":
                    financialDetails[i]=0
                self.income.append(financialDetails[i])
            self.totalIncome=int(self.income[0])+int(self.income[1])+int(self.income[2])
            self.txtTotalIncome.configure(state=NORMAL)
            self.txtTotalIncome.insert(0,self.totalIncome)
            self.txtTotalIncome.configure(state=DISABLED)
            self.txtBasicSalary.configure(state=DISABLED)
            self.txtFixedAllowance.configure(state=DISABLED)
            self.txtVariableIncome.configure(state=DISABLED)
            self.btnIncome.configure(text="Change Income")
        else:
            self.txtTotalIncome.configure(state=NORMAL)
            self.txtTotalIncome.delete(0,END)
            self.txtTotalIncome.configure(state=DISABLED)
            self.txtBasicSalary.configure(state=NORMAL)
            self.txtFixedAllowance.configure(state=NORMAL)
            self.txtVariableIncome.configure(state=NORMAL)
            self.txtBasicSalary.delete(0,END)
            self.txtFixedAllowance.delete(0,END)
            self.txtVariableIncome.delete(0,END)
            self.btnIncome.configure(text="Total Income")

    def getTotalExpenses(self):
        financialDetails=[self.txtTax.get(),self.txtLoanRepayments.get()]  
        if self.btnExpenses['text']=="Total Expenses":
            self.expenses=[]
            for i in range(2):
                if financialDetails[i]=="":
                    financialDetails[i]=0
                self.expenses.append(financialDetails[i])
            self.totalExpenses=int(self.expenses[0])+int(self.expenses[1])
            self.txtTotalExpenses.configure(state=NORMAL)
            self.txtTotalExpenses.insert(0,self.totalExpenses)
            self.txtTotalExpenses.configure(state=DISABLED)
            self.txtTax.configure(state=DISABLED)
            self.txtLoanRepayments.configure(state=DISABLED)
            self.btnExpenses.configure(text="Change Expenses")
        else:
            self.txtTotalExpenses.configure(state=NORMAL)
            self.txtTotalExpenses.delete(0,END)
            self.txtTotalExpenses.configure(state=DISABLED)
            self.txtTax.configure(state=NORMAL)
            self.txtLoanRepayments.configure(state=NORMAL)
            self.txtTax.delete(0,END)
            self.txtLoanRepayments.delete(0,END)
            self.btnExpenses.configure(text="Total Expenses")

    def check(self):
        if self.var1.get()==1:
            self.check2.configure(state=DISABLED)
        elif self.var2.get()==1:
            self.check1.configure(state=DISABLED)
        else:
            self.check1.configure(state=NORMAL)
            self.check2.configure(state=NORMAL)
                           
    def next(self):
        if self.var1.get()==0 and self.var2.get()==0:
            messagebox.showerror("Loan Application", "Please select a option")
        elif self.btnIncome['text']=="Change Income" and self.btnExpenses['text']=="Change Expenses":
            if self.var1.get()==1:
                employment="Salaried"
            else:
                employment="Self Employment"
            page1Details=[self.accountNumber,self.title,self.name,employment,self.income[0],self.income[1],self.income[2],self.expenses[0],self.expenses[1]]
            for widgets in self.frame.winfo_children():
                widgets.destroy()
            obj=LoanPage3(self.main_frame,self.frame,page1Details)
        else:
            messagebox.showerror("Loan Application", "Please fill the income and expenses details")
class LoanPage3:
    def __init__(self,main_frame,frame,page1Details):
        self.main_frame=main_frame
        self.frame=frame
        self.page1Details=page1Details
        lbl=Label(self.frame,text="Loan Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=5)
        ########################
        lblLoanType = Label(self.frame, text="Loan Type", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=50)
        self.cmbLoanType = ttk.Combobox(self.frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbLoanType['values'] = ("Select","Personal Loan","Home Loan","Education Loan")
        self.cmbLoanType.place(x=150, y=50)
        self.cmbLoanType.current(0)
        bntRate=Button(self.frame,text="Rate",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.changeRate,cursor="hand2",borderwidth=5).place(x=380,y=50)
        self.lblLoanRate=Label(self.frame,text="",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.lblLoanRate.place(x=450,y=50)
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

        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        lblOption1 = Label(self.frame, text="Replacement Option", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=235)
        self.check1 = Checkbutton(self.frame, text="Fixed Installments", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var1,command=self.check)
        self.check1.place(x=20, y=275)
        self.check2 = Checkbutton(self.frame, text="Reducing Installments", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var2,command=self.check)
        self.check2.place(x=350, y=275)

        lblOption2 = Label(self.frame, text="Availability of Guarantors", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=320)
        self.check3 = Checkbutton(self.frame, text="Yes", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var3,command=self.check)
        self.check3.place(x=20, y=360)
        self.check4 = Checkbutton(self.frame, text="No", font=("times new roman", 15),bg="white", onvalue=1, offvalue=0,variable=self.var4,command=self.check)
        self.check4.place(x=350, y=360)
        
        bntSubmit=Button(self.frame,text="SUBMIT",font=("times new roman",15,"bold"),bg="red",fg="white",command=self.submit,cursor="hand2",borderwidth=5).place(x=480,y=435)
    def changeRate(self):
        self.getRates()
        if self.cmbLoanType.get()=="Select":
            messagebox.showerror("Update Rates","Please Select a type")
            self.lblLoanRate.configure(text="Rate")
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

    def submit(self):
        if self.cmbLoanType.get()=="Select":
            messagebox.showerror("Loan Application", "Please select the loan type")
        elif self.txtLoanAmount.get()=="":
            messagebox.showerror("Loan Application", "Please fil the Amount")
        elif self.txtRepeymentPeriod.get()=="":
            messagebox.showerror("Loan Application", "Please fill the repayment period")
        elif self.txtPurpose.get()=="":
            messagebox.showerror("Loan Application", "Please fill the purpose of the loan")
        elif self.var3.get()==0 and self.var4.get()==0:
            messagebox.showerror("Loan Application", "Please select a option")
        elif self.var1.get()==0 and self.var2.get()==0:
            messagebox.showerror("Loan Application", "Please select a option")
        else:
            option1=" "
            if self.var1.get()==1:
                option1="Fixed Installmets"
            elif self.var2.get()==1:
                option1="Reducing Installments"
            if self.var3.get()==1:
                option2="Yes"
            elif self.var4.get()==1:
                option2="No"

            LoanDetails=[self.page1Details[0],self.page1Details[1],self.page1Details[2],self.page1Details[3],self.page1Details[4],self.page1Details[5],self.page1Details[6],self.page1Details[7],self.page1Details[8],self.cmbLoanType.get(),self.txtLoanAmount.get(),self.txtRepeymentPeriod.get(),self.txtPurpose.get(),option1,option2]
            with open("Loan_Details.txt",'a') as file:
                file.write(str(LoanDetails[0])+"|"+str(LoanDetails[1])+"|"+str(LoanDetails[2])+"|"+str(LoanDetails[3])+"|"+str(LoanDetails[4])+"|"+str(LoanDetails[5])+"|"+str(LoanDetails[6])+"|"+str(LoanDetails[7])+"|"+str(LoanDetails[8])+"|"+str(LoanDetails[9])+"|"+str(LoanDetails[10])+"|"+str(LoanDetails[11])+"|"+str(LoanDetails[12])+"|"+str(LoanDetails[13])+"|"+str(LoanDetails[14])+"\n")
            messagebox.showinfo("Loan Application", "Your loan application successfully submited for the approval")
            for widgets in self.main_frame.winfo_children():
                widgets.destroy()
            from User_Interface import AccountDetailsView
            obj1=AccountDetailsView(self.main_frame,self.page1Details[0])

  


        



