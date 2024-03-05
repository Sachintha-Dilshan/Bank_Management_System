from tkinter import *
from Get_Personal_Info import GetPersonalInfo

class FixedDepositPage1(GetPersonalInfo):
    def __init__(self,main_frame,accountNumber,date):
        self.mainTitle="Smart FD Application"
        super().__init__(main_frame,accountNumber,date)
       
    def next(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        obj=FixedDepositPage2(self.main_frame,self.frame,self.accountNumber,self.title,self.name)
        
class FixedDepositPage2:
    def __init__(self,main_frame,frame,accountNumber,title,name):
        self.main_frame=main_frame
        self.frame=frame
        self.accountNumber=accountNumber
        self.title=title
        self.name=name
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
        self.lblTerm1 = Label(self.frame, text=" ", font=("times new roman", 15, "bold"), bg="white")
        self.lblTerm1.place(x=250,y=130)
        ############################################################################################################################################## 

        lbl2=Label(self.frame,text="Funds Availability",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=180)
        self.lblOption1 = Label(self.frame, text=" ", font=("times new roman", 15, "bold"), bg="white")
        self.lblOption1.place(x=10, y=215)
        ##############################################################################################################################################
        lbl3=Label(self.frame,text="Maturity Instructions & Interest Payment",font=("times new roman",15,"bold"),fg="white",bg="green",width=48).place(x=10,y=265)
        lblRenewelOption = Label(self.frame, text="Interest Payment", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=10,y=305)
        self.lblOption2 = Label(self.frame, text=" ", font=("times new roman", 15, "bold"), bg="white")
        self.lblOption2.place(x=10, y=330)
        ##################################################################################################################################################
        lbl4=Label(self.frame,text="If interest to be transfered to an account, please indicate whether \ninterest payment is tobe made monthly or at maturity",font=("times new roman",15,"bold"),bg="white",fg="gray",justify=LEFT).place(x=10,y=370)
        self.lblOption3 = Label(self.frame, text=" ", font=("times new roman", 15, "bold"), bg="white")
        self.lblOption3.place(x=10, y=420)
        self.insertInfo()   
    def getFDInfo(self):
        FDInfo=[]
        with open("FD_Details.txt",'r') as file:
            for line in file:
                split=line.strip().split("|")
                if self.accountNumber in split:
                    FDInfo=split
        
        self.amountInfigure=FDInfo[3]
        self.amountInWord=FDInfo[4]
        self.term=FDInfo[5]
        self.fundAvailability=FDInfo[6]
        self.interestPayment=FDInfo[7]
        self.interestOption=FDInfo[8]
    def insertInfo(self):
        self.getFDInfo()
        self.txtamountInFigure.insert(0,self.amountInfigure)
        self.txtamountInWords.insert(0,self.amountInWord)
        self.lblTerm1.configure(text=self.term)
        self.lblOption1.configure(text=self.fundAvailability)
        self.lblOption2.configure(text=self.interestPayment)
        self.lblOption3.configure(text=self.interestOption)
        self.txtamountInFigure.configure(state=DISABLED)
        self.txtamountInWords.configure(state=DISABLED)
    
                

                            
        



 