from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

win = Tk()

win.geometry("600x400")
win.configure(background="cyan")
win.title("Artificial Intelligence based Classification")

title = Label(win, text="Artificial Intelligence based Classification", bg="gray",
              width="300", height="2", fg="white", font=("Calibri 18 bold")).pack()
case = Label(win, text="Case Details: ", bg="cyan",
             font=("Verdana 12")).place(x=12, y=75)
case_txt = Text(win, height=8, width=70).place(x=12, y=100)
case = Label(win, text="OR", bg="cyan", font=(
    "Verdana 12")).place(x=290, y=240)
b1 = tk.Button(win, text='Upload PDF File',
               width=80).place(x=12, y=270)
file_location = Label(win, text="File name :", bg="cyan",
                      font=("Verdana 10")).place(x=12, y=300)

reset = Button(win, text="Reset", width="12", height="1",
               activebackground="red", bg="Pink", font=("Calibri 12 ")).place(x=100, y=340)
submit = Button(win, text="Predict", width="12", height="1",
                activebackground="violet", bg="Pink", font=("Calibri 12 ")).place(x=380, y=340)


win.mainloop()
