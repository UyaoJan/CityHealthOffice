from tkinter import *
from tkcalendar import Calendar,DateEntry
from tkinter import ttk


Frontdesk_GUI=Tk()
Frontdesk_GUI.title('CITY HEALTH')
width= Frontdesk_GUI.winfo_screenwidth()
height=Frontdesk_GUI.winfo_screenheight()
Frontdesk_GUI.geometry("%dx%d"%(width,height))

#Header-------
Frame_Header=Frame(Frontdesk_GUI,width=1360,height=50,highlightbackground="black",highlightthickness=1)
Frame_Header.grid(row=0,column=0)

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
#Header-------
#Body-------
Frame_Body=Frame(Frontdesk_GUI)
Frame_Body.grid(row=1,column=0)

Frame_LIST=Frame(Frame_Body,width=680,height=700,bg="green",highlightbackground="black",highlightthickness=1)
Frame_LIST.grid(row=0,column=0)

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

Checkbutton(Box,text="Complete Blood Count",variable=services[0]).grid(row=0,column=0)
Checkbutton(Box,text="Blood Type",variable=services[1]).grid(row=1,column=0)
Checkbutton(Box,text="Stool Exam",variable=services[2]).grid(row=2,column=0)
Checkbutton(Box,text="Urinalysis (“Urine Test”)",variable=services[3]).grid(row=3,column=0)
Checkbutton(Box,text="Syphilis Rapid Test",variable=services[4]).grid(row=4,column=0)
Checkbutton(Box,text="Hepatitis B (“Antigen Test”)",variable=services[5]).grid(row=5,column=0)
Checkbutton(Box,text="Anti-HAV Test",variable=services[6]).grid(row=6,column=0)
Checkbutton(Box,text="Drug Test",variable=services[7]).grid(row=7,column=0)
Checkbutton(Box,text="Pregnancy Test",variable=services[8]).grid(row=8,column=0)
Checkbutton(Box,text="Fasting Blood Suger Test",variable=services[9]).grid(row=0,column=1)
Checkbutton(Box,text="Blood Uric Acid Test",variable=services[10]).grid(row=1,column=1)
Checkbutton(Box,text="Blood Cholesterol Test",variable=services[11]).grid(row=2,column=1)
Checkbutton(Box,text="Blood Creatinine Test",variable=services[12]).grid(row=3,column=1)
Checkbutton(Box,text="Acid Fast Staining",variable=services[13]).grid(row=4,column=1)
Checkbutton(Box,text="X-Ray Test",variable=services[14]).grid(row=5,column=1)

#Body-------
#DEF INPUT------
def Gender_Click():
    Genderlabel=Label(Frame_Input,Gender_Mune.get(),font="Arial 12")

#IMPUT-----------------
Frame_Input=Frame(Frame_Body,width=680,height=700,highlightbackground="black",highlightthickness=1)
Frame_Input.grid(row=0,column=1)

Img=Label(Frame_Input,width=50,height=20,bg="green").place(x=170,y=40)

Name_Label=Label(Frame_Input,text="Name: ",font='Arial 12').place(x=46,y=400)
Name_Entry=Entry(Frame_Input,width=59,borderwidth=3,font='Arial 12').place(x=100,y=400)

AGE_Label=Label(Frame_Input,text="Age: ",font='Arial 12').place(x=46,y=430)
AGE_Entry=Entry(Frame_Input,width=5,font='Arial 12',borderwidth=3).place(x=100,y=430)

Birth_Label=Label(Frame_Input,text="BirthDay:",font="Arial 12").place(x=160,y=430)
Birth_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2)
Birth_Entry.place(x=230,y=430)

Gender_Label=Label(Frame_Input,text="Gender:",font='Arial 12').place(x=350,y=430)
Option=["Male","Female","Other"]
Gender_Mune=ttk.Combobox(Frame_Input,value=Option)
Gender_Mune.current(0)
Gender_Mune.bind("<<ComboboxSelected>>",Gender_Click)
Gender_Mune.place(x=412,y=432)

Address_Label=Label(Frame_Input,text="Address: ",font='Arial 12').place(x=46,y=460)
Address_Entry=Entry(Frame_Input,width=38,borderwidth=3,font='Arial 12').place(x=120,y=460)

Date_Label=Label(Frame_Input,text="Date:",font="Arial 12").place(x=480,y=460)
Date_Entry=DateEntry(Frame_Input,width=10,backgroud="magenta3",foreground="White",font="Arial 12",bd=2,archor=W)
Date_Entry.place(x=525,y=460)

Submit_Input=Button(Frame_Input,text="Submit",width=10,bg="green",font='Arial 11').place(x=540,y=530)

Frontdesk_GUI.mainloop()