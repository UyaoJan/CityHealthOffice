from tkinter import *
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


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
        Genderlabel=Label(Frame_Input,Gender_Mune.get(),font="Arial 12")

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

    Gender_Label=Label(Frame_Input,text="Gender:",font='Arial 12').place(x=350,y=430)
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

    Record_Button=Button(Frame_Body,text="Record",width=10,bg="green")
    Record_Button.place(x=1250,y=50)

    #Frame for the Testing 
    Frame_Test=Frame(Page_Laboratory,highlightbackground="black",highlightthickness=1,bg="blue")
    Frame_Test.pack(expand=1,fill=BOTH)

    Test_Label=Label(Frame_Test,text="Laboratory Test",width=123,font="Arial 15",anchor=W,highlightbackground="black",highlightthickness=1)
    Test_Label.place(x=0,y=0)

    def Option_TEST():
        LabTestlabel=Label(Frame_Body,LabTest_Mune.get(),font="Arial 12 bold")

    Test_Label=Label(Frame_Test,text="TEST:",font='Arial 12 bold').place(x=1075,y=3)
    Option=["Complete Blood Count","Blood Type","Stool Exam"]
    LabTest_Mune=ttk.Combobox(Frame_Test,value=Option,font='Arial 12',state='readonly')
    LabTest_Mune.set("Select Gender")
    LabTest_Mune.bind("<<ComboboxSelected>>",Option_TEST)
    LabTest_Mune.place(x=1130,y=3)

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
        Findlabel=Label(Detail_Body,FINDING_Mune.get(),font="Arial 12 bold")
        

    Option=["Normal","Chest PA"]
    FINDING_Mune=ttk.Combobox(Detail_Body,value=Option,font='Arial 12',width=20)
    FINDING_Mune.set("Select FINDING")
    FINDING_Mune.bind("<<ComboboxSelected>>",FIND_Click)
    FINDING_Mune.place(x=449,y=310)

    Find_ADD=Button(Detail_Body,text="+",font='Arial 10 bold',width=2,height=1)
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