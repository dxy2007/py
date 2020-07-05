from tkinter import*
from tkinter.messagebox import*
def hello():
    showinfo('hetao101','hello world')
root = Tk()
root.title('hetao101')
root.geometry('300x300')
menubar = Menu(root)
menubar.add_command(label='hello',command=hello)
menubar.add_command(label='exit',command=exit)
root.config(menu=menubar)
root.mainloop()