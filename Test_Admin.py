from calendar import calendar
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import datetime
from datetime import date, datetime
from tkcalendar import Calendar,DateEntry
import calendar
import employee
import employee, LoginPage

class Admin:
    def __init__(self):
        self.AdminGUI = None
        global PageOpen
        PageOpen = 1
        global update_id

    
    def Rig_close(self):
        global PageOpen
        if username.get()=="" and password.get()=="" and firstname.get()=="" and lastname.get()=="" and age.get()=="" and address.get()=="" and profession.get() =="":
            PageOpen=1
            self.AdminGUI.grab_release()
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
                self.AdminGUI.grab_release()
                self.Registration_Page.destroy()

    def Regist(self):
        global PageOpen
        def submit():
            global PageOpen
            uname=Entry_Username.get()
            passwd=Entry_Password.get()
            fname=Entry_FName.get()
            lname=Entry_LName.get()
            how_muchyour_age=Entry_Age.get()
            addrss=Entry_Address.get()
            role=Entry_Pro.get()
            license=LicensePRO.get()

            self.AdminGUI.grab_release()
            if how_muchyour_age.isnumeric()==True:
                NewEmp=employee.Employee(None,uname,passwd,fname,lname,how_muchyour_age,addrss,role,license,Entry_Dept.get(),None)
                NewEmp.register()
                messagebox.showinfo("Account Added Successfully","Added Succesfully")
                PageOpen = 1
                self.Registration_Page.destroy()
                self.update_main()
                self.Stop_update()
                
            else:
                self.Registration_Page.grab_set()
                messagebox.showerror("ERROR","AGE not A number please use Number only!")

        if PageOpen<2:
            self.Registration_Page=Toplevel(self.AdminGUI)
            self.Registration_Page.title("Registration")
            Rig_width=400
            Rig_height=560
            self.Registration_Page.geometry(f'{Rig_width}x{Rig_height}+{480}+{100}')
            self.Registration_Page.resizable(False,False)
            self.Registration_Page.grab_set()

            self.Registration_Page.protocol("WM_DELETE_WINDOW", self.Rig_close)

            Regist_Body=Frame(self.Registration_Page)
            Regist_Body.pack(expand=1,fill=BOTH)

            Registration_Title=Label(Regist_Body,text="Registration",font=("Arial",35,"bold")).place(x=15,y=10)

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
            license_no=IntVar()


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

            global Year_Birth
            thisyear=datetime.today().year
            Year_number=list(range(thisyear,1900,-1))
            Year=Year_number
            Year_Birth=ttk.Combobox(Regist_Body,value=Year,font='Roboto 12',width=6,state='readonly')
            Year_Birth.set(thisyear)
            Year_Birth.current(0)
            Year_Birth.place(x=260,y=289)

            month_num=datetime.now()
            month_num=month_num.month
            curr_month=datetime.strptime(str(month_num),"%m")
            curr_year=datetime.strptime(Year_Birth.get(),"%Y")

            cal=calendar.monthcalendar(int(curr_year.year),int(curr_month.month))
            number=[day for week in cal for day in week if day != 0]
            self.client_bmonth=month_num
            print(month_num)
            def setMonth(event):
                month_num= datetime.strptime(event.widget.get(), '%B').month
                print(month_num)
                curr_month=datetime.strptime(str(month_num),"%m")
                curr_year=datetime.strptime(Year_Birth.get(),"%Y")
                global cal,number
                cal=calendar.monthcalendar(int(curr_year.year),int(curr_month.month))
                number=[day for week in cal for day in week if day != 0]
                Day_Birth.config(value=number)
                self.client_bmonth=month_num

            def calculate_age(event):
                birthdate=event.widget.get()
                birthdate=datetime.strptime(birthdate,'%Y')
                birthdate=birthdate.year
                today = date.today()
                age= today.year - birthdate
                Entry_Age.delete(0,END)
                Entry_Age.insert(0,age)

                month_num=datetime.strptime(Month_Birth.get(), '%B').month
                curr_month=datetime.strptime(str(month_num),"%m")
                curr_year=datetime.strptime(Year_Birth.get(),"%Y")
                global cal,number
                cal=calendar.monthcalendar(int(curr_year.year),int(curr_month.month))
                number=[day for week in cal for day in week if day != 0]
                Day_Birth.config(value=number)
                self.client_bmonth=month_num

            Year_Birth.bind("<<ComboboxSelected>>",calculate_age)

            Birth_Label=Label(Regist_Body,text="Birthdate:",font="Roboto 12").place(x=100,y=270)
            global Month_Birth
            Month=['January','February','March','April','May','June','July','August','September','October','November','December']
            Month_Birth=ttk.Combobox(Regist_Body,value=Month,font='Roboto 12',width=9,state='readonly')
            Month_Birth.current(0)
            Month_Birth.place(x=100,y=289)
            Month_Birth.bind("<<ComboboxSelected>>",setMonth)

            global Day_Birth
            Day=number
            Day_Birth=ttk.Combobox(Regist_Body,value=Day,font='Roboto 12',width=2,state='readonly')
            Day_Birth.current(0)
            Day_Birth.place(x=213,y=289) 

            Label_Address=Label(Regist_Body,text="Address:",font=("Arial",10,"bold")).place(x=15,y=320)
            Entry_Address=Entry(Regist_Body,text="Address:",textvariable=address,font=("Arial",10,"bold"),width=50,borderwidth=3)
            Entry_Address.place(x=15,y=340)

            Label_Pro=Label(Regist_Body,text="Profession:",font=("Arial",10,"bold")).place(x=15,y=370)
            Entry_Pro=Entry(Regist_Body,textvariable=profession,font=("Arial",10,"bold"),width=50,borderwidth=3)
            Entry_Pro.place(x=15,y=390)

            Label_Pro=Label(Regist_Body,text="License No:",font=("Arial",10,"bold")).place(x=15,y=420)
            LicensePRO=Entry(Regist_Body,textvariable=license_no,font=("Arial",10,"bold"),width=50,borderwidth=3)
            LicensePRO.place(x=15,y=440)

            Label(Regist_Body,text="Department",font=("Arial",10,"bold")).place(x=15,y=460)
            Entry_Dept=ttk.Combobox(Regist_Body,value=["None",'Laboratory Department', 'Imaging Center'],font='Arial 12',width=37,state='readonly')
            Entry_Dept.place(x=15,y=490)

            Reg_Submit=Button(Regist_Body,text="Submit",width=5,height=1,font=("Arail",8,"bold"),borderwidth=3,command=submit)
            Reg_Submit.place(x=270,y=520)
            
            Reg_Cancel=Button(Regist_Body,text="Cancel",width=5,height=1,font=("Arail",8,"bold"),borderwidth=3,command=self.Rig_close)
            Reg_Cancel.place(x=320,y=520)

            PageOpen +=1
        else:
            messagebox.showinfo("Error","The Window Registration is already Open!")

    def View_on_close(self):
        global PageOpen
        self.AdminGUI.grab_release()
        if tk.messagebox.askokcancel('Close', 'Are you sure you want to close the View Page all the data will not be Save?'):
            PageOpen=1
            self.View_Page.destroy()

    def ViewProfile(self,id,label_reference):        
            global label_refer
            label_refer=label_reference
            global PageOpen, state
            global EditAccount, res
            
            res=employee.Employee.findAccount(id)
            if PageOpen<2:
                self.View_Page=Toplevel(self.AdminGUI)
                self.View_Page.title("Edit Profile")
                self.View_Page.grab_set()
                PAGE_width=700
                PAGE_height=430
                self.View_Page.geometry(f'{PAGE_width}x{PAGE_height}+{400}+{200}')
                self.View_Page.resizable(False,False)
                self.View_Page.protocol("WM_DELETE_WINDOW", self.View_on_close)

                self.View_Body=Frame(self.View_Page)
                self.View_Body.pack(expand=1,fill=BOTH)

                global username2,password2,firstname2,lastname2,age2,address2,profession2

                username2=StringVar()
                username2.set(res[8])
                password2=StringVar()
                password2.set(res[9])
                firstname2=StringVar()
                firstname2.set(res[1])
                lastname2=StringVar()
                lastname2.set(res[2])
                age2=IntVar()
                age2.set(str(res[6]))
                address2=StringVar()
                address2.set(res[7])
                profession2=StringVar()
                profession2.set(res[3])

                license=IntVar()
                license.set(res[4])

                dept=StringVar()
                dept.set(5)

                state=0
                print(state)
                
                def deleteAccount(id):
                    self.AdminGUI.grab_release()
                    global update_id,PageOpen,result
                    answer=messagebox.askyesno("Confirm Delete","Delete User?")
                    if answer:
                        messagebox.showinfo("User Deleted","User Deleted Successfully")
                        employee.Employee.deleteEmployee(id)
                        self.Profile_Number.destroy()
                        self.View_Page.destroy()

                        result=employee.Employee.getAllEmployees()

                        global labels
                        self.update_main()
                        self.Stop_update()
                        PageOpen = 1

                def editAccount2(id,state):
                    self.View_Page.wm_attributes("-topmost",0)
                    global update_id
                    if state==0:
                        state=1
                        self.Entry_View_Username.config(state='normal')
                        self.Entry_View_Password.config(state='normal')
                        self.Entry_View_FName.config(state='normal')
                        self.Entry_View_LName.config(state='normal')
                        self.Entry_View_Age.config(state='normal')
                        self.Entry_Birthdate.config(state='readonly')
                        self.Entry_View_Address.config(state='normal')
                        self.Entry_View_Pro.config(state='readonly')
                        self.EntryLicense.config(state='normal')
                        self.Entry_Pro.config(state='readonly')

                        View_EDIT=Button(self.View_Body,text="Save",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda: editAccount2(id,state))
                        View_EDIT.place(x=510,y=270)
                        
                    elif state==1:
                        Account=(
                        id,
                        firstname2.get(),
                        lastname2.get(),
                        profession2.get(),
                        license.get(),
                        dept.get(),
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
                                self.Account_List.pack_forget()
                                employee.Employee.editAccount(Account)
                                self.Account_List.pack(fill=BOTH,padx=20,expand=1)
                                messagebox.showinfo("Changes Saved","Account Update Succesful")
                            else: 
                                self.Profile_BOX.pack(side=LEFT,fill=BOTH,expand=1)
                                messagebox.showinfo("No Changes Made","No Changes have been Made!")
                                
                           
                            state=0
                            self.Entry_View_Username.config(state='disabled')
                            self.Entry_View_Password.config(state='disabled')
                            self.Entry_View_FName.config(state='disabled')
                            self.Entry_View_LName.config(state='disabled')
                            self.Entry_View_Age.config(state='disabled')
                            self.Entry_Birthdate.config(state='disabled')
                            self.Entry_View_Address.config(state='disabled')
                            self.Entry_View_Pro.config(state='disabled')
                            self.EntryLicense.config(state='disabled')
                            self.Entry_Pro.config(state='disabled')
                        self.update_main()
                        self.Stop_update()
                        self.AdminGUI.grab_release()
                        

                print(state)
            
                Profile=Label(self.View_Body,text="Profile",font=("Arial",35,"bold")).place(x=10,y=10)

                View_img=Label(self.View_Body,text="Image",font=("Arial",15),bg="gray").place(x=470,y=10,relwidth=0.3,relheight=0.5)

                Label_View_Username=Label(self.View_Body,text="Username:",font=("Arial",10,"bold")).place(x=10,y=80)
                self.Entry_View_Username=Entry(self.View_Body,textvariable=username2,font=("Arial",10,"bold"),width=30,borderwidth=3,state='disabled')
                self.Entry_View_Username.place(x=10,y=100)

                Label_View_Password=Label(self.View_Body,text="Password:",font=("Arial",10,"bold")).place(x=240,y=80)
                self.Entry_View_Password=Entry(self.View_Body,text="Password:",textvariable=password2,font=("Arial",10,"bold"),width=30,borderwidth=3,state='disabled')
                self.Entry_View_Password.place(x=240,y=100)

                Label_View_FName=Label(self.View_Body,text="First Name:",font=("Arial",10,"bold")).place(x=10,y=130)
                self.Entry_View_FName=Entry(self.View_Body,text="First Name:",textvariable=firstname2,font=("Arial",10,"bold"),width=30,borderwidth=3,state='disabled')
                self.Entry_View_FName.place(x=10,y=150)

                Label_View_LName=Label(self.View_Body,text="Last Name:",font=("Arial",10,"bold")).place(x=240,y=130)
                self.Entry_View_LName=Entry(self.View_Body,text="Last Name:",textvariable=lastname2,font=("Arial",10,"bold"),width=30,borderwidth=3,state='disabled')
                self.Entry_View_LName.place(x=240,y=150)

                Label_View_Age=Label(self.View_Body,text="Age:",font=("Arial",10,"bold")).place(x=10,y=180)
                self.Entry_View_Age=Entry(self.View_Body,text="Age:",textvariable=age2,font=("Arial",10,"bold"),width=10,borderwidth=3,state='disabled')
                self.Entry_View_Age.place(x=10,y=200)

                Label_Birthdate=Label(self.View_Body,text="BirthDate:",font="Arial 12").place(x=100,y=180)
                self.Entry_Birthdate=DateEntry(self.View_Body,width=26,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='disabled')
                self.Entry_Birthdate.place(x=100,y=200)

                Label_View_Address=Label(self.View_Body,text="Address:",font=("Arial",10,"bold")).place(x=10,y=230)
                self.Entry_View_Address=Entry(self.View_Body,text="Address:",textvariable=address2,font=("Arial",10,"bold"),width=50,borderwidth=3,state='disabled')
                self.Entry_View_Address.place(x=10,y=250)

                Label_View_Pro=Label(self.View_Body,text="Profession:",font=("Arial",10,"bold")).place(x=10,y=280)
                self.Entry_View_Pro=Entry(self.View_Body,text="Profession:",textvariable=profession2,font=("Arial",10,"bold"),width=50,borderwidth=3,state='disabled')
                self.Entry_View_Pro.place(x=10,y=300)

                Label_View_Pro=Label(self.View_Body,text="License No:",font=("Arial",10,"bold")).place(x=10,y=280)
                self.EntryLicense=Entry(self.View_Body,textvariable=license,font=("Arial",10,"bold"),width=50,borderwidth=3,state='disabled')
                self.EntryLicense.place(x=10,y=300)

                Label_Pro=Label(self.View_Body,text="Department",font=("Arial",10,"bold")).place(x=10,y=330)
                self.Entry_Pro=ttk.Combobox(self.View_Body,value=['None','Laboratory Department', 'Imaging Center'],textvariable=dept,font='Arial 12',width=37,state='disabled')
                print(res)

                View_DELETE=Button(self.View_Body,text="Delete",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda: deleteAccount(id))
                View_DELETE.place(x=510,y=310)

                self.Entry_Pro.current(self.Entry_Pro['values'].index(res[5]))
                self.Entry_Pro.place(x=10,y=350)
                
                View_EDIT=Button(self.View_Body,text="Edit",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda: editAccount2(id,state))
                View_EDIT.place(x=510,y=270)

                View_Cancel=Button(self.View_Body,text="Cancel",width=15,height=1,font=("Arail",10),borderwidth=5,command=self.View_on_close)
                View_Cancel.place(x=510,y=350)

                PageOpen +=1
            else:
                messagebox.showinfo("Error","The Window EDIT is already Open!")
    
    def update_main(self):
        self.Account_List.pack_forget()
        
        self.Account_List=Frame(self.Admin_RIGHT,highlightbackground="black",highlightthickness=1,)
        self.Account_List.pack(fill=BOTH,padx=20,expand=1)

        self.Profile_BOX=Canvas(self.Account_List)
        self.Profile_BOX.pack(side=LEFT,fill=BOTH,expand=1)

        Profilescroll=ttk.Scrollbar(self.Account_List,orient=VERTICAL,command=self.Profile_BOX.yview)
        Profilescroll.pack(side=RIGHT,fill=Y)

        self.Profile_BOX.configure(yscrollcommand=Profilescroll.set)
        self.Profile_BOX.bind('<Configure>',lambda e: self.Profile_BOX.configure(scrollregion= self.Profile_BOX.bbox("all")))

        self.Profile=Frame(self.Profile_BOX)
        self.Profile_BOX.create_window((0,0),window=self.Profile,anchor=NW)

        result=employee.Employee.getAllEmployees()
        for self.Account_Num in range(len(result)):
            self.Profile_Number=Frame(self.Profile,padx=10, pady=10, width=1023, height=200)
            self.Profile_Number.grid(row=self.Account_Num,column=0)

            Profile_Detail=Frame(self.Profile_Number,highlightbackground="black",highlightthickness=1,)
            Profile_Detail.place(x=5,y=7,relwidth=0.99,relheight=0.92)

            # Access Image URL thru result[self.Account_Num][8] 
            Profile_Image=Label(Profile_Detail,text="IMAGE",bg="gray").place(x=10,y=10,relwidth=0.2,relheight=0.88)
            global Profile_Name
            Profile_Name=Label(Profile_Detail,text=result[self.Account_Num][1]+" "+result[self.Account_Num][2],font=("Arail",25,"bold"))
            Profile_Name.place(x=220,y=10)
            labels.append(Profile_Name)

            Profile_Edit=Button(Profile_Detail,text="View",width=10,height=2,font=("Arail",10),borderwidth=5,command=lambda x= result[self.Account_Num][0]:self.ViewProfile(x, labels[self.Account_Num]))
            Profile_Edit.place(x=850,y=50)
        global update_id
        update_id=self.AdminGUI.after(1000, self.update_main)

    def Stop_update(self):
        global update_id
        self.AdminGUI.after_cancel(update_id)
    
    def logout(self):
        self.AdminGUI.destroy()
        interface=LoginPage.Loginpage()
        interface.start()

    def AdminGUI_Main(self):
        self.AdminGUI=Tk()
        self.AdminGUI.title('CITY HEALTH')
        width= self.AdminGUI.winfo_screenwidth()
        height=self.AdminGUI.winfo_screenheight()
        self.AdminGUI.geometry("%dx%d"%(width,height))


        self.Page_Admin=Frame(self.AdminGUI)
        self.Page_Admin.pack(expand=1, fill=BOTH)

        Frame_Header=Frame(self.Page_Admin,bg='#BDFFC4',highlightbackground="black",highlightthickness=1)
        Frame_Header.pack(fill=X)
        image3 = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((40, 40)))
        IMG_HEADER_Xray=Label(Frame_Header,image=image3,bg='#BDFFC4',width=40,height=40)
        IMG_HEADER_Xray.image=image3
        IMG_HEADER_Xray.pack(side=LEFT)
        HEADER_TITLE=Label(Frame_Header,text="City Health Office",bg='#BDFFC4',font='Roboto 20 bold')
        HEADER_TITLE.pack(side=LEFT)

        LOGOUT=Button(Frame_Header,text="LOGOUT",borderwidth=5,font=("Arial",12),command=lambda:self.logout())
        LOGOUT.pack(side=RIGHT,padx=10)
        #Header END-----------
        Admin_Body=Frame(self.Page_Admin)
        Admin_Body.pack(expand=1,fill=BOTH)

        Admin_LEFT=Frame(Admin_Body,width=270)
        Admin_LEFT.pack(fill=Y,side=LEFT)

        Logo_Admin=Label(Admin_LEFT,text="LOGO",width=30,height=15,bg="white",highlightbackground="black",highlightthickness=1)
        Logo_Admin.pack(padx=30,pady=40)

        Registration_Button=Button(Admin_LEFT,text="Registration",width=20,height=2,font=("Arail",10),borderwidth=5,command=self.Regist)
        Registration_Button.pack()

        self.Admin_RIGHT=Frame(Admin_Body,width=250)
        self.Admin_RIGHT.pack(expand=1,fill=BOTH,side=RIGHT)

        Title_Admin=Label(self.Admin_RIGHT,text="Account Management Page",font=("Arail",35,"bold"),anchor=W)
        Title_Admin.pack(fill=X,padx=20)

        self.Account_List=Frame(self.Admin_RIGHT,highlightbackground="black",highlightthickness=1,)
        self.Account_List.pack(fill=BOTH,padx=20,expand=1)

        self.Profile_BOX=Canvas(self.Account_List)
        self.Profile_BOX.pack(side=LEFT,fill=BOTH,expand=1)

        Profilescroll=ttk.Scrollbar(self.Account_List,orient=VERTICAL,command=self.Profile_BOX.yview)
        Profilescroll.pack(side=RIGHT,fill=Y)

        self.Profile_BOX.configure(yscrollcommand=Profilescroll.set)
        self.Profile_BOX.bind('<Configure>',lambda e: self.Profile_BOX.configure(scrollregion= self.Profile_BOX.bbox("all")))

        self.Profile=Frame(self.Profile_BOX)
        self.Profile_BOX.create_window((0,0),window=self.Profile,anchor=NW)

        result=employee.Employee.getAllEmployees()

        global labels
        labels=[]
        for self.Account_Num in range(len(result)):
            self.Profile_Number=Frame(self.Profile,padx=10, pady=10, width=1023, height=200)
            self.Profile_Number.grid(row=self.Account_Num,column=0)

            Profile_Detail=Frame(self.Profile_Number,highlightbackground="black",highlightthickness=1,)
            Profile_Detail.place(x=5,y=7,relwidth=0.99,relheight=0.92)

            # Access Image URL thru result[self.Account_Num][8] 
            Profile_Image=Label(Profile_Detail,text="IMAGE",bg="gray").place(x=10,y=10,relwidth=0.2,relheight=0.88)
            global Profile_Name
            Profile_Name=Label(Profile_Detail,text=result[self.Account_Num][1]+" "+result[self.Account_Num][2],font=("Arail",25,"bold"))
            Profile_Name.place(x=220,y=10)
            labels.append(Profile_Name)

            Profile_Edit=Button(Profile_Detail,text="View",width=10,height=2,font=("Arail",10),borderwidth=5,command=lambda x= result[self.Account_Num][0]:self.ViewProfile(x, labels[self.Account_Num]))
            Profile_Edit.place(x=850,y=50)

        self.AdminGUI.mainloop()

    def start(self):
        self.AdminGUI_Main()