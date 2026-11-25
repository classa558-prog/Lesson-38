from tkinter import *
Window = Tk()
Window.geometry("300x300")
Window.title("Basic event Handling.")
Button1 = Button(text = "Press Me!")
Button1.pack()
def Button_pressed(event):
    print("The button has been pressed!")
Window.bind("<Button-1>", Button_pressed)
def Key_pressed(event):
    print(f"The {event.char} key has been pressed!")
Window.bind("<Key>", Key_pressed)
Window.mainloop()