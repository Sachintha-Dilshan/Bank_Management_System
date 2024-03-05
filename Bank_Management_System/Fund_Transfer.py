from tkinter import *
from  datetime import datetime
from tkinter import messagebox

class FundTransfer:
    def __init__(self,main_frame,accountBalance,accountNumber):
        self.main_frame=main_frame
        self.accountBalance=accountBalance
        self.accountNumber=accountNumber
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)       
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        lblTitle=Label(frame,text="Fund Transfer",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=10)
        lblFromAccount=Label(frame,font=("times new roman",20,"bold"),text="From Account",bg="white",fg="green").place(x=20,y=50)
        self.txtFromAccount=Entry(frame,font=("times new roman",20,"bold"),justify=CENTER,bg="lightgray")
        self.txtFromAccount.place(x=120,y=100)
        self.txtFromAccount.insert(0,self.accountNumber)
        self.txtFromAccount.configure(state=DISABLED)
        lblTitle1=Label(frame,font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=160)
        lblToAccount=Label(frame,font=("times new roman",20,"bold"),text="Beneficiery Account Number",bg="white",fg="green").place(x=20,y=200)
        self.txtToAccount=Entry(frame,font=("times new roman",20,"bold"),justify=CENTER,bg="lightgray")
        self.txtToAccount.place(x=120,y=250)
        self.lblBeneficieryName=Label(frame,font=("times new roman",15,"bold"),text="Beneficiery Name",bg="white",fg="red")
        self.lblBeneficieryName.place(x=20,y=300)        
        btnGetAccountDetails=Button(frame,text="Check Account",font=("times new roman",15,"bold"),fg="white",bg="green",cursor="hand2",borderwidth=5,command=self.getBeneficieryInfo).place(x=430,y=240)

        lblTransferAmount=Label(frame,font=("times new roman",20,"bold"),text="Transfer Amount",bg="white",fg="green").place(x=20,y=350)
        self.txtTransferAmount=Entry(frame,font=("times new roman",20,"bold"),justify=CENTER,bg="lightgray")
        self.txtTransferAmount.place(x=120,y=400)

        btnTransfer=Button(frame,text="Transfer",font=("times new roman",20,"bold"),fg="white",bg="red",cursor="hand2",borderwidth=5,command=self.trasfer).place(x=240,y=450)
        self.main_frame.mainloop()


    def getBeneficieryInfo(self):

        accountHolderDetails=[]
        with open("Personal_Details.txt", 'r') as file:
            for line in file:
                split1 = line.strip().split("|")
                if self.txtToAccount.get() in split1:
                    accountHolderDetails=split1
        if len(accountHolderDetails)==0:
            messagebox.showerror("Fund Treansfer","Invalid Account Numnber")
        else:
            self.title=accountHolderDetails[1]
            self.name=accountHolderDetails[3]
    

            passbookData=[]
            recentActivity=[]
            with open("Passbook.txt", 'r') as file1:
                for line in file1:
                    split2 = line.strip().split("|")
                    if self.accountNumber in split2:
                        passbookData.append(split2)
                            
            recentActivity=passbookData[-1]
            self.BeneficieryAccountbalance=recentActivity[4]
            self.lblBeneficieryName.configure(text=(str(self.title)+"."+str(self.name)))
    def trasfer(self):
        if self.txtToAccount.get()=="":
            messagebox.showerror("Fund Trasfer","Please Enter the Beneficiery Account Number")
        elif self.txtTransferAmount.get()=="":
            messagebox.showerror("Fund Trasfer","Please Enter the Transfer Amount")
        else:
            self.update_clock()
            self.getBeneficieryInfo()
            updatedBeneficieryAccountBalance=int(self.txtTransferAmount.get())+int(self.BeneficieryAccountbalance)
            updatedUserAccountBalance=int(self.accountBalance)-int(self.txtTransferAmount.get())
            with open("Passbook.txt", 'a') as file:
                file.write(str(self.txtToAccount.get()) + "|" + str(self.date_now) +"|"+str(self.time_now)+ "|" + ("+"+str(self.txtTransferAmount.get())) + "|" + str(updatedBeneficieryAccountBalance) + "\n")
                
                file.write(str(self.accountNumber) + "|" + str(self.date_now) +"|" + str(self.time_now) + "|" + ("-"+str(self.txtTransferAmount.get())) + "|" + str(updatedUserAccountBalance) + "\n")
            messagebox.showinfo("Deposit Money", "Your A/C:" + str(self.txtToAccount.get())+" Successfully Credited Rs:"+str(self.txtTransferAmount.get()))
            messagebox.showinfo("Withdrawal Money", "Your A/C:" + str(self.accountNumber)+" Successfully Debited Rs:"+str(self.txtTransferAmount.get()))
            from User_Interface import AccountDetailsView
            for widgets in self.main_frame.winfo_children():
                    widgets.destroy()
            obj=AccountDetailsView(self.main_frame,self.accountNumber)

    def update_clock(self):
        raw_TS=datetime.now()
        self.date_now=raw_TS.strftime("%d %b %Y")
        self.time_now=raw_TS.strftime("%H:%M:%S %p")
