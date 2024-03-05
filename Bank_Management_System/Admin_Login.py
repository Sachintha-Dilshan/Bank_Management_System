from tkinter import *
from tkinter import messagebox
from Manager_Interface import Admin

class AdminLogin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600+280+80")
        frame=Frame(self.root,bg="white")
        frame.place(x=320, y=40, width=600, height=530)
        lblbackground = Label(self.root, bg="green", width=35, height=35).place(x=70, y=40)
        title = Label(frame, text="Login to the Admin Section", font=("times new roman", 30, "bold"),fg="red",bg="white").place(x=50, y=30)
        lbl1=Label(frame,font=("times new roman",20,"bold"),text="User Name",fg="green",bg="white").place(x=50,y=150)
        self.txt1=Entry(frame, font=("times new roman",20),bg="lightgray")
        self.txt1.place(x=200,y=150)

        lbl2=Label(frame,font=("times new roman",20,"bold"),text="Password",fg="green",bg="white").place(x=50,y=200)
        self.txt2=Entry(frame, font=("times new roman",20),bg="lightgray",show="*")
        self.txt2.place(x=200,y=200)

        btnLogin=Button(frame,text="Login",font=("times new roman",20),borderwidth=10,fg="white",bg="green",command=self.showUser)
        btnLogin.place(x=50,y=250,width=100)
        
        self.root.mainloop()

    def showUser(self):
        if self.txt1.get()=="admin" and self.txt2.get()=="admin":
            self.root.destroy()   
            root=Tk()
            obj=Admin(root)
 
        else:
            messagebox.showerror("Login to the Admin section", "User name or Password is incorrect\n Please chek again")
