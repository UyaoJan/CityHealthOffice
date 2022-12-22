from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkcalendar import Calendar,DateEntry


AdminGUI=Tk()
AdminGUI.title('CITY HEALTH')
width= AdminGUI.winfo_screenwidth()
height=AdminGUI.winfo_screenheight()
AdminGUI.geometry("%dx%d"%(width,height))

Page_Admin=Frame(AdminGUI)
Page_Admin.pack(expand=1, fill=BOTH)
Frame_Header=Frame(Page_Admin,width=1360,height=50,highlightbackground="black",highlightthickness=1)
Frame_Header.pack()

IMG_HEADER=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
IMG_HEADER.place(x=10,y=8)
HEADER_TITLE=Label(Frame_Header,text="City Health Office",font='Arial 20 bold').place(x=50,y=8)

HEADER_USERNAME=Label(Frame_Header,text="UserName:",font='Arial 12 ').place(x=1100,y=10)
IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
IMG_USERNAME.place(x=1200,y=8)

Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
Toggle_Button.place(x=1290,y=10)
Toggle_Button.menu=Menu(Toggle_Button)
Toggle_Button["menu"]=Toggle_Button.menu

Toggle_Button.menu.add_command(label="HOME",command=lambda:print("I hate this"))
Toggle_Button.menu.add_command(label="Setting",command=lambda:print("Luck of knowlegde"))
Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))
#Header END-----------


global PageOpen
PageOpen = 1
def Regist():
    global PageOpen
    def on_close():
        global PageOpen
        if tk.messagebox.askokcancel('Close', 'Are you sure you want to close the Registration Page all the data will not be Save?'):
            PageOpen=1

            Registration_Page.destroy()

    if PageOpen<2:
        Registration_Page=Toplevel()
        Registration_Page.title("Registration")
        Rig_width=400
        Rig_height=500
        Registration_Page.geometry(f'{Rig_width}x{Rig_height}+{500}+{80}')
        Registration_Page.resizable(False,False)

        Registration_Page.protocol("WM_DELETE_WINDOW", on_close)

        Regist_Body=Frame(Registration_Page)
        Regist_Body.pack(expand=1,fill=BOTH)

        Registration_Title=Label(Regist_Body,text="Registation",font=("Arial",35,"bold")).place(x=15,y=10)

        Image_Box=Frame(Regist_Body,width=124,height=120,bg="green",highlightbackground="black",highlightthickness=2)
        Image_Box.place(x=25,y=90)

        Image_upload=Label(Image_Box,width=30,height=25,borderwidth=2,padx=2,pady=2)
        Image_upload.place()

        Upload_button=Button(Image_Box,text="Profile Image",command=lambda:open_file(),width=16,height=7,borderwidth=2)
        Upload_button.place(x=0,y=0)

        def open_file():
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filepath = filedialog.askopenfilename(filetypes=f_types)
            img=Image.open(filepath)
            img_resized=img.resize((108,105)) # new width & height
            img=ImageTk.PhotoImage(img_resized)
            b2 =Button(Image_Box,image=img,borderwidth=5,command=lambda:open_file()) # using Button 
            b2.place(x=0,y=0)

        Label_Username=Label(Regist_Body,text="Username:",font=("Arial",10,"bold")).place(x=160,y=100)
        Entry_Username=Entry(Regist_Body,text="Username:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=160,y=120)

        Label_Password=Label(Regist_Body,text="Password:",font=("Arial",10,"bold")).place(x=160,y=150)
        Entry_Password=Entry(Regist_Body,text="Password:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=160,y=170)

        Label_FName=Label(Regist_Body,text="First Name:",font=("Arial",10,"bold")).place(x=15,y=220)
        Entry_FName=Entry(Regist_Body,text="First Name:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=15,y=240)

        Label_LName=Label(Regist_Body,text="Last Name:",font=("Arial",10,"bold")).place(x=240,y=220)
        Entry_LName=Entry(Regist_Body,text="Last Name:",font=("Arial",10,"bold"),width=19,borderwidth=3).place(x=240,y=240)

        Label_Age=Label(Regist_Body,text="Age:",font=("Arial",10,"bold")).place(x=15,y=270)
        Entry_Age=Entry(Regist_Body,text="Age:",font=("Arial",10,"bold"),width=10,borderwidth=3).place(x=15,y=290)

        Label_Birthdate=Label(Regist_Body,text="BirthDate:",font="Arial 12").place(x=100,y=270)
        Entry_Birthdate=DateEntry(Regist_Body,width=26,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='readonly')
        Entry_Birthdate.place(x=100,y=289)

        Label_Address=Label(Regist_Body,text="Address:",font=("Arial",10,"bold")).place(x=15,y=320)
        Entry_Address=Entry(Regist_Body,text="Address:",font=("Arial",10,"bold"),width=50,borderwidth=3).place(x=15,y=340)

        Label_Pro=Label(Regist_Body,text="Profission:",font=("Arial",10,"bold")).place(x=15,y=370)
        Entry_Pro=Entry(Regist_Body,text="Profission:",font=("Arial",10,"bold"),width=50,borderwidth=3).place(x=15,y=390)

        Reg_Submit=Button(Regist_Body,text="Submit",width=5,height=1,font=("Arail",10),borderwidth=3,bg="green")
        Reg_Submit.place(x=250,y=440)

        Reg_Cancel=Button(Regist_Body,text="Cancel",width=5,height=1,font=("Arail",10),borderwidth=3,bg="gray",command=on_close)
        Reg_Cancel.place(x=320,y=440)

        PageOpen +=1
    else:
        messagebox.showinfo("Error","The Window Registration is already Open!")


def ViewProfile():
    global PageOpen
    def View_on_close():
        global PageOpen
        if tk.messagebox.askokcancel('Close', 'Are you sure you want to close the View Page all the data will not be Save?'):
            PageOpen=1
            View_Page.destroy()

             
    if PageOpen<2:
        View_Page=Toplevel()
        View_Page.title("Edit Profile")
        PAGE_width=700
        PAGE_height=350
        View_Page.geometry(f'{PAGE_width}x{PAGE_height}+{400}+{200}')
        View_Page.resizable(False,False)
        View_Page.protocol("WM_DELETE_WINDOW", View_on_close)

        View_Body=Frame(View_Page)
        View_Body.pack(expand=1,fill=BOTH)

        View_img=Label(View_Body,text="Image",font=("Arial",15),bg="gray").place(x=470,y=10,relwidth=0.3,relheight=0.5)

        Label_View_Username=Label(View_Body,text="Username:",font=("Arial",10,"bold")).place(x=10,y=80)
        Entry_View_Username=Entry(View_Body,text="Username:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=10,y=100)

        Label_View_Password=Label(View_Body,text="Password:",font=("Arial",10,"bold")).place(x=240,y=80)
        Entry_View_Password=Entry(View_Body,text="Password:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=240,y=100)

        Label_View_FName=Label(View_Body,text="First Name:",font=("Arial",10,"bold")).place(x=10,y=130)
        Entry_View_FName=Entry(View_Body,text="First Name:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=10,y=150)

        Label_View_LName=Label(View_Body,text="Last Name:",font=("Arial",10,"bold")).place(x=240,y=130)
        Entry_View_LName=Entry(View_Body,text="Last Name:",font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=240,y=150)

        Label_View_Age=Label(View_Body,text="Age:",font=("Arial",10,"bold")).place(x=10,y=180)
        Entry_View_Age=Entry(View_Body,text="Age:",font=("Arial",10,"bold"),width=10,borderwidth=3).place(x=10,y=200)

        Label_Birthdate=Label(View_Body,text="BirthDate:",font="Arial 12").place(x=100,y=180)
        Entry_Birthdate=DateEntry(View_Body,width=26,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='readonly')
        Entry_Birthdate.place(x=100,y=200)

        Label_View_Address=Label(View_Body,text="Address:",font=("Arial",10,"bold")).place(x=10,y=230)
        Entry_View_Address=Entry(View_Body,text="Address:",font=("Arial",10,"bold"),width=50,borderwidth=3).place(x=10,y=250)

        Label_View_Pro=Label(View_Body,text="Profission:",font=("Arial",10,"bold")).place(x=10,y=280)
        Entry_View_Pro=Entry(View_Body,text="Profission:",font=("Arial",10,"bold"),width=50,borderwidth=3).place(x=10,y=300)

        View_EDIT=Button(View_Body,text="Edit",width=15,height=1,font=("Arail",10),borderwidth=5)
        View_EDIT.place(x=510,y=200)

        View_DELETE=Button(View_Body,text="Delete",width=15,height=1,font=("Arail",10),borderwidth=5)
        View_DELETE.place(x=510,y=240)

        View_Cancel=Button(View_Body,text="Cancel",width=15,height=1,font=("Arail",10),borderwidth=5,command=View_on_close)
        View_Cancel.place(x=510,y=290)

        PageOpen +=1
    else:
        messagebox.showinfo("Error","The Window EDIT is already Open!")


Admin_Body=Frame(Page_Admin)
Admin_Body.pack(expand=1,fill=BOTH)

Admin_LEFT=Frame(Admin_Body,width=270)
Admin_LEFT.pack(fill=Y,side=LEFT)

Logo_Admin=Label(Admin_LEFT,text="LOGO",width=30,height=15,bg="white",highlightbackground="black",highlightthickness=1).place(x=20,y=30)

Registration_Button=Button(Admin_LEFT,text="Registration",width=20,height=2,font=("Arail",10),borderwidth=5,command=Regist)
Registration_Button.place(x=40,y=300)

Admin_RIGHT=Frame(Admin_Body,width=250)
Admin_RIGHT.pack(expand=1,fill=BOTH,side=RIGHT)

Title_Admin=Label(Admin_RIGHT,text="Account Management Page",font=("Arail",35,"bold")).place(x=20,y=5)

Account_List=Frame(Admin_RIGHT)
Account_List.place(x=20,y=70,relwidth=0.96,relheight=0.88)

Profile_BOX=Canvas(Account_List)
Profile_BOX.pack(side=LEFT,fill=BOTH,expand=1)

Profilescroll=ttk.Scrollbar(Account_List,orient=VERTICAL,command=Profile_BOX.yview)
Profilescroll.pack(side=RIGHT,fill=Y)

Profile_BOX.configure(yscrollcommand=Profilescroll.set)
Profile_BOX.bind('<Configure>',lambda e: Profile_BOX.configure(scrollregion= Profile_BOX.bbox("all")))

Profile=Frame(Profile_BOX)
Profile_BOX.create_window((0,0),window=Profile,anchor=NW)

for Account_Num in range(10):

    Profile_Number=Frame(Profile,padx=10, pady=10, width=1023, height=200)
    Profile_Number.grid(row=Account_Num,column=0)

    Profile_Detail=Frame(Profile_Number,highlightbackground="black",highlightthickness=1,)
    Profile_Detail.place(x=5,y=7,relwidth=0.99,relheight=0.92)

    Profile_Image=Label(Profile_Detail,text="IMAGE",bg="gray").place(x=10,y=10,relwidth=0.2,relheight=0.88)

    Profile_Name=Label(Profile_Detail,text="Profile Username",font=("Arail",25,"bold")).place(x=220,y=10)
    Profile_Profession=Label(Profile_Detail,text="Professional: DOCTOR",font=("Arail",15,"bold")).place(x=220,y=50)

    Profile_Edit=Button(Profile_Detail,text="View",width=10,height=2,font=("Arail",10),borderwidth=5,command=ViewProfile)
    Profile_Edit.place(x=850,y=50)

AdminGUI.mainloop()