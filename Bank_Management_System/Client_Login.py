from tkinter import *
from Create_a_New_Account import Create
from tkinter import messagebox
from User_Interface import User

class ClientLogin:
    def __init__(self,root):
        self.root=root
        self.root.title("Checking User Informations")
        self.root.geometry("1000x600+280+80")
        frame=Frame(self.root,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.root, bg="green", width=35, height=35).place(x=70, y=40)
        title = Label(frame, text="Client Login", font=("times new roman", 30, "bold"),fg="red",bg="white").place(x=50, y=30)
        btn1=Button(frame,text="Login to the Account",borderwidth=10,font=("times new roman",20,'bold'),fg="white",bg="green",comman=self.loginAccount)
        btn1.place(x=50,y=100,width=400)
        btn2=Button(frame,text="Create a New Account",borderwidth=10,font=("times new roman",20,"bold"),fg="white",bg="green",command=self.createANewAccount)
        btn2.place(x=50,y=200,width=400)
        self.root.mainloop()

    def loginAccount(self):
        obj=CheckUser(self.root)
    def createANewAccount(self):
        self.root.destroy()
        root=Tk()
        obj=Create(root)
        
class CheckUser:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600+280+80")
        frame=Frame(self.root,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.root, bg="green", width=35, height=35).place(x=70, y=40)
        title = Label(frame, text="Login to the Account", font=("times new roman", 30, "bold"),fg="red",bg="white").place(x=50, y=30)
        lbl1=Label(frame,font=("times new roman",20,"bold"),text="Account Number",fg="green",bg="white").place(x=50,y=150)
        self.txt1=Entry(frame, font=("times new roman",20),bg="lightgray")
        self.txt1.place(x=300,y=150)

        lbl2=Label(frame,font=("times new roman",20,"bold"),text="Confirm AC No",fg="green",bg="white").place(x=50,y=200)
        self.txt2=Entry(frame, font=("times new roman",20),bg="lightgray")
        self.txt2.place(x=300,y=200)

        btnLogin=Button(frame,text="Login",font=("times new roman",20),borderwidth=10,fg="white",bg="green",command=self.showUser)
        btnLogin.place(x=50,y=250,width=100)
        
        self.root.mainloop()

    def showUser(self):
        if self.txt1.get()==self.txt2.get():
            accountHolderDetails=[]
            with open("Personal_Details.txt", 'r') as file:
                for line in file:
                    split1 = line.strip().split("|")
                    if self.txt1.get() in split1:
                        accountHolderDetails=split1
            if len(accountHolderDetails)==0:
                messagebox.showwarning("Login to the Account", "Invalid Account Number\n Please chek again")
            else:
                passbookData=[]
                recentActivity=[]
                with open("Passbook.txt", 'r') as file1:
                    for line in file1:
                        split2 = line.strip().split("|")
                        if self.txt1.get() in split2:
                            passbookData.append(split2)
                
                        
                recentActivity=passbookData[-1]
                balance=recentActivity[3]
                accountNumber=accountHolderDetails[0]
                title=accountHolderDetails[1]
                name=accountHolderDetails[3]
                self.root.destroy()
                
                root=Tk()
                obj=User(root,accountNumber)
        else:
            messagebox.showwarning("Login to the Account", "Dosent't match the Account Numbers\n Please chek again")

        