from tkinter import *
from tkinter import messagebox
import Test_MAIN, employee, Test_Admin
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv
env_loc="config.env"
load_dotenv(env_loc)

# Admin Username and Password
global admin_uname,admin_pass
admin_uname=os.getenv('ADMIN_USERNAME')
admin_pass=os.getenv('ADMIN_PASSWORD')

from ctypes import windll
h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)

class Loginpage():
    def __init__(self):
        self.LoginGUI=Tk()
        windll.user32.ShowWindow(h, 9)


    def loginLogic(self):
        uname=username.get()
        passwd=password.get()
        if uname==admin_uname and passwd==admin_pass:
            admin=Test_Admin.Admin()
            self.LoginGUI.destroy()
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
        width=700
        height=350
        self.LoginGUI.geometry(f'{width}x{height}+{350}+{170}')

        global username,password
        username=StringVar()
        password=StringVar()

        self.LoginFrame1=Frame(self.LoginGUI,bg="#EAEAEA")
        self.LoginFrame1.pack(side=LEFT,fill=BOTH)
        H_LOGO = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((300, 300)))
        self.IMG=Label(self.LoginFrame1,image=H_LOGO,bg="#EAEAEA")
        self.IMG.pack(padx=30,pady=28)

        #Frame2
        self.LoginFrame2=Frame(self.LoginGUI,width=350,height=350,bg="#EAEAEA")
        self.LoginFrame2.pack(side=RIGHT)

        self.Label_Login=Label(self.LoginFrame2,text="LOGIN",font='Roboto 60 bold',bg="#EAEAEA").place(x=20,y=20)

        self.Username_Label=Label(self.LoginFrame2,text="Username",font='Roboto 12',bg="#EAEAEA").place(x=46,y=130)
        self.Username=StringVar()
        self.Username_Entry=Entry(self.LoginFrame2,width=40,textvariable=username,borderwidth=3).place(x=50,y=150)

        self.Password_Label=Label(self.LoginFrame2,text="Password",font='Roboto 12',bg="#EAEAEA").place(x=46,y=180)
        self.Password=StringVar()
        self.Password_Entry=Entry(self.LoginFrame2,width=40,textvariable=password,show="*",borderwidth=3,).place(x=50,y=200)

        self.Login_Enter=Button(self.LoginFrame2,text="ENTER",width=10,borderwidth=5,bg="green",command=self.loginLogic)
        self.Login_Enter.place(x=220,y=250)
        self.LoginGUI.mainloop()
    
    def start(self):
        self.LoginStart()