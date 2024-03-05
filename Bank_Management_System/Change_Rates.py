from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class ChangeRates:
    def __init__(self,main_frame):
        self.main_frame=main_frame
        frame=Frame(self.main_frame,bg="white")
        frame.place(x=320, y=40, width=600, height=530)       
        lblbackground = Label(self.main_frame, bg="green", width=35, height=35).place(x=70, y=40)
        lblTitle=Label(frame,text="Update Rates",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=10)
        lblCurrentRate=Label(frame,font=("times new roman",20,"bold"),text="Current Rates",bg="white",fg="green").place(x=20,y=50)
        self.cmbLoanType = ttk.Combobox(frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbLoanType['values'] = ("Select","Saving Account","Personal Loan","Home Loan","Education Loan")
        self.cmbLoanType.place(x=60, y=120)
        self.cmbLoanType.current(0)
        self.lblLoanRate=Label(frame,text="Rate",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.lblLoanRate.place(x=400,y=120)
        bntRate=Button(frame,text="Rate",font=("times new roman",12,"bold"),bg="green",fg="white",command=self.changeRate,cursor="hand2",borderwidth=5).place(x=300,y=120)
        lblTitle1=Label(frame,font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=180)
        lblUpdateRate=Label(frame,font=("times new roman",20,"bold"),text="Update Rates",bg="white",fg="green").place(x=20,y=220)
        self.cmbLoanType1 = ttk.Combobox(frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmbLoanType1['values'] = ("Select","Saving Account","Personal Loan","Home Loan","Education Loan")
        self.cmbLoanType1.place(x=60, y=270)
        self.cmbLoanType1.current(0)
        self.txtUpdateRate=Entry(frame,font=("times new roman",20),fg='red',bg='lightgray',justify=CENTER)
        self.txtUpdateRate.place(x=300,y=270,width=200)
        lblUpdateRate=Label(frame,font=("times new roman",20,"bold"),text="%",bg="white",fg="red").place(x=500,y=270)
        bntUpdate=Button(frame,text="Update Rate",font=("times new roman",15,"bold"),bg="red",fg="white",command=self.updateRates,cursor="hand2",borderwidth=5).place(x=250,y=320)
        self.getRates
        main_frame.mainloop()
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
    def updateRates(self):
        self.getRates()
        if self.cmbLoanType1.get()=="Select":
            messagebox.showerror("Update Rates","Please Select a type")
        elif self.cmbLoanType1.get()=="Saving Account":
            self.Rate[0]=self.txtUpdateRate.get()
        elif self.cmbLoanType1.get()=="Personal Loan":
            self.Rate[1]=self.txtUpdateRate.get()
        elif self.cmbLoanType1.get()=="Home Loan":
            self.Rate[2]=self.txtUpdateRate.get()
        elif self.cmbLoanType1.get()=="Education Loan":
            self.Rate[3]=self.txtUpdateRate.get()
        with open("Rates.txt",'w') as file:
            for i in range(len(self.Rate)):
                file.write(str(self.Type[i])+"|"+str(self.Rate[i])+"\n")
        messagebox.showinfo("Update Rates","Rate Update Successfully!")
        from Manager_Interface import Status
        obj=Status(self.main_frame)
        

