from tkinter import *

LoginGUI=Tk()
LoginGUI.title('CITY HEALTH')
LoginGUI.geometry("700x350")
#Frame1
LoginFrame1=Frame(LoginGUI,width=350,height=350,highlightbackground="black",highlightthickness=1)
LoginFrame1.grid(row=0,column=0)

IMG=Label(LoginFrame1,text="IGM")
IMG.place(relx=0.5,rely=0.5,anchor=CENTER)
#Frame2
LoginFrame2=Frame(LoginGUI,width=350,height=350,highlightbackground="black",highlightthickness=1)
LoginFrame2.grid(row=0,column=1)

Label_Login=Label(LoginFrame2,text="LOGIN",font='Arial 60 bold').place(x=20,y=20)

Username_Label=Label(LoginFrame2,text="Username",font='Arial 12').place(x=46,y=130)
Username=StringVar()
Username_Entry=Entry(LoginFrame2,width=40,textvariable=Username,borderwidth=3).place(x=50,y=150)

Password_Label=Label(LoginFrame2,text="Password",font='Arial 12').place(x=46,y=180)
Password=StringVar()
Password_Entry=Entry(LoginFrame2,width=40,textvariable=Password,show="*",borderwidth=3,).place(x=50,y=200)

Forget=Label(LoginFrame2,text="Forget Password:",font='Arial 8').place(x=60,y=253)
Chick_Here=Label(LoginFrame2,text="Chick Here",fg="blue",font='Arial 8').place(x=150,y=253)
Login_Enter=Button(LoginFrame2,text="ENTER",width=10,bg="green").place(x=220,y=250)

LoginGUI.mainloop()