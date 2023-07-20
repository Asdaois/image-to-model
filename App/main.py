from tkinter import *

root = Tk()
root.geometry("1280x720")

frame = Frame(root, background="#F77")
frame.pack(side="top")

leftFrame = Frame(root, background="#272")
leftFrame.pack(side="left")

rightFrame = Frame(root, background="#500")
rightFrame.pack(side="right")

label = Label(frame, text="Hello world")
label.pack(padx=3, pady=3)

button1 = Button(leftFrame, text="Button1")
button1.pack(padx=3, pady=3)

button1 = Button(rightFrame, text="Button2")
button1.pack(padx=3, pady=3)

button1 = Button(leftFrame, text="Button3")
button1.pack(padx=3, pady=3)

root.title("Test")

root.mainloop()
