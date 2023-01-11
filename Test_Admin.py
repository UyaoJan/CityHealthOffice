from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkcalendar import Calendar,DateEntry

import employee

class Admin:
    def __init__(self):
        self.AdminGUI = None
        global PageOpen
        PageOpen = 1
    
    def Rig_close(self):
        global PageOpen
        if username.get()=="" and password.get()=="" and firstname.get()=="" and lastname.get()=="" and age.get()=="" and address.get()=="" and profession.get() =="":
            PageOpen=1
            self.Registration_Page.destroy()

        else:
            if tk.messagebox.askokcancel('Close', 'Are you sure you want to close the Registration Page?\nAll Progress will not be Saved'):
                PageOpen=1
                username.set("")
                password.set("")
                firstname.set("")
                lastname.set("")
                age.set("")
                address.set("")
                profession.set("")

                self.Registration_Page.destroy()

    def Regist(self):
        global PageOpen

        def submit():
            uname=Entry_Username.get()
            passwd=Entry_Password.get()
            fname=Entry_FName.get()
            lname=Entry_LName.get()
            how_muchyour_age=Entry_Age.get()
            addrss=Entry_Address.get()
            role=Entry_Pro.get()
        def submit():
            uname=Entry_Username.get()
            passwd=Entry_Password.get()
            fname=Entry_FName.get()
            lname=Entry_LName.get()
            how_muchyour_age=Entry_Age.get()
            addrss=Entry_Address.get()
            role=Entry_Pro.get()

            NewEmp=employee.Employee(None,uname,passwd,fname,lname,how_muchyour_age,addrss,role,Entry_Dept.get(),filepath)
            NewEmp.register()

            messagebox.showinfo("Account Added Successfully","Added Succesfully")

            messagebox.showinfo("Account Added Successfully","Added Succesfully")

        if PageOpen<2:
            self.Registration_Page=Toplevel()
            self.Registration_Page.title("Registration")
            Rig_width=400
            Rig_height=520
            self.Registration_Page.geometry(f'{Rig_width}x{Rig_height}+{480}+{100}')
            self.Registration_Page.resizable(False,False)

            self.Registration_Page.protocol("WM_DELETE_WINDOW", self.Rig_close)

            Regist_Body=Frame(self.Registration_Page)
            Regist_Body.pack(expand=1,fill=BOTH)

            Registration_Title=Label(Regist_Body,text="Registation",font=("Arial",35,"bold")).place(x=15,y=10)

            Image_Box=Frame(Regist_Body,width=124,height=120,bg="green",highlightbackground="black",highlightthickness=2)
            Image_Box.place(x=25,y=90)

            Image_upload=Label(Image_Box,width=30,height=25,borderwidth=2,padx=2,pady=2)
            Image_upload.place()

            Upload_button=Button(Image_Box,text="Profile Image",command=lambda:open_file(),width=16,height=7,borderwidth=2)
            Upload_button.place(x=0,y=0)

            def open_file():
                global img, filepath
                f_types = [('Jpg Files', '*.jpg')]
                filepath = filedialog.askopenfilename(filetypes=f_types)
                img=Image.open(filepath)
                img_resized=img.resize((108,105)) # new width & height
                img=ImageTk.PhotoImage(img_resized)
                b2 =Button(Image_Box,image=img,borderwidth=5,command=open_file) # using Button 
                b2.place(x=0,y=0)
                
            global username,password, firstname,lastname,age,Entry_Birthdate,address,profession

            username=StringVar()
            password=StringVar()
            firstname=StringVar()
            lastname=StringVar()
            age=StringVar()
            address=StringVar()
            profession=StringVar()


            global Entry_Username, Entry_Password, Entry_FName, Entry_LName, Entry_Age, Entry_Birthdate, Entry_Address, Entry_Pro
            Label_Username=Label(Regist_Body,text="Username:",font=("Arial",10,"bold")).place(x=160,y=100)
            Entry_Username=Entry(Regist_Body,text="Username:",textvariable=username,font=("Arial",10,"bold"),width=30,borderwidth=3)
            Entry_Username.place(x=160,y=120)

            Label_Password=Label(Regist_Body,text="Password:",font=("Arial",10,"bold")).place(x=160,y=150)
            Entry_Password=Entry(Regist_Body,text="Password:",textvariable=password,font=("Arial",10,"bold"),width=30,borderwidth=3)
            Entry_Password.place(x=160,y=170)

            Label_FName=Label(Regist_Body,text="First Name:",font=("Arial",10,"bold")).place(x=15,y=220)
            Entry_FName=Entry(Regist_Body,text="First Name:",textvariable=firstname,font=("Arial",10,"bold"),width=30,borderwidth=3)
            Entry_FName.place(x=15,y=240)

            Label_LName=Label(Regist_Body,text="Last Name:",font=("Arial",10,"bold")).place(x=240,y=220)
            Entry_LName=Entry(Regist_Body,text="Last Name:",textvariable=lastname,font=("Arial",10,"bold"),width=19,borderwidth=3)
            Entry_LName.place(x=240,y=240)

            Label_Age=Label(Regist_Body,text="Age:",font=("Arial",10,"bold")).place(x=15,y=270)
            Entry_Age=Entry(Regist_Body,text="Age:",textvariable=age,font=("Arial",10,"bold"),width=10,borderwidth=3)
            Entry_Age.place(x=15,y=290)

            Label_Birthdate=Label(Regist_Body,text="Birthdate:",font="Arial 12").place(x=100,y=270)
            Entry_Birthdate=DateEntry(Regist_Body,width=26,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='readonly')
            Entry_Birthdate.place(x=100,y=289)

            Label_Address=Label(Regist_Body,text="Address:",font=("Arial",10,"bold")).place(x=15,y=320)
            Entry_Address=Entry(Regist_Body,text="Address:",textvariable=address,font=("Arial",10,"bold"),width=50,borderwidth=3)
            Entry_Address.place(x=15,y=340)

            Label_Pro=Label(Regist_Body,text="Profession:",font=("Arial",10,"bold")).place(x=15,y=370)
            Entry_Pro=Entry(Regist_Body,text="Profession:",textvariable=profession,font=("Arial",10,"bold"),width=50,borderwidth=3)
            Entry_Pro.place(x=15,y=390)

            Label(Regist_Body,text="Department",font=("Arial",10,"bold")).place(x=15,y=425)
            Entry_Dept=ttk.Combobox(Regist_Body,value=['Laboratory Department', 'Imaging Center'],font='Arial 12',width=37,state='readonly')
            Entry_Dept.place(x=15,y=440)

            Reg_Submit=Button(Regist_Body,text="Submit",width=5,height=1,font=("Arail",8,"bold"),borderwidth=3,command=submit)
            Reg_Submit.place(x=270,y=500)
            
            Reg_Cancel=Button(Regist_Body,text="Cancel",width=5,height=1,font=("Arail",8,"bold"),borderwidth=3,command=self.Rig_close)
            Reg_Cancel.place(x=320,y=500)

            PageOpen +=1
        else:
            messagebox.showinfo("Error","The Window Registration is already Open!")

    def View_on_close(self):
        global PageOpen
        if tk.messagebox.askokcancel('Close', 'Are you sure you want to close the View Page all the data will not be Save?'):
            PageOpen=1
            self.View_Page.destroy()

    def ViewProfile(self,id,label_reference):        
            global label_refer
            label_refer=label_reference
            global PageOpen    
            global EditAccount, res
            res=employee.Employee.findAccount(id)
            if PageOpen<2:
                self.View_Page=Toplevel()
                self.View_Page.title("Edit Profile")
                PAGE_width=700
                PAGE_height=450
                self.View_Page.geometry(f'{PAGE_width}x{PAGE_height}+{400}+{200}')
                self.View_Page.resizable(False,False)
                self.View_Page.protocol("WM_DELETE_WINDOW", self.View_on_close)

                self.View_Body=Frame(self.View_Page)
                self.View_Body.pack(expand=1,fill=BOTH)

                global username2,password2,firstname2,lastname2,age2,address2,profession2

                username2=StringVar()
                username2.set(res[6])
                password2=StringVar()
                password2.set(res[7])
                firstname2=StringVar()
                firstname2.set(res[1])
                lastname2=StringVar()
                lastname2.set(res[2])
                age2=IntVar()
                age2.set(str(res[4]))
                address2=StringVar()
                address2.set(res[5])
                profession2=StringVar()
                profession2.set(res[3])

                
                def deleteAccount(id):
                    answer=messagebox.askyesno("Confirm Delete","Delete User?")
                    if answer:
                        messagebox.showinfo("User Deleted","User Deleted Successfully")
                        employee.Employee.deleteEmployee(id)
                                
                def editAccount2(id):
                    Account=(
                    id,
                    firstname2.get(),
                    lastname2.get(),
                    profession2.get(),
                    age2.get(),
                    address2.get(),
                    
                    username2.get(),
                    password2.get(),)
                    
                    ress=list(res)
                    del ress[-1]
                    ress=tuple(ress)

                    if Account==ress: 
                        messagebox.showinfo("No Changes Made","No Changes have been Made!")
                    
                    else:
                        answer = messagebox.askyesno(title='confirmation',
                                    message='Save Changes?')

                        if answer:
                            self.View_Page.destroy()
                            employee.Employee.editAccount(Account)
                            messagebox.showinfo("Changes Saved","Account Update Succesful")

                        else: messagebox.showinfo("No Changes Made","No Changes have been Made!")
                

                View_img=Label(self.View_Body,text="Image",font=("Arial",15),bg="gray").place(x=470,y=10,relwidth=0.3,relheight=0.5)

                Label_View_Username=Label(self.View_Body,text="Username:",font=("Arial",10,"bold")).place(x=10,y=80)
                self.Entry_View_Username=Entry(self.View_Body,text="Username:",textvariable=username2,font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=10,y=100)

                Label_View_Password=Label(self.View_Body,text="Password:",font=("Arial",10,"bold")).place(x=240,y=80)
                self.Entry_View_Password=Entry(self.View_Body,text="Password:",textvariable=password2,font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=240,y=100)

                Label_View_FName=Label(self.View_Body,text="First Name:",font=("Arial",10,"bold")).place(x=10,y=130)
                self.Entry_View_FName=Entry(self.View_Body,text="First Name:",textvariable=firstname2,font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=10,y=150)

                Label_View_LName=Label(self.View_Body,text="Last Name:",font=("Arial",10,"bold")).place(x=240,y=130)
                self.Entry_View_LName=Entry(self.View_Body,text="Last Name:",textvariable=lastname2,font=("Arial",10,"bold"),width=30,borderwidth=3).place(x=240,y=150)

                Label_View_Age=Label(self.View_Body,text="Age:",font=("Arial",10,"bold")).place(x=10,y=180)
                self.Entry_View_Age=Entry(self.View_Body,text="Age:",textvariable=age2,font=("Arial",10,"bold"),width=10,borderwidth=3).place(x=10,y=200)

                Label_Birthdate=Label(self.View_Body,text="BirthDate:",font="Arial 12").place(x=100,y=180)
                self.Entry_Birthdate=DateEntry(self.View_Body,width=26,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='readonly')
                self.Entry_Birthdate.place(x=100,y=200)

                Label_View_Address=Label(self.View_Body,text="Address:",font=("Arial",10,"bold")).place(x=10,y=230)
                self.Entry_View_Address=Entry(self.View_Body,text="Address:",textvariable=address2,font=("Arial",10,"bold"),width=50,borderwidth=3).place(x=10,y=250)

                Label_View_Pro=Label(self.View_Body,text="Profession:",font=("Arial",10,"bold")).place(x=10,y=280)
                self.Entry_View_Pro=Entry(self.View_Body,text="Profession:",textvariable=profession2,font=("Arial",10,"bold"),width=50,borderwidth=3).place(x=10,y=300)

                Entry_Pro=ttk.Combobox(self.View_Body,value=['Laboratory Department', 'Imaging Center'],font='Arial 12',width=37,state='readonly')
                Entry_Pro.current(Entry_Pro['values'].index(res[4]))
                Entry_Pro.place(x=15,y=425)
                
                View_EDIT=Button(self.View_Body,text="Edit",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda: editAccount2(id))
                View_EDIT.place(x=510,y=200)

                View_DELETE=Button(self.View_Body,text="Delete",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda: deleteAccount(id))
                View_DELETE=Button(self.View_Body,text="Delete",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda: deleteAccount(id))
                View_DELETE.place(x=510,y=240)

                View_Cancel=Button(self.View_Body,text="Cancel",width=15,height=1,font=("Arail",10),borderwidth=5,command=self.View_on_close)
                View_Cancel.place(x=510,y=290)

                PageOpen +=1
            else:
                messagebox.showinfo("Error","The Window EDIT is already Open!")

    def AdminGUI_Main(self):
        self.AdminGUI=Tk()
        self.AdminGUI.title('CITY HEALTH')
        width= self.AdminGUI.winfo_screenwidth()
        height=self.AdminGUI.winfo_screenheight()
        self.AdminGUI.geometry("%dx%d"%(width,height))

        Page_Admin=Frame(self.AdminGUI)
        Page_Admin.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(Page_Admin,width=1360,height=50,highlightbackground="black",highlightthickness=1)
        Frame_Header.pack()

        IMG_HEADER=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
        IMG_HEADER.place(x=10,y=8)
        HEADER_TITLE=Label(Frame_Header,text="City Health Office",font='Arial 20 bold').place(x=50,y=8)
        #Header END-----------

        Admin_Body=Frame(Page_Admin)
        Admin_Body.pack(expand=1,fill=BOTH)

        Admin_LEFT=Frame(Admin_Body,width=270)
        Admin_LEFT.pack(fill=Y,side=LEFT)

        Logo_Admin=Label(Admin_LEFT,text="LOGO",width=30,height=15,bg="white",highlightbackground="black",highlightthickness=1).place(x=20,y=30)

        Registration_Button=Button(Admin_LEFT,text="Registration",width=20,height=2,font=("Arail",10),borderwidth=5,command=self.Regist)
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

        result=employee.Employee.getAllEmployees()

        global labels
        labels=[]
        for Account_Num in range(len(result)):
            Profile_Number=Frame(Profile,padx=10, pady=10, width=1023, height=200)
            Profile_Number.grid(row=Account_Num,column=0)

            Profile_Detail=Frame(Profile_Number,highlightbackground="black",highlightthickness=1,)
            Profile_Detail.place(x=5,y=7,relwidth=0.99,relheight=0.92)

            # Access Image URL thru result[Account_Num][8] 
            Profile_Image=Label(Profile_Detail,text="IMAGE",bg="gray").place(x=10,y=10,relwidth=0.2,relheight=0.88)
            global Profile_Name
            Profile_Name=Label(Profile_Detail,text=result[Account_Num][1]+" "+result[Account_Num][2],font=("Arail",25,"bold"))
            Profile_Name.place(x=220,y=10)
            labels.append(Profile_Name)

            Profile_Edit=Button(Profile_Detail,text="View",width=10,height=2,font=("Arail",10),borderwidth=5,command=lambda x= result[Account_Num][0]:self.ViewProfile(x, labels[Account_Num]))
            Profile_Edit.place(x=850,y=50)

        self.AdminGUI.mainloop()

    def start(self):
        self.AdminGUI_Main()