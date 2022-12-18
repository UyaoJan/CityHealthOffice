from tkinter import *


class Loginpage():
    def __init__(self):
        self.LoginGUI=None
#LOGIC----------------------------------------------------------------------------------------------------------------------------------------------

#GUI----------------------------------------------------------------------------------------------------------------------------------------------
    def LoginGUI(self):
        self.LoginFrame1=Frame(self.LoginGUI,width=350,height=350,highlightbackground="black",highlightthickness=1)
        self.LoginFrame1.grid(row=0,column=0)

        self.IMG=Label(self.LoginFrame1,text="IGM")
        self.IMG.place(relx=0.5,rely=0.5,anchor=CENTER)
        #Frame2
        self.LoginFrame2=Frame(self.LoginGUI,width=350,height=350,highlightbackground="black",highlightthickness=1)
        self.LoginFrame2.grid(row=0,column=1)

        self.Label_Login=Label(self.LoginFrame2,text="LOGIN",font='Arial 60 bold').place(x=20,y=20)

        self.Username_Label=Label(self.LoginFrame2,text="Username",font='Arial 12').place(x=46,y=130)
        self.Username=StringVar()
        self.Username_Entry=Entry(self.LoginFrame2,width=40,textvariable=self.Username,borderwidth=3).place(x=50,y=150)

        self.Password_Label=Label(self.LoginFrame2,text="Password",font='Arial 12').place(x=46,y=180)
        self.Password=StringVar()
        self.Password_Entry=Entry(self.LoginFrame2,width=40,textvariable=self.Password,show="*",borderwidth=3,).place(x=50,y=200)

        self.Forget=Label(self.LoginFrame2,text="Forget Password:",font='Arial 8').place(x=60,y=253)
        self.Chick_Here=Label(self.LoginFrame2,text="Chick Here",fg="blue",font='Arial 8').place(x=150,y=253)
        self.Login_Enter=Button(self.LoginFrame2,text="ENTER",width=10,bg="green").place(x=220,y=250)
        self.LoginGUI.mainloop()
    
    def start(self,id):
        self.LoginGUI()

#GUI----------------------------------------------------------------------------------------------------------------------------------------------

        

