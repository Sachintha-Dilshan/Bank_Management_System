from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from User_Interface import BankStatement
from Get_Loan_Details import LoanPage1
from Get_FD_Info import FixedDepositPage1
from Get_Approved_Loan_Details import ApprobvedLoanPage1

class Search:
    def __init__(self,main_frame,date):
        self.main_frame=main_frame
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        self.date=date
        title = Label(frame, text="Search Informations", font=("times new roman", 20, "bold"), bg="white",fg="green").place(x=10, y=30)
        lblNote=Label(frame,text="*Enter Account number to search details",font=("times new roman",15),fg="red",bg="white").place(x=20,y=120)
        self.cmbSearch = ttk.Combobox(frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbSearch['values'] = ("Select","Personal Informations","Pending Loan Details","Approved Loan Details","FD Details","Transaction Report")
        self.cmbSearch.place(x=70, y=170)
        self.cmbSearch.current(0)
        self.txtSearch=Entry(frame,font=("times new roman",15),bg="lightgray")
        self.txtSearch.place(x=320,y=170)
        
        btnSearch=Button(frame,text="Search",font=("times new roman",15,"bold"),fg="white",bg="red",command=self.search,cursor="hand2",borderwidth=5).place(x=250,y=220)
        self.main_frame.mainloop()
    def search(self):
        self.accountNumber=str(self.txtSearch.get())
        if self.cmbSearch.get()=="Select":
             messagebox.showerror("Search Info","Please select a type to search")
        elif self.accountNumber=="":
            messagebox.showerror("Search Info","Please enter a account number")
        else:   
            x=0
            with open("personal_details.txt",'r') as file:
                for line in file:
                    split=line.strip().split("|")
                    if self.accountNumber in split:
                        x=1
            if x==1:
                if self.cmbSearch.get()=="Personal Informations":
                    obj=GetPersonalInfo(self.main_frame,self.accountNumber,self.date)
                elif self.cmbSearch.get()=="Pending Loan Details":
                    obj=LoanPage1(self.main_frame,self.accountNumber,self.date)
                elif self.cmbSearch.get()=="Approved Loan Details":
                    obj=ApprobvedLoanPage1(self.main_frame,self.accountNumber,self.date)
                elif self.cmbSearch.get()=="FD Details":
                    obj=FixedDepositPage1(self.main_frame,self.accountNumber,self.date)
                elif self.cmbSearch.get()=="Transaction Report":
                    obj=BankStatement(self.accountNumber)
            else:
                messagebox.showerror("Search Info","Invalid Account Number")
class GetPersonalInfo:
    def __init__(self,main_frame,accountNumber,date):
        self.main_frame=main_frame
        self.accountNumber=accountNumber
        self.date=date
        self.getClientInfo()
   
        self.frame=Frame(self.main_frame,bg="white")
        self.frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        #----------------Row1
        lblAccountNo = Label(self.frame, text="Account Number", font=("times new roman", 16, "bold"), bg="white", fg="gray").place(x=10, y=40)
        self.txtAccountNo = Entry(self.frame, font=("times new roman", 15), bg="lightgray", width=15,justify=CENTER)
        self.txtAccountNo.place(x=10, y=69)

        lblDate = Label(self.frame, text="Date", font=("times new roman", 16, "bold"),
                             bg="white", fg="gray").place(x=425, y=40)
        self.txtDate = Entry(self.frame, font=("times new roman", 15), bg="lightgray", width=15,justify=CENTER)
        self.txtDate.place(x=425, y=69)
     

   ########################################
        title = Label(self.frame, text="Personal Details", font=("times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=10, y=10)
        lblPersonalDetails=Label(self.frame,text="Personal Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=18).place(x=10,y=100)
        # --------------------Row1

        lblfullName = Label(self.frame, text="Full Name", font=("times new roman", 15, "bold"), bg="white",
                            fg="gray").place(x=250, y=115)
        self.txtFullName = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtFullName.place(x=10, y=140, width=570)
        # --------------------Row2
        lblNameInt = Label(self.frame, text="Name With Initials (surname x.x.x)", font=("times new roman", 15, "bold"),
                           bg="white", fg="gray").place(x=10, y=170)
        self.txtNameInt = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtNameInt.place(x=10, y=200, width=250)

        lblId = Label(self.frame, text="National ID No", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=330, y=170)
        self.txtId = Entry(self.frame, font=("times new roman", 15), bg="lightgray",justify=CENTER)
        self.txtId.place(x=330, y=200, width=250)
        # --------------------Row3
        lblDOB = Label(self.frame, text="Date of Birth (0000/00/00)", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=10, y=240)

        lblYear = Label(self.frame, text="Year", font=("times new roman", 12), bg="white").place(x=10, y=270)
        self.txtYear = Entry(self.frame, font=("times new roman", 15), bg="lightgray",justify=CENTER)
        self.txtYear.place(x=45, y=270, width=50)

        lblMonth = Label(self.frame, text="Month", font=("times new roman", 12), bg="white").place(x=95, y=270)
        self.txtMonth = Entry(self.frame, font=("times new roman", 15), bg="lightgray",justify=CENTER)
        self.txtMonth.place(x=140, y=270, width=40)

        lblDate = Label(self.frame, text="Date", font=("times new roman", 12), bg="white").place(x=185, y=270)
        self.txtBirthDate = Entry(self.frame, font=("times new roman", 15), bg="lightgray",justify=CENTER)
        self.txtBirthDate.place(x=220, y=270, width=40)

        lblOcupation = Label(self.frame, text="Ocupation", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=330, y=240)
        self.txtOcupation = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtOcupation.place(x=330, y=270, width=250)
        # --------------------Row4
        lblAddress = Label(self.frame, text="Address", font=("times new roman", 15, "bold"), bg="white",
                           fg="gray").place(x=10, y=310)
        self.txtAddressNo = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtAddressNo.place(x=100, y=340, width=160)

        lblAdressNo=Label(self.frame,text="House No", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=10, y=340)
        lblLine1=Label(self.frame,text="Line  01", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=10, y=380) 
        self.txtLine1 = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtLine1.place(x=100, y=380, width=160)                    
        lblLine2=Label(self.frame,text="Line  02", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=10, y=420)
        self.txtLine2 = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtLine2.place(x=100, y=420, width=160)                            
        lblLine3=Label(self.frame,text="Line  03", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=10, y=460)
        self.txtLine3 = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtLine3.place(x=100, y=460, width=160)    

        lblContactNo = Label(self.frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=330, y=310)  
        self.txtContactNo = Entry(self.frame, font=("times new roman", 15), bg="lightgray",justify=CENTER)
        self.txtContactNo.place(x=330, y=340, width=250)
        lblEmail=Label(self.frame,text="Email", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=330, y=380)  
        self.txtEmail = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtEmail.place(x=330, y=420, width=250)
        self.insertInfo()                        
        self.main_frame.mainloop()
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
        
    def insertInfo(self):
        self.txtAccountNo.insert(0,self.accountNumber)
        self.txtDate.insert(0,self.date)
        self.txtFullName.insert(0,(self.title+"."+self.fullName))
        self.txtNameInt.insert(0,self.name)
        self.txtId.insert(0,self.IDNo)
        self.txtYear.insert(0,self.birthYear)
        self.txtMonth.insert(0,self.birthMonth)
        self.txtBirthDate.insert(0,self.birthDate)
        self.txtOcupation.insert(0,self.occupation)
        self.txtAddressNo.insert(0,self.addressNo)
        self.txtLine1.insert(0,self.line1)
        self.txtLine2.insert(0,self.line2)
        self.txtLine3.insert(0,self.line3)
        self.txtContactNo.insert(0,self.accountNumber)
        self.txtEmail.insert(0,self.email)

        self.txtDate.configure(state=DISABLED)
        self.txtAccountNo.configure(state=DISABLED)
        self.txtFullName.configure(state=DISABLED)
        self.txtNameInt.configure(state=DISABLED)
        self.txtId.configure(state=DISABLED)
        self.txtYear.configure(state=DISABLED)
        self.txtMonth.configure(state=DISABLED)
        self.txtBirthDate.configure(state=DISABLED)
        self.txtOcupation.configure(state=DISABLED)
        self.txtAddressNo.configure(state=DISABLED)
        self.txtLine1.configure(state=DISABLED)
        self.txtLine2.configure(state=DISABLED)
        self.txtLine3.configure(state=DISABLED)
        self.txtContactNo.configure(state=DISABLED)
        self.txtEmail.configure(state=DISABLED)   
