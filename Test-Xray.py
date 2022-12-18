from tkinter import *


X_rayGUI=Tk()
X_rayGUI.title('CITY HEALTH')
width= X_rayGUI.winfo_screenwidth()
height=X_rayGUI.winfo_screenheight()
X_rayGUI.geometry("%dx%d"%(width,height))

Frame_Header=Frame(X_rayGUI,width=1360,height=80,highlightbackground="black",highlightthickness=1)
Frame_Header.grid(row=1,column=0)

X_rayGUI.mainloop()