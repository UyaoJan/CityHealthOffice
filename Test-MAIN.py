from tkinter import *
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

Dashboard_GUI=Tk()
Dashboard_GUI.title('CITY HEALTH')
width= Dashboard_GUI.winfo_screenwidth()
height=Dashboard_GUI.winfo_screenheight()
Dashboard_GUI.geometry("%dx%d"%(width,height))

#DEF Header-------

def FrontDesk():
    def Home():
        Page_FrontDesk.destroy()
        Page_Dashboard.pack()
    Page_Dashboard.forget()
    Page_FrontDesk=Frame(Dashboard_GUI,bg="green")
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
    Toggle_Button.menu.add_command(label="Setting",command=lambda:print("Luck of knowlegde"))
    Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))

    #Header-------
    #Body-------
    Frame_Body=Frame(Page_FrontDesk)
    Frame_Body.pack(side=RIGHT)

    Frame_LIST=Frame(Frame_Body,width=680,height=700)
    Frame_LIST.pack(side=LEFT)
    FrontDesk_Title=Label(Frame_Body,text="FrontDesk!",font='Arial 75')
    FrontDesk_Title.place(x=20,y=20)
    Box_Title=Label(Frame_Body,text="Laboratory Test List",font='Arial 25')
    Box_Title.place(x=54,y=300)
    Box=Frame(Frame_LIST,width=560,height=300,highlightbackground="black",highlightthickness=1)
    Box.place(x=50,y=320)
    #Checkbox Def
    def showCheckbox():
        for i in range(len(services)):
            Selected=""
            if services[i].get()>=1:
                Selected += str(i)
                print(Selected)
    #checkbox
    services=[]
    for i in range(15):
        Test=StringVar()
        Test.set(0)
        services.append(Test)
    
    Checkbutton(Box,text="Complete Blood Count",variable=services[0],font='Arial 12 ').place(x=30,y=50)
    Checkbutton(Box,text="Blood Type",variable=services[1],font='Arial 12 ').place(x=30,y=75)
    Checkbutton(Box,text="Stool Exam",variable=services[2],font='Arial 12 ').place(x=30,y=100)
    Checkbutton(Box,text="Urinalysis (“Urine Test”)",variable=services[3],font='Arial 12 ').place(x=30,y=125)
    Checkbutton(Box,text="Syphilis Rapid Test",variable=services[4],font='Arial 12 ').place(x=30,y=150)
    Checkbutton(Box,text="Hepatitis B (“Antigen Test”)",variable=services[5],font='Arial 12 ').place(x=30,y=175)
    Checkbutton(Box,text="Anti-HAV Test",variable=services[6],font='Arial 12 ').place(x=30,y=200)
    Checkbutton(Box,text="Drug Test",variable=services[7],font='Arial 12 ').place(x=30,y=222)
    Checkbutton(Box,text="Pregnancy Test",variable=services[8],font='Arial 12 ').place(x=30,y=245)
    Checkbutton(Box,text="Fasting Blood Suger Test",variable=services[9],font='Arial 12 ').place(x=280,y=50)
    Checkbutton(Box,text="Blood Uric Acid Test",variable=services[10],font='Arial 12 ').place(x=280,y=75)
    Checkbutton(Box,text="Blood Cholesterol Test",variable=services[11],font='Arial 12 ').place(x=280,y=100)
    Checkbutton(Box,text="Blood Creatinine Test",variable=services[12],font='Arial 12 ').place(x=280,y=125)
    Checkbutton(Box,text="Acid Fast Staining",variable=services[13],font='Arial 12 ').place(x=280,y=150)
    Checkbutton(Box,text="X-Ray Test",variable=services[14],font='Arial 12 ').place(x=280,y=175)

    #Body-------
    #DEF INPUT------
    def Gender_Click():
        F_Genderlabel=Label(Frame_Input,Gender_Mune.get(),font="Arial 12")

    #IMPUT-----------------
    Frame_Input=Frame(Frame_Body,width=680,height=700)
    Frame_Input.pack()

    Img=Label(Frame_Input,width=50,height=20,bg="green").place(x=170,y=40)

    Name_Label=Label(Frame_Input,text="Name: ",font='Arial 12').place(x=46,y=400)
    Name_Entry=Entry(Frame_Input,width=59,borderwidth=3,font='Arial 12')
    Name_Entry.place(x=100,y=400)

    AGE_Label=Label(Frame_Input,text="Age: ",font='Arial 12').place(x=46,y=430)
    AGE_Entry=Entry(Frame_Input,width=5,font='Arial 12',borderwidth=3)
    AGE_Entry.place(x=100,y=430)

    Birth_Label=Label(Frame_Input,text="BirthDay:",font="Arial 12").place(x=160,y=430)
    Birth_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,state='readonly')
    Birth_Entry.place(x=230,y=430)

    F_Gender_Label=Label(Frame_Input,text="Gender:",font='Arial 12').place(x=350,y=430)
    Option=["Male","Female","Other"]
    Gender_Mune=ttk.Combobox(Frame_Input,value=Option,font='Arial 12',state='readonly')
    Gender_Mune.current(0)
    Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
    Gender_Mune.place(x=412,y=432)

    Address_Label=Label(Frame_Input,text="Address: ",font='Arial 12').place(x=46,y=460)
    Address_Entry=Entry(Frame_Input,width=38,borderwidth=3,font='Arial 12').place(x=120,y=460)

    Date_Label=Label(Frame_Input,text="Date:",font="Arial 12").place(x=480,y=460)
    Date_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W,state='readonly')
    Date_Entry.place(x=525,y=460)

    Submit_Input=Button(Frame_Input,text="Submit",width=10,bg="green",font='Arial 11').place(x=540,y=530)


#FrontDesk-END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Laboratory>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Laboratory():
    def Home():
        Page_Laboratory.destroy()
        Page_Dashboard.pack()
    Page_Dashboard.forget()
    Page_Laboratory=Frame(Dashboard_GUI,bg="green")
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
    Toggle_Button.menu.add_command(label="Setting",command=lambda:print("Luck of knowlegde"))
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
        L_Genderlabel=Label(Frame_Body,Gender_Mune.get(),font="Arial 12")

    L_Gender_Label=Label(Frame_Body,text="Gender:",font='Arial 12').place(x=150,y=100)
    Option=["Male","Female","Other"]
    Gender_Mune=ttk.Combobox(Frame_Body,value=Option,font='Arial 12',state='readonly')
    Gender_Mune.set("Select Gender")
    Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
    Gender_Mune.place(x=150,y=120)

    Date_Label=Label(Frame_Body,text="Date:",font="Arial 12").place(x=20,y=100)
    Date_Entry=DateEntry(Frame_Body,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
    Date_Entry.place(x=20,y=120)

    Record_Button=Button(Frame_Body,text="Record",width=10,bg="green")
    Record_Button.place(x=1250,y=50)

    #Frame for the Testing 
    Frame_Test=Frame(Page_Laboratory,highlightbackground="black",highlightthickness=1,bg="blue")
    Frame_Test.pack(expand=1,fill=BOTH)

    Test_Label=Label(Frame_Test,text="Laboratory Test",width=123,font="Arial 15",anchor=W,highlightbackground="black",highlightthickness=1)
    Test_Label.place(x=0,y=0)

    def Option_TEST(value):
        CBC_Frame.pack_forget()
        BT_Frame.pack_forget()
        SE_Frame.pack_forget()
        UT_Frame.pack_forget()
        PT_Frame.pack_forget()


        #THIS IS THE FRAME OF Complete Blood Count
        if Lab_Option.get() == "Complete Blood Count":
            CBC_Frame.pack(fill="both",expand=True)
                        
        #THIS IS THE FRAME OF Blood Type
        elif Lab_Option.get() == "Blood Type":
            BT_Frame.pack(fill="both",expand=True)
            BT_TableBOX=Frame(BT_Frame,highlightbackground="black",highlightthickness=2)
            BT_TableBOX.place(x=420,y=150,relwidth=0.39,relheight=0.32)

            BT_Table=[  ["", "RESULT"],
                        ["BLOOD TYPE", ""],
                        ["HEPATITIS B SCREENING (HNsAg)", ""],
                        ["ANTI-HAV SCREENING (HAV lgG/lgM)", ""],
                        ["SYPHILIS SCREENING", ""],
                        ["GENGUE NS1 ANTIGEN TEST", ""],
                        ]
            BT_Row=len(BT_Table)

            for i in range(BT_Row):
                Column_BT_1=Label(BT_TableBOX,text=f'{BT_Table[i][0]}',width=30,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1,anchor=W)
                Column_BT_1.grid(row=i,column=0)

                Column_BT_RESULT=Label(BT_TableBOX,text=f'{BT_Table[0][1]}',width=21,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1)
                Column_BT_RESULT.grid(row=0,column=1)

                Column_BT_2=Entry(BT_TableBOX,font=("Arail",12),width=23,highlightbackground="black",highlightthickness=2)
                Column_BT_2.grid(row=i,column=1)
                Column_BT_2.insert(END,BT_Table[i][1])
            
            BT_Print=Button(BT_Frame,text="PRINT",width=8,height=2,bg="green",)
            BT_Print.place(x=1200,y=450)

        #THIS IS THE FRAME OF Stool Exam
        elif Lab_Option.get() == "Stool Exam":
            SE_Frame.pack(fill="both",expand=True)
            SE_Frame.pack(fill="both",expand=True)
            SE_TableBOX=Frame(SE_Frame,highlightbackground="black",highlightthickness=2)
            SE_TableBOX.place(x=420,y=140,relwidth=0.39,relheight=0.53)

            SE_Table=[  ["COLOR:", ""],
                        ["CONSISTENCY:", ""],
                        ["MICROSCOPIC EXAMINATION", "RESULT"],
                        ["WBC", ""],
                        ["RBC", ""],
                        ["BACTERIA", ""],
                        ["FAT GLOBULES", ""],
                        ["OVA OR PATASITE", ""],
                        ["E. Histolytica CYST", ""],
                        ["E coli CYST", ""],
                        ]
            SE_Row=len(SE_Table)

            for i in range(SE_Row):
                SE_Culomn_1=Label(SE_TableBOX,text=f'{SE_Table[i][0]}',width=30,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1,anchor=W)
                SE_Culomn_1.grid(row=i,column=0)

                SE_Culomn_reslut=Label(SE_TableBOX,text=f'{SE_Table[2][1]}',width=21,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1)
                SE_Culomn_reslut.grid(row=2,column=1)

                SE_Culomn_2=Entry(SE_TableBOX,font=("Arail",12),width=23,highlightbackground="black",highlightthickness=2)
                SE_Culomn_2.grid(row=i,column=1)
                SE_Culomn_2.insert(END,SE_Table[i][1])
            
            SE_Print=Button(SE_Frame,text="PRINT",width=8,height=2,bg="green",)
            SE_Print.place(x=1200,y=450)
            
        #THIS IS THE FRAME OF Urinalysis (“Urine Test”)
        elif Lab_Option.get() == "Urinalysis (“Urine Test”)":
            UT_Frame.pack(fill="both",expand=True)
            UT_Frame.pack(fill="both",expand=True)
            UT_TableBOX=Frame(UT_Frame,highlightbackground="black",highlightthickness=2)
            UT_TableBOX.place(x=420,y=50,relwidth=0.39,relheight=0.9)

            UT_Table=[  ["COLOR:", "",""],
                        ["CLARITY:", "",""],
                        ["BLOOD", "RESULT",""],
                        ["BILIRUBIN", "",""],
                        ["LEUKOCYTE", "",""],
                        ["KETONE", "",""],
                        ["NITRITE", "",""],
                        ["PROTEIN", "",""],
                        ["GLUCOSE", "",""],
                        ["PH", "",""],
                        ["SPECIFIC GRAVITY", "",""],
                        ["MICROSCOPIC EXAMINATION", "",""],
                        ["WBC", "",""],
                        ["RBC", "",""],
                        ["EPITHELICAL CELLS", "",""],
                        ["MUCOUS THREADS", "",""],
                        ["BACTERIA", "",""],
                        ["A. URATES/PHOSPHATE", "",""],
                        ["CAST", "",""],
                        ["CRYSTALS", "",""],
                        ["OTHERS", "",""],
                        ]
            UT_Row=len(UT_Table)

            for i in range(UT_Row):
                UT_Culomn_1=Label(UT_TableBOX,text=f'{UT_Table[i][0]}',width=30,font=("Arail",8,"bold"),highlightbackground="black",highlightthickness=1,anchor=W)
                UT_Culomn_1.grid(row=i,column=0)

                UT_Culomn_2=Entry(UT_TableBOX,font=("Arail",8),width=23,highlightbackground="black",highlightthickness=2)
                UT_Culomn_2.grid(row=i,column=1)
                UT_Culomn_2.insert(END,UT_Table[i][1])

                UT_Culomn_3=Entry(UT_TableBOX,font=("Arail",8),width=23,highlightbackground="black",highlightthickness=1)
                UT_Culomn_3.grid(row=i,column=2)
                UT_Culomn_3.insert(END,UT_Table[i][2])
            
            UT_Print=Button(UT_Frame,text="PRINT",width=8,height=2,bg="green",)
            UT_Print.place(x=1200,y=450)


        #THIS IS THE FRAME OF Pregnancy Test
        elif Lab_Option.get() == "Pregnancy Test":
            PT_Frame.pack(fill="both",expand=True)

            PT_TableBOX=Frame(PT_Frame,highlightbackground="black",highlightthickness=2)
            PT_TableBOX.place(x=420,y=180,relwidth=0.35,relheight=0.13)

            PT_Table=[  ["TEST", "PREGNANCY"],
                        ["RESULT", ""],
                        ]

            Column_TEST=Label(PT_TableBOX,text=f'{PT_Table[0][0]}',width=19,font=("Arail",15,"bold"),highlightbackground="black",highlightthickness=1)
            Column_TEST.grid(row=0,column=0)

            Column_Result=Label(PT_TableBOX,text=f'{PT_Table[1][0]}',width=19,font=("Arail",15,"bold"),highlightbackground="black",highlightthickness=1)
            Column_Result.grid(row=1,column=0)

            Column_Result=Label(PT_TableBOX,text=f'{PT_Table[0][1]}',width=19,font=("Arail",14,"bold"),highlightbackground="black",highlightthickness=1)
            Column_Result.grid(row=0,column=1)

            def PN_Click():
                RESULT_PN=Label(PT_TableBOX,Gender_Mune.get(),font="Arial 12")
            ResultPN=["POSITIVE","NEGATIVE"]
            Column_Mune=ttk.Combobox(PT_TableBOX,value=ResultPN,state='readonly',width=19,font=("Arail",15,"bold"))
            Column_Mune.set("Select RESULT")
            Column_Mune.bind("<<ComboboxSelected>>",PN_Click)
            Column_Mune.grid(row=1,column=1)

            PT_Print=Button(PT_Frame,text="PRINT",width=8,height=2,bg="green",)
            PT_Print.place(x=1200,y=450)

        else:
            messagebox.showinfo("Error","There Are something wrong in the System!")

    Test_Label=Label(Frame_Test,text="TEST:",font='Arial 12 bold').place(x=1075,y=3)
    
    LabOptionBox=Frame(Frame_Test,bg="Gray",highlightbackground="black",highlightthickness=2)
    LabOptionBox.place(x=0,y=30,relwidth=1.0,relheight=0.95)
    Lab_Option=tk.StringVar(LabOptionBox)
    Lab_Option.set("CBC_Frame")
    LabTest_Mune=ttk.Combobox(Frame_Test,textvariable=Lab_Option,font='Arial 12',state='readonly',
    value=["Complete Blood Count",
            "Blood Type",
            "Stool Exam",
            "Urinalysis (“Urine Test”)",
            # "Syphilis Rapid Test",
            # "Hepatitis B (“Antigen Test”)",
            # "Anti-HAV Test",
            # "Drug Test",
            "Pregnancy Test",
            # "Fasting Blood Suger Test",
            # "Blood Uric Acid Test",
            # "Blood Cholesterol Test",
            # "Blood Creatinine Test",
            # "Acid Fast Staining",
            ])

    LabTest_Mune.bind("<<ComboboxSelected>>",Option_TEST)
    LabTest_Mune.place(x=1130,y=3)

    #Labtest Frame LIST
    CBC_Frame=Frame(LabOptionBox)
    CBC_Frame.pack(fill="both",expand=True)

    CBC_TableBOX=Frame(CBC_Frame,highlightbackground="black",highlightthickness=2)
    CBC_TableBOX.place(x=300,y=30,relwidth=0.50,relheight=0.9)

    CBC_Table=[ ["", "Result", "Normal Values"],
                ["WBC", " ", "5,0000-10,000/CUMM"],
                ["RBC", " ", "F: 3.8-5.1 10^ uL; M:4.20-5.6 10^ uL"],
                ["HEMOGLOBIN"," ","F: 11.70-14.5g/dL; M: 13.7-16.7g/dL"],
                ["HEMATOCRIT"," ","F: 34.1-44.3 vol%; M; 41.5-49.7 vol%"],
                ["MCV"," ","80-100 fl"],
                ["MCH"," ","29 + 2 pg"],
                ["MCHC"," ","33.4-35.5 g/dL"],
                ["RDW"," ","12% to 15%"],
                ["PLATELET"," ","150,000 - 450,000 uL"],
                ["MPV"," ","8.9 - 11.8 fL"],
                ["DEFFERENTIAL COUNT"," ",""],
                ["NEUTROPHIL"," ","45% - 70%"],
                ["LYMPHOCYTE"," ","18% - 45%"],
                ["MONOCYTE"," ","4% - 8%"],
                ["EOSINOPHIL"," ","2% - 3%"],
                ["BOSAPHIL"," ","0% - 2%"],  
                ]

    Row=len(CBC_Table)

    for i in range (Row):
        Column1_LABEL=Label(CBC_TableBOX,text=f'{CBC_Table[i][0]}',width=19,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1)
        Column1_LABEL.grid(row=i,column=0)

        Column1R_LABEL=Label(CBC_TableBOX,text=f'{CBC_Table[0][1]}',width=18,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1)
        Column1R_LABEL.grid(row=0,column=1)

        Column2_Entry=Entry(CBC_TableBOX,font=("Arail",12),width=20,highlightbackground="black",highlightthickness=2)
        Column2_Entry.grid(row=i,column=1)
        Column2_Entry.insert(END,CBC_Table[i][1])

        Column2D_LABEL=Label(CBC_TableBOX,text=f'{CBC_Table[11][1]}',width=18,font=("Arail",12,"bold"),highlightbackground="black",highlightthickness=1)
        Column2D_LABEL.grid(row=11,column=1)

        Column3_LABEL=Label(CBC_TableBOX,text=f'{CBC_Table[i][2]}',width=31,wraplength=400,justify=tk.LEFT,font=("Arail",12),highlightbackground="black",highlightthickness=1)
        Column3_LABEL.grid(row=i,column=2)
    
    CBC_Print=Button(CBC_Frame,text="PRINT",width=8,height=2,bg="green",)
    CBC_Print.place(x=1200,y=450)

    BT_Frame=Frame(LabOptionBox)
    SE_Frame=Frame(LabOptionBox)
    UT_Frame=Frame(LabOptionBox)
    PT_Frame=Frame(LabOptionBox)
    


#Laboratory-END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#X_Ray Laboratory>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def X_Ray():
    def Home():
        Page_XRAY.destroy()
        Page_Dashboard.pack()
    Page_Dashboard.forget()
    Page_XRAY=Frame(Dashboard_GUI,bg="green")
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
    Toggle_Button.menu.add_command(label="Setting",command=lambda:print("Luck of knowlegde"))
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
        X_Genderlabel=Label(Detail_Body,Gender_Mune.get(),font="Arial 12 bold")

    X_Gender_Label=Label(Detail_Body,text="Gender:",font='Arial 12 ').place(x=100,y=220)
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

    def FIND_Result():
        print("this")

    Option=["Normal","Chest PA"]
    FINDING_Mune=ttk.Combobox(Detail_Body,value=Option,font='Arial 12',width=20)
    FINDING_Mune.set("Select FINDING")
    FINDING_Mune.bind("<<ComboboxSelected>>",FIND_Result)
    FINDING_Mune.place(x=449,y=310)
    
    
    global PageOpen
    PageOpen = 1
    def Find_Add():
        global PageOpen
        def on_close():
            global PageOpen
            if tk.messagebox.askokcancel('Close', 'Are you sure you want to close the Add Finding all the Input will not be Save?'):
                PageOpen=1
                Find_Page.destroy()
        
        if PageOpen<2:
            Find_Page=Toplevel()
            Find_Page.title("Add FINDING")
            Rig_width=600
            Rig_height=550
            Find_Page.geometry(f'{Rig_width}x{Rig_height}+{430}+{90}')
            Find_Page.protocol("WM_DELETE_WINDOW", on_close)
            Find_Page.resizable(False,False)

            Add_Find_Body=Frame(Find_Page)
            Add_Find_Body.pack(expand=1,fill=BOTH)

            Finding_Title=Label(Add_Find_Body,text="Add Finding",font=("Arail",35,"bold"))
            Finding_Title.place(x=10,y=10)

            Find_Addoption_title=Label(Add_Find_Body,text="Title: ",font=("Arail",15,"bold")).place(x=5,y=100)
            Find_Addoption_Entry=Entry(Add_Find_Body,width=50,border=5)
            Find_Addoption_Entry.place(x=56,y=103)

            Finding_TextTitle=Label(Add_Find_Body,text="Finding",font=("Arail",20,"bold"))
            Finding_TextTitle.place(x=5,y=138)
            Add_Find_Box=Frame(Add_Find_Body,width=550,height=200,padx=5,pady=5,highlightbackground="black",highlightthickness=1)
            Add_Find_Box.place(x=0,y=170)
            Add_Find_scroll=Scrollbar(Add_Find_Box,orient='vertical')
            Add_Find_scroll.pack(side=RIGHT,fill='y')
            Add_Find_Text = Text(Add_Find_Box, height = 21, width = 70,borderwidth=5,font=("Arial 11 "),yscrollcommand=Add_Find_scroll.set)
            Add_Find_scroll.config(command=Add_Find_Text.yview)
            Add_Find_Text.pack()

            ADD_Find_Button=Button(Add_Find_Body,text="Add",width=5,height=1,bg="green",font=("Arial 11 "))
            ADD_Find_Button.place(x=450,y=134)

            Close_Find_Button=Button(Add_Find_Body,text="Close",width=5,height=1,bg="green",font=("Arial 11 "),command=on_close)
            Close_Find_Button.place(x=520,y=134)

            PageOpen+= 1
        else:
            messagebox.showinfo("Error","The Window Registration is already Open!")

    Find_ADD=Button(Detail_Body,text="+",font='Arial 10 bold',width=2,height=1,command=Find_Add)
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
        b2 =Button(Image_Box,image=img,borderwidth=5) # using Button 
        b2.place(x=0,y=0)
    
    Record_Xray=Button(Img_Body,text="Record",width=10,bg="green",font='Arial 11').place(x=410,y=630)
    Submit_Xray=Button(Img_Body,text="Submit",width=10,bg="green",font='Arial 11').place(x=520,y=630)

#X_Ray Laboratory  END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Summary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Summary():
    def Home():
        Page_Summary.destroy()
        Page_Dashboard.pack()
    Page_Dashboard.forget()
    Page_Summary=Frame(Dashboard_GUI,bg="green")
    Page_Summary.pack(expand=1, fill=BOTH)
    # Page_scroll=Scrollbar(Page_Summary,orient='vertical')
    # Page_scroll.pack(side=RIGHT,fill='y')
    Frame_Header=Frame(Page_Summary,width=1360,height=50,highlightbackground="black",highlightthickness=1)
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
    Toggle_Button.menu.add_command(label="Setting",command=lambda:print("Luck of knowlegde"))
    Toggle_Button.menu.add_command(label="Logout",command=lambda:print("Needed to learn more"))
    #Header-------
    #BODY >> Summary

    Frame_SumBody=Frame(Page_Summary)
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

#Dashboard>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Header-------
Page_Dashboard=Frame(Dashboard_GUI,bg="green")
Page_Dashboard.pack(expand=1, fill=BOTH)
Frame_Header=Frame(Page_Dashboard,width=1360,height=50,highlightbackground="black",highlightthickness=1)
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
#Header END------------

#Message
Frame_Center=Frame(Page_Dashboard,width=1360,height=413,highlightbackground="black",highlightthickness=1)
Frame_Center.pack()

Frame_Laboratory=Frame(Page_Dashboard,width=1360,height=290,highlightbackground="black",highlightthickness=1)
Frame_Laboratory.pack()

Frame_FrontDesk=Frame(Frame_Laboratory,width=350,height=290,highlightbackground="black",highlightthickness=1)
Frame_FrontDesk.place(x=0,y=0)
Button_FronDesk=Button(Frame_FrontDesk,text="ENTER",width=8,height=2,bg="green",command=FrontDesk).place(x=120,y=200)

#Lab-list
Frame_LabTest=Frame(Frame_Laboratory,width=660,height=290)
Frame_LabTest.place(x=350,y=0)
Frame_LabCH=Frame(Frame_LabTest,width=660,height=145,highlightbackground="black",highlightthickness=1)
Frame_LabCH.place(x=0,y=0)
Button_LabCH=Button(Frame_LabCH,text="ENTER",width=8,height=2,bg="green",command=Laboratory).place(x=500,y=50)

Frame_XRay=Frame(Frame_LabTest,width=660,height=145,highlightbackground="black",highlightthickness=1)
Frame_XRay.place(x=0,y=145)
Button_XRay=Button(Frame_XRay,text="ENTER",width=8,height=2,bg="green",command=X_Ray).place(x=500,y=50)

Frame_Summary=Frame(Frame_Laboratory,width=350,height=290,highlightbackground="black",highlightthickness=1)
Frame_Summary.place(x=1009,y=0)
Button_Summary=Button(Frame_Summary,text="ENTER",width=8,height=2,bg="green",command=Summary).place(x=140,y=200)

Dashboard_GUI.mainloop()