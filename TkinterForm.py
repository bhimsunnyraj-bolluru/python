from tkinter import * 
from tkinter import messagebox

#Window TK() is the method where form will be generated
window = Tk()
window.title("Process Recorder 3.0")
window.geometry('600x600')

def clicked():
    messagebox.showinfo('Message title', 'Message content')

btn = Button(window,text='Click here', command=clicked)
 
btn.grid(column=0,row=0)
 
window.mainloop()
 
