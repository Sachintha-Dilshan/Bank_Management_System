from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  datetime import datetime
from Cash_Deposit import CashDeposit

class Create:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600+280+80")
        self.root.title("Create a New Account")
        lblbackground = Label(self.root, bg="green", width=35, height=35).place(x=70, y=40)

        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=320, y=40, width=600, height=530)

        title = Label(self.frame, text="Create a New Account", font=("times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=10, y=30)
        lblPersonalDetails=Label(self.frame,text="Personal Details",font=("times new roman",15,"bold"),fg="white",bg="green",width=18).place(x=10,y=70)

        # --------------------Row1
        title2 = Label(self.frame, text="Title", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=10,
                                                                                                                   y=100)
        self.cmbtitle = ttk.Combobox(self.frame, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.cmbtitle['values'] = ("Mr", "Ms", "Rev", "Dr", "Prof")
        self.cmbtitle.place(x=10, y=130, width=100)
        self.cmbtitle.current(0)

        lblfullName = Label(self.frame, text="Full Name", font=("times new roman", 15, "bold"), bg="white",
                            fg="gray").place(x=330, y=100)
        self.txtFullName = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtFullName.place(x=110, y=130, width=470)
        # --------------------Row2
        lblNameInt = Label(self.frame, text="Name With Initials (surname x.x.x)", font=("times new roman", 15, "bold"),
                           bg="white", fg="gray").place(x=10, y=170)
        self.txtNameInt = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtNameInt.place(x=10, y=200, width=250)

        lblId = Label(self.frame, text="National ID No", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=330, y=170)
        self.txtId = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtId.place(x=330, y=200, width=250)
        # --------------------Row3
        lblDOB = Label(self.frame, text="Date of Birth (0000/00/00)", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=10, y=240)
        lblYear = Label(self.frame, text="Year", font=("times new roman", 12), bg="white").place(x=10, y=270)
        self.txtYear = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtYear.place(x=45, y=270, width=50)

        lblMonth = Label(self.frame, text="Month", font=("times new roman", 12), bg="white").place(x=95, y=270)
        self.txtMonth = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtMonth.place(x=140, y=270, width=40)

        lblDate = Label(self.frame, text="Date", font=("times new roman", 12), bg="white").place(x=185, y=270)
        self.txtDate = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtDate.place(x=220, y=270, width=40)

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
        self.txtContactNo = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtContactNo.place(x=330, y=340, width=250)
        lblEmail=Label(self.frame,text="Email", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray").place(x=330, y=380)  
        self.txtEmail = Entry(self.frame, font=("times new roman", 15), bg="lightgray")
        self.txtEmail.place(x=330, y=420, width=250)                                 
        btn = Button(self.frame, text="Create a New Account", font=("times new roman", 16, "bold"), cursor="hand2",
                     bg="red", fg="white", command=self.CreateAccount).place(x=330,y=460)
        root.mainloop()
    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")
        
    def CreateAccount(self):
        branchCode = "1200"
        accountDetails = []
        with open("Personal_Details.txt", 'r') as file:
            for line in file:
                split = line.strip().split("|")
                accountDetails.append(split)

        if len(accountDetails) == 0:
            self.accountNumber = branchCode + "000001"
        else:
            lastDetails = accountDetails[-1]
            lastAccountNumber = int(lastDetails[0])
            self.accountNumber = str(lastAccountNumber + 1 )

        details = [self.accountNumber, self.cmbtitle.get(), self.txtFullName.get(), self.txtNameInt.get(), self.txtId.get(),self.txtYear.get(), self.txtMonth.get(), self.txtDate.get(), self.txtOcupation.get(),self.txtAddressNo.get(),self.txtLine1.get(),self.txtLine2.get(),self.txtLine3.get(), self.txtContactNo.get(),self.txtEmail.get()]

        if details[2]=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Full Name ")
        elif details[3]=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Name With Initials")
        elif details[4]=="":
            messagebox.showerror("Create a New Account", "Please Fill Your National ID No")
        elif self.txtYear.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Birth Year")
        elif self.txtMonth.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Birth Month")
        elif self.txtDate.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Birth date")
        elif details[6]=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Occupation")
        elif self.txtAddressNo.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your House NO")
        elif self.txtLine1.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Address Line 01")
        elif self.txtLine2.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Address Line 02")
        elif self.txtLine3.get()=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Address Line 03")
        elif details[8]=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Contact No")
        elif details[9]=="":
            messagebox.showerror("Create a New Account", "Please Fill Your Email Address")
        else:
            for widgets in self.root.winfo_children():
                widgets.destroy()

            with open("Personal_Details.txt", 'a') as file1:
                file1.write(
                    str(details[0]) + "|" + str(details[1]) + "|" + str(details[2]) + "|" + str(details[3]) + "|" + str(
                        details[4]) + "|" + str(details[5]) + "|" + str(details[6]) + "|" + details[7] + "|" +
                    str(details[8])+ "|" + str(details[9]) + "|" + str(details[10])+ "|" + str(details[11])+ "|" + str(details[12])+ "|" + str(details[13])+ "|" + str(details[14])+ "\n")
    
            messagebox.showinfo("Create a New Account", "Your New Account Creating Successfully!" + "\n" +"Account Number :" + str(self.accountNumber))
            messagebox.showinfo("Create a New Account", "You first deposit should be minimum Rs.1000.00 ") 
            self.update_clock()
            obj=CashDeposit(self.root,0,self.accountNumber,self.date_now,self.time_now,details[1],details[3])
                
        
            







