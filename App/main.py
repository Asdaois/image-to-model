from tkinter import *


def greet_in_console():
    print("Hello")


root = Tk()
root.geometry("1280x720")

frame = Frame(root, background="#F77")
frame.pack(side="top")

leftFrame = Frame(root, background="#272")
leftFrame.pack(side="left")

rightFrame = Frame(root, background="#500")
rightFrame.pack(side="right")

textVariable = StringVar(value="Unmodified")


def greet_in_label():
    textVariable.set("Greet with button")


label = Label(frame, textvariable=textVariable)
label.pack(padx=3, pady=3)


button1 = Button(
    leftFrame, text="Show Hello world in the console", command=greet_in_console)
button1.pack(padx=3, pady=3)


button1 = Button(
    rightFrame, text="Show Hello world in the label", command=greet_in_label)
button1.pack(padx=3, pady=3)


button1 = Button(leftFrame, text="Button3")
button1.pack(padx=3, pady=3)

root.title("Test")

root.mainloop()
