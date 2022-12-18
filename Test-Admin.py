from tkinter import *


AdminGUi=Tk()
AdminGUi.title('CITY HEALTH')
width= AdminGUi.winfo_screenwidth()
height=AdminGUi.winfo_screenheight()
AdminGUi.geometry("%dx%d"%(width,height))

Frame_Header=Frame(AdminGUi,width=1360,height=80,highlightbackground="black",highlightthickness=1)
Frame_Header.grid(row=1,column=0)

AdminGUi.mainloop()