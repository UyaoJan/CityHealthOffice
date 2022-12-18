from tkinter import *


SummaryGUI=Tk()
SummaryGUI.title('CITY HEALTH')
width= SummaryGUI.winfo_screenwidth()
height=SummaryGUI.winfo_screenheight()
SummaryGUI.geometry("%dx%d"%(width,height))

Frame_Header=Frame(SummaryGUI,width=1360,height=80,highlightbackground="black",highlightthickness=1)
Frame_Header.grid(row=1,column=0)

SummaryGUI.mainloop()