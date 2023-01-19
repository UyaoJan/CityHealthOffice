from tkinter import *
from tkinter import messagebox
import Test_MAIN, employee, Test_Admin

# Admin Username and Password
global admin_uname,admin_pass
admin_uname="admin"
admin_pass="admin123"

class Loginpage():
    def __init__(self):
        self.LoginGUI=Tk()

    def loginLogic(self):
        uname=username.get()
        passwd=password.get()
        if uname==admin_uname and passwd==admin_pass:
            admin=Test_Admin.Admin()
            admin.start()
        else:
            log=employee.Employee.login(uname,passwd)
            if log!=0:
                start=Test_MAIN.Main(log)
                self.LoginGUI.destroy()
                start.start()
            else: messagebox.showerror("Credentials Not Found","Username and Password do not Match")

    def LoginStart(self):
        self.LoginGUI.title("CITY HEALTH OFFICE LOGIN PAGE")
        self.LoginGUI.resizable(False,False)

        global username,password
        username=StringVar()
        password=StringVar()

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
        self.Username_Entry=Entry(self.LoginFrame2,width=40,textvariable=username,borderwidth=3).place(x=50,y=150)

        self.Password_Label=Label(self.LoginFrame2,text="Password",font='Arial 12').place(x=46,y=180)
        self.Password=StringVar()
        self.Password_Entry=Entry(self.LoginFrame2,width=40,textvariable=password,show="*",borderwidth=3,).place(x=50,y=200)

        self.Forget=Label(self.LoginFrame2,text="Forget Password:",font='Arial 8').place(x=60,y=253)
        self.Chick_Here=Label(self.LoginFrame2,text="Check Here",fg="blue",font='Arial 8').place(x=150,y=253)
        self.Login_Enter=Button(self.LoginFrame2,text="ENTER",width=10,bg="green", command=self.loginLogic)
        self.Login_Enter.place(x=220,y=250)
        self.LoginGUI.mainloop()
    
    def start(self):
        self.LoginStart()