from tkinter import *
from Client_Login import ClientLogin
from Admin_Login import AdminLogin


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+100+40")
        self.root.title("Login Page")
        self.root.config(bg="white")
        # ======Background image======
        img1 =  PhotoImage(file="1.png")
    
        label1 = Label(self.root, image=img1)
        label1.place(x=250, y=0,relwidth=1, relheight=1) 
        img2 = PhotoImage(file="2.png")
        label2 = Label(self.root, image=img2).place(x=80, y=100, width=400, height=500)
        # =====Register frame=========
        frame = Frame(self.root)
        frame.place(x=480, y=100, width=700, height=500)

        title = Label(frame, text="Login Page", font=("times new roman", 30, "bold"),fg="red").place(x=50, y=30)

        btnAdmin=Button(frame,text="Administrator Login",borderwidth=10,font=("times new roman",40,"bold"),bg="red",fg="white",command=self.adminLogin).place(x=120,y=300,width=500)
        btnUser=Button(frame,text="Client Login",borderwidth=10,font=("times new roman",40,"bold"),bg="green",fg="white",command=self.clientLogin).place(x=120,y=150,width=500)
        self.root.mainloop()
    
    def adminLogin(self):
        self.root.destroy()
        root=Tk()
        obj=AdminLogin(root)
    def clientLogin(self):
        self.root.destroy()
        root = Tk()
        obj=ClientLogin(root)

root = Tk()
obj = Login(root)



