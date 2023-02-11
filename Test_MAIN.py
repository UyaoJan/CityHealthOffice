from tkinter import *
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry
import calendar
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
from datetime import date, datetime
import employee, LoginPage
import docx
from pathlib import Path
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Inches
import numpy as np
import matplotlib.pyplot as plt
import win32api, os, time
import win32print
import summary_filter

from ctypes import windll

# get the handle to the taskbar
h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)


class Main:
    def __init__(self,init):
        self.user=init
        self.Dashboard_GUI = None
        self.Page_Summary = None
        self.Page_FrontDesk = None
        self.Page_XRAY = None
        global PageOpen
        PageOpen = 1
        self.Value_Laboratory = ["Laboratory","X_RAY"]
        
        windll.user32.ShowWindow(h, 0)

        self.test_date=date.today()
    
        #Checkbox Def

    def showCheckbox(self):
        errors=0
        chosen_serve=[]
        if Name_Entry.get() is None:
            errors +=1
        name=Name_Entry.get()
        if AGE_Entry.get() is None or AGE_Entry.get().isnumeric()==False:
            errors+=1
        age=AGE_Entry.get()
        global month_num
        bdate=str(Year_Birth.get())+'-'+str(month_num)+'-'+str(Day_Birth.get())
        bdate=datetime.strptime(bdate,"%Y-%m-%d")
        gender=Gender_Mune.get()
        if Address_Entry.get() is None:
            errors+=1
        address=Address_Entry.get()
        today=date.today()
        client_id=employee.Employee.generateID()
        
        for i in range(len(self.services)):
            Selected=""
            if int(self.services[i].get()) == 1:
                Selected += str(i)
                this=self.Value[i]
                # print(self.services[i].get())
                # print(this)
                chosen_serve.append(this)
                # print(self.services[i].get())

        if len(chosen_serve)==0:
            errors+=1
            
        if errors ==0:
            client=(client_id,name,age,gender,bdate,address)
            user=self.user
            user.addNewClient(user, client,chosen_serve,today)
            messagebox.showinfo("Client Entered Successfully","New Client Data Registered Successfully")
                
            Page_FrontDesk.destroy()
            self.Page_Dashboard.pack()

        else: messagebox.showerror("Input Error","There is one or More Errors in Data Entered. \nPlease Make sure that the Data you entered followed Specifications")

    def logout(self):
        self.Dashboard_GUI.destroy()
        interface=LoginPage.Loginpage()
        interface.start()

    def FrontDesk(self):
        def Home():
            Page_FrontDesk.destroy()
            self.Page_Dashboard.pack()
        self.Page_Dashboard.forget()
        global Page_FrontDesk
        Page_FrontDesk=Frame(self.Dashboard_GUI)
        Page_FrontDesk.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(Page_FrontDesk,width=1360,height=50,bg='#BDFFC4',highlightbackground="black",highlightthickness=1)
        Frame_Header.pack()
        image5 = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((40, 40)))
        IMG_HEADER_FD=Label(Frame_Header,image=image5,bg='#BDFFC4',width=40,height=40)
        IMG_HEADER_FD.image=image5
        IMG_HEADER_FD.place(x=5,y=1)
        HEADER_TITLE=Label(Frame_Header,text="City Health Office",bg='#BDFFC4',font='Roboto 25 bold').place(x=50,y=1)

        HEADER_USERNAME=Label(Frame_Header,text=str(self.user.username),bg='#BDFFC4',font='Roboto 20 ').place(x=1150,y=5)
        # IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
        # IMG_USERNAME.place(x=1200,y=5)

        Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
        Toggle_Button.place(x=1290,y=10)
        Toggle_Button.menu=Menu(Toggle_Button)
        Toggle_Button["menu"]=Toggle_Button.menu

        Toggle_Button.menu.add_command(label="Home",font='Roboto 12',command=Home)
        Toggle_Button.menu.add_command(label="Logout",font='Roboto 12',command=lambda:self.logout())

        #Header-------
        #Body-------
        Frame_Body=Frame(Page_FrontDesk)
        Frame_Body.pack(side=RIGHT)

        Frame_LIST=Frame(Frame_Body,width=680,height=700)
        Frame_LIST.pack(side=LEFT)
        FrontDesk_Title=Label(Frame_Body,text="New Client",font='Roboto 75')
        FrontDesk_Title.place(x=20,y=20)
        Box_Title=Label(Frame_Body,text="Laboratory Test List",font='Roboto 25')
        Box_Title.place(x=54,y=300)
        self.Box=Frame(Frame_LIST,width=560,height=300,highlightbackground="black",highlightthickness=1)
        self.Box.place(x=50,y=320)
        #checkbox
        self.Value=[
                    "Complete Blood Count",
                    "Blood Type",
                    "Stool Exam",
                    "Urinalysis (Urine Test)",
                    "Syphilis Rapid Test",
                    "Hepatitis B (Antigen Test)",
                    "Anti-HAV Test",
                    "Drug Test",
                    "Pregnancy Test",
                    "Fasting Blood Suger Test",
                    "Blood Uric Acid Test",
                    "Blood Cholesterol Test",
                    "Blood Creatinine Test",
                    "Acid Fast Staining",
                    "X-Ray Test",
                    "Serology",
                    "Medical Certificate",
                    "Fecalysis"
                    ]
        
        self.services=[]
        for i in range (len(self.Value)):
            Test=IntVar()
            Test.set(0)
            self.services.append(Test)


            
        Checkbutton(self.Box,text="Complete Blood Count",variable=self.services[0],font='Roboto 12 ').place(x=30,y=50)
        Checkbutton(self.Box,text="Blood Type",variable=self.services[1],font='Roboto 12 ').place(x=30,y=75)
        Checkbutton(self.Box,text="Stool Exam",variable=self.services[2],font='Roboto 12 ').place(x=30,y=100)
        Checkbutton(self.Box,text="Urinalysis (“Urine Test”)",variable=self.services[3],font='Roboto 12 ').place(x=30,y=125)
        Checkbutton(self.Box,text="Syphilis Rapid Test",variable=self.services[4],font='Roboto 12 ').place(x=30,y=150)
        Checkbutton(self.Box,text="Hepatitis B (“Antigen Test”)",variable=self.services[5],font='Roboto 12 ').place(x=30,y=175)
        Checkbutton(self.Box,text="Anti-HAV Test",variable=self.services[6],font='Roboto 12 ').place(x=30,y=200)
        Checkbutton(self.Box,text="Drug Test",variable=self.services[7],font='Roboto 12 ').place(x=30,y=222)
        Checkbutton(self.Box,text="Pregnancy Test",variable=self.services[8],font='Roboto 12 ').place(x=30,y=245)
        Checkbutton(self.Box,text="Fasting Blood Suger Test",variable=self.services[9],font='Roboto 12 ').place(x=280,y=50)
        Checkbutton(self.Box,text="Blood Uric Acid Test",variable=self.services[10],font='Roboto 12 ').place(x=280,y=75)
        Checkbutton(self.Box,text="Blood Cholesterol Test",variable=self.services[11],font='Roboto 12 ').place(x=280,y=100)
        Checkbutton(self.Box,text="Blood Creatinine Test",variable=self.services[12],font='Roboto 12 ').place(x=280,y=125)
        Checkbutton(self.Box,text="Acid Fast Staining",variable=self.services[13],font='Roboto 12 ').place(x=280,y=150)
        Checkbutton(self.Box,text="X-Ray Test",variable=self.services[14],font='Roboto 12 ').place(x=280,y=175)
        Checkbutton(self.Box,text="Serology",variable=self.services[15],font='Roboto 12 ').place(x=280,y=200)
        Checkbutton(self.Box,text="Medical Certificate",variable=self.services[16],font='Roboto 12 ').place(x=280,y=220)
        Checkbutton(self.Box,text="Fecalysis",variable=self.services[17],font='Roboto 12 ').place(x=280,y=240)

        #Body-------


        #IMPUT-----------------
        Frame_Input=Frame(Frame_Body,width=680,height=700)
        Frame_Input.pack()
                
        FrameIMG=Frame(Frame_Input,width=300,height=300)
        FrameIMG.place(x=170,y=40)

        image = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((300, 300)))
        Img=Label(FrameIMG,image = image)
        Img.image=image
        Img.place(x=0,y=0,width=300, height=300)

        global Name_Entry
        Name_Label=Label(Frame_Input,text="Name: ",font='Roboto 12').place(x=46,y=400)
        Name_Entry=Entry(Frame_Input,width=59,borderwidth=3,font='Roboto 12')
        Name_Entry.place(x=100,y=400)

        global AGE_Entry
        AGE_Label=Label(Frame_Input,text="Age: ",font='Roboto 12').place(x=46,y=430)
        AGE_Entry=Entry(Frame_Input,width=5,font='Roboto 12',borderwidth=3)
        AGE_Entry.place(x=100,y=430)

        global month_num, cal, number
        month_num=1

        global Year_Birth
        thisyear=2023
        Year_number=list(range(thisyear,1900,-1))
        Year=Year_number
        Year_Birth=ttk.Combobox(Frame_Input,value=Year,font='Roboto 12',width=6,state='readonly')
        Year_Birth.set("2023")
        Year_Birth.current(0)
        Year_Birth.place(x=380,y=430)

        curr_month=datetime.strptime(str(month_num),"%m")
        curr_year=datetime.strptime(Year_Birth.get(),"%Y")

        cal=calendar.monthcalendar(int(curr_year.year),int(curr_month.month))
        number=[day for week in cal for day in week if day != 0]
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

        def calculate_age(event):
            birthdate=event.widget.get()
            birthdate=datetime.strptime(birthdate,'%Y')
            birthdate=birthdate.year
            today = date.today()
            age= today.year - birthdate
            AGE_Entry.delete(0,END)
            AGE_Entry.insert(0,age)

            global month_num
            month_num=datetime.strptime(Month_Birth.get(), '%B').month
            curr_month=datetime.strptime(str(month_num),"%m")
            curr_year=datetime.strptime(Year_Birth.get(),"%Y")
            global cal,number
            cal=calendar.monthcalendar(int(curr_year.year),int(curr_month.month))
            number=[day for week in cal for day in week if day != 0]
            Day_Birth.config(value=number)

        Year_Birth.bind("<<ComboboxSelected>>",calculate_age)

        Birth_Label=Label(Frame_Input,text="Birthdate:",font="Roboto 12").place(x=153,y=430)
        global Month_Birth
        Month=['January','February','March','April','May','June','July','August','September','October','November','December']
        Month_Birth=ttk.Combobox(Frame_Input,value=Month,font='Roboto 12',width=9,state='readonly')
        Month_Birth.current(0)
        Month_Birth.place(x=225,y=430)
        Month_Birth.bind("<<ComboboxSelected>>",setMonth)

        global Day_Birth
        Day=number
        Day_Birth=ttk.Combobox(Frame_Input,value=Day,font='Roboto 12',width=2,state='readonly')
        Day_Birth.current(0)
        Day_Birth.place(x=334,y=430) 


        # global Birth_Entry
        #Birth_Label=Label(Frame_Input,text="Birthdate:",font="Roboto 12").place(x=160,y=430)
        # Birth_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Roboto 12",bd=2,state='readonly')
        # Birth_Entry.place(x=230,y=430)

        # Birth_Entry.bind("<<DateEntrySelected>>",calculate_age)

        global Gender_Mune
        Gender_Label=Label(Frame_Input,text="Gender:",font='Roboto 12').place(x=460,y=430)
        Option=["Male","Female","Other"]
        Gender_Mune=ttk.Combobox(Frame_Input,value=Option,font='Roboto 12',width=10,state='readonly')
        Gender_Mune.current(0)
        Gender_Mune.place(x=524,y=430)

        global Address_Entry,addrs
        addrs=StringVar()
        Address_Label=Label(Frame_Input,text="Address: ",font='Roboto 12').place(x=46,y=460)
        Address_Entry=Entry(Frame_Input,textvariable=addrs,width=38,borderwidth=3,font='Roboto 12')
        Address_Entry.place(x=120,y=460)

        # global Date_Entry
        # Date_Label=Label(Frame_Input,text="Date:",font="Roboto 12").place(x=480,y=460)
        # Date_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Roboto 12",bd=2,archor=W,state='readonly')
        # Date_Entry.place(x=525,y=460)

        Submit_Input=Button(Frame_Input,text="Submit",width=10,bg="green",font='Roboto 11',command=self.showCheckbox)
        Submit_Input.place(x=540,y=530)


#FrontDesk-END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Record_on_close(self):
        global PageOpen
        if messagebox.askokcancel('Close', 'Are you sure you want to close the View Page all the data will not be Save?'):
            PageOpen=1
            self.RecordPage.destroy()
    
    def Record(self,value):
        global PageOpen
        if PageOpen < 2:
            self.RecordPage=Toplevel()
            self.RecordPage.title("Record")
            self.RecordPage
            Record_width=450
            Record_height=600
            self.RecordPage.geometry(f'{Record_width}x{Record_height}+{480}+{100}')
            self.RecordPage.protocol("WM_DELETE_WINDOW", self.Record_on_close)
            self.RecordPage.resizable(False,False)

            self.RecordBody= Frame(self.RecordPage)
            self.RecordBody.pack(expand=1,fill=BOTH)

            Record_search_LB=Label(self.RecordBody,text="SEARCH: ",font='Roboto 12 bold').place(x=10,y=100)
            Record_search_EN=Entry(self.RecordBody,font='Roboto 12',borderwidth=5)
            Record_search_EN.place(x=90,y=98,relwidth=0.6)
            Record_search_BT=Button(self.RecordBody,text="Search",font='Roboto 10',width=6,height=0,borderwidth=5)
            Record_search_BT.place(x=365,y=94)

            RecordFrame=Frame(self.RecordBody,highlightbackground="black",highlightthickness=1)
            RecordFrame.place(x=0,y=130,relwidth=1.0,relheight=0.78)
            RecordBOX= Canvas(RecordFrame,highlightbackground="black",highlightthickness=1)
            RecordBOX.pack(side=LEFT,fill=BOTH,expand=1)

            Recordscroll=ttk.Scrollbar(RecordFrame,orient=VERTICAL,command=RecordBOX.yview)
            Recordscroll.pack(side=RIGHT,fill=Y)

            RecordBOX.configure(yscrollcommand=Recordscroll.set)
            RecordBOX.bind('<Configure>',lambda e: RecordBOX.configure(scrollregion= RecordBOX.bbox("all")))

            Record_List=Frame(RecordBOX,highlightbackground="black",highlightthickness=2)
            RecordBOX.create_window((0,0),window=Record_List,anchor=NW)
            #print(self.Value_Laboratory)
            if value == "Laboratory":
                records=self.user.getClients_lab()
                #print(value)
                for i in range(len(records)):
                    Record_Number=Frame(Record_List,width=427,height=80)
                    Record_Number.grid(row=i,column=0)

                    Record_Page=Frame(Record_Number,width=250,height=50,highlightbackground="black",highlightthickness=1)
                    Record_Page.place(x=5,y=5,relwidth=0.98,relheight=0.9)

                    Number_BOX=Frame(Record_Page,width=70,height=50,highlightbackground="black",highlightthickness=1)
                    Number_BOX.place(x=10,y=10)
                    Client_Number=Label(Number_BOX,text=records[i][0],font=("Roboto",25,"bold")).place(x=3,y=0)#luna please limit the Number of the of to 3 only

                    Client_Name=Label(Record_Page,text="NAME: "+records[i][1],font=("Roboto",12,"bold")).place(x=85,y=10)
                    Client_Test=Label(Record_Page,text="TEST: "+records[i][6],font=("Roboto",8,"bold")).place(x=85,y=30)

                    Take_Button=Button(Record_Page,text="Take",font=("Roboto",8),width=6,height=0,borderwidth=5)
                    Take_Button.place(x=360,y=37)
            
            elif value == "X_RAY":
                records=self.user.getClients_Xray()
                def take(e):
                    result=self.user.getClient(e)
                    self.client_name=result[1]
                    self.client_age=result[2]
                    self.client_gender=result[3]
                    self.client_bdate=result[4]
                    self.client_address=result[5]

                for i in range(len(records)):
                    X_RAY_Record_Number=Frame(Record_List,width=427,height=80)
                    X_RAY_Record_Number.grid(row=i,column=0)

                    X_RAY_Record_Page=Frame(X_RAY_Record_Number,width=250,height=50,highlightbackground="black",highlightthickness=1)
                    X_RAY_Record_Page.place(x=5,y=5,relwidth=0.98,relheight=0.9)

                    XRAY_Number_BOX=Frame(X_RAY_Record_Page,width=70,height=50,highlightbackground="black",highlightthickness=1)
                    XRAY_Number_BOX.place(x=10,y=10)
                    XRAY_Client_Number=Label(XRAY_Number_BOX,text=records[i][0],font=("Roboto",25,"bold")).place(x=3,y=0)

                    XRAY_Client_Name=Label(X_RAY_Record_Page,text="NAME: "+records[i][1],font=("Roboto",12,"bold")).place(x=85,y=10)
                    XRAY_Client_Test=Label(X_RAY_Record_Page,text="TEST: XRAY TEST",font=("Roboto",8,"bold")).place(x=85,y=30)

                    XRAY_Take_Button=Button(X_RAY_Record_Page,text="Take",font=("Roboto",8),width=6,height=0,borderwidth=5,command=lambda e= records[i][0]:take(e))
                    XRAY_Take_Button.place(x=360,y=37)
            
            PageOpen += 1

        else:
            messagebox.showinfo("Error","The Window is already Open!")

#Laboratory>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Laboratory(self):
        if self.user.return_dept()!='Laboratory Department':
            messagebox.showerror("Access Denied","Only Employees from Laboratory Department or Users with Administrative Access can Access this Page")
        else: 
            def Home():
                Page_Laboratory.destroy()
                self.Page_Dashboard.pack()

            self.Page_Dashboard.forget()
            Page_Laboratory=Frame(self.Dashboard_GUI,bg="green")
            Page_Laboratory.pack(expand=1, fill=BOTH)
            Frame_Header=Frame(Page_Laboratory,width=1360,height=50,bg='#BDFFC4',highlightbackground="black",highlightthickness=1)
            Frame_Header.pack()
            image4 = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((40, 40)))
            IMG_HEADER_Lab=Label(Frame_Header,image=image4,bg='#BDFFC4',width=40,height=40)
            IMG_HEADER_Lab.image=image4
            IMG_HEADER_Lab.place(x=5,y=1)
            HEADER_TITLE=Label(Frame_Header,text="City Health Office",bg='#BDFFC4',font='Roboto 25 bold').place(x=50,y=1)

            HEADER_USERNAME=Label(Frame_Header,text=str(self.user.username),bg='#BDFFC4',font='Roboto 20 ').place(x=1150,y=5)
            # IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
            # IMG_USERNAME.place(x=1250,y=8)

            Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
            Toggle_Button.place(x=1290,y=10)
            Toggle_Button.menu=Menu(Toggle_Button)
            Toggle_Button["menu"]=Toggle_Button.menu

            Toggle_Button.menu.add_command(label="Home",font='Roboto 12',command=Home)
            Toggle_Button.menu.add_command(label="Logout",font='Roboto 12',command=lambda:self.logout())
            #Header-------
            #BODY >> Laboratory
            Frame_Body=Frame(Page_Laboratory,width=1360,height=150,highlightbackground="black",highlightthickness=1)
            Frame_Body.pack()

            Labo_Title=Label(Frame_Body,text="Laboratory Test!",font='Roboto 20')
            Labo_Title.place(x=10,y=5)
            Name_Label=Label(Frame_Body,text="Name: ",font='Roboto 12').place(x=19,y=50)
            # Name_Entry=Entry(Frame_Body,width=59,borderwidth=3,font='Roboto 9')
            res=self.user.getClients_all()
            names=[x[1] for x in res]
            Name_Entry=ttk.Combobox(Frame_Body,value=names,font='Roboto 12',state='readonly',width=40)
            Name_Entry.place(x=20,y=70)

            def setClient(event):
                res=self.user.getClient_name(Name_Entry.get())
                age=IntVar()
                age.set(res[2])
            
                Gender_Mune.set(res[3])

            Name_Entry.bind("<<ComboboxSelected>>",setClient)

            AGE_Label=Label(Frame_Body,text="Age: ",font='Roboto 12').place(x=400,y=50)
            AGE_Entry=Entry(Frame_Body,width=8,font='Roboto 9',borderwidth=3,state='disabled')
            AGE_Entry.place(x=400,y=70)

            ID_LABEL=Label(Frame_Body,text="ID: ",font='Roboto 12').place(x=500,y=50)
            ID_ENTRY=Entry(Frame_Body,width=8,font='Roboto 9',borderwidth=3,state='disabled')
            ID_ENTRY.place(x=500,y=70)

            # def Gender_Click(event):
            #     Genderlabel=Label(Frame_Body,Gender_Mune.get(),font="Roboto 12")

            Gender_Label=Label(Frame_Body,text="Gender:",font='Roboto 12').place(x=150,y=100)
            Option=["Male","Female","Other"]
            Gender_Mune=ttk.Combobox(Frame_Body,value=Option,font='Roboto 12',state='readonly')
            Gender_Mune.set("Select Gender")
            # Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
            Gender_Mune.place(x=150,y=120)

            Date_Label=Label(Frame_Body,text="Date:",font=("Roboto 12")).place(x=20,y=100)
            Date_Entry=DateEntry(Frame_Body,width=10,backgroud="magenta3",foreground="White",font="Roboto 12",bd=2,archor=W)
            Date_Entry.place(x=20,y=120)
            
            Testlist=Frame(Frame_Body,bg="blue",highlightbackground="black",highlightthickness=1)
            Testlist.place(x=850,y=0,relwidth=0.25,relheight=1.0)

            Test_Table=ttk.Treeview(Testlist)
            style=ttk.Style()
            style.theme_use("default")
            style.configure("Treeview")
            Test_Table['column']=("Laboratory","Complete")

            Test_Table.column("#0",width=0,stretch=NO)
            Test_Table.column("Laboratory",width=200)
            Test_Table.column("Complete",width=100)

            Test_Table.heading("#0")
            Test_Table.heading("Laboratory",text="Laboratory Test")
            Test_Table.heading("Complete",text="Complete")
            Test_Table.pack(expand=1,fill=BOTH)

            def setClient(event):
                if Test_Table.get_children()!=0:
                    Test_Table.delete(*Test_Table.get_children())

                res=self.user.getClient_name(Name_Entry.get())
                age=IntVar()
                age.set(res[2])
                AGE_Entry.config(textvariable=age)
                Gender_Mune.set(res[3])

                client_identification=IntVar()
                client_identification.set(res[0])
                ID_ENTRY.config(textvariable=client_identification)
                res=self.user.getclientTests(res[0])
                count=0
                for i in res:
                    Test_Table.insert('','end',iid=count,text=res[count][0],values=(i[3],))
                    count+=1
                
            # def double_click(event):
            #     iid=Test_Table.focus()
            #     Test_Table.set(iid, 'Complete','Done')
            #     item=Test_Table.item(iid)["text"]
            #     self.user.markTest_as_done(item)


            Name_Entry.bind("<<ComboboxSelected>>",setClient)
            Record_Button=Button(Frame_Body,text="Record",bg="green",width=15,height=1,font=("Roboto",10),borderwidth=5,command=lambda:self.Record(self.Value_Laboratory[0]))
            Record_Button.place(x=1200,y=100)

            #Frame for the Testing 
            Frame_Test=Frame(Page_Laboratory,highlightbackground="black",highlightthickness=1,bg="blue")
            Frame_Test.pack(expand=1,fill=BOTH)

            Test_Label=Label(Frame_Test,text="Laboratory Test",width=123,font="Roboto 15",anchor=W,highlightbackground="black",highlightthickness=1)
            Test_Label.place(x=0,y=0)

            Test=[  
                    "Complete Blood Count / Hematology",
                    "Urinalysis",
                    "Serology",
                    "Miscelaneous",
                    "FECALYSIS"
                ]

            def Option_TEST(event):
                if LabTest_Mune.get() == "Serology":
                    Miscelaneous_Page.pack_forget()
                    Urinalysis_Page.pack_forget()
                    CBC_Page.pack_forget()
                    FE_Page.pack_forget()

                    Serology_Page.pack(expand=1,fill=BOTH)

                    Serology_Title = Label(Serology_Page,text=LabTest_Mune.get(),font=("Roboto",20,"bold"))
                    Serology_Title.place(x=570,y=30)

                    #RIGHT
                    ST_Box=Frame(Serology_Page,bg='white')
                    ST_Box.place(x=380,y=150)
                    ST_BOX1_R= Label(ST_Box,text="",font=("Roboto",15,"bold"),width=35,anchor=W,highlightbackground="black",highlightthickness=1)
                    ST_BOX1_R.grid(row=0,column=0)
                    ST_BOX2_R= Label(ST_Box,text="BLOOD TYPE",font=("Roboto",15,"bold"),width=35,anchor=W,highlightbackground="black",highlightthickness=1)
                    ST_BOX2_R.grid(row=1,column=0)
                    ST_BOX3_R= Label(ST_Box,text="HEPATITIS B SCREENING (HBsAg)",font=("Roboto",15,"bold"),width=35,anchor=W,highlightbackground="black",highlightthickness=1)
                    ST_BOX3_R.grid(row=2,column=0)
                    ST_BOX4_R= Label(ST_Box,text="ANTI-HAV SCREENING (HAV lgG/igM)",font=("Roboto",15,"bold"),width=35,anchor=W,highlightbackground="black",highlightthickness=1)
                    ST_BOX4_R.grid(row=3,column=0)
                    ST_BOX5_R= Label(ST_Box,text="SYPHILIS SCREENING",font=("Roboto",15,"bold"),width=35,anchor=W,highlightbackground="black",highlightthickness=1)
                    ST_BOX5_R.grid(row=4,column=0)
                    ST_BOX6_R= Label(ST_Box,text="DENGUE NS1 ANTIGEN TEST",font=("Roboto",15,"bold"),width=35,anchor=W,highlightbackground="black",highlightthickness=1)
                    ST_BOX6_R.grid(row=5,column=0)
                    
                    #LEFT
                    ST_BOX7_L= Label(ST_Box,text="RESULT",font=("Roboto",15,"bold"),width=18,highlightbackground="black",highlightthickness=1)
                    ST_BOX7_L.grid(row=0,column=1)
                    ST_BOX8_L= Entry(ST_Box,text="",font=("Roboto",15,"bold"),borderwidth=3,highlightbackground="black",highlightthickness=1)
                    ST_BOX8_L.grid(row=1,column=1)
                    ST_BOX9_L= Entry(ST_Box,text="",font=("Roboto",15,"bold"),borderwidth=3,highlightbackground="black",highlightthickness=1)
                    ST_BOX9_L.grid(row=2,column=1)
                    ST_BOX10_L= Entry(ST_Box,text="",font=("Roboto",15,"bold"),borderwidth=3,highlightbackground="black",highlightthickness=1)
                    ST_BOX10_L.grid(row=3,column=1)
                    ST_BOX11_L= Entry(ST_Box,text="",font=("Roboto",15,"bold"),borderwidth=3,highlightbackground="black",highlightthickness=1)
                    ST_BOX11_L.grid(row=4,column=1)
                    ST_BOX12_L= Entry(ST_Box,text="",font=("Roboto",15,"bold"),borderwidth=3,highlightbackground="black",highlightthickness=1)
                    ST_BOX12_L.grid(row=5,column=1)

                    def submit():
                        serviceid=self.user.get_test_id("Serology")
                        client_id=self.user.getClient_name(Name_Entry.get())
                        services=self.user.getClientTestRequests(client_id,serviceid)
                        if services is None:
                            messagebox.showerror("Error","This Test was not Requested by the Client")
                        else: 
                            blood_type=ST_BOX8_L.get()
                            hepatitis_b_Screening=ST_BOX9_L.get()
                            anti_hav_screening=ST_BOX10_L.get()
                            syphilis_screen=ST_BOX11_L.get()
                            dengue_ns1_antigen_test=ST_BOX12_L.get()
                            document=Path(__file__).parent / "SEROLOGY_TEMPLATE.docx"
                            doc=DocxTemplate(document)
                                
                            context={
                                "NAME":Name_Entry.get(),
                                "AGE_SEX":AGE_Entry.get()+'/'+Gender_Mune.get(),
                                "DATE":self.test_date,
                                "OR_NO":self.user.generateClient_ORNumber(),
                                "BLOODTYPE": blood_type,
                                "HEPA_B_SCREEN": hepatitis_b_Screening,
                                "ANTI_HAV_SCREEN": anti_hav_screening,
                                "SYPHILIS_SCREEN": syphilis_screen,
                                "DENGUE_ANTIGEN_TEST": dengue_ns1_antigen_test,
                                "MEDTECH_NAME":self.user.fname+" "+self.user.lname,
                                "PATHOLOGIST":"JERRY C. ABROGUEÑA, MD, FPSP"
                            }
                            doc.render(context)
                            doc.save(Path(__file__).parent/"newDoc.docx")
                            win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)
                            serviceid=self.user.get_test_id("Serology")
                            total=self.user.get_test_price(serviceid[0])
                            id=self.user.save_to_summary(total[0],serviceid[0],client_id[0])
                            self.user.update_summaryID_test(id,client_id[0],serviceid[0])
                            test_id=self.user.get_tests_id(client_id[0],serviceid[0])
                            self.user.markTest_as_done(test_id[0])
                            for item in Test_Table.get_children():
                                if Test_Table.item(item)['values'][0]=="Serology":
                                    Test_Table.set(item, 'Complete','Done')



                    ST_Button=Button(Serology_Page,text="Submit",font=("Roboto",10,"bold"),width=10,height=1,borderwidth=5,command=lambda: submit())
                    ST_Button.place(x=1200,y=430)

                elif LabTest_Mune.get() == "Miscelaneous":
                    Serology_Page.pack_forget()
                    Urinalysis_Page.pack_forget()
                    CBC_Page.pack_forget()
                    FE_Page.pack_forget()

                    Miscelaneous_Page.pack(expand=1,fill=BOTH)
                    Miscelaneous_Title = Label(Miscelaneous_Page,text=LabTest_Mune.get(),font=("Roboto",20,"bold"))
                    Miscelaneous_Title.place(x=570,y=30)

                    PT_Box=Frame(Miscelaneous_Page,bg='white')
                    PT_Box.place(x=430,y=200)
                    PT_BOX1= Label(PT_Box,text="TEST",width=20,anchor=W,font=("Roboto",15,"bold"),highlightbackground="black",highlightthickness=1)
                    PT_BOX1.grid(row=0,column=0)
                    # PT_BOX2= Label(PT_Box,text="PREGNANCY TEST",width=20,anchor=W,font=("Roboto",15,"bold"))
                    res_test=self.user.getAllTest()
                    TEST=[x[0] for x in res_test]
                    PT_BOX2= ttk.Combobox(PT_Box,value=TEST,font=("Roboto",15),state='readonly')
                    PT_BOX2.grid(row=0,column=1)
                    PT_BOX3= Label(PT_Box,text="RESULT",width=20,anchor=W,font=("Roboto",15,"bold"),highlightbackground="black",highlightthickness=1)
                    PT_BOX3.grid(row=1,column=0)

                    # PT_Result=["POSITIVE","NEGATIVE"]
                    # PT_BOX4=ttk.Combobox(PT_Box,value=PT_Result,font=("Roboto",15),state='readonly')
                    # PT_BOX4.set("Select Result")
                    PT_BOX4=Entry(PT_Box,font=("Roboto",12),width=25,borderwidth=3,highlightbackground="black",highlightthickness=1)
                    PT_BOX4.grid(row=1,column=1)

                    def submit():
                        print(PT_BOX2.get())
                        print(res[0][0])
                        serviceid=self.user.get_test_id(PT_BOX2.get())
                        services=self.user.getClientTestRequests(int(ID_ENTRY.get()),serviceid)
                        print(serviceid)
                        print(services)
                        if services is None:
                            messagebox.showerror("Error","This Test was not Requested by the Client")
                        else: 
                            document=Path(__file__).parent / "MISCELLANEOUS_TEMPLATE.docx"
                            doc=DocxTemplate(document)

                            context={
                                "NAME":Name_Entry.get(),
                                "AGE_SEX":AGE_Entry.get()+'/'+Gender_Mune.get(),
                                "DATE":self.test_date,
                                "OR_NO":self.user.generateClient_ORNumber(),
                                "TEST":PT_BOX2.get(),
                                "RESULT":PT_BOX4.get(),
                                "MEDTECH_NAME":self.user.fname+" "+self.user.lname,
                                "PATHOLOGIST":"JERRY C. ABROGUEÑA, MD, FPSP"
                            }
                            doc.render(context)
                            doc.save(Path(__file__).parent/"newDoc.docx")
                            win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)
                            total=self.user.get_test_price(serviceid[0])
                            id=self.user.save_to_summary(total[0],serviceid[0],int(ID_ENTRY.get()))
                            self.user.update_summaryID_test(id,int(ID_ENTRY.get()),serviceid[0])
                            test_id=self.user.get_tests_id(int(ID_ENTRY.get()),serviceid[0])
                            self.user.markTest_as_done(test_id[0])

                            for item in Test_Table.get_children():
                                if Test_Table.item(item)['values'][0]==PT_BOX2.get():
                                    Test_Table.set(item, 'Complete','Done')

                    PT_Button=Button(Miscelaneous_Page,text="Submit",font=("Roboto",10,"bold"),width=10,height=1,borderwidth=5, command=lambda: submit())
                    PT_Button.place(x=1200,y=430)
                
                elif LabTest_Mune.get() == "Urinalysis":
                    Serology_Page.pack_forget()
                    Miscelaneous_Page.pack_forget()
                    CBC_Page.pack_forget()
                    FE_Page.pack_forget()

                    Urinalysis_Page.pack(expand=1,fill=BOTH)

                    Urinalysis_Title = Label(Urinalysis_Page,text=LabTest_Mune.get(),font=("Roboto",20,"bold"))
                    Urinalysis_Title.place(x=570,y=30)

                    UR_Box=Frame(Urinalysis_Page,bg='white')
                    UR_Box.place(x=130,y=90)
                    UR_Column1_BOX= Label(UR_Box,text="COLOR",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column1_BOX.grid(row=0,column=0)
                    UR_Column1_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column1_BOX1.grid(row=0,column=1,padx=1)
                    UR_Column1_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column1_BOX2.grid(row=0,column=2)

                    UR_Column2_BOX= Label(UR_Box,text="CLARITY",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column2_BOX.grid(row=1,column=0)
                    UR_Column2_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column2_BOX1.grid(row=1,column=1,padx=1)
                    UR_Column2_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column2_BOX2.grid(row=1,column=2)

                    UR_Column3_BOX= Label(UR_Box,text="BLOOD",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column3_BOX.grid(row=2,column=0)
                    UR_Column3_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column3_BOX1.grid(row=2,column=1,padx=1)
                    UR_Column3_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column3_BOX2.grid(row=2,column=2)

                    UR_Column4_BOX= Label(UR_Box,text="BILIRUBIN",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column4_BOX.grid(row=4,column=0)
                    UR_Column4_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column4_BOX1.grid(row=4,column=1,padx=1)
                    UR_Column4_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column4_BOX2.grid(row=4,column=2)

                    UR_Column5_BOX= Label(UR_Box,text="LEUKOCYTE",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column5_BOX.grid(row=5,column=0)
                    UR_Column5_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column5_BOX1.grid(row=5,column=1,padx=1)
                    UR_Column5_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column5_BOX2.grid(row=5,column=2)

                    UR_Column6_BOX= Label(UR_Box,text="KETONE",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column6_BOX.grid(row=6,column=0)
                    UR_Column6_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column6_BOX1.grid(row=6,column=1,padx=1)
                    UR_Column6_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column6_BOX2.grid(row=6,column=2)

                    UR_Column7_BOX= Label(UR_Box,text="NITRITE",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column7_BOX.grid(row=7,column=0)
                    UR_Column7_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column7_BOX1.grid(row=7,column=1,padx=1)
                    UR_Column7_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column7_BOX2.grid(row=7,column=2)

                    UR_Column8_BOX= Label(UR_Box,text="PROTEIN",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column8_BOX.grid(row=8,column=0)
                    UR_Column8_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column8_BOX1.grid(row=8,column=1,padx=1)
                    UR_Column8_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column8_BOX2.grid(row=8,column=2)

                    UR_Column9_BOX= Label(UR_Box,text="GLUCOSE",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column9_BOX.grid(row=9,column=0)
                    UR_Column9_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column9_BOX1.grid(row=9,column=1,padx=1)
                    UR_Column9_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column9_BOX2.grid(row=9,column=2)

                    UR_Column10_BOX= Label(UR_Box,text="PH",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column10_BOX.grid(row=10,column=0)
                    UR_Column10_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column10_BOX1.grid(row=10,column=1,padx=1)
                    UR_Column10_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column10_BOX2.grid(row=10,column=2)

                    UR_Column11_BOX= Label(UR_Box,text="SPECIFIC GRAVITY",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column11_BOX.grid(row=11,column=0)
                    UR_Column11_BOX1= Entry(UR_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column11_BOX1.grid(row=11,column=1,padx=1)
                    UR_Column11_BOX2= Label(UR_Box,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column11_BOX2.grid(row=11,column=2)

                    UR_Box_Side=Frame(Urinalysis_Page,bg='white')
                    UR_Box_Side.place(x=650,y=90)

                    UR_Column12_BOX= Label(UR_Box_Side,text="MICROSCOPIC EXAMINATION",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column12_BOX.grid(row=12,column=0)
                    UR_Column12_BOX1= Label(UR_Box_Side,text="RESULT",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column12_BOX1.grid(row=12,column=1,padx=1)
                    UR_Column12_BOX2= Label(UR_Box_Side,text="UNIT",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column12_BOX2.grid(row=12,column=2)

                    UR_Column13_BOX= Label(UR_Box_Side,text="WBC",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column13_BOX.grid(row=13,column=0)
                    UR_Column13_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column13_BOX1.grid(row=13,column=1,padx=1)
                    UR_Column13_BOX2= Label(UR_Box_Side,text="/HPF",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column13_BOX2.grid(row=13,column=2)

                    UR_Column14_BOX= Label(UR_Box_Side,text="RBC",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column14_BOX.grid(row=14,column=0)
                    UR_Column14_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column14_BOX1.grid(row=14,column=1,padx=1)
                    UR_Column14_BOX2= Label(UR_Box_Side,text="/HPF",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column14_BOX2.grid(row=14,column=2)

                    UR_Column15_BOX= Label(UR_Box_Side,text="EPITHELIAL CELLS",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column15_BOX.grid(row=15,column=0)
                    UR_Column15_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column15_BOX1.grid(row=15,column=1,padx=1)
                    UR_Column15_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column15_BOX2.grid(row=15,column=2)

                    UR_Column16_BOX= Label(UR_Box_Side,text="MUCOUS THREADS",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column16_BOX.grid(row=16,column=0)
                    UR_Column16_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column16_BOX1.grid(row=16,column=1,padx=1)
                    UR_Column16_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column16_BOX2.grid(row=16,column=2)

                    UR_Column17_BOX= Label(UR_Box_Side,text="BACTERIA",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column17_BOX.grid(row=17,column=0)
                    UR_Column17_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column17_BOX1.grid(row=17,column=1,padx=1)
                    UR_Column17_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column17_BOX2.grid(row=17,column=2)

                    UR_Column18_BOX= Label(UR_Box_Side,text="A. URATES / PHOSPHATE",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column18_BOX.grid(row=18,column=0)
                    UR_Column18_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column18_BOX1.grid(row=18,column=1,padx=1)
                    UR_Column18_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column18_BOX2.grid(row=18,column=2)

                    UR_Column19_BOX= Label(UR_Box_Side,text="CASTS",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column19_BOX.grid(row=19,column=0)
                    UR_Column19_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column19_BOX1.grid(row=19,column=1,padx=1)
                    UR_Column19_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column19_BOX2.grid(row=19,column=2)

                    UR_Column20_BOX= Label(UR_Box_Side,text="CRYSTALS:",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column20_BOX.grid(row=20,column=0)
                    UR_Column20_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column20_BOX1.grid(row=20,column=1,padx=1)
                    UR_Column20_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column20_BOX2.grid(row=20,column=2)

                    UR_Column21_BOX= Label(UR_Box_Side,text="OTHERS",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column21_BOX.grid(row=21,column=0)
                    UR_Column21_BOX1= Entry(UR_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    UR_Column21_BOX1.grid(row=21,column=1,padx=1)
                    UR_Column21_BOX2= Label(UR_Box_Side,text=" ",width=18,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    UR_Column21_BOX2.grid(row=21,column=2)

                    def submit():
                        client_id=self.user.getClient_name(Name_Entry.get())
                        serviceid=self.user.get_test_id("Urinalysis (Urine Test)")
                        services=self.user.getClientTestRequests(client_id,serviceid)
                        if services is None:
                            messagebox.showerror("Error","This Test was not Requested by the Client")
                        else: 
                            document=Path(__file__).parent / "URINALYSIS_TEMPLATE.docx"
                            doc=DocxTemplate(document)
                                
                            context={
                                "NAME":Name_Entry.get(),
                                "AGE_SEX":AGE_Entry.get()+'/'+Gender_Mune.get(),
                                "DATE":self.test_date,
                                "OR_NO":self.user.generateClient_ORNumber(),

                                "COLOR":UR_Column1_BOX1.get(),
                                "CLARITY":UR_Column2_BOX1.get(),
                                "BLOOD":UR_Column3_BOX1.get(),
                                "BILIRUBIN":UR_Column4_BOX1.get(),
                                "LEUKOCYTE":UR_Column5_BOX1.get(),
                                "KETONE":UR_Column6_BOX1.get(),
                                "NITRITE":UR_Column7_BOX1.get(),
                                "PROTEIN":UR_Column8_BOX1.get(),
                                "GLUCOSE":UR_Column9_BOX1.get(),
                                "PH":UR_Column10_BOX1.get(),
                                "SPECIFIC_GRAVITY":UR_Column11_BOX1.get(),
                                "WBC":UR_Column13_BOX1.get(),
                                "RBC":UR_Column14_BOX1.get(),
                                "EPITHERIAL_CELLS":UR_Column15_BOX1.get(),
                                "MUCOUS_THREADS":UR_Column16_BOX1.get(),
                                "BACTERIA":UR_Column17_BOX1.get(),
                                "PHOSPHATE":UR_Column18_BOX1.get(),
                                "CASTS":UR_Column19_BOX1.get(),
                                "CRYSTALS":UR_Column20_BOX1.get(),
                                "OTHERS":UR_Column21_BOX1.get(),
                                
                                "MEDTECH_NAME":self.user.fname+" "+self.user.lname,
                                "PATHOLOGIST":"JERRY C. ABROGUEÑA, MD, FPSP"
                            }
                            doc.render(context)
                            doc.save(Path(__file__).parent/"newDoc.docx")
                            win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)
                            total=self.user.get_test_price(serviceid[0])
                            id=self.user.save_to_summary(total[0],serviceid[0],client_id[0])
                            self.user.update_summaryID_test(id,client_id[0],serviceid[0])
                            test_id=self.user.get_tests_id(client_id[0],serviceid[0])
                            self.user.markTest_as_done(test_id[0])
                            for item in Test_Table.get_children():
                                if Test_Table.item(item)['values'][0]=="Urinalysis (Urine Test)":
                                    Test_Table.set(item, 'Complete','Done')

                    ST_Button=Button(Urinalysis_Page,text="Submit",font=("Roboto",10,"bold"),width=10,height=1,borderwidth=5,command=submit)
                    ST_Button.place(x=1200,y=430)
                
                elif LabTest_Mune.get() == "Complete Blood Count / Hematology":
                    Serology_Page.pack_forget()
                    Miscelaneous_Page.pack_forget()
                    Urinalysis_Page.pack_forget()
                    FE_Page.pack_forget()

                    CBC_Page.pack(expand=1,fill=BOTH)
                    CBC_Title = Label(CBC_Page,text=LabTest_Mune.get(),font=("Roboto",20,"bold"))
                    CBC_Title.place(x=400,y=30)

                    CBC_Box=Frame(CBC_Page,bg='white')
                    CBC_Box.place(x=60,y=120)
                    CBC_Column1_BOX= Label(CBC_Box,text="",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column1_BOX.grid(row=0,column=0)
                    CBC_Column1_BOX1= Label(CBC_Box,text="RESULT",width=18,anchor=CENTER,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column1_BOX1.grid(row=0,column=1,padx=1)
                    CBC_Column1_BOX2= Label(CBC_Box,text="NORMAL VALUES",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column1_BOX2.grid(row=0,column=2)

                    CBC_Column2_BOX= Label(CBC_Box,text="WBC",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column2_BOX.grid(row=1,column=0)
                    CBC_Column2_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column2_BOX1.grid(row=1,column=1,padx=1)
                    CBC_Column2_BOX2= Label(CBC_Box,text="5,000 - 10,000 / CUMM",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column2_BOX2.grid(row=1,column=2)

                    CBC_Column3_BOX= Label(CBC_Box,text="RBC",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column3_BOX.grid(row=2,column=0)
                    CBC_Column3_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column3_BOX1.grid(row=2,column=1,padx=1)
                    CBC_Column3_BOX2= Label(CBC_Box,text="F: 3.8 - 5.1 10^ uL ; M: 4.20 - 5.6 10^ uL",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column3_BOX2.grid(row=2,column=2)

                    CBC_Column4_BOX= Label(CBC_Box,text="HEMOGLOBIN",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column4_BOX.grid(row=4,column=0)
                    CBC_Column4_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column4_BOX1.grid(row=4,column=1,padx=1)
                    CBC_Column4_BOX2= Label(CBC_Box,text="F: 11.70 - 14.5g/dL ; M: 13.7 - 16.7g/dL",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column4_BOX2.grid(row=4,column=2)

                    CBC_Column5_BOX= Label(CBC_Box,text="HEMATOCRIT",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column5_BOX.grid(row=5,column=0)
                    CBC_Column5_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column5_BOX1.grid(row=5,column=1,padx=1)
                    CBC_Column5_BOX2= Label(CBC_Box,text="F: 34.1  - 44.3vol% ; M: 13.7 - 49.7 vol%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column5_BOX2.grid(row=5,column=2)

                    CBC_Column6_BOX= Label(CBC_Box,text="MCV",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column6_BOX.grid(row=6,column=0)
                    CBC_Column6_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column6_BOX1.grid(row=6,column=1,padx=1)
                    CBC_Column6_BOX2= Label(CBC_Box,text="80-100 El",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column6_BOX2.grid(row=6,column=2)

                    CBC_Column7_BOX= Label(CBC_Box,text="MCH",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column7_BOX.grid(row=7,column=0)
                    CBC_Column7_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column7_BOX1.grid(row=7,column=1,padx=1)
                    CBC_Column7_BOX2= Label(CBC_Box,text="29 + 2 pg",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column7_BOX2.grid(row=7,column=2)

                    CBC_Column8_BOX= Label(CBC_Box,text="MCHC",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column8_BOX.grid(row=8,column=0)
                    CBC_Column8_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column8_BOX1.grid(row=8,column=1,padx=1)
                    CBC_Column8_BOX2= Label(CBC_Box,text="33.4-35.5 g/dL",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column8_BOX2.grid(row=8,column=2)

                    CBC_Column9_BOX= Label(CBC_Box,text="RDW",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column9_BOX.grid(row=9,column=0)
                    CBC_Column9_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column9_BOX1.grid(row=9,column=1,padx=1)
                    CBC_Column9_BOX2= Label(CBC_Box,text="12% to 15%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column9_BOX2.grid(row=9,column=2)

                    CBC_Column10_BOX= Label(CBC_Box,text="PLATELET",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column10_BOX.grid(row=10,column=0)
                    CBC_Column10_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column10_BOX1.grid(row=10,column=1,padx=1)
                    CBC_Column10_BOX2= Label(CBC_Box,text="150,000 - 450,000 uL",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column10_BOX2.grid(row=10,column=2)

                    CBC_Column11_BOX= Label(CBC_Box,text="MPV",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column11_BOX.grid(row=11,column=0)
                    CBC_Column11_BOX1= Entry(CBC_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBC_Column11_BOX1.grid(row=11,column=1,padx=1)
                    CBC_Column11_BOX2= Label(CBC_Box,text="8.9 - 11.8 fL",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBC_Column11_BOX2.grid(row=11,column=2)


                    #SIDE 
                    CBC_Box_Side=Frame(CBC_Page,bg='white')
                    CBC_Box_Side.place(x=700,y=120)
                    CBCS_Column1_BOX= Label(CBC_Box_Side,text="DIFFERENTIAL COUNT",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column1_BOX.grid(row=0,column=0)
                    CBCS_Column1_BOX1= Label(CBC_Box_Side,text="",width=18,anchor=CENTER,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column1_BOX1.grid(row=0,column=1,padx=1)
                    CBCS_Column1_BOX2= Label(CBC_Box_Side,text="",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column1_BOX2.grid(row=0,column=2)

                    CBCS_Column2_BOX= Label(CBC_Box_Side,text="NEUTROPHIL",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column2_BOX.grid(row=1,column=0)
                    CBCS_Column2_BOX1= Entry(CBC_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBCS_Column2_BOX1.grid(row=1,column=1,padx=1)
                    CBCS_Column2_BOX2= Label(CBC_Box_Side,text="45%"+" - "+"70%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column2_BOX2.grid(row=1,column=2)

                    CBCS_Column3_BOX= Label(CBC_Box_Side,text="LYMPHOCYTE",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column3_BOX.grid(row=2,column=0)
                    CBCS_Column3_BOX1= Entry(CBC_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBCS_Column3_BOX1.grid(row=2,column=1,padx=1)
                    CBCS_Column3_BOX2= Label(CBC_Box_Side,text="18%"+" - ""45%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column3_BOX2.grid(row=2,column=2)

                    CBCS_Column4_BOX= Label(CBC_Box_Side,text="MONOCYTE",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column4_BOX.grid(row=4,column=0)
                    CBCS_Column4_BOX1= Entry(CBC_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBCS_Column4_BOX1.grid(row=4,column=1,padx=1)
                    CBCS_Column4_BOX2= Label(CBC_Box_Side,text="4% "+" - "+"8%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column4_BOX2.grid(row=4,column=2)

                    CBCS_Column5_BOX= Label(CBC_Box_Side,text="EOSINOPHIL",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column5_BOX.grid(row=5,column=0)
                    CBCS_Column5_BOX1= Entry(CBC_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBCS_Column5_BOX1.grid(row=5,column=1,padx=1)
                    CBCS_Column5_BOX2= Label(CBC_Box_Side,text="2% "+" - "+"3%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column5_BOX2.grid(row=5,column=2)

                    CBCS_Column6_BOX= Label(CBC_Box_Side,text="BASOPHIL",width=20,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column6_BOX.grid(row=6,column=0)
                    CBCS_Column6_BOX1= Entry(CBC_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBCS_Column6_BOX1.grid(row=6,column=1,padx=1)
                    CBCS_Column6_BOX2= Label(CBC_Box_Side,text="0% "+" - "+"2%",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column6_BOX2.grid(row=6,column=2)

                    CBCS_Column7_BOX= Label(CBC_Box_Side,text="TOTAL:",width=20,anchor=E,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column7_BOX.grid(row=7,column=0)
                    CBCS_Column7_BOX1= Entry(CBC_Box_Side,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    CBCS_Column7_BOX1.grid(row=7,column=1,padx=1)
                    CBCS_Column7_BOX2= Label(CBC_Box_Side,text="",width=33,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    CBCS_Column7_BOX2.grid(row=7,column=2)

                    def submit():
                        serviceid=self.user.get_test_id("Complete Blood Count")
                        client_id=self.user.getClient_name(Name_Entry.get())
                        services=self.user.getClientTestRequests(client_id,serviceid)
                        if services is None:
                            messagebox.showerror("Error","This Test was not Requested by the Client")
                        else: 
                            document=Path(__file__).parent / "HEMATOLOGY COMPLETE BLOOD COUNT.docx"
                            doc=DocxTemplate(document)
                                
                            context={
                                "NAME":Name_Entry.get(),
                                "AGE_SEX":AGE_Entry.get()+'/'+Gender_Mune.get(),
                                "DATE":self.test_date,
                                "OR_NUM":self.user.generateClient_ORNumber(),
                                "WBC":CBC_Column2_BOX1.get(),
                                "RBC":CBC_Column3_BOX1.get(),
                                "HEMOGLOBIN":CBC_Column4_BOX1.get(),
                                "HEMATOCRIT":CBC_Column5_BOX1.get(),
                                "MCV":CBC_Column6_BOX1.get(),
                                "MCH":CBC_Column7_BOX1.get(),
                                "MCHC":CBC_Column8_BOX1.get(),
                                "RDW":CBC_Column9_BOX1.get(),
                                "PLATELET":CBC_Column10_BOX1.get(),
                                "MPV":CBC_Column11_BOX1.get(),
                                "NEUTROPHIL":CBCS_Column2_BOX1.get(),
                                "LYMPHOCYTE":CBCS_Column3_BOX1.get(),
                                "MONOCYTE":CBCS_Column4_BOX1.get(),
                                "EOSINOPHIL":CBCS_Column5_BOX1.get(),
                                "BASOPHIL":CBCS_Column6_BOX1.get(),
                                "TOTAL":CBCS_Column7_BOX1.get(),
                                "MEDTECH_NAME":self.user.fname+" "+self.user.lname,
                                "LICENSE_NO":self.user.license_no,
                                "PATHOLOGIST":"JERRY C. ABROGUEÑA, MD, FPSP"
                            }
                            doc.render(context)
                            doc.save(Path(__file__).parent/"newDoc.docx")
                            win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)
                            total=self.user.get_test_price(serviceid[0])
                            id=self.user.save_to_summary(total[0],serviceid[0],client_id[0])
                            self.user.update_summaryID_test(id,client_id[0],serviceid[0])
                            test_id=self.user.get_tests_id(client_id[0],serviceid[0])
                            self.user.markTest_as_done(test_id[0])
                            for item in Test_Table.get_children():
                                if Test_Table.item(item)['values'][0]=="Complete Blood Count":
                                    Test_Table.set(item, 'Complete','Done')

                    CBC_Button=Button(CBC_Page,text="Submit",font=("Roboto",10,"bold"),width=10,height=1,borderwidth=5,command=submit)
                    CBC_Button.place(x=1200,y=430)
                
                elif LabTest_Mune.get() == "FECALYSIS":
                    Serology_Page.pack_forget()
                    Miscelaneous_Page.pack_forget()
                    Urinalysis_Page.pack_forget()

                    FE_Page.pack(expand=1,fill=BOTH)
                    FE_Title = Label(FE_Page,text=LabTest_Mune.get(),font=("Roboto",20,"bold"))
                    FE_Title.place(x=550,y=30)

                    FE_Box=Frame(FE_Page,bg='white')
                    FE_Box.place(x=450,y=100)
                    FE_Column1_BOX= Label(FE_Box,text="COLOR",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column1_BOX.grid(row=0,column=0)
                    FE_Column1_BOX1=Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column1_BOX1.grid(row=0,column=1,padx=1)

                    FE_Column2_BOX= Label(FE_Box,text="CONSISTENCY",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column2_BOX.grid(row=1,column=0)
                    FE_Column2_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column2_BOX1.grid(row=1,column=1,padx=1)

                    FE_Column3_BOX= Label(FE_Box,text="MICROSCOPIC EXAMINATION",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column3_BOX.grid(row=2,column=0)
                    FE_Column3_BOX1= Label(FE_Box,text="RESULT",width=18,anchor=CENTER,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column3_BOX1.grid(row=2,column=1,padx=1)

                    FE_Column4_BOX= Label(FE_Box,text="WBC",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column4_BOX.grid(row=4,column=0)
                    FE_Column4_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column4_BOX1.grid(row=4,column=1,padx=1)

                    FE_Column5_BOX= Label(FE_Box,text="RBC",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column5_BOX.grid(row=5,column=0)
                    FE_Column5_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column5_BOX1.grid(row=5,column=1,padx=1)

                    FE_Column6_BOX= Label(FE_Box,text="BACTERIA",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column6_BOX.grid(row=6,column=0)
                    FE_Column6_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column6_BOX1.grid(row=6,column=1,padx=1)

                    FE_Column7_BOX= Label(FE_Box,text="FAT GLOBULES",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column7_BOX.grid(row=7,column=0)
                    FE_Column7_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column7_BOX1.grid(row=7,column=1,padx=1)

                    FE_Column8_BOX= Label(FE_Box,text="OVA OR PARASITE",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column8_BOX.grid(row=8,column=0)
                    FE_Column8_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column8_BOX1.grid(row=8,column=1,padx=1)

                    FE_Column9_BOX= Label(FE_Box,text="E. Histolytica CYST",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column9_BOX.grid(row=9,column=0)
                    FE_Column9_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column9_BOX1.grid(row=9,column=1,padx=1)

                    FE_Column10_BOX= Label(FE_Box,text="E. coli CYST",width=25,anchor=W,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1)
                    FE_Column10_BOX.grid(row=10,column=0)
                    FE_Column10_BOX1= Entry(FE_Box,width=20,font=("Roboto",10,"bold"),highlightbackground="black",highlightthickness=1,borderwidth=3)
                    FE_Column10_BOX1.grid(row=10,column=1,padx=1)

                    def submit():
                        serviceid=self.user.get_test_id("Fecalysis")
                        client_id=self.user.getClient_name(Name_Entry.get())
                        services=self.user.getClientTestRequests(client_id,serviceid)
                        if services is None:
                            messagebox.showerror("Error","This Test was not Requested by the Client")
                        else: 
                            document=Path(__file__).parent / "FECALYSIS.docx"
                            doc=DocxTemplate(document)
                                
                            context={
                                "NAME":Name_Entry.get(),
                                "AGE_SEX":AGE_Entry.get()+'/'+Gender_Mune.get(),
                                "DATE":self.test_date,
                                "OR_NO":self.user.generateClient_ORNumber(),

                                "COLOR":FE_Column1_BOX1.get(),
                                "CONSISTENCY":FE_Column2_BOX1.get(),
                                "WBC": FE_Column4_BOX1.get(),
                                "RBC":FE_Column5_BOX1.get(),
                                "BACTERIA":FE_Column6_BOX1.get(),
                                "FAT_GLOBULES":FE_Column7_BOX1.get(),
                                "OVA_PARASITE":FE_Column8_BOX1.get(),
                                "E_HISTOLYTICA":FE_Column9_BOX1.get(),
                                "E_COLI":FE_Column10_BOX1.get(),

                                "MEDTECH":self.user.fname+" "+self.user.lname,
                                "PATHOLOGIST":"JERRY C. ABROGUEÑA, MD, FPSP"
                            }
                            doc.render(context)
                            doc.save(Path(__file__).parent/"newDoc.docx")
                            win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)
                            total=self.user.get_test_price(serviceid[0])
                            id=self.user.save_to_summary(total[0],serviceid[0],client_id[0])
                            self.user.update_summaryID_test(id,client_id[0],serviceid[0])
                            test_id=self.user.get_tests_id(client_id[0],serviceid[0])
                            self.user.markTest_as_done(test_id[0])
                            for item in Test_Table.get_children():
                                if Test_Table.item(item)['values'][0]=="Fecalysis":
                                    Test_Table.set(item, 'Complete','Done')

                    FE_Button=Button(FE_Page,text="Submit",font=("Roboto",10,"bold"),width=10,height=1,borderwidth=5, command=submit)
                    FE_Button.place(x=1200,y=430)



            Test_Label=Label(Frame_Test,text="TEST:",font='Roboto 12 bold').place(x=1075,y=3)
            LabTest_Mune=ttk.Combobox(Frame_Test,value=Test,font='Roboto 12',state='readonly')
            # LabTest_Mune.set("Serology")
            LabTest_Mune.bind("<<ComboboxSelected>>",Option_TEST)
            LabTest_Mune.place(x=1130,y=3)

            Contener = Frame(Frame_Test,highlightbackground="white",highlightthickness=5)
            Contener.place(x=0,y=31,relwidth=1.0,relheight=0.95)

            #List Frame of the Test
            Serology_Page = Frame(Contener)
            Serology_Page.pack(expand=1,fill=BOTH)
            Miscelaneous_Page = Frame(Contener)
            Urinalysis_Page= Frame(Contener)
            CBC_Page= Frame(Contener)
            FE_Page = Frame(Contener)

#Laboratory-END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Close_Plus_Finding(self):
        global PageOpen
        if messagebox.askokcancel('Close', 'Are you sure you want to close the Window all the data will not be Save?'):
            PageOpen=1
            self.Plus_Finding_Page.destroy()

    def Plus_Finding(self):
        global PageOpen
        if PageOpen < 2:
            self.Plus_Finding_Page=Toplevel()
            self.Plus_Finding_Page.title("Add Finding For X-Ray")
            Plus_Finding_width=600
            Plus_Finding_height=600
            self.Plus_Finding_Page.geometry(f'{Plus_Finding_width}x{Plus_Finding_height}+{400}+{80}')
            self.Plus_Finding_Page.protocol("WM_DELETE_WINDOW",self.Close_Plus_Finding)
            self.Plus_Finding_Page.resizable(False,False)

            Plus_Body=Frame(self.Plus_Finding_Page)
            Plus_Body.pack(expand=1,fill=BOTH)
            Plus_Title=Label(Plus_Body,text="ADD Finding",font=("Roboto",35,"bold")).place(x=5,y=10)

            Plus_Name=Label(Plus_Body,text="NAME:",font=("Roboto",12,"bold")).place(x=5,y=140)
            Plus_Name_Entry=Entry(Plus_Body,font=("Roboto",12),borderwidth=5)
            Plus_Name_Entry.place(x=65,y=137,relwidth=0.7)

            Label_Plus_Body=Label(Plus_Body,text="FINDING BODY:",font=("Roboto 15 bold"))
            Label_Plus_Body.place(x=5,y=170)
            Plus_Body_Text=Frame(Plus_Body,width=550,height=600,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            Plus_Body_Text.place(x=0,y=200)
            Plus__scroll=Scrollbar(Plus_Body_Text,orient='vertical')
            Plus__scroll.pack(side=RIGHT,fill='y')
            Plus__BOX = Text(Plus_Body_Text,width = 70,height = 19,borderwidth=5,font=("Roboto 11 "),yscrollcommand=Plus__scroll.set)
            Plus__scroll.config(command=Plus__BOX.yview)
            Plus__BOX.pack()

            def addFinding():
                self.user.addXrayFinding(Plus_Name_Entry.get(),Plus__BOX.get("1.0", "end-1c"))

            Plus_ADD_button=Button(Plus_Body,text="ADD",font=("Roboto 10"),width=5,borderwidth=5,command=addFinding)
            Plus_ADD_button.place(x=450,y=560)
           
            Plus_Cancel_button=Button(Plus_Body,text="Cancel",font=("Roboto 10"),width=5,borderwidth=5,command=lambda:self.Plus_Finding_Page.destroy())
            Plus_Cancel_button.place(x=520,y=560)

            PageOpen += 1
        else:
            messagebox.showinfo("Error","The Window is already Open!")

#X_Ray Laboratory>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def X_Ray(self):
        if self.user.return_dept()!='Imaging Center':
            messagebox.showerror("Access Denied","Only Employees from Imaging Center or Users with Administrative Access can Access this Page")
        else: 
            global title, body
            def Home():
                Page_XRAY.destroy()
                self.Page_Dashboard.pack()

            self.Page_Dashboard.forget()
            Page_XRAY=Frame(self.Dashboard_GUI,bg="green")
            Page_XRAY.pack(expand=1, fill=BOTH)
            Frame_Header=Frame(Page_XRAY,width=1360,height=50,bg='#BDFFC4',highlightbackground="black",highlightthickness=1)
            Frame_Header.pack()
            image3 = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((40, 40)))
            IMG_HEADER_Xray=Label(Frame_Header,image=image3,bg='#BDFFC4',width=40,height=40)
            IMG_HEADER_Xray.image=image3
            IMG_HEADER_Xray.place(x=3,y=1)
            HEADER_TITLE=Label(Frame_Header,text="City Health Office",bg='#BDFFC4',font='Roboto 20 bold').place(x=50,y=8)

            HEADER_USERNAME=Label(Frame_Header,text=str(self.user.username),bg='#BDFFC4',font='Roboto 20 ').place(x=1150,y=5)
            # IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
            # IMG_USERNAME.place(x=1200,y=8)

            Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
            Toggle_Button.place(x=1290,y=10)
            Toggle_Button.menu=Menu(Toggle_Button)
            Toggle_Button["menu"]=Toggle_Button.menu

            Toggle_Button.menu.add_command(label="Home",font='Roboto 12',command=Home)
            Toggle_Button.menu.add_command(label="Logout",font='Roboto 12',command=lambda:self.logout())
            #Header-------
            #BODY >> Laboratory
            Detail_Body=Frame(Page_XRAY,width=300)
            Detail_Body.pack(expand=1,fill=BOTH,side=LEFT)
            
            XRAY_Title=Label(Detail_Body,text="X-Ray Laboratory Test",font='Roboto 40 bold')
            XRAY_Title.place(x=10,y=15) 

            def setValue(event):
                global client_id, test_id
                res=self.user.getClient_name_Xray(Name_Entry.get())
                test_id=res[-1]
                Name_Entry.set(res[1])
                Birth_Entry.set_date(res[4])
                age.set(res[2])
                Gender_Mune.set(res[3])
                client_id=res[0]


            name=StringVar()
            Label(Detail_Body,text="Name: ",font='Roboto 12').place(x=100,y=130)
            # Name_Entry=Entry(Detail_Body,width=50,textvariable=name,borderwidth=3,font='Roboto 9')
            Name_Entry=ttk.Combobox(Detail_Body,textvariable=name,font='Roboto 9',width=48,state='readonly')
            result=self.user.getClients_Xray()
            n=1
            Name_Entry['values']=[x[n] for x in result]
            Name_Entry.place(x=160,y=130)
            Name_Entry.bind('<<ComboboxSelected>>', setValue)

            Birth_Label=Label(Detail_Body,text="Birthdate:",font="Roboto 12").place(x=100,y=160)
            Birth_Entry=DateEntry(Detail_Body,width=36,backgroud="magenta3",foreground="White",font="Roboto 12",bd=2,archor=W)
            Birth_Entry.place(x=170,y=160)

            age=StringVar()
            AGE_Label=Label(Detail_Body,text="Age: ",font='Roboto 12').place(x=100,y=190)
            AGE_Entry=Entry(Detail_Body,width=50,textvariable=age,font='Roboto 9',borderwidth=3)
            AGE_Entry.place(x=160,y=190)

            def Gender_Click():
                Genderlabel=Label(Detail_Body,Gender_Mune.get(),font="Roboto 12 bold")

            Gender_Label=Label(Detail_Body,text="Gender:",font='Roboto 12 ').place(x=100,y=220)
            Option=["Male","Female","Other"]
            Gender_Mune=ttk.Combobox(Detail_Body,value=Option,font='Roboto 12',width=37,state='readonly')
            Gender_Mune.set("Select Gender")
            Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
            Gender_Mune.place(x=160,y=220)

            # Date_Label=Label(Detail_Body,text="Date:",font="Roboto 12").place(x=100,y=250)
            # Date_Entry=DateEntry(Detail_Body,width=37,backgroud="magenta3",foreground="White",font="Roboto 12",bd=2,archor=W)
            # Date_Entry.place(x=160,y=250)

            Label_Finding=Label(Detail_Body,text="Finding:",font=("Roboto 20 bold"))
            Label_Finding.place(x=60,y=305)

            FindBody=Frame(Detail_Body,width=550,height=200,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            FindBody.place(x=60,y=340)
            Find_scroll=Scrollbar(FindBody,orient='vertical')
            Find_scroll.pack(side=RIGHT,fill='y')
            Finding_BOX = Text(FindBody, height = 9, width = 70,borderwidth=5,font=("Roboto 11 "),yscrollcommand=Find_scroll.set)
            Find_scroll.config(command=Finding_BOX.yview)
            Finding_BOX.pack()

            Label_IMPRESSIONSBody=Label(Detail_Body,text="Impression:",font=("Roboto 20 bold"))
            Label_IMPRESSIONSBody.place(x=60,y=530)
            IMPRESSIONSBody=Frame(Detail_Body,width=550,height=200,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            IMPRESSIONSBody.place(x=60,y=570)
            IMPRESSIONS_scroll=Scrollbar(IMPRESSIONSBody,orient='vertical')
            IMPRESSIONS_scroll.pack(side=RIGHT,fill='y')
            IMPRESSIONS_BOX = Text(IMPRESSIONSBody, height = 5, width = 70,borderwidth=5,font=("Roboto 11 "),yscrollcommand=IMPRESSIONS_scroll.set)
            IMPRESSIONS_scroll.config(command=IMPRESSIONS_BOX.yview)
            IMPRESSIONS_BOX.pack()

            def FIND_Click(event):
                chosen_finding_title=FINDING_Mune.get()
                findings=self.user.getXrayFindingDetails(chosen_finding_title)
                title=findings[0]
                body=findings[1]
                # print(title,body)
                Finding_BOX.insert("1.0",body)

            opts=self.user.getAllXrayFinding()
            n=2
            if opts is not None:
                Option=[x[n] for x in opts]
            # Option=["Normal","Chest PA"]
            FINDING_Mune=ttk.Combobox(Detail_Body,value=Option,font='Roboto 12',width=20)
            FINDING_Mune.set("Select FINDING")
            FINDING_Mune.bind("<<ComboboxSelected>>",FIND_Click)
            FINDING_Mune.place(x=449,y=310)

            Find_ADD=Button(Detail_Body,text="+",font='Roboto 10 bold',width=2,height=1,command=self.Plus_Finding)
            Find_ADD.place(x=420,y=309)

            Img_Body=Frame(Page_XRAY,width=300)
            Img_Body.pack(expand=1,fill=BOTH,side=RIGHT)

            Image_Box=Frame(Img_Body,width=300,height=390,bg="green",highlightbackground="black",highlightthickness=2)
            Image_Box.place(x=210,y=20)

            Image_upload=Label(Image_Box,width=40,height=25,borderwidth=2,padx=2,pady=2)
            Image_upload.place()

            Upload_button=Button(Image_Box,text="Upload the X-Ray",command=lambda:open_file(),width=41,height=25,borderwidth=2)
            Upload_button.place(x=0,y=0)

            def open_file():
                global img, filepath
                f_types = [('Jpg Files', '*.jpg')]
                filepath = filedialog.askopenfilename(filetypes=f_types)
                img=Image.open(filepath)
                img_resized=img.resize((285,375)) 
                img=ImageTk.PhotoImage(img_resized)
                b2 =Button(Image_Box,image=img,borderwidth=5,command=open_file) 
                b2.place(x=0,y=0)
            
            def submit():
                if name.get() =="":
                    messagebox.showerror("Error","Select a Client First")
                else:
                    if Finding_BOX.get("1.0","end-1c")=="" and IMPRESSIONS_BOX.get("1.0","end-1c")=="" and 'filepath' not in globals():
                        messagebox.showerror("Error","Empty Finding, Impression and Xray Box")
                    elif Finding_BOX.get("1.0","end-1c")=="": messagebox.showerror("Error","Empty Finding Box")
                    elif IMPRESSIONS_BOX.get("1.0","end-1c")=="": messagebox.showerror("Error","Empty Impression Box")
                    elif filepath is None:messagebox.showerror("Error","Empty Xray Box")
                    else:
                        serviceid=self.user.get_test_id("X-Ray Test")
                        client_id=self.user.getClient_name_Xray(Name_Entry.get())
                        total=self.user.get_test_price(serviceid[0])
                        test_id=self.user.get_tests_id(client_id[0],serviceid[0])

                        document=Path(__file__).parent / "XRAY_TEMPLATE.docx"
                        doc=DocxTemplate(document)

                        image=InlineImage(doc,filepath,width=Inches(3), height=Inches(2.94))
                        context={
                            "NAME":name.get(),
                            "DOB":Birth_Entry.get_date(),
                            "AGE":age.get(),
                            "GENDER":Gender_Mune.get(),
                            "DATE":self.test_date,
                            "ID":client_id,
                            "FINDINGS":Finding_BOX.get("1.0","end-1c"),
                            "IMPRESSION":IMPRESSIONS_BOX.get("1.0","end-1c"),
                            "IMAGE":image,
                            "medtech_name":self.user.fname+" "+self.user.lname
                        }
                        doc.render(context)
                        doc.save(Path(__file__).parent/"newDoc.docx")
                        win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)
                        
                        # self.user.markXray_as_done(test_id)

                        
                        id=self.user.save_to_summary(total[0],serviceid[0],client_id[0])
                        self.user.update_summaryID_test(id,client_id[0],serviceid[0])
                        self.user.markTest_as_done(test_id[0])
                        
            Record_Xray=Button(Img_Body,text="Record",width=10,bg="green",font='Roboto 11',borderwidth=2,command=lambda:self.Record(self.Value_Laboratory[1])).place(x=410,y=630)
            Submit_Xray=Button(Img_Body,text="Submit",width=10,bg="green",font='Roboto 11',borderwidth=2,command=lambda: submit()).place(x=520,y=630)

#X_Ray Laboratory  END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Summary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Summary(self):
        def Home():
            self.Page_Summary.destroy()
            self.Page_Dashboard.pack()

        self.Page_Dashboard.forget()
        self.Page_Summary=Frame(self.Dashboard_GUI,bg="green")
        self.Page_Summary.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(self.Page_Summary,width=1360,height=50,bg='#BDFFC4',highlightbackground="black",highlightthickness=1)
        Frame_Header.pack()
        image2 = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((40, 40)))
        IMG_HEADER_SUM=Label(Frame_Header,image=image2,bg='#BDFFC4',width=40,height=40)
        IMG_HEADER_SUM.image=image2
        IMG_HEADER_SUM.place(x=5,y=1)
        HEADER_TITLE=Label(Frame_Header,text="City Health Office",bg='#BDFFC4',font='Roboto 25 bold').place(x=50,y=1)

        HEADER_USERNAME=Label(Frame_Header,text=str(self.user.username),font='Roboto 20 ',bg='#BDFFC4').place(x=1150,y=5)
        # IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
        # IMG_USERNAME.place(x=1200,y=8)

        Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
        Toggle_Button.place(x=1290,y=10)
        Toggle_Button.menu=Menu(Toggle_Button)
        Toggle_Button["menu"]=Toggle_Button.menu

        Toggle_Button.menu.add_command(label="Home",font='Roboto 12 ',command=Home)
        Toggle_Button.menu.add_command(label="Logout",font='Roboto 12 ',command=lambda:self.logout())
        #Header-------
        #BODY >> Summary

        Frame_SumBody=Frame(self.Page_Summary)
        Frame_SumBody.pack(expand=1,fill=BOTH,side=TOP)
        
        Frame_FilterBody=Frame(Frame_SumBody,height=130,border=2,borderwidth=5,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
        Frame_FilterBody.pack(fill=X)

        FrameIMG1=Frame(Frame_FilterBody,width=110,height=110)
        FrameIMG1.place(x=40,y=0)

        image = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((110, 110)))
        Img1=Label(FrameIMG1,image = image)
        Img1.image=image
        Img1.place(x=0,y=0,width=110, height=110)

        res= self.user.getAllTest()
        Sum_Test=[x[0] for x in res]
        Sum_Test.insert(0,'All')

        Label(Frame_FilterBody,text="Laboratory Test:",font='Roboto 11',).place(x=200,y=12)
        LabTest_Test=ttk.Combobox(Frame_FilterBody,value=Sum_Test,font='Roboto 10',state='readonly',width=30)
        LabTest_Test.set("All")
        LabTest_Test.place(x=310,y=14)

        emp=employee.Employee.getAllEmployees()
        emp_choices=[x[1]+' '+x[2] for x in emp]
        emp_choices.insert(0,'All')

        Label(Frame_FilterBody,text="Medical Technologist",font='Roboto 11',).place(x=200,y=40)
        MidTech_Emp=ttk.Combobox(Frame_FilterBody,value=emp_choices,font='Roboto 10',state='readonly',width=45)
        MidTech_Emp.set("All")
        MidTech_Emp.place(x=203,y=60)

        filter_options=["No Filter","Monthly","Yearly","1st Semi Annual","2nd Semi Annual","1st Quarter","2nd Quarter","3rd Quarter","4th Quarter"]
        Label(Frame_FilterBody,text="Filter By:",font='Roboto 11',).place(x=560,y=12)
        MidTech_Filter=ttk.Combobox(Frame_FilterBody,value=filter_options,font='Roboto 10',state='readonly',width=20)
        MidTech_Filter.set("No Filter")
        MidTech_Filter.place(x=620,y=14)

        global Valuebox, Monthly_year

        Valuebox_V=list(calendar.month_name)
        Valuebox_label=Label(Frame_FilterBody,text="Choose Month:",font='Roboto 11',)

        Valuebox=ttk.Combobox(Frame_FilterBody,value=Valuebox_V,font='Roboto 10',state='readonly',width=20)
        Valuebox.set("Select Month")

        Monthly_yearr=datetime.today().year
        Monthly_years=[Monthly_yearr - i for i in range (6)]
        Monthly_Lyears=Label(Frame_FilterBody,text="Choose Year :",font='Roboto 11')
        Monthly_year=ttk.Combobox(Frame_FilterBody,value=Monthly_years,font='Roboto 10',state='readonly',width=20)
        Monthly_year.set("Select Year")

        Graph_Label=Label(Frame_FilterBody,text="Graph Model:",font='Roboto 11').place(x=850,y=14)
        Graph_Value=["GRAPH BAR","GRAPH PIE"]        
        Graph_Selection=ttk.Combobox(Frame_FilterBody,value=Graph_Value,font='Roboto 10',state='readonly',width=20)
        Graph_Selection.set("Select Graph Model")
        Graph_Selection.place(x=940,y=14)

        def Graph_create():
            Selected_value = Graph_Selection.get()
            if Selected_value== "GRAPH BAR":
                fig, ax = plt.subplots()
                fruits = ['apple', 'blueberry', 'cherry', 'orange']
                counts = [40, 100, 30, 55]
                bar_labels = ['red', 'blue', '_red', 'orange']
                bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
                ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
                ax.set_ylabel('fruit supply')
                ax.set_title('Fruit supply by kind and color')
                ax.legend(title='Fruit color')

                plt.show()

            elif Selected_value== "GRAPH PIE":
                labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
                sizes = [15, 30, 45, 10]
                explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.show()
            
            else:
                messagebox.showerror("Access Denied","Please Select A Graph Model to Use For Data Analyst")

        Graph_button = Button(Frame_FilterBody,text="Create Graph",font='Roboto 7',borderwidth=3,command=Graph_create)
        Graph_button.place(x=1100,y=12)

        global name_Choice,test_choice, filter_choice,filter_date_from,filter_date_to

        name_Choice=None
        test_choice=None
        filter_choice=None
        filter_date_from=None
        filter_date_to=None

        def filter_Option(event):
            global filter_choice
            filter_choice=event.widget.get()
            if event.widget.get() == "No Filter":
                filter_choice=None
            elif event.widget.get()=="Monthly":
                Monthly_months=list(calendar.month_name)
                Valuebox_label.config(text="Choose Month:")
                Valuebox.config(values=Monthly_months)

                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)

                Monthly_Lyears.place(x=750,y=40)
                Monthly_year.place(x=750,y=60)

            elif event.widget.get()=="Yearly":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="Choose Yearly:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)

                Yearly_yearr=datetime.today().year
                Yearly_years=[Yearly_yearr - i for i in range (6)]
                Valuebox.config(values=Yearly_years)
                Valuebox.set('Select Year')

            elif event.widget.get()=="1st Semi Annual":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="1st Semi Annual:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Semi_1=datetime.today().year
                Semi_1_years=[Semi_1 - i for i in range (6)]
                Valuebox.config(values=Semi_1_years)
                Valuebox.set('Select Year')

            elif event.widget.get()=="2nd Semi Annual":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="2nd Semi Annual:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Semi_2=datetime.today().year
                Semi_2_years=[Semi_2 - i for i in range (6)]
                Valuebox.config(values=Semi_2_years)
                Valuebox.set('Select Year')
            
            elif event.widget.get()=="1st Quarter":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="1st Quarter:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_1=datetime.today().year
                Quarter_1_years=[Quarter_1 - i for i in range (6)]
                Valuebox.config(values=Quarter_1_years)
                Valuebox.set('Select Year')

            elif event.widget.get()=="2nd Quarter":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="2nd Quarter:")
                Valuebox.set('Select Year')
                
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_2=datetime.today().year
                Quarter_2_years=[Quarter_2 - i for i in range (6)]
                Valuebox.config(values=Quarter_2_years)
                Valuebox.set('Select Year')

            elif event.widget.get()=="3rd Quarter":
                Valuebox_label.config(text="3rd Quarter:")
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_3=datetime.today().year
                Quarter_3_years=[Quarter_3 - i for i in range (6)]
                Valuebox.config(values=Quarter_3_years)
                Valuebox.set('Select Year')
                
            elif event.widget.get()=="4th Quarter":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="4th Quarter:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_4=datetime.today().year
                Quarter_4_years=[Quarter_4 - i for i in range (6)]
                Valuebox.config(values=Quarter_4_years)
                Valuebox.set('Select Year')
                
        MidTech_Filter.bind("<<ComboboxSelected>>",filter_Option)

        Frame_TableBody=Frame(Frame_SumBody,bg="grey",borderwidth=5,highlightbackground="black",highlightthickness=1)
        Frame_TableBody.pack(expand=1,fill=BOTH)
        Summary_Table=ttk.Treeview(Frame_TableBody)
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        Summary_Table['column']=("ID","NAME","GENDER","TEST","AGE","DATE STARTED","DATE FINISHED","MEDTECH")
        #Column
        Summary_Table.column("#0",width=0,stretch=NO)
        Summary_Table.column("ID",width=50,stretch=NO,anchor=CENTER)
        Summary_Table.column("NAME")
        Summary_Table.column("GENDER")
        Summary_Table.column("TEST",width=200,stretch=NO)
        Summary_Table.column("AGE")
        Summary_Table.column("DATE STARTED",width=100,stretch=NO,anchor=CENTER)
        Summary_Table.column("DATE FINISHED",width=100,stretch=NO,anchor=CENTER)
        Summary_Table.column("MEDTECH")
        #Header
        Summary_Table.heading("#0")
        Summary_Table.heading("ID",text="No")
        Summary_Table.heading("NAME",text="NAME",anchor=W)
        Summary_Table.heading("GENDER",text="Gender",anchor=W)
        Summary_Table.heading("TEST",text="TEST")
        Summary_Table.heading("AGE",text="Age",anchor=W)
        Summary_Table.heading("DATE STARTED",text="DATE STARTED",anchor=W)
        Summary_Table.heading("DATE FINISHED",text="DATE FINISHED",anchor=W)
        Summary_Table.heading("MEDTECH",text="Medical Technologists",anchor=W)
        Summaryscroll=ttk.Scrollbar(Frame_TableBody,orient=VERTICAL,command=Summary_Table.yview)
        Summaryscroll.pack(side=RIGHT,fill=Y)
        Summary_Table.pack(expand=1,fill=BOTH)

        res=self.user.getAllClient_Done()
        count=0
        number=1
        for item in range(len(res)):
            Summary_Table.insert(parent='',index='end',iid=count,value=(number,res[item][1],res[item][2],res[item][3],res[item][4],res[item][5],res[item][6],res[item][7]))
            count+=1
            number+=1


        def LabTest_callback(event):
            global test_choice
            test_choice=event.widget.get()
            
        def nameCallback(event):
            global name_Choice
            name_Choice=event.widget.get()

        LabTest_Test.bind("<<ComboboxSelected>>",LabTest_callback)
        MidTech_Emp.bind("<<ComboboxSelected>>",nameCallback)

        def ApplyFilter():
            months=['January','February',"March","April","May","June","July","August","September","October","November","December"]
            global name_Choice,test_choice,filter_date_from,filter_date_to,filter_choice
            if filter_choice=="Monthly":
                if Valuebox.get()=="Select Month" or Monthly_year.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Month and/or Year is Empty.")
                elif Valuebox.get()!="Select Month" and Valuebox.get() in months:
                    if Valuebox.get()=="January":
                        month_num=1
                    elif Valuebox.get()=="February":
                        month_num=2
                    elif Valuebox.get()=="March":
                        month_num=3
                    elif Valuebox.get()=="April":
                        month_num=4
                    elif Valuebox.get()=="May":
                        month_num=5
                    elif Valuebox.get()=="June":
                        month_num=6
                    elif Valuebox.get()=="July":
                        month_num=7
                    elif Valuebox.get()=="August":
                        month_num=8
                    elif Valuebox.get()=="September":
                        month_num=9
                    elif Valuebox.get()=="October":
                        month_num=10
                    elif Valuebox.get()=="November":
                        month_num=11
                    elif Valuebox.get()=="December":
                        month_num=12

                    filter_date_from_dateObj=date(int(Monthly_year.get()),month_num,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(filter_date_from_dateObj.year, filter_date_from_dateObj.month)
                    day=res[1]
                    filter_date_to=date(int(Monthly_year.get()),month_num,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            elif filter_choice=="Yearly":
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()
            elif filter_choice=="1st Semi Annual": 
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()

                    filter_date_from_dateObj=date(int(year),1,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(int(year), 6)
                    day=res[1]
                    filter_date_to=date(int(year),6,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            elif filter_choice=="2nd Semi Annual": 
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()

                    filter_date_from_dateObj=date(int(year),7,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(int(year), 12)
                    day=res[1]
                    filter_date_to=date(int(year),12,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            elif filter_choice=="1st Quarter":
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()

                    filter_date_from_dateObj=date(int(year),1,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(int(year), 3)
                    day=res[1]
                    filter_date_to=date(int(year),3,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            elif filter_choice=="2nd Quarter":
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()

                    filter_date_from_dateObj=date(int(year),4,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(int(year), 6)
                    day=res[1]
                    filter_date_to=date(int(year),6,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            elif filter_choice=="3rd Quarter":
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()

                    filter_date_from_dateObj=date(int(year),7,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(int(year), 9)
                    day=res[1]
                    filter_date_to=date(int(year),9,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            elif filter_choice=="4th Quarter":
                if Valuebox.get()=="Select Year":
                    messagebox.showerror("No Value Selected", "Year is Empty.")
                elif Valuebox.get()!="Select Year":
                    year=Valuebox.get()

                    filter_date_from_dateObj=date(int(year),10,1)
                    filter_date_from=filter_date_from_dateObj.strftime("%Y-%m-%d")

                    res=calendar.monthrange(int(year), 12)
                    day=res[1]
                    filter_date_to=date(int(year),12,day)
                    filter_date_to=filter_date_to.strftime("%Y-%m-%d")

            if name_Choice is None:
                name_Choice="All"
            if test_choice is None:
                test_choice="All"
            sum=summary_filter.Summary()
            if filter_choice is None and name_Choice!="All" and test_choice!="All" or  filter_choice is None and  name_Choice=="All" and test_choice=="All" or  filter_choice is None and name_Choice=="All" and test_choice!="All" or  filter_choice is None and name_Choice!="All" and test_choice=="All":
                res=sum.filterOut(name_Choice,test_choice)

            elif filter_choice=="Monthly" and name_Choice=="All" and test_choice=="All":
                res=sum.filterMonthly(filter_date_from,filter_date_to)
            elif filter_choice=="Monthly" and name_Choice!="All" and test_choice=="All" or filter_choice=="Monthly" and name_Choice=="All" and test_choice!="All":
                res=sum.filterMonthlyTest(filter_date_from,filter_date_to,name_Choice,test_choice)

            elif filter_choice=="Yearly" and name_Choice!="All" and test_choice=="All" or filter_choice=="Yearly" and name_Choice!="All" and test_choice!="All":
                res=sum.filterYearlyTest(year,name_Choice,test_choice)
            elif filter_choice=="Yearly" and name_Choice=="All" and test_choice=="All":
                res=sum.filterYearly(year)

            elif filter_choice=='1st Semi Annual' and name_Choice=="All" and test_choice=="All" or filter_choice=='2nd Semi Annual' and name_Choice=="All" and test_choice=="All":
                res=sum.filterMonthly(filter_date_from,filter_date_to)
            elif filter_choice == '2nd Semi Annual' and name_Choice!="All" or test_choice!="All" or filter_choice == '2nd Semi Annual' and name_Choice!="All" or test_choice!="All":
                res=sum.filterMonthlyTest(filter_date_from,filter_date_to,name_Choice,test_choice) 

            elif filter_choice=='1st Quarter' and name_Choice=="All" and test_choice=="All" or filter_choice=='1st Quarter' and name_Choice=="All" and test_choice=="All":
                res=sum.filterMonthly(filter_date_from,filter_date_to)
            elif filter_choice == '1st Quarter' and name_Choice!="All" or test_choice!="All" or filter_choice == '1st Quarter' and name_Choice!="All" or test_choice!="All":
                res=sum.filterMonthlyTest(filter_date_from,filter_date_to,name_Choice,test_choice)  

            elif filter_choice=='2nd Quarter' and name_Choice=="All" and test_choice=="All" or filter_choice=='2nd Quarter' and name_Choice=="All" and test_choice=="All":
                res=sum.filterMonthly(filter_date_from,filter_date_to)
            elif filter_choice == '2nd Quarter' and name_Choice!="All" or test_choice!="All" or filter_choice == '2nd Quarter' and name_Choice!="All" or test_choice!="All":
                res=sum.filterMonthlyTest(filter_date_from,filter_date_to,name_Choice,test_choice)  

            elif filter_choice=='3rd Quarter' and name_Choice=="All" and test_choice=="All" or filter_choice=='3rd Quarter' and name_Choice=="All" and test_choice=="All":
                res=sum.filterMonthly(filter_date_from,filter_date_to)
            elif filter_choice == '3rd Quarter' and name_Choice!="All" or test_choice!="All" or filter_choice == '3rd Quarter' and name_Choice!="All" or test_choice!="All":
                res=sum.filterMonthlyTest(filter_date_from,filter_date_to,name_Choice,test_choice)  

            elif filter_choice=='4th Quarter' and name_Choice=="All" and test_choice=="All" or filter_choice=='4th Quarter' and name_Choice=="All" and test_choice=="All":
                res=sum.filterMonthly(filter_date_from,filter_date_to)
            elif filter_choice == '4th Quarter' and name_Choice!="All" or test_choice!="All" or filter_choice == '4th Quarter' and name_Choice!="All" or test_choice!="All":
                res=sum.filterMonthlyTest(filter_date_from,filter_date_to,name_Choice,test_choice) 

            count=0
            number=1
            Summary_Table.delete(*Summary_Table.get_children())
            for item in range(len(res)):
                Summary_Table.insert(parent='',index='end',iid=count,value=(number,res[item][1],res[item][2],res[item][3],res[item][4],res[item][5],res[item][6],res[item][7]))
                count+=1
                number+=1
                
        def PrintResults():
            all_items=Summary_Table.get_children()
            tests={}
            Gender={}
            age={}
            testXMale={}
            testXFemale={}
            testXOther={}
            TestXAge={}

            for item in Summary_Table.get_children():
                itemValues=Summary_Table.item(item)['values']
                
                if itemValues[3] not in tests.keys():
                    tests[itemValues[3]]=1
                elif itemValues[3] in tests.keys():
                    tests[itemValues[3]]+=1

                if itemValues[2] not in tests.keys():
                    Gender[itemValues[2]]=1
                else:
                    Gender[itemValues[2]]+=1

                if itemValues[4] not in age.keys():
                    age[itemValues[4]]=1
                else:
                    age[itemValues[4]]+=1

                if itemValues[3] not in testXMale.keys():
                    if itemValues[2]=="Male":
                        testXMale[itemValues[3]]=1
                else:
                    testXMale[itemValues[3]]+=1
                
                if itemValues[3] not in testXFemale.keys():
                    if itemValues[2]=="Female":
                        testXFemale[itemValues[3]]=1
                else:
                    testXFemale[itemValues[3]]+=1

                if itemValues[3] not in testXOther.keys():
                    if itemValues[2]=="Other":
                        testXOther[itemValues[3]]=1 
                else:
                    testXOther[itemValues[3]]+=1

                # TestXAge[1]=itemValues[0]
                # TestXAge['test']=itemValues[3]
                # TestXAge['age']=itemValues[4]


            fig, ax = plt.subplots()
            ax.bar(tests.keys(), tests.values())
            plt.xlabel("Number of Clients in Each Test")
            xticks = ax.get_xticks()
            ax.set_xticklabels(tests.keys(), fontsize=5)
            plt.savefig('tests.png', dpi=300)

            fig, ax = plt.subplots()
            # ax.bar(Gender.keys(), Gender.values())
            ax.pie(Gender.values(), labels=Gender.keys(), autopct='%1.0f%%')
            plt.savefig('gender.png', dpi=300)

            fig, ax = plt.subplots()
            ax.pie(age.values(), labels=age.keys(), autopct='%1.0f%%')
            plt.savefig('age.png', dpi=300)

            fig, ax = plt.subplots()
            ax.bar(testXMale.keys(),testXMale.values())
            plt.xlabel("Test")
            plt.ylabel("Number of Males")
            xticks = ax.get_xticks()
            ax.set_xticklabels(testXMale.keys(), fontsize=5)
            plt.savefig('testXMale.png', dpi=300)

            fig, ax = plt.subplots()
            ax.bar(testXFemale.keys(),testXFemale.values())
            plt.xlabel("Test")
            plt.ylabel("Number of Females")
            xticks = ax.get_xticks()
            ax.set_xticklabels(testXFemale.keys(), fontsize=5)
            plt.savefig('testXFemale.png', dpi=300)

            fig, ax = plt.subplots()
            ax.bar(testXOther.keys(),testXOther.values())
            plt.xlabel("Test")
            plt.ylabel("Number of 'Other'")
            xticks = ax.get_xticks()
            ax.set_xticklabels(testXOther.keys(), fontsize=5)
            plt.savefig('testXOther.png', dpi=300)
            # print(TestXAge)

            doc = docx.Document("SUMMARY_REPORT_TEMPLATE.docx")
            data=[]
            for i in all_items:
                itemVal=Summary_Table.item(i, "values")
                data.append(itemVal)

            menuTable = doc.add_table(rows=1,cols=6)
            hdr_Cells = menuTable.rows[0].cells
            hdr_Cells[0].text="No"
            hdr_Cells[1].text="Name"
            hdr_Cells[2].text="Test"
            hdr_Cells[3].text="Date Started"
            hdr_Cells[4].text="Date Finished"
            hdr_Cells[5].text="Medical Technologist"

            for no, name,test, dateStart,dateFin,medTech in data:
                row_cell=menuTable.add_row().cells
                row_cell[0].text=str(no)
                row_cell[1].text=name
                row_cell[2].text=test
                row_cell[3].text=dateStart
                row_cell[4].text=dateFin
                row_cell[5].text=medTech

            doc.add_picture('tests.png')
            doc.add_picture('gender.png')
            doc.add_picture('age.png')
            doc.add_picture('testXMale.png')
            doc.add_picture('testXFemale.png')
            doc.add_picture('testXOther.png')

            doc.save("new_document.docx")
            win32api.ShellExecute(0, "print", str(Path(__file__).parent/"new_document.docx"), None, ".", 0)

        Button(Frame_FilterBody,text="Apply Filter",command=lambda: ApplyFilter()).place(x=1000,y=50)
        Button(Frame_FilterBody,text="Print Out Results",command=lambda: PrintResults()).place(x=1100,y=50)

    def onClose(self):
        windll.user32.ShowWindow(h, 9)
        self.Dashboard_GUI.destroy()

    def Cer_onClose(self):
        global PageOpen
        if messagebox.askokcancel('Close', 'Are you sure you want to close the View Page all the data will not be Save?'):
            PageOpen=1
            self.Dashboard_GUI.grab_release()
            self.Certificate.destroy()

    def Certificate_Page(self):
        global PageOpen
        if PageOpen < 2:
            self.Certificate = Toplevel(self.Dashboard_GUI)
            self.Certificate.title("Medical Certificate")
            Record_width=400
            Record_height=400
            self.Certificate.geometry(f'{Record_width}x{Record_height}+{480}+{100}')
            self.Certificate.resizable(False,False)
            self.Certificate.protocol("WM_DELETE_WINDOW", self.Cer_onClose)
            self.Certificate.grab_set()

            Certificate_title=Label(self.Certificate,text="Medical Certificate",font='Roboto 30 bold').place(x=7,y=7)
            res=self.user.getClientsMedCert()
            Patent_Label=Label(self.Certificate,text="Patients",font='Roboto 11').place(x=48,y=130)
            Patent_Value=[x[1] for x in res]        
            Patent_Selection=ttk.Combobox(self.Certificate,value=Patent_Value,font='Roboto 10',state='readonly',width=40)
            Patent_Selection.set("Select Patients")
            Patent_Selection.place(x=50,y=150)

            def setClient(event):
                res=self.user.getClient_name(Patent_Selection.get())
                global name, age, address
                name = res[1]
                age = res[2]
                address = res[5]

            Patent_Selection.bind("<<ComboboxSelected>>",setClient)

            P_lABEL=Label(self.Certificate,text="Please Select the Patients, its Purpose \nand its Validity",font='Roboto 13').place(x=50,y=70)

            PURPOSE_lABEL=Label(self.Certificate,text="Purpose",font='Roboto 11').place(x=48,y=180)
            PURPOSE_ENTRY=Entry(self.Certificate,width=33,borderwidth=3,font='Roboto 12')
            PURPOSE_ENTRY.place(x=50,y=200)

            REMARKS_lABEL=Label(self.Certificate,text="Remarks",font='Roboto 11').place(x=48,y=230)
            REMARKS_ENTRY=Entry(self.Certificate,width=33,borderwidth=3,font='Roboto 12')
            REMARKS_ENTRY.place(x=50,y=250)

            VALID_FROM_LABEL=Label(self.Certificate,text="Valid Until:",font='Roboto 11').place(x=48,y=280)
            VALID_FROM=DateEntry(self.Certificate,width=10,backgroud="magenta3",foreground="White",font="Roboto 12",bd=2,state='readonly')
            VALID_FROM.place(x=50, y=300)



            def submit():
                serviceid=self.user.get_test_id("Medical Certificate")
                client_id=self.user.getClient_name(name)
                amount=self.user.getTestAmount(serviceid)

                document=Path(__file__).parent / "MEDICAL_CERTIFICATE_TEMPLATE.docx"
                doc=DocxTemplate(document)
                                
                context={
                    "DATE_TODAY":self.test_date,
                    "CLIENT_NAME":name,
                    "AGE":age,
                    "CLIENT_ADDRESS":address,
                    "PURPOSE": PURPOSE_ENTRY.get(),
                    "REMARKS": REMARKS_ENTRY.get(),
                    "VALID_UNTIL": str(self.test_date)+'-'+str(VALID_FROM.get_date()),
                    "OR_NUM": self.user.generateClient_ORNumber(),
                    "AMOUNT": amount[0],
        
                    "NAME_OF_DOCTOR":self.user.fname+" "+self.user.lname,
                    "POSITION":self.user.role,
                    "LICENSE_NO": self.user.license_no
                }
                doc.render(context)
                doc.save(Path(__file__).parent/"newDoc.docx")
                win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)

                total=self.user.get_test_price(serviceid[0])
                id=self.user.save_to_summary(total[0],serviceid[0],client_id[0])
                self.user.update_summaryID_test(id,client_id[0],serviceid[0])
                test_id=self.user.get_tests_id(client_id[0],serviceid[0])
                self.user.markTest_as_done(test_id[0])

            Certificate_button=Button(self.Certificate,text="Print Certificate",width=12,height=1,bg="green",borderwidth=5,command=submit).place(x=260,y=350)

            PageOpen += 1

        else:
            messagebox.showinfo("Error","The Window is already Open!")
            
    #Dashboard>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Main_Dashboard(self):   
        self.Dashboard_GUI=Tk()
        self.Dashboard_GUI.title('CITY HEALTH')
        width= self.Dashboard_GUI.winfo_screenwidth()
        height=self.Dashboard_GUI.winfo_screenheight()
        self.Dashboard_GUI.geometry("%dx%d"%(width,height))
        self.Dashboard_GUI.protocol("WM_DELETE_WINDOW", self.onClose)

        self.Page_Dashboard=Frame(self.Dashboard_GUI)
        self.Page_Dashboard.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(self.Page_Dashboard,width=1360,height=50,bg='#BDFFC4',highlightbackground="black",highlightthickness=1)
        Frame_Header.pack()
        image = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((40, 40)))
        IMG_HEADER_MD=Label(Frame_Header,image=image,bg='#BDFFC4',width=40,height=40)
        IMG_HEADER_MD.place(x=3,y=1)
        HEADER_TITLE=Label(Frame_Header,text="City Health Office",bg='#BDFFC4',font='Roboto 25 bold').place(x=50,y=1)

        HEADER_USERNAME=Label(Frame_Header,text=str(self.user.username),bg='#BDFFC4',font='Roboto 20').place(x=1150,y=3)
        # IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
        # IMG_USERNAME.place(x=1200,y=8)

        Toggle_Button=Menubutton(Frame_Header,width=5,text="=",bg="white",highlightbackground="black",highlightthickness=1,justify=RIGHT)
        Toggle_Button.place(x=1290,y=10)
        Toggle_Button.menu=Menu(Toggle_Button)
        Toggle_Button["menu"]=Toggle_Button.menu
        Toggle_Button.menu.add_command(label="LOGOUT",font='Roboto 12 bold',command=lambda:self.logout())
        #Header END------------

        #Message
        Frame_Center=Frame(self.Page_Dashboard,width=1360,height=413,highlightbackground="black",highlightthickness=1)
        Frame_Center.pack()
        VISION=Label(Frame_Center,text="VISSION:",font=("Roboto",20,'bold')).place(x=440,y=20)
        VISION_BODY=Label(Frame_Center,text="CAGAYAN DE ORO CITY HEALTH OFFICE - \nThe nations ideal public health care service provider to ensure healthy and empowered \nCagay-anons",justify=LEFT,font=("Roboto",13)).place(x=480,y=56)
        MISSION=Label(Frame_Center,text="MISSION",justify=LEFT,font=("Roboto",20,'bold')).place(x=440,y=150)
        MISSION_BODY=Label(Frame_Center,text="We, the Health care managers and providers pledge to deliver quality health care through \nregulative, preventive, curative and rehabilitative services. To attain our mission, \nwe subscribed to the following \nValues: \n• Equality / Liberty \n• Knowledge / Insight \n• Self-actualization \n• Service / vocation",justify=LEFT,font=("Roboto",13)).place(x=480,y=186)

        CDOH_LOGO = ImageTk.PhotoImage(Image.open("CHO_LOGO.png").resize((300, 300)))
        CDOH_Label=Label(Frame_Center,image=CDOH_LOGO)
        CDOH_Label.place(x=80,y=50,width=300, height=300)

        
        Certificate=Button(Frame_Center,text="Certificate",font=("Roboto",8,"bold"),width=9,height=1,bg="green",borderwidth=5,command=self.Certificate_Page).place(x=1240,y=370)

        #FrontDesk
        Frame_Laboratory=Frame(self.Page_Dashboard,width=1360,height=290,highlightbackground="black",highlightthickness=1)
        Frame_Laboratory.pack()

        Frame_FrontDesk=Frame(Frame_Laboratory,width=350,height=290,highlightbackground="black",highlightthickness=1)
        Frame_FrontDesk.place(x=0,y=0)
        CHO_F= ImageTk.PhotoImage(Image.open("CHO_Front.jpg").resize((140, 150)))
        CHO_FL=Label(Frame_FrontDesk,image=CHO_F,highlightbackground="black",highlightthickness=1)
        CHO_FL.place(x=80,y=70,width=140, height=150)
        FrontDesk_label=Label(Frame_FrontDesk,text="FRONT DESK",font=("Roboto",30,"bold")).place(x=20,y=10)
        Button_FronDesk=Button(Frame_FrontDesk,text="CHECK HERE",font=("Roboto",8,"bold"),width=9,height=1,bg="green",borderwidth=5,command=self.FrontDesk).place(x=118,y=230)

        #Lab-list
        Frame_LabTest=Frame(Frame_Laboratory,width=660,height=290)
        Frame_LabTest.place(x=350,y=0)
        Frame_LabCH=Frame(Frame_LabTest,width=660,height=145,highlightbackground="black",highlightthickness=1)
        Frame_LabCH.place(x=0,y=0)
        CHO_L= ImageTk.PhotoImage(Image.open("CHO_Lab.jpg").resize((140, 140)))
        CHO_LL=Label(Frame_LabTest,image=CHO_L,highlightbackground="black",highlightthickness=1)
        CHO_LL.place(x=2,y=2,width=140, height=140)
        Laboratory_label=Label(Frame_LabCH,text="LABORATORY TEST",font=("Roboto",30,"bold")).place(x=147,y=5)
        Button_LabCH=Button(Frame_LabCH,text="CHECK HERE",font=("Roboto",8,"bold"),width=9,height=1,bg="green",borderwidth=5,command=self.Laboratory).place(x=570,y=100)

        Frame_XRay=Frame(Frame_LabTest,width=660,height=145,highlightbackground="black",highlightthickness=1)
        Frame_XRay.place(x=0,y=145)
        CHO_X= ImageTk.PhotoImage(Image.open("CHO_Xray.jpg").resize((138, 138)))
        CHO_XL=Label(Frame_XRay,image=CHO_X,highlightbackground="black",highlightthickness=1)
        CHO_XL.place(x=2,y=2,width=138, height=138)
        Xray_label=Label(Frame_XRay,text="X-RAY LABORATORY",font=("Roboto",30,"bold")).place(x=147,y=5)
        Button_XRay=Button(Frame_XRay,text="CHECK HERE",font=("Roboto",8,"bold"),width=9,height=1,bg="green",borderwidth=5,command=self.X_Ray).place(x=570,y=100)

        Frame_Summary=Frame(Frame_Laboratory,width=350,height=290,highlightbackground="black",highlightthickness=1)
        Frame_Summary.place(x=1009,y=0)
        CHO_S= ImageTk.PhotoImage(Image.open("CHO_Summary.jpg").resize((200, 150)))
        CHO_SL=Label(Frame_Summary,image=CHO_S,highlightbackground="black",highlightthickness=1)
        CHO_SL.place(x=60,y=70,width=200, height=150)
        Summary_label=Label(Frame_Summary,text="SUMMARY",font=("Roboto",30,"bold")).place(x=40,y=10)
        Button_Summary=Button(Frame_Summary,text="CHECK HERE",font=("Roboto",8,"bold"),width=9,height=1,bg="green",borderwidth=5,command=self.Summary).place(x=118,y=230)

        self.Dashboard_GUI.mainloop()
    
    def start(self):
        self.Main_Dashboard()