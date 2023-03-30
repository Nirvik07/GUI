
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as font


def back_home():
    frame_ana.destroy()
    frame_home.pack()


def browse_file():
    file_path = filedialog.askopenfilename()
    file_location.configure(text="File Selected: "+file_path)
    print(file_path)


def analyze():
    frame_home.destroy()
    frame_ana.pack()


def details():
    frame_ana.destroy()
    frame_details.pack()


win = tk.Tk()

win.geometry("600x400")
win.resizable(False, False)
win.title("Artificial Intelligence based Classification")
btnFont = font.Font(size=16)
lebel_title = tk.Label(win, text="Artificial Intelligence based Classification", bg="gray",
                       width="300", height="2", fg="white", font=("Calibri 18 bold"))
lebel_title.pack()


frame_home = tk.Frame(win, width=600, height=350)
frame_home.pack()
img = Image.open("bg.png")
img = img.resize((200, 200))
img_bg = ImageTk.PhotoImage(img)
lebel_img_bg = tk.Label(frame_home, image=img_bg)
lebel_img_bg.place(x=200, y=0)
btn_eda = tk.Button(frame_home, text="Show EDA", font=btnFont, width=20)
btn_eda.place(x=20, y=240)
btn_analyze = tk.Button(frame_home, text="Analyze Document",
                        font=btnFont, command=analyze)
btn_analyze.place(x=340, y=240)


frame_ana = tk.Frame(win, width=600, height=350)
# frame_ana.pack()
label_case = tk.Label(frame_ana, text="Case Details: ", font=("Verdana 12"))
label_case.place(x=12, y=10)
text_details = tk.Text(frame_ana, height=8, width=70)
text_details.place(x=12, y=40)
lebel_or = tk.Label(frame_ana, text="OR", font=(
    "Verdana 12"))
lebel_or.place(x=290, y=180)
btn_brouse = tk.Button(frame_ana, text="Upload PDF File", command=browse_file,
                       width=80, bg="cyan")
btn_brouse.place(x=12, y=210)
file_location = tk.Label(frame_ana, text="No file selected")
file_location.place(x=12, y=240)
btn_reset = tk.Button(frame_ana, text="Reset", width="12", height="1",
                      activebackground="red", bg="Pink", font=("Calibri 12 "))
btn_reset.place(x=240, y=280)
btn_back_home = tk.Button(frame_ana, text="Back", width="12", height="1",
                          activebackground="red", bg="Pink", font=("Calibri 12 "), command=back_home)
btn_back_home.place(x=60, y=280)
btn_details = tk.Button(frame_ana, text="Show Details", width="12", height="1",
                        activebackground="violet", bg="Pink", font=("Calibri 12 "), command=details)
btn_details.place(x=420, y=280)


frame_details = tk.Frame(win, width=600, height=350)
# frame_ana.pack()
label_name = tk.Label(frame_details, text="Victim Name: Name ")
label_name.place(x=10, y=10)
label_place = tk.Label(frame_details, text="Location: Location ")
label_place.place(x=10, y=30)
label_date = tk.Label(frame_details, text="Date & Time: 31 march 2023 ")
label_date.place(x=10, y=50)
label_cause = tk.Label(frame_details, text="Cause of death: It is cause")
label_cause.place(x=10, y=70)
label_demand = tk.Label(frame_details, text="Dowry demand :250000")
label_demand.place(x=10, y=90)
label_demand = tk.Label(
    frame_details, text="Police investigation details : Extracting information about the police investigation")
label_demand.place(x=10, y=110)
btn_predict = tk.Button(frame_details, text="Predict", width="12", height="1",
                        activebackground="violet", bg="Pink", font=("Calibri 12 "))
btn_predict.place(x=420, y=280)


win.mainloop()
