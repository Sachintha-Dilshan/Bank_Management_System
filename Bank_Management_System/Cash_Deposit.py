from tkinter import *
import datetime
from tkinter import messagebox

class CashDeposit:
    def __init__(self,root1,balance,accountNumber,date,time,title,accountHolderName):
        self.root2 = root1      
        self.root1=Frame(self.root2,bg="white")
        self.root1.place(x=320, y=40, width=600, height=530)

        lblbackground = Label(self.root2, bg="green", width=35, height=35).place(x=70, y=40)
        self.balance=balance
        self.accountNumber=accountNumber
        self.date=date
        self.time=time
        self.title=title
        self.name=accountHolderName
        #----------------Row1
        lblAccountNo = Label(self.root1, text="Account Number", font=("times new roman", 16, "bold"), bg="white", fg="green").place(x=10, y=10)
        self.txtAccountNo = Entry(self.root1, font=("times new roman", 20), bg="lightgray", width=15,justify=CENTER)
        self.txtAccountNo.insert(0,self.accountNumber)
        self.txtAccountNo.configure(state=DISABLED)
        self.txtAccountNo.place(x=10, y=40)

        lblDate = Label(self.root1, text="Date", font=("times new roman", 16, "bold"),
                             bg="white", fg="green").place(x=315, y=10)
        self.txtDate = Entry(self.root1, font=("times new roman", 20), bg="lightgray", width=15,justify=CENTER)
        self.txtDate.insert(0,self.date)
        self.txtDate.configure(state=DISABLED)
        self.txtDate.place(x=315, y=40)
        #----------------Row2
        lblName = Label(self.root1, text="Account Holder's Name", font=("times new roman", 16, "bold"),
                        bg="white", fg="green").place(x=10, y=75)
        self.txtname = Entry(self.root1, font=("times new roman", 20), bg="lightgray", width=37)
        self.txtname.insert(0, (self.title+"."+self.name))
        self.txtname.configure(state=DISABLED)
        self.txtname.place(x=10, y=105)
        #--------------Row3
        lblCD = Label(self.root1, text="Cash Deposit", font=("times new roman", 16, "bold"),
                        bg="white", fg="green").place(x=10, y=145)
        #--------------Row4
        lblNotes = Label(self.root1, text="Notes", font=("times new roman", 15, "bold"),
                      bg="white", fg="green").place(x=10, y=180)
        lblCount = Label(self.root1, text="Count", font=("times new roman", 15, "bold"),
                      bg="white", fg="green").place(x=250, y=180)
        lblRs = Label(self.root1, text="Rs", font=("times new roman", 15, "bold"),
                      bg="white", fg="green").place(x=450, y=180)
        #-------------Cash_Table
        lbl5000 = Label(self.root1, text="5000", font=("times new roman", 15, "bold"),
                         bg="white").place(x=10, y=210)
        self.txt5000 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt5000.place(x=200,y=210)
        self.txtcount1 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount1.place(x=385,y=210)

        lbl2000 = Label(self.root1, text="2000", font=("times new roman", 15, "bold"),
                        bg="white").place(x=10, y=240)
        self.txt2000 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt2000.place(x=200, y=240)
        self.txtcount2 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount2.place(x=385, y=240)

        lbl1000 = Label(self.root1, text="1000", font=("times new roman", 15, "bold"),
                        bg="white").place(x=10, y=270)
        self.txt1000 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt1000.place(x=200, y=270)
        self.txtcount3 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount3.place(x=385, y=270)

        lbl500 = Label(self.root1, text="500", font=("times new roman", 15, "bold"),
                        bg="white").place(x=10, y=300)
        self.txt500 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt500.place(x=200, y=300)
        self.txtcount4 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount4.place(x=385, y=300)

        lbl100 = Label(self.root1, text="100", font=("times new roman", 15, "bold"),
                       bg="white").place(x=10, y=330)
        self.txt100 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt100.place(x=200, y=330)
        self.txtcount5 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount5.place(x=385, y=330)

        lbl50 = Label(self.root1, text="50", font=("times new roman", 15, "bold"),
                       bg="white").place(x=10, y=360)
        self.txt50 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt50.place(x=200, y=360)
        self.txtcount6 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount6.place(x=385, y=360)

        lbl20 = Label(self.root1, text="20", font=("times new roman", 15, "bold"),
                       bg="white").place(x=10, y=390)
        self.txt20 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt20.place(x=200, y=390)
        self.txtcount7 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount7.place(x=385, y=390)

        lbl10 = Label(self.root1, text="10", font=("times new roman", 15, "bold"),
                       bg="white").place(x=10, y=420)
        self.txt10 = Entry(self.root1, font=(12), bg="lightgray", width=15, justify="center")
        self.txt10.place(x=200, y=420)
        self.txtcount8 = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtcount8.place(x=385, y=420)

        self.btnTotal = Button(self.root1, text="Total", font=("times new roman",14,"bold"), fg="white", bg="green", width=15, command=self.getSubTotal,cursor="hand2",borderwidth=3)
        self.btnTotal.place(x=204,y=450)
        self.txtSubTotal = Entry(self.root1, state=DISABLED, bg="white", font=(12), width=13, justify="right")
        self.txtSubTotal.place(x=385, y=455)
        self.btnDeposit = Button(self.root1, text="DEPOSIT", font=("times new roman",14,"bold"), fg="white", bg="red", width=15, command=self.deposit,state=DISABLED,cursor="hand2",borderwidth=3)
        self.btnDeposit.place(x=20,y=450)
        self.getStockInfo()
        

    def getSubTotal(self):
        cash = [self.txt5000.get(),self.txt2000.get(),self.txt1000.get(),self.txt500.get(),self.txt100.get(),self.txt50.get(),self.txt20.get(),self.txt10.get()]
        newCash = []
        for i in cash:
            if i == "":
                i = 0
            newCash.append(i)

        x1 = int(newCash[0]) * 5000
        x2 = int(newCash[1]) * 2000
        x3 = int(newCash[2]) * 1000
        x4 = int(newCash[3]) * 500
        x5 = int(newCash[4]) * 100
        x6 = int(newCash[5]) * 50
        x7 = int(newCash[6]) * 20
        x8 = int(newCash[7]) * 10
        self.total = x1+x2+x3+x4+x5+x6+x7+x8

        self.Unable()
        self.txtcount1.insert(0,x1)           
        self.txtcount2.insert(0,x2)              
        self.txtcount3.insert(0,x3)               
        self.txtcount4.insert(0,x4)        
        self.txtcount5.insert(0,x5)      
        self.txtcount6.insert(0,x6)
        self.txtcount7.insert(0,x7)            
        self.txtcount8.insert(0,x8)          
        self.txtSubTotal.insert(0, self.total)
        self.Disable()
        self.btnTotal.configure(state=DISABLED)
        self.btnDeposit.configure(state=NORMAL)
   
        
    def Unable(self):
        self.txtcount1.configure(state=NORMAL)
        self.txtcount2.configure(state=NORMAL)
        self.txtcount3.configure(state=NORMAL)
        self.txtcount4.configure(state=NORMAL)
        self.txtcount5.configure(state=NORMAL) 
        self.txtcount6.configure(state=NORMAL)     
        self.txtcount7.configure(state=NORMAL)    
        self.txtcount8.configure(state=NORMAL)
        self.txtSubTotal.configure(state=NORMAL)  
    def Disable(self):
        self.txtcount1.configure(state=DISABLED)
        self.txtcount2.configure(state=DISABLED)
        self.txtcount3.configure(state=DISABLED)
        self.txtcount4.configure(state=DISABLED)
        self.txtcount5.configure(state=DISABLED) 
        self.txtcount6.configure(state=DISABLED)     
        self.txtcount7.configure(state=DISABLED)    
        self.txtcount8.configure(state=DISABLED)
        self.txtSubTotal.configure(state=DISABLED)
       

    def clear(self):
        self.Unable()
        self.txt5000.delete(0,END)
        self.txt2000.delete(0,END)
        self.txt1000.delete(0,END)
        self.txt500.delete(0,END)
        self.txt100.delete(0,END)
        self.txt50.delete(0,END)
        self.txt20.delete(0,END)
        self.txt10.delete(0,END)
        self.txtcount1.delete(0,END)
        self.txtcount2.delete(0,END)
        self.txtcount3.delete(0,END)
        self.txtcount4.delete(0,END)
        self.txtcount5.delete(0,END)
        self.txtcount6.delete(0,END)
        self.txtcount7.delete(0,END)
        self.txtcount8.delete(0,END)
        self.txtSubTotal.delete(0,END)
        self.Disable()
        self.btnTotal.configure(state=NORMAL)
        self.btnDeposit.configure(state=DISABLED)

    def getStockInfo(self):
        stockDetails=[]
        with open("Money_Stock.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                stockDetails.append(split)            
            lastTransaction=stockDetails[-1]
            self.currentStock=lastTransaction[3]   
        
    def deposit(self):
        if self.total!=0:
            x=0
            with open("Passbook.txt", 'r') as file1:
                for line in file1:
                    split2 = line.strip().split("|")
                    if self.accountNumber in split2:
                        x=1
            if x==1:
                self.clear()
                updatedBalance=int(self.balance)+int(self.total)
                with open("Passbook.txt", 'a') as file1:
                    file1.write(str(self.accountNumber) + "|" + str(self.date) +"|"+str(self.time)+ "|" + ("+"+str(self.total)) + "|" + str(updatedBalance) + "\n")
                messagebox.showinfo("Deposit Money", "Your A/C:" + str(self.accountNumber)+" Successfully Credited Rs:"+str(self.total))
                UpdatedStock=int(self.total)+int(self.currentStock)
                with open("Money_Stock.txt",'a') as file2:
                    file2.write( str(self.date) +"|"+str(self.time)+ "|" + ("+"+str(self.total)) + "|" + str(UpdatedStock) + "\n")

                for widgets in self.root2.winfo_children():
                    widgets.destroy()
                from User_Interface import AccountDetailsView
                obj1=AccountDetailsView(self.root2,self.accountNumber)
                
            else:
                if self.total>=1000:
                    updatedBalance=int(self.balance)+int(self.total)
                    with open("Passbook.txt", 'a') as file1:
                        file1.write(str(self.accountNumber) + "|" + str(self.date) +"|"+str(self.time)+ "|" + ("+"+str(self.total)) + "|" + str(updatedBalance) + "\n")
                    messagebox.showinfo("Deposit Money", "Your A/C:" + str(self.accountNumber)+" Successfully Credited Rs:"+str(self.total))
                    UpdatedStock=int(self.total)+int(self.currentStock)
                    with open("Money_Stock.txt",'a') as file2:
                        file2.write( str(self.date) +"|"+str(self.time)+ "|" + ("+"+str(self.total)) + "|" + str(UpdatedStock) + "\n")
                    self.root2.destroy()
                    from User_Interface import User
                    root=Tk()
                    obj1=User(root,self.accountNumber) 
                else:
                    messagebox.showerror("Deposit Money", "Your first deposit shold be minimum Rs.1000") 
                    self.clear()
        else:
            messagebox.showerror("Deposit Money", "Please enter cash to deposit")
            self.clear()














