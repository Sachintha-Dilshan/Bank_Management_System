from tkinter import *
import datetime
from tkinter import messagebox

class Withdrawal:
    def __init__(self,main_frame,accountNumber,balance,date,time,title,accountHolderName):
        self.main_frame=main_frame
        self.accountNumber=accountNumber
        self.balance=balance
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        self.date=date
        self.time=time
        self.title=title
        self.name=accountHolderName

        title = Label(frame, text="Cash Withdrawal", font=("times new roman", 20, "bold"), bg="green",fg="white").place(x=10, y=30)
        #----------------Row1
        lblAccountNo = Label(frame, text="Account Number", font=("times new roman", 16, "bold"), bg="white", fg="green").place(x=10, y=76)
        self.txtAccountNo = Entry(frame, font=("times new roman", 20), bg="lightgray", width=15,justify=CENTER)
        self.txtAccountNo.insert(0,self.accountNumber)
        self.txtAccountNo.configure(state=DISABLED)
        self.txtAccountNo.place(x=10, y=105)

        lblDate = Label(frame, text="Date", font=("times new roman", 16, "bold"),
                             bg="white", fg="green").place(x=315, y=76)
        self.txtDate = Entry(frame, font=("times new roman", 20), bg="lightgray", width=15,justify=CENTER)
        self.txtDate.insert(0,self.date)
        self.txtDate.configure(state=DISABLED)
        self.txtDate.place(x=315, y=105)
        #----------------Row2
        lblName = Label(frame, text="Account Holder's Name", font=("times new roman", 16, "bold"),
                        bg="white", fg="green").place(x=10, y=140)
        self.txtname = Entry(frame, font=("times new roman", 20), bg="lightgray", width=37)
        self.txtname.insert(0, (self.title+"."+self.name))
        self.txtname.configure(state=DISABLED)
        self.txtname.place(x=10, y=175)

        lblBalance=Label(frame,text="Account Balance", font=("times new roman", 20, "bold"),
                        bg="white", fg="green").place(x=10, y=220)
        self.txtBalance = Entry(frame, font=("times new roman", 30), bg="lightgray",justify=CENTER,borderwidth=5)
        self.txtBalance.insert(0, ("Rs. "+str(self.balance)))
        self.txtBalance.configure(state=DISABLED)
        self.txtBalance.place(x=90, y=270)

        lblnote=Label(frame,text="*For withdrawal minimum account balance sholde be Rs.1000", font=("times new roman", 12, "bold"),
                        bg="white", fg="red").place(x=10, y=330)
        lblWithdrawalAmount=Label(frame,text="Withdrawal Amount", font=("times new roman", 20, "bold"),
                        bg="white", fg="green").place(x=10, y=360)
        lblRs=Label(frame,text="Rs.", font=("times new roman", 20, "bold"),
                        bg="white", fg="green").place(x=100, y=400)
        self.txtWithdrawalAmount = Entry(frame, font=("times new roman", 25), bg="lightgray",justify=CENTER,width=17,fg="red")
        self.txtWithdrawalAmount.place(x=150, y=400)
        btnWithdrawal=Button(frame,text="WITHDRAWAL",font=("times new roman",20,"bold"),fg="white",bg="red",command=self.withdrawal,cursor="hand2",borderwidth=5).place(x=180,y=460)
        self.getStockInfo()
    def getStockInfo(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)            
            lastTransaction=stockDetails[-1]
            self.currentStock=lastTransaction[3]   
    def withdrawal(self):
        if self.txtWithdrawalAmount.get()=="":
            messagebox.showerror("Withdrawal Money", "Please enter the withdrawal amount to process")
        else:
            if (int(self.balance)-1000)>=int(self.txtWithdrawalAmount.get()):
                updatedBalance=int(self.balance)-int(self.txtWithdrawalAmount.get())
                debitedAmount=self.txtWithdrawalAmount.get()
                with open("Passbook.txt", 'a') as file:
                    file.write(str(self.accountNumber) + "|" + str(self.date) +"|" + str(self.time) + "|" + ("-"+str(debitedAmount)) + "|" + str(updatedBalance) + "\n")
                UpdatedStock=int(self.currentStock)-int(debitedAmount)
                with open("Money_Stock.txt",'a') as file2:
                    file2.write(str(self.date) +"|" + str(self.time) + "|" + ("-"+str(debitedAmount)) + "|" + str(UpdatedStock) + "\n")
                messagebox.showinfo("Withdrawal Money", "Your A/C:" + str(self.accountNumber)+" Successfully Debited Rs:"+str(debitedAmount))
                for widgets in self.main_frame.winfo_children():
                    widgets.destroy()
                from User_Interface import AccountDetailsView
                obj1=AccountDetailsView(self.main_frame,self.accountNumber)
                
            else:
                messagebox.showerror("Withdrawal Money", "Your acount balance is not enough to do this withdrawal")

        



