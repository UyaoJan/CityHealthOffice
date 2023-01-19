from tkinter import *
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry
import calendar
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date, datetime
import employee, LoginPage

from pathlib import Path
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Inches

import win32api, os, time
import win32print


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


        self.test_date=date.today()
    
        #Checkbox Def

    def showCheckbox(self):
        chosen_serve=[]
        name=Name_Entry.get()
        age=AGE_Entry.get()
        bdate=Birth_Entry.get_date()
        gender=Gender_Mune.get()
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
        client=(client_id,name,age,gender,bdate,address)
        user=self.user
        user.addNewClient(user, client,chosen_serve,today)

    def logout(self):
        self.Dashboard_GUI.destroy()
        interface=LoginPage.Loginpage()
        interface.start()

    def FrontDesk(self):
        def Home():
            Page_FrontDesk.destroy()
            self.Page_Dashboard.pack()
        self.Page_Dashboard.forget()
        Page_FrontDesk=Frame(self.Dashboard_GUI)
        Page_FrontDesk.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(Page_FrontDesk,width=1360,height=50,highlightbackground="black",highlightthickness=1)
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

        Toggle_Button.menu.add_command(label="HOME",command=Home)
        Toggle_Button.menu.add_command(label="Logout",command=lambda:self.logout())

        #Header-------
        #Body-------
        Frame_Body=Frame(Page_FrontDesk)
        Frame_Body.pack(side=RIGHT)

        Frame_LIST=Frame(Frame_Body,width=680,height=700)
        Frame_LIST.pack(side=LEFT)
        FrontDesk_Title=Label(Frame_Body,text="New Client",font='Arial 75')
        FrontDesk_Title.place(x=20,y=20)
        Box_Title=Label(Frame_Body,text="Laboratory Test List",font='Arial 25')
        Box_Title.place(x=54,y=300)
        self.Box=Frame(Frame_LIST,width=560,height=300,highlightbackground="black",highlightthickness=1)
        self.Box.place(x=50,y=320)
        #checkbox
        
        self.services=[]
        for i in range (15):
            Test=IntVar()
            Test.set(0)
            self.services.append(Test)

        def check(i):
            i.set(1)
        
        Checkbutton(self.Box,text="Complete Blood Count",variable=self.services[0],font='Arial 12 ',command=lambda i=self.services[0]:check(i)).place(x=30,y=50)
        Checkbutton(self.Box,text="Blood Type",variable=self.services[1],font='Arial 12 ',command=lambda i=self.services[1]:check(i)).place(x=30,y=75)
        Checkbutton(self.Box,text="Stool Exam",variable=self.services[2],font='Arial 12 ',command=lambda i=self.services[2]:check(i)).place(x=30,y=100)
        Checkbutton(self.Box,text="Urinalysis (“Urine Test”)",variable=self.services[3],font='Arial 12 ',command=lambda i=self.services[3]:check(i)).place(x=30,y=125)
        Checkbutton(self.Box,text="Syphilis Rapid Test",variable=self.services[4],font='Arial 12 ',command=lambda i=self.services[4]:check(i)).place(x=30,y=150)
        Checkbutton(self.Box,text="Hepatitis B (“Antigen Test”)",variable=self.services[5],font='Arial 12 ',command=lambda i=self.services[5]:check(i)).place(x=30,y=175)
        Checkbutton(self.Box,text="Anti-HAV Test",variable=self.services[6],font='Arial 12 ',command=lambda i=self.services[6]:check(i)).place(x=30,y=200)
        Checkbutton(self.Box,text="Drug Test",variable=self.services[7],font='Arial 12 ',command=lambda i=self.services[7]:check(i)).place(x=30,y=222)
        Checkbutton(self.Box,text="Pregnancy Test",variable=self.services[8],font='Arial 12 ',command=lambda i=self.services[8]:check(i)).place(x=30,y=245)
        Checkbutton(self.Box,text="Fasting Blood Suger Test",variable=self.services[9],font='Arial 12 ',command=lambda i=self.services[9]:check(i)).place(x=280,y=50)
        Checkbutton(self.Box,text="Blood Uric Acid Test",variable=self.services[10],font='Arial 12 ',command=lambda i=self.services[10]:check(i)).place(x=280,y=75)
        Checkbutton(self.Box,text="Blood Cholesterol Test",variable=self.services[11],font='Arial 12 ',command=lambda i=self.services[11]:check(i)).place(x=280,y=100)
        Checkbutton(self.Box,text="Blood Creatinine Test",variable=self.services[12],font='Arial 12 ',command=lambda i=self.services[12]:check(i)).place(x=280,y=125)
        Checkbutton(self.Box,text="Acid Fast Staining",variable=self.services[13],font='Arial 12 ',command=lambda i=self.services[13]:check(i)).place(x=280,y=150)
        Checkbutton(self.Box,text="X-Ray Test",variable=self.services[14],font='Arial 12 ',command=lambda i=self.services[14]:check(i)).place(x=280,y=175)

        #Body-------


        #IMPUT-----------------
        Frame_Input=Frame(Frame_Body,width=680,height=700)
        Frame_Input.pack()

        Img=Label(Frame_Input,width=50,height=20,bg="green").place(x=170,y=40)

        global Name_Entry
        Name_Label=Label(Frame_Input,text="Name: ",font='Arial 12').place(x=46,y=400)
        Name_Entry=Entry(Frame_Input,width=59,borderwidth=3,font='Arial 12')
        Name_Entry.place(x=100,y=400)

        global AGE_Entry
        AGE_Label=Label(Frame_Input,text="Age: ",font='Arial 12').place(x=46,y=430)
        AGE_Entry=Entry(Frame_Input,width=5,font='Arial 12',borderwidth=3)
        AGE_Entry.place(x=100,y=430)

        global Birth_Entry
        Birth_Label=Label(Frame_Input,text="Birthdate:",font="Arial 12").place(x=160,y=430)
        Birth_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='readonly')
        Birth_Entry.place(x=230,y=430)

        global Gender_Mune
        Gender_Label=Label(Frame_Input,text="Gender:",font='Arial 12').place(x=350,y=430)
        Option=["Male","Female","Other"]
        Gender_Mune=ttk.Combobox(Frame_Input,value=Option,font='Arial 12',state='readonly')
        Gender_Mune.current(0)
        Gender_Mune.place(x=412,y=432)

        global Address_Entry,addrs
        addrs=StringVar()
        Address_Label=Label(Frame_Input,text="Address: ",font='Arial 12').place(x=46,y=460)
        Address_Entry=Entry(Frame_Input,textvariable=addrs,width=38,borderwidth=3,font='Arial 12')
        Address_Entry.place(x=120,y=460)

        global Date_Entry
        Date_Label=Label(Frame_Input,text="Date:",font="Arial 12").place(x=480,y=460)
        Date_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W,state='readonly')
        Date_Entry.place(x=525,y=460)

        Submit_Input=Button(Frame_Input,text="Submit",width=10,bg="green",font='Arial 11',command=self.showCheckbox)
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

            Record_search_LB=Label(self.RecordBody,text="SEARCH: ",font='Arial 12 bold').place(x=10,y=100)
            Record_search_EN=Entry(self.RecordBody,font='Arial 12',borderwidth=5)
            Record_search_EN.place(x=90,y=98,relwidth=0.6)
            Record_search_BT=Button(self.RecordBody,text="Search",font='Arial 10',width=6,height=0,borderwidth=5)
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
                    Client_Number=Label(Number_BOX,text=records[i][0],font=("Arial",25,"bold")).place(x=3,y=0)#luna please limit the Number of the of to 3 only

                    Client_Name=Label(Record_Page,text="NAME: "+records[i][1],font=("Arial",12,"bold")).place(x=85,y=10)
                    Client_Test=Label(Record_Page,text="TEST: "+records[i][6],font=("Arial",8,"bold")).place(x=85,y=30)

                    Take_Button=Button(Record_Page,text="Take",font=("Arial",8),width=6,height=0,borderwidth=5)
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
                    XRAY_Client_Number=Label(XRAY_Number_BOX,text=records[i][0],font=("Arial",25,"bold")).place(x=3,y=0)

                    XRAY_Client_Name=Label(X_RAY_Record_Page,text="NAME: "+records[i][1],font=("Arial",12,"bold")).place(x=85,y=10)
                    XRAY_Client_Test=Label(X_RAY_Record_Page,text="TEST: XRAY TEST",font=("Arial",8,"bold")).place(x=85,y=30)

                    XRAY_Take_Button=Button(X_RAY_Record_Page,text="Take",font=("Arial",8),width=6,height=0,borderwidth=5,command=lambda e= records[i][0]:take(e))
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
            Frame_Header=Frame(Page_Laboratory,width=1360,height=50,highlightbackground="black",highlightthickness=1)
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

            Toggle_Button.menu.add_command(label="HOME",command=Home)
            Toggle_Button.menu.add_command(label="Logout",command=lambda:self.logout())
            #Header-------
            #BODY >> Laboratory
            Frame_Body=Frame(Page_Laboratory,width=1360,height=150,highlightbackground="black",highlightthickness=1)
            Frame_Body.pack()

            Labo_Title=Label(Frame_Body,text="Laboratory Test!",font='Arial 20')
            Labo_Title.place(x=10,y=5)
            Name_Label=Label(Frame_Body,text="Name: ",font='Arial 12').place(x=19,y=50)
            # Name_Entry=Entry(Frame_Body,width=59,borderwidth=3,font='Arial 9')
            res=self.user.getClients_all()
            names=[x[1] for x in res]
            Name_Entry=ttk.Combobox(Frame_Body,value=names,font='Arial 12',state='readonly',width=40)
            Name_Entry.place(x=20,y=70)

            def setClient(event):
                res=self.user.getClient_name(Name_Entry.get())
                age=IntVar()
                age.set(res[2])
                
                AGE_Entry.config(textvariable=age)
                Gender_Mune.set(res[3])

            Name_Entry.bind("<<ComboboxSelected>>",setClient)

            AGE_Label=Label(Frame_Body,text="Age: ",font='Arial 12').place(x=400,y=50)
            AGE_Entry=Entry(Frame_Body,width=8,font='Arial 9',borderwidth=3)
            AGE_Entry.place(x=400,y=70)

            # def Gender_Click(event):
            #     Genderlabel=Label(Frame_Body,Gender_Mune.get(),font="Arial 12")

            Gender_Label=Label(Frame_Body,text="Gender:",font='Arial 12').place(x=150,y=100)
            Option=["Male","Female","Other"]
            Gender_Mune=ttk.Combobox(Frame_Body,value=Option,font='Arial 12',state='readonly')
            Gender_Mune.set("Select Gender")
            # Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
            Gender_Mune.place(x=150,y=120)

            Date_Label=Label(Frame_Body,text="Date:",font=("Arial 12")).place(x=20,y=100)
            Date_Entry=DateEntry(Frame_Body,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
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

            Record_Button=Button(Frame_Body,text="Record",bg="green",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda:self.Record(self.Value_Laboratory[0]))
            Record_Button.place(x=1200,y=100)

            #Frame for the Testing 
            Frame_Test=Frame(Page_Laboratory,highlightbackground="black",highlightthickness=1,bg="blue")
            Frame_Test.pack(expand=1,fill=BOTH)

            Test_Label=Label(Frame_Test,text="Laboratory Test",width=123,font="Arial 15",anchor=W,highlightbackground="black",highlightthickness=1)
            Test_Label.place(x=0,y=0)

            Test=[  
                    #"Complete Blood Count",
                    # "Blood Type",
                    # "Stool Exam",
                    "Serology",
                    "Miscelaneous",
                ]

            def Option_TEST(event):
                if LabTest_Mune.get() == "Serology":
                    Miscelaneous_Page.pack_forget()
                    Serology_Page.pack(expand=1,fill=BOTH)

                    Serology_Title = Label(Serology_Page,text="MISCELLANEOUS",font=("Arial",20,"bold"))
                    Serology_Title.place(x=570,y=30)

                    #RIGHT
                    ST_Box=Frame(Serology_Page,bg='white')
                    ST_Box.place(x=380,y=150)
                    ST_BOX1_R= Label(ST_Box,text="",font=("Arial",15,"bold"),width=35,anchor=W)
                    ST_BOX1_R.grid(row=0,column=0)
                    ST_BOX2_R= Label(ST_Box,text="BLOOD TYPE",font=("Arial",15,"bold"),width=35,anchor=W)
                    ST_BOX2_R.grid(row=1,column=0)
                    ST_BOX3_R= Label(ST_Box,text="HEPATITIS B SCREENING (HBsAg)",font=("Arial",15,"bold"),width=35,anchor=W)
                    ST_BOX3_R.grid(row=2,column=0)
                    ST_BOX4_R= Label(ST_Box,text="ANTI-HAV SCREENING (HAV lgG/igM)",font=("Arial",15,"bold"),width=35,anchor=W)
                    ST_BOX4_R.grid(row=3,column=0)
                    ST_BOX5_R= Label(ST_Box,text="SYPHILIS SCREENING",font=("Arial",15,"bold"),width=35,anchor=W)
                    ST_BOX5_R.grid(row=4,column=0)
                    ST_BOX6_R= Label(ST_Box,text="DENGUE NS1 ANTIGEN TEST",font=("Arial",15,"bold"),width=35,anchor=W)
                    ST_BOX6_R.grid(row=5,column=0)
                    
                    #LEFT
                    ST_BOX7_L= Label(ST_Box,text="RESULT",font=("Arial",15,"bold"))
                    ST_BOX7_L.grid(row=0,column=1)
                    ST_BOX8_L= Entry(ST_Box,text="",font=("Arial",15,"bold"),borderwidth=5)
                    ST_BOX8_L.grid(row=1,column=1)
                    ST_BOX9_L= Entry(ST_Box,text="",font=("Arial",15,"bold"),borderwidth=5)
                    ST_BOX9_L.grid(row=2,column=1)
                    ST_BOX10_L= Entry(ST_Box,text="",font=("Arial",15,"bold"),borderwidth=5)
                    ST_BOX10_L.grid(row=3,column=1)
                    ST_BOX11_L= Entry(ST_Box,text="",font=("Arial",15,"bold"),borderwidth=5)
                    ST_BOX11_L.grid(row=4,column=1)
                    ST_BOX12_L= Entry(ST_Box,text="",font=("Arial",15,"bold"),borderwidth=5)
                    ST_BOX12_L.grid(row=5,column=1)

                    def submit():   
                        
                        print(ST_BOX12_L.get()," blood type")
                        # document=Path(__file__).parent / "SEROLOGY_TEMPLATE.docx"
                        # doc=DocxTemplate(document)

                        # context={
                        #     "NAME":Name_Entry.get(),
                        #     "AGE_SEX":AGE_Entry.get()+'/'+Gender_Mune.get(),
                        #     "DATE":self.test_date,
                        #     "OR_NO":self.user.generateClient_ORNumber(),
                            


                        #     "MEDTECH_NAME":self.user.fname+" "+self.user.lname,
                        #     "PATHOLOGIST":"JERRY C. ABROGUEÑA, MD, FPSP"
                        # }
                        # doc.render(context)
                        # doc.save(Path(__file__).parent/"newDoc.docx")
                        # win32api.ShellExecute(0, "print", str(Path(__file__).parent/"newDoc.docx"), None, ".", 0)


                    ST_Button=Button(Serology_Page,text="Submit",font=("Arial",10,"bold"),width=10,height=1,borderwidth=5,command=submit())
                    ST_Button.place(x=1200,y=430)

                elif LabTest_Mune.get() == "Miscelaneous":
                    Serology_Page.pack_forget()
                    Miscelaneous_Page.pack(expand=1,fill=BOTH)

                    Miscelaneous_Title = Label(Miscelaneous_Page,text="MISCELLANEOUS",font=("Arial",20,"bold"))
                    Miscelaneous_Title.place(x=570,y=30)

                    PT_Box=Frame(Miscelaneous_Page,bg='white')
                    PT_Box.place(x=430,y=200)
                    PT_BOX1= Label(PT_Box,text="TEST",width=20,anchor=W,font=("Arial",15,"bold"))
                    PT_BOX1.grid(row=0,column=0)
                    # PT_BOX2= Label(PT_Box,text="PREGNANCY TEST",width=20,anchor=W,font=("Arial",15,"bold"))
                    res=self.user.getAllTest()
                    TEST=[x[0] for x in res]
                    PT_BOX2= ttk.Combobox(PT_Box,value=TEST,font=("Arial",15),state='readonly')
                    PT_BOX2.grid(row=0,column=1)
                    PT_BOX3= Label(PT_Box,text="RESULT",width=20,anchor=W,font=("Arial",15,"bold"))
                    PT_BOX3.grid(row=1,column=0)

                    # PT_Result=["POSITIVE","NEGATIVE"]
                    # PT_BOX4=ttk.Combobox(PT_Box,value=PT_Result,font=("Arial",15),state='readonly')
                    # PT_BOX4.set("Select Result")
                    PT_BOX4=Entry(PT_Box,font=("Arial",12),borderwidth=5)
                    PT_BOX4.grid(row=1,column=1)

                    def submit():
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


                    PT_Button=Button(Miscelaneous_Page,text="Submit",font=("Arial",10,"bold"),width=10,height=1,borderwidth=5, command=lambda: submit())
                    PT_Button.place(x=1200,y=430)


            Test_Label=Label(Frame_Test,text="TEST:",font='Arial 12 bold').place(x=1075,y=3)
            LabTest_Mune=ttk.Combobox(Frame_Test,value=Test,font='Arial 12',state='readonly')
            LabTest_Mune.set("Serology")
            LabTest_Mune.bind("<<ComboboxSelected>>",Option_TEST)
            LabTest_Mune.place(x=1130,y=3)

            Contener = Frame(Frame_Test,highlightbackground="white",highlightthickness=5)
            Contener.place(x=0,y=31,relwidth=1.0,relheight=0.95)

            #List Frame of the Test
            Serology_Page = Frame(Contener)
            Serology_Page.pack(expand=1,fill=BOTH)
            Miscelaneous_Page = Frame(Contener)

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
            Plus_Title=Label(Plus_Body,text="ADD Finding",font=("Arial",35,"bold")).place(x=5,y=10)

            Plus_Name=Label(Plus_Body,text="NAME:",font=("Arial",12,"bold")).place(x=5,y=140)
            Plus_Name_Entry=Entry(Plus_Body,font=("Arail",12),borderwidth=5)
            Plus_Name_Entry.place(x=65,y=137,relwidth=0.7)

            Label_Plus_Body=Label(Plus_Body,text="FINDING BODY:",font=("Arial 15 bold"))
            Label_Plus_Body.place(x=5,y=170)
            Plus_Body_Text=Frame(Plus_Body,width=550,height=600,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            Plus_Body_Text.place(x=0,y=200)
            Plus__scroll=Scrollbar(Plus_Body_Text,orient='vertical')
            Plus__scroll.pack(side=RIGHT,fill='y')
            Plus__BOX = Text(Plus_Body_Text,width = 70,height = 19,borderwidth=5,font=("Arial 11 "),yscrollcommand=Plus__scroll.set)
            Plus__scroll.config(command=Plus__BOX.yview)
            Plus__BOX.pack()

            def addFinding():
                self.user.addXrayFinding(Plus_Name_Entry.get(),Plus__BOX.get("1.0", "end-1c"))

            Plus_ADD_button=Button(Plus_Body,text="ADD",font=("Arail 10"),width=5,borderwidth=5,command=addFinding)
            Plus_ADD_button.place(x=450,y=560)
           
            Plus_Cancel_button=Button(Plus_Body,text="Cancel",font=("Arail 10"),width=5,borderwidth=5,command=lambda:self.Plus_Finding_Page.destroy())
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
            # Page_scroll=Scrollbar(Page_XRAY,orient='vertical')
            # Page_scroll.pack(side=RIGHT,fill='y')
            Frame_Header=Frame(Page_XRAY,width=1360,height=50,highlightbackground="black",highlightthickness=1)
            Frame_Header.pack()
            IMG_HEADER=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
            IMG_HEADER.place(x=10,y=8)
            HEADER_TITLE=Label(Frame_Header,text="City Health Office",font='Arial 20 bold').place(x=50,y=8)

            HEADER_USERNAME=Label(Frame_Header,text="Username:",font='Arial 12 ').place(x=1100,y=10)
            IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
            IMG_USERNAME.place(x=1200,y=8)

            Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
            Toggle_Button.place(x=1290,y=10)
            Toggle_Button.menu=Menu(Toggle_Button)
            Toggle_Button["menu"]=Toggle_Button.menu

            Toggle_Button.menu.add_command(label="HOME",command=Home)
            Toggle_Button.menu.add_command(label="Logout",command=lambda:self.logout())
            #Header-------
            #BODY >> Laboratory
            Detail_Body=Frame(Page_XRAY,width=300)
            Detail_Body.pack(expand=1,fill=BOTH,side=LEFT)
            
            XRAY_Title=Label(Detail_Body,text="X-Ray Laboratory Test",font='Arial 40 bold')
            XRAY_Title.place(x=10,y=15) 

            def setValue(event):
                global client_id
                res=self.user.getClient_name(Name_Entry.get())
                Name_Entry.set(res[1])
                Birth_Entry.set_date(res[4])
                age.set(res[2])
                Gender_Mune.set(res[3])
                client_id=res[0]


            name=StringVar()
            Label(Detail_Body,text="Name: ",font='Arial 12').place(x=100,y=130)
            # Name_Entry=Entry(Detail_Body,width=50,textvariable=name,borderwidth=3,font='Arial 9')
            Name_Entry=ttk.Combobox(Detail_Body,textvariable=name,font='Arial 9',width=48,state='readonly')
            result=self.user.getClients_Xray()
            n=1
            Name_Entry['values']=[x[n] for x in result]
            Name_Entry.place(x=160,y=130)
            Name_Entry.bind('<<ComboboxSelected>>', setValue)

            Birth_Label=Label(Detail_Body,text="Birthdate:",font="Arial 12").place(x=100,y=160)
            Birth_Entry=DateEntry(Detail_Body,width=36,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
            Birth_Entry.place(x=170,y=160)

            age=StringVar()
            AGE_Label=Label(Detail_Body,text="Age: ",font='Arial 12').place(x=100,y=190)
            AGE_Entry=Entry(Detail_Body,width=50,textvariable=age,font='Arial 9',borderwidth=3)
            AGE_Entry.place(x=160,y=190)

            def Gender_Click():
                Genderlabel=Label(Detail_Body,Gender_Mune.get(),font="Arial 12 bold")

            Gender_Label=Label(Detail_Body,text="Gender:",font='Arial 12 ').place(x=100,y=220)
            Option=["Male","Female","Other"]
            Gender_Mune=ttk.Combobox(Detail_Body,value=Option,font='Arial 12',width=37,state='readonly')
            Gender_Mune.set("Select Gender")
            Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
            Gender_Mune.place(x=160,y=220)

            # Date_Label=Label(Detail_Body,text="Date:",font="Arial 12").place(x=100,y=250)
            # Date_Entry=DateEntry(Detail_Body,width=37,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
            # Date_Entry.place(x=160,y=250)

            Label_Finding=Label(Detail_Body,text="Finding:",font=("Arial 20 bold"))
            Label_Finding.place(x=60,y=305)

            FindBody=Frame(Detail_Body,width=550,height=200,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            FindBody.place(x=60,y=340)
            Find_scroll=Scrollbar(FindBody,orient='vertical')
            Find_scroll.pack(side=RIGHT,fill='y')
            Finding_BOX = Text(FindBody, height = 9, width = 70,borderwidth=5,font=("Arial 11 "),yscrollcommand=Find_scroll.set)
            Find_scroll.config(command=Finding_BOX.yview)
            Finding_BOX.pack()

            Label_IMPRESSIONSBody=Label(Detail_Body,text="Impression:",font=("Arial 20 bold"))
            Label_IMPRESSIONSBody.place(x=60,y=530)
            IMPRESSIONSBody=Frame(Detail_Body,width=550,height=200,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            IMPRESSIONSBody.place(x=60,y=570)
            IMPRESSIONS_scroll=Scrollbar(IMPRESSIONSBody,orient='vertical')
            IMPRESSIONS_scroll.pack(side=RIGHT,fill='y')
            IMPRESSIONS_BOX = Text(IMPRESSIONSBody, height = 5, width = 70,borderwidth=5,font=("Arial 11 "),yscrollcommand=IMPRESSIONS_scroll.set)
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
            FINDING_Mune=ttk.Combobox(Detail_Body,value=Option,font='Arial 12',width=20)
            FINDING_Mune.set("Select FINDING")
            FINDING_Mune.bind("<<ComboboxSelected>>",FIND_Click)
            FINDING_Mune.place(x=449,y=310)

            Find_ADD=Button(Detail_Body,text="+",font='Arial 10 bold',width=2,height=1,command=self.Plus_Finding)
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
                        
            CList_Xray=Button(Img_Body,text="Client List",width=10,bg="green",font='Arial 11',command=lambda:self.ClientList(self.Value_Laboratory[1])).place(x=300,y=630)
            Record_Xray=Button(Img_Body,text="Record",width=10,bg="green",font='Arial 11',command=lambda:self.Record(self.Value_Laboratory[1])).place(x=410,y=630)
            Submit_Xray=Button(Img_Body,text="Submit",width=10,bg="green",font='Arial 11',command=lambda: submit()).place(x=520,y=630)

#X_Ray Laboratory  END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Summary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Summary(self):
        def Home():
            self.Page_Summary.destroy()
            self.Page_Dashboard.pack()
        self.Page_Dashboard.forget()
        self.Page_Summary=Frame(self.Dashboard_GUI,bg="green")
        self.Page_Summary.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(self.Page_Summary,width=1360,height=50,highlightbackground="black",highlightthickness=1)
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

        Toggle_Button.menu.add_command(label="HOME",command=Home)
        Toggle_Button.menu.add_command(label="Logout",command=lambda:self.logout())
        #Header-------
        #BODY >> Summary

        Frame_SumBody=Frame(self.Page_Summary)
        Frame_SumBody.pack(expand=1,fill=BOTH,side=TOP)
        
        Frame_FilterBody=Frame(Frame_SumBody,height=130,border=2,borderwidth=5,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
        Frame_FilterBody.pack(fill=X)

        res= self.user.getAllTest()
        Sum_Test=[x[0] for x in res]

        Label(Frame_FilterBody,text="Laboratory Test:",font='Arial 11',).place(x=200,y=12)
        LabTest_Test=ttk.Combobox(Frame_FilterBody,value=Sum_Test,font='Arial 10',state='readonly',width=30)
        LabTest_Test.set("Select Here")
        LabTest_Test.place(x=310,y=14)

        emp=employee.Employee.getAllEmployees()
        emp_choices=[x[1] for x in emp]

        Label(Frame_FilterBody,text="Medical Technologist",font='Arial 11',).place(x=200,y=40)
        MidTech_Emp=ttk.Combobox(Frame_FilterBody,value=emp_choices,font='Arial 10',state='readonly',width=45)
        MidTech_Emp.set("Select Medical Technologist")
        MidTech_Emp.place(x=203,y=60)

        filter_options=["Monthly","Yearly","1st Semi Annual","2nd Semi Annual","1st Quarter","2nd Quarter","3rd Quarter","4th Quarter"]
        Label(Frame_FilterBody,text="Filter By:",font='Arial 11',).place(x=560,y=12)
        MidTech_Filter=ttk.Combobox(Frame_FilterBody,value=filter_options,font='Arial 10',state='readonly',width=20)
        MidTech_Filter.set("Select Filter Option")
        MidTech_Filter.place(x=620,y=14)

        Valuebox_V=list(calendar.month_name)
        Valuebox_label=Label(Frame_FilterBody,text="Choose Month:",font='Arial 11',)

        Valuebox=ttk.Combobox(Frame_FilterBody,value=Valuebox_V,font='Arial 10',state='readonly',width=20)
        Valuebox.set("Select Month")


        Monthly_yearr=datetime.today().year
        Monthly_years=[Monthly_yearr - i for i in range (6)]
        Monthly_Lyears=Label(Frame_FilterBody,text="Choose Year :",font='Arial 11',)
        Monthly_year=ttk.Combobox(Frame_FilterBody,value=Monthly_years,font='Arial 10',state='readonly',width=20)
        Monthly_year.set("Select Year")
       
        

        def filter_Option(event):
            if event.widget.get()=="Monthly":
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

            elif event.widget.get()=="1st Semi Annual":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="1st Semi Annual:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Semi_1=datetime.today().year
                Semi_1_years=[Semi_1 - i for i in range (6)]
                Valuebox.config(values=Semi_1_years)

            elif event.widget.get()=="2nd Semi Annual":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="2nd Semi Annual:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Semi_2=datetime.today().year
                Semi_2_years=[Semi_2 - i for i in range (6)]
                Valuebox.config(values=Semi_2_years)
            
            elif event.widget.get()=="1st Quarter":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="1st Quarter:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_1=datetime.today().year
                Quarter_1_years=[Quarter_1 - i for i in range (6)]
                Valuebox.config(values=Quarter_1_years)

            elif event.widget.get()=="2nd Quarter":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="2nd Quarter:")
                
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_2=datetime.today().year
                Quarter_2_years=[Quarter_2 - i for i in range (6)]
                Valuebox.config(values=Quarter_2_years)

            elif event.widget.get()=="3rd Quarter":
                Valuebox_label.config(text="3rd Quarter:")
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_3=datetime.today().year
                Quarter_3_years=[Quarter_3 - i for i in range (6)]
                Valuebox.config(values=Quarter_3_years)
                
            elif event.widget.get()=="4th Quarter":
                Monthly_Lyears.place_forget()
                Monthly_year.place_forget()
                Valuebox_label.config(text="4th Quarter:")
                Valuebox_label.place(x=560,y=40)
                Valuebox.place(x=560,y=60)
                Quarter_4=datetime.today().year
                Quarter_4_years=[Quarter_4 - i for i in range (6)]
                Valuebox.config(values=Quarter_4_years)

        MidTech_Filter.bind("<<ComboboxSelected>>",filter_Option)

        Frame_TableBody=Frame(Frame_SumBody,bg="grey",borderwidth=5,highlightbackground="black",highlightthickness=1)
        Frame_TableBody.pack(expand=1,fill=BOTH)
        Summary_Table=ttk.Treeview(Frame_TableBody)
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview")
        Summary_Table['column']=("ID","NAME","TEST","MEDTECH","FILE")
        #Column
        Summary_Table.column("#0",width=0,stretch=NO)
        Summary_Table.column("ID")
        Summary_Table.column("NAME")
        Summary_Table.column("TEST")
        Summary_Table.column("MEDTECH")
        Summary_Table.column("FILE")
        #Header
        Summary_Table.heading("#0")
        Summary_Table.heading("ID",text="ID")
        Summary_Table.heading("NAME",text="NAME")
        Summary_Table.heading("TEST",text="TEST")
        Summary_Table.heading("MEDTECH",text="MEDTECH")
        Summary_Table.heading("FILE",text="FILE")
        Summary_Table.pack(expand=1,fill=BOTH)

    def Main_Dashboard(self):   
        self.Dashboard_GUI=Tk()
        self.Dashboard_GUI.title('CITY HEALTH')
        width= self.Dashboard_GUI.winfo_screenwidth()
        height=self.Dashboard_GUI.winfo_screenheight()
        self.Dashboard_GUI.geometry("%dx%d"%(width,height))

        self.Page_Dashboard=Frame(self.Dashboard_GUI,bg="green")
        self.Page_Dashboard.pack(expand=1, fill=BOTH)
        Frame_Header=Frame(self.Page_Dashboard,width=1360,height=50,highlightbackground="black",highlightthickness=1)
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

        Toggle_Button.menu.add_command(label="Logout",command=lambda:self.logout())
        #Header END------------

        #Message
        Frame_Center=Frame(self.Page_Dashboard,width=1360,height=413,highlightbackground="black",highlightthickness=1)
        Frame_Center.pack()

        Frame_Laboratory=Frame(self.Page_Dashboard,width=1360,height=290,highlightbackground="black",highlightthickness=1)
        Frame_Laboratory.pack()

        Frame_FrontDesk=Frame(Frame_Laboratory,width=350,height=290,highlightbackground="black",highlightthickness=1)
        Frame_FrontDesk.place(x=0,y=0)
        Button_FronDesk=Button(Frame_FrontDesk,text="ENTER",width=8,height=2,bg="green",command=self.FrontDesk).place(x=120,y=200)

        #Lab-list
        Frame_LabTest=Frame(Frame_Laboratory,width=660,height=290)
        Frame_LabTest.place(x=350,y=0)
        Frame_LabCH=Frame(Frame_LabTest,width=660,height=145,highlightbackground="black",highlightthickness=1)
        Frame_LabCH.place(x=0,y=0)
        Button_LabCH=Button(Frame_LabCH,text="ENTER",width=8,height=2,bg="green",command=self.Laboratory).place(x=500,y=50)

        Frame_XRay=Frame(Frame_LabTest,width=660,height=145,highlightbackground="black",highlightthickness=1)
        Frame_XRay.place(x=0,y=145)
        Button_XRay=Button(Frame_XRay,text="ENTER",width=8,height=2,bg="green",command=self.X_Ray).place(x=500,y=50)

        Frame_Summary=Frame(Frame_Laboratory,width=350,height=290,highlightbackground="black",highlightthickness=1)
        Frame_Summary.place(x=1009,y=0)
        Button_Summary=Button(Frame_Summary,text="ENTER",width=8,height=2,bg="green",command=self.Summary).place(x=140,y=200)

        self.Dashboard_GUI.mainloop()
    
    def start(self):
        self.Main_Dashboard()