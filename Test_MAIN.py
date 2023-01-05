from tkinter import *
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date
import employee


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
        Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))

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
        Box=Frame(Frame_LIST,width=560,height=300,highlightbackground="black",highlightthickness=1)
        Box.place(x=50,y=320)
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
                    ]

        self.services=[]
        for i in range (15):
            Test=IntVar()
            Test.set(0)
            self.services.append(Test)

        def check(i):
            i.set(1)
        
        Checkbutton(Box,text="Complete Blood Count",variable=self.services[0],font='Arial 12 ',command=lambda i=self.services[0]:check(i)).place(x=30,y=50)
        Checkbutton(Box,text="Blood Type",variable=self.services[1],font='Arial 12 ',command=lambda i=self.services[1]:check(i)).place(x=30,y=75)
        Checkbutton(Box,text="Stool Exam",variable=self.services[2],font='Arial 12 ',command=lambda i=self.services[2]:check(i)).place(x=30,y=100)
        Checkbutton(Box,text="Urinalysis (“Urine Test”)",variable=self.services[3],font='Arial 12 ',command=lambda i=self.services[3]:check(i)).place(x=30,y=125)
        Checkbutton(Box,text="Syphilis Rapid Test",variable=self.services[4],font='Arial 12 ',command=lambda i=self.services[4]:check(i)).place(x=30,y=150)
        Checkbutton(Box,text="Hepatitis B (“Antigen Test”)",variable=self.services[5],font='Arial 12 ',command=lambda i=self.services[5]:check(i)).place(x=30,y=175)
        Checkbutton(Box,text="Anti-HAV Test",variable=self.services[6],font='Arial 12 ',command=lambda i=self.services[6]:check(i)).place(x=30,y=200)
        Checkbutton(Box,text="Drug Test",variable=self.services[7],font='Arial 12 ',command=lambda i=self.services[7]:check(i)).place(x=30,y=222)
        Checkbutton(Box,text="Pregnancy Test",variable=self.services[8],font='Arial 12 ',command=lambda i=self.services[8]:check(i)).place(x=30,y=245)
        Checkbutton(Box,text="Fasting Blood Suger Test",variable=self.services[9],font='Arial 12 ',command=lambda i=self.services[9]:check(i)).place(x=280,y=50)
        Checkbutton(Box,text="Blood Uric Acid Test",variable=self.services[10],font='Arial 12 ',command=lambda i=self.services[10]:check(i)).place(x=280,y=75)
        Checkbutton(Box,text="Blood Cholesterol Test",variable=self.services[11],font='Arial 12 ',command=lambda i=self.services[11]:check(i)).place(x=280,y=100)
        Checkbutton(Box,text="Blood Creatinine Test",variable=self.services[12],font='Arial 12 ',command=lambda i=self.services[12]:check(i)).place(x=280,y=125)
        Checkbutton(Box,text="Acid Fast Staining",variable=self.services[13],font='Arial 12 ',command=lambda i=self.services[13]:check(i)).place(x=280,y=150)
        Checkbutton(Box,text="X-Ray Test",variable=self.services[14],font='Arial 12 ',command=lambda i=self.services[14]:check(i)).place(x=280,y=175)

        #Body-------
        #DEF INPUT------
        def Gender_Click():
            Genderlabel=Label(Frame_Input,Gender_Mune.get(),font="Arial 12")

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
        Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
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
                #print(value)
                for i in range(10):
                    Record_Number=Frame(Record_List,width=427,height=80)
                    Record_Number.grid(row=i,column=0)

                    Record_Page=Frame(Record_Number,width=250,height=50,highlightbackground="black",highlightthickness=1)
                    Record_Page.place(x=5,y=5,relwidth=0.98,relheight=0.9)

                    Number_BOX=Frame(Record_Page,width=70,height=50,highlightbackground="black",highlightthickness=1)
                    Number_BOX.place(x=10,y=10)
                    Client_Number=Label(Number_BOX,text="100",font=("Arial",25,"bold")).place(x=3,y=0)#luna please limit the Number of the of to 3 only

                    Client_Name=Label(Record_Page,text="NAME: DARKHOURSE OF THE NIGHT",font=("Arial",12,"bold")).place(x=85,y=10)
                    Client_Test=Label(Record_Page,text="TEST: love my life",font=("Arial",8,"bold")).place(x=85,y=30)

                    Take_Button=Button(Record_Page,text="Take",font=("Arial",8),width=6,height=0,borderwidth=5)
                    Take_Button.place(x=360,y=37)

            
            elif value == "X_RAY":
                #print(value)
                for i in range(10):
                    X_RAY_Record_Number=Frame(Record_List,width=427,height=80)
                    X_RAY_Record_Number.grid(row=i,column=0)

                    X_RAY_Record_Page=Frame(X_RAY_Record_Number,width=250,height=50,highlightbackground="black",highlightthickness=1)
                    X_RAY_Record_Page.place(x=5,y=5,relwidth=0.98,relheight=0.9)

                    XRAY_Number_BOX=Frame(X_RAY_Record_Page,width=70,height=50,highlightbackground="black",highlightthickness=1)
                    XRAY_Number_BOX.place(x=10,y=10)
                    XRAY_Client_Number=Label(XRAY_Number_BOX,text="100",font=("Arial",25,"bold")).place(x=3,y=0)#luna please limit the Number of the of to 3 only

                    XRAY_Client_Name=Label(X_RAY_Record_Page,text="NAME: DARKHOURSE OF THE NIGHT",font=("Arial",12,"bold")).place(x=85,y=10)
                    XRAY_Client_Test=Label(X_RAY_Record_Page,text="TEST:X_RAY TEST",font=("Arial",8,"bold")).place(x=85,y=30)

                    XRAY_Take_Button=Button(X_RAY_Record_Page,text="Take",font=("Arial",8),width=6,height=0,borderwidth=5)
                    XRAY_Take_Button.place(x=360,y=37)
            
            PageOpen += 1

        else:
            messagebox.showinfo("Error","The Window is already Open!")


    def Client_on_close(self):
        global PageOpen
        if messagebox.askokcancel('Close', 'Are you sure you want to close the View Page all the data will not be Save?'):
            PageOpen=1
            self.Client_Page.destroy()
    
    def ClientList(self,value):
        global PageOpen
        if PageOpen < 2:
            self.Client_Page=Toplevel()
            self.Client_Page.title("Client List")
            self.Client_Page
            Record_width=450
            Record_height=600
            self.Client_Page.geometry(f'{Record_width}x{Record_height}+{480}+{100}')
            self.Client_Page.protocol("WM_DELETE_WINDOW", self.Client_on_close)

            self.CListBody= Frame(self.Client_Page)
            self.CListBody.pack(expand=1,fill=BOTH)

            Client_search_LB=Label(self.CListBody,text="SEARCH: ",font='Arial 12 bold').place(x=10,y=100)
            Client_search_EN=Entry(self.CListBody,font='Arial 12',borderwidth=5)
            Client_search_EN.place(x=90,y=98,relwidth=0.6)
            Client_search_BT=Button(self.CListBody,text="Search",font='Arial 10',width=6,height=0,borderwidth=5)
            Client_search_BT.place(x=365,y=94)

            ClistFrame=Frame(self.CListBody,highlightbackground="black",highlightthickness=1)
            ClistFrame.place(x=0,y=130,relwidth=1.0,relheight=0.78)
            CListBOX= Canvas(ClistFrame,highlightbackground="black",highlightthickness=1)
            CListBOX.pack(side=LEFT,fill=BOTH,expand=1)

            Clistscroll=ttk.Scrollbar(ClistFrame,orient=VERTICAL,command=CListBOX.yview)
            Clistscroll.pack(side=RIGHT,fill=Y)

            CListBOX.configure(yscrollcommand=Clistscroll.set)
            CListBOX.bind('<Configure>',lambda e: CListBOX.configure(scrollregion= CListBOX.bbox("all")))

            Client_List=Frame(CListBOX,highlightbackground="black",highlightthickness=2)
            CListBOX.create_window((0,0),window=Client_List,anchor=NW)
            #print(self.Value_Laboratory)
            if value == "Laboratory":
                #print(value)
                for i in range(10):
                    ClientL_Number=Frame(Client_List,width=427,height=80)
                    ClientL_Number.grid(row=i,column=0)

                    Client_Page=Frame(ClientL_Number,width=250,height=50,bg="gray",highlightbackground="black",highlightthickness=1)
                    Client_Page.place(x=5,y=5,relwidth=0.98,relheight=0.9)

                    CL_Number_BOX=Frame(Client_Page,width=70,height=50,highlightbackground="black",highlightthickness=1)
                    CL_Number_BOX.place(x=10,y=10)
                    Client_Number=Label(CL_Number_BOX,text="100",font=("Arial",25,"bold")).place(x=3,y=0)#luna please limit the Number of the of to 3 only

                    Client_Name=Label(Client_Page,text="NAME: DARKHOURSE OF THE NIGHT",font=("Arial",12,"bold")).place(x=85,y=10)
                    Client_Test=Label(Client_Page,text="TEST: love my life",font=("Arial",8,"bold")).place(x=85,y=30)

                    Take_Button=Button(Client_Page,text="Take",font=("Arial",8),width=6,height=0,borderwidth=5)
                    Take_Button.place(x=360,y=37)
            
            elif value == "X_RAY":
                #print(value)
                for i in range(10):
                    X_RAY_Client_Number=Frame(Client_List,width=427,height=80)
                    X_RAY_Client_Number.grid(row=i,column=0)

                    X_RAY_Client_Page=Frame(X_RAY_Client_Number,width=250,height=50,highlightbackground="black",highlightthickness=1)
                    X_RAY_Client_Page.place(x=5,y=5,relwidth=0.98,relheight=0.9)

                    CLX_Number_BOX=Frame(X_RAY_Client_Page,width=70,height=50,highlightbackground="black",highlightthickness=1)
                    CLX_Number_BOX.place(x=10,y=10)
                    Client_Number=Label(CLX_Number_BOX,text="100",font=("Arial",25,"bold")).place(x=3,y=0)#luna please limit the Number of the of to 3 only

                    X_Client_Name=Label(X_RAY_Client_Page,text="NAME: DARKHOURSE OF THE NIGHT",font=("Arial",12,"bold")).place(x=85,y=10)
                    X_Client_Test=Label(X_RAY_Client_Page,text="TEST: love my life",font=("Arial",8,"bold")).place(x=85,y=30)

                    Take_Button=Button(X_RAY_Client_Page,text="Take",font=("Arial",8),width=6,height=0,borderwidth=5)
                    Take_Button.place(x=360,y=37)

            PageOpen += 1

        else:
            messagebox.showinfo("Error","The Window is already Open!")
#Laboratory>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Laboratory(self):
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
        Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))
        #Header-------
        #BODY >> Laboratory
        Frame_Body=Frame(Page_Laboratory,width=1360,height=150,highlightbackground="black",highlightthickness=1)
        Frame_Body.pack()

        Labo_Title=Label(Frame_Body,text="Laboratory Test!",font='Arial 20')
        Labo_Title.place(x=10,y=5)
        Name_Label=Label(Frame_Body,text="Name: ",font='Arial 12').place(x=19,y=50)
        Name_Entry=Entry(Frame_Body,width=59,borderwidth=3,font='Arial 9')
        Name_Entry.place(x=20,y=70)

        AGE_Label=Label(Frame_Body,text="Age: ",font='Arial 12').place(x=450,y=50)
        AGE_Entry=Entry(Frame_Body,width=8,font='Arial 9',borderwidth=3)
        AGE_Entry.place(x=450,y=70)

        def Gender_Click():
            Genderlabel=Label(Frame_Body,Gender_Mune.get(),font="Arial 12")

        Gender_Label=Label(Frame_Body,text="Gender:",font='Arial 12').place(x=150,y=100)
        Option=["Male","Female","Other"]
        Gender_Mune=ttk.Combobox(Frame_Body,value=Option,font='Arial 12',state='readonly')
        Gender_Mune.set("Select Gender")
        Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
        Gender_Mune.place(x=150,y=120)

        Date_Label=Label(Frame_Body,text="Date:",font="Arial 12").place(x=20,y=100)
        Date_Entry=DateEntry(Frame_Body,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
        Date_Entry.place(x=20,y=120)

        CList_Button=Button(Frame_Body,text="Client List",bg="green",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda:self.ClientList(self.Value_Laboratory[0]))
        CList_Button.place(x=1200,y=60)

        Record_Button=Button(Frame_Body,text="Record",bg="green",width=15,height=1,font=("Arail",10),borderwidth=5,command=lambda:self.Record(self.Value_Laboratory[0]))
        Record_Button.place(x=1200,y=100)

        #Frame for the Testing 
        Frame_Test=Frame(Page_Laboratory,highlightbackground="black",highlightthickness=1,bg="blue")
        Frame_Test.pack(expand=1,fill=BOTH)

        Test_Label=Label(Frame_Test,text="Laboratory Test",width=123,font="Arial 15",anchor=W,highlightbackground="black",highlightthickness=1)
        Test_Label.place(x=0,y=0)

        Test=[#"Complete Blood Count",
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


            elif LabTest_Mune.get() == "Miscelaneous":
                Serology_Page.pack_forget()
                Miscelaneous_Page.pack(expand=1,fill=BOTH)

                Miscelaneous_Title = Label(Miscelaneous_Page,text="MISCELLANEOUS",font=("Arial",20,"bold"))
                Miscelaneous_Title.place(x=570,y=30)

                PT_Box=Frame(Miscelaneous_Page,bg='white')
                PT_Box.place(x=430,y=200)
                PT_BOX1= Label(PT_Box,text="TEST",width=20,anchor=W,font=("Arial",15,"bold"))
                PT_BOX1.grid(row=0,column=0)
                PT_BOX2= Label(PT_Box,text="PREGNANCY TEST",width=20,anchor=W,font=("Arial",15,"bold"))
                PT_BOX2.grid(row=0,column=1)
                PT_BOX3= Label(PT_Box,text="RESULT",width=20,anchor=W,font=("Arial",15,"bold"))
                PT_BOX3.grid(row=1,column=0)

                PT_Result=["POSITIVE","NEGATIVE"]
                PT_BOX4=ttk.Combobox(PT_Box,value=PT_Result,font=("Arial",15),state='readonly')
                PT_BOX4.set("Select Result")
                PT_BOX4.grid(row=1,column=1)


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

            Plus_ADD_button=Button(Plus_Body,text="ADD",font=("Arail 10"),width=5,borderwidth=5)
            Plus_ADD_button.place(x=450,y=560)
           
            Plus_Cancel_button=Button(Plus_Body,text="Cancel",font=("Arail 10"),width=5,borderwidth=5)
            Plus_Cancel_button.place(x=520,y=560)

            PageOpen += 1
        else:
            messagebox.showinfo("Error","The Window is already Open!")

#X_Ray Laboratory>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def X_Ray(self):
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

        HEADER_USERNAME=Label(Frame_Header,text="UserName:",font='Arial 12 ').place(x=1100,y=10)
        IMG_USERNAME=Label(Frame_Header,text='IMG',bg='green',width=5,height=2)
        IMG_USERNAME.place(x=1200,y=8)

        Toggle_Button=Menubutton(Frame_Header,width=5,text="=",highlightbackground="black",highlightthickness=1,justify=RIGHT)
        Toggle_Button.place(x=1290,y=10)
        Toggle_Button.menu=Menu(Toggle_Button)
        Toggle_Button["menu"]=Toggle_Button.menu

        Toggle_Button.menu.add_command(label="HOME",command=Home)
        Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))
        #Header-------
        #BODY >> Laboratory
        Detail_Body=Frame(Page_XRAY,width=300)
        Detail_Body.pack(expand=1,fill=BOTH,side=LEFT)

        XRAY_Title=Label(Detail_Body,text="X-Ray Laboratory Test!",font='Arial 40 bold')
        XRAY_Title.place(x=10,y=15) 

        Name_Label=Label(Detail_Body,text="Name: ",font='Arial 12').place(x=100,y=130)
        Name_Entry=Entry(Detail_Body,width=50,borderwidth=3,font='Arial 9')
        Name_Entry.place(x=160,y=130)

        Birth_Label=Label(Detail_Body,text="BirthDay:",font="Arial 12").place(x=100,y=160)
        Birth_Entry=DateEntry(Detail_Body,width=36,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
        Birth_Entry.place(x=170,y=160)

        AGE_Label=Label(Detail_Body,text="Age: ",font='Arial 12').place(x=100,y=190)
        AGE_Entry=Entry(Detail_Body,width=50,font='Arial 9',borderwidth=3)
        AGE_Entry.place(x=160,y=190)

        def Gender_Click():
            Genderlabel=Label(Detail_Body,Gender_Mune.get(),font="Arial 12 bold")

        Gender_Label=Label(Detail_Body,text="Gender:",font='Arial 12 ').place(x=100,y=220)
        Option=["Male","Female","Other"]
        Gender_Mune=ttk.Combobox(Detail_Body,value=Option,font='Arial 12',width=37,state='readonly')
        Gender_Mune.set("Select Gender")
        Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
        Gender_Mune.place(x=160,y=220)

        Date_Label=Label(Detail_Body,text="Date:",font="Arial 12").place(x=100,y=250)
        Date_Entry=DateEntry(Detail_Body,width=37,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
        Date_Entry.place(x=160,y=250)

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

        def FIND_Click():
            print("Find_Click")

        Option=["Normal","Chest PA"]
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
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filepath = filedialog.askopenfilename(filetypes=f_types)
            img=Image.open(filepath)
            img_resized=img.resize((285,375)) # new width & height
            img=ImageTk.PhotoImage(img_resized)
            b2 =Button(Image_Box,image=img,borderwidth=5,command=open_file) # using Button 
            b2.place(x=0,y=0)
        
        CList_Xray=Button(Img_Body,text="Client List",width=10,bg="green",font='Arial 11',command=lambda:self.ClientList(self.Value_Laboratory[1])).place(x=300,y=630)
        Record_Xray=Button(Img_Body,text="Record",width=10,bg="green",font='Arial 11',command=lambda:self.Record(self.Value_Laboratory[1])).place(x=410,y=630)
        Submit_Xray=Button(Img_Body,text="Submit",width=10,bg="green",font='Arial 11').place(x=520,y=630)

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
        Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))
        #Header-------
        #BODY >> Summary

        Frame_SumBody=Frame(self.Page_Summary)
        Frame_SumBody.pack(expand=1,fill=BOTH,side=TOP)
        
        Frame_FilterBody=Frame(Frame_SumBody,height=130,border=2,borderwidth=5,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
        Frame_FilterBody.pack(fill=X)

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

        Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))
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


# app=Main()
# app.start()