from tkinter import *


LaboratoryGUI=Tk()
LaboratoryGUI.title('CITY HEALTH')
width= LaboratoryGUI.winfo_screenwidth()
height=LaboratoryGUI.winfo_screenheight()
LaboratoryGUI.geometry("%dx%d"%(width,height))

Frame_Header=Frame(LaboratoryGUI,width=1360,height=80,highlightbackground="black",highlightthickness=1)
Frame_Header.grid(row=1,column=0)

LaboratoryGUI.mainloop()