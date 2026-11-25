from tkinter import *
from tkinter import messagebox
Window = Tk()
Window.geometry("300x300")
Window.title("Virus Detected!")
def pressed():
    messagebox.showerror("Error", "You are hacked!")

Button1 = Button(text = "Press me!", command = pressed)
Button1.pack()
Window.mainloop()

