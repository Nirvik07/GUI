import customtkinter
from customtkinter import filedialog
import os
from PIL import Image
import analyze
import EDA
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("light")

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

# configan the main window

        self.title("CourtAI")
        self.geometry("1100x650")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

# nav image variable

        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "home.png")), size=(26, 26))
        self.analyze_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "analyze.png")), size=(26, 26))
        self.history_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "restore.png")), size=(26, 26))
        self.extract_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "extract.png")), size=(26, 26))
        self.model_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "model.png")), size=(26, 26))
        self.predict_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "predict.png")), size=(26, 26))
        self.eda_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "eda.png")), size=(26, 26))

# nav button variable declearing & call

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  Home",
                                                   fg_color="transparent", image=self.logo_image, text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.home_button_event)
        self.home_button.grid(row=0, column=0, sticky="ew")

        self.analyze_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  Analyze Document", image=self.analyze_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.analyze_button_event)
        self.analyze_button.grid(row=1, column=0, sticky="ew")

        self.extract_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  Feature extraction", image=self.extract_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.extract_button_event)
        self.extract_button.grid(row=2, column=0, sticky="ew")

        self.model_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  Model selection", image=self.model_image,
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.model_button_event)
        self.model_button.grid(row=3, column=0, sticky="ew")

        self.prediction_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  Prediction", image=self.predict_image,
                                                         fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.prediction_button_event)
        self.prediction_button.grid(row=4, column=0, sticky="ew")

        self.history_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  Historical judgments", image=self.history_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.history_button_event)
        self.history_button.grid(row=5, column=0, sticky="ew")
        self.eda_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="  EDA", image=self.eda_image,
                                                  fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.eda_button_event)
        self.eda_button.grid(row=6, column=0, sticky="ew")

############################################################################################
################################    home frame    ##########################################
############################################################################################

        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_title_label = customtkinter.CTkLabel(
            self.home_frame, text="CourtAI", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.home_title_label.grid(
            row=0, column=0, pady=50)
        self.home_description_label = customtkinter.CTkLabel(
            self.home_frame, text="Description: Our Court Judgment Prediction and Document Analysis Software \nis a cutting-edge tool that utilizes machine learning algorithms to predict court judgments and analyze \nlegal documents. Our software is designed to save you time and money by providing accurate and reliable \nlegal insights at your fingertips.")
        self.home_description_label.grid(
            row=1, column=0)

############################################################################################
#########################    analyze frame    ##############################################
############################################################################################

        self.analyze_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.analyze_frame.grid_columnconfigure(0, weight=1)
        self.analyze_title_label = customtkinter.CTkLabel(
            self.analyze_frame, text="Analyze Page", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.analyze_title_label.grid(
            row=0, column=0, pady=10, padx=10, sticky="new")
# Analize Upload Frame
        self.analyze_upload_frame = customtkinter.CTkFrame(self.analyze_frame)
        self.analyze_upload_frame.grid(
            row=1, column=0, pady=10, padx=10, sticky="new")
        self.file_upload_btn = customtkinter.CTkButton(
            self.analyze_upload_frame, text="Upload PDF", command=self.upload_file)
        self.file_location_label = customtkinter.CTkLabel(
            self.analyze_upload_frame, text="No File Selected", text_color="red")
        self.analyze_file_btn = customtkinter.CTkButton(
            self.analyze_upload_frame, text="Analyze File", command=self.analyze_btn)
        self.file_upload_btn.grid(
            row=0, column=0, pady=10, padx=10, sticky="nw")
        self.file_location_label.grid(
            row=0, column=1, pady=10, padx=10, sticky="nw")
# file analyze frame
        self.analyze_file_frame = customtkinter.CTkFrame(self.analyze_frame)
        self.analyze_doc_label1 = customtkinter.CTkLabel(
            self.analyze_file_frame)
        self.analyze_doc_label2 = customtkinter.CTkLabel(
            self.analyze_file_frame)
        self.analyze_doc_label3 = customtkinter.CTkLabel(
            self.analyze_file_frame)
        self.analyze_doc_label4 = customtkinter.CTkLabel(
            self.analyze_file_frame)
        self.search_entry = customtkinter.CTkEntry(self.analyze_file_frame, width=200, placeholder_text="FIR,Police station")
        search_text=self.search_entry.get()
        self.analyze_search_btn = customtkinter.CTkButton(self.analyze_file_frame, text="Search", command=lambda:self.search_event(search_text), width=100)
        self.analyze_doc_search_label = customtkinter.CTkLabel(
            self.analyze_file_frame)
        


############################################################################################
############################    extract page    ############################################
############################################################################################

        self.extract_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.extract_title_label = customtkinter.CTkLabel(
            self.extract_frame, text="Extract Feature Page")
        self.extract_title_label.grid(
            row=0, column=0, pady=10, padx=10, sticky="ne")

############################################################################################
######################    model selection page   ###########################################
############################################################################################
        self.model_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.model_title_label = customtkinter.CTkLabel(
            self.model_frame, text="Model selection Page")
        self.model_title_label.grid(
            row=0, column=0, pady=10, padx=10, sticky="ne")

############################################################################################
#########################    Prediction page    ############################################
############################################################################################
        self.prediction_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.prediction_title_label = customtkinter.CTkLabel(
            self.prediction_frame, text="Prediction page")
        self.prediction_title_label.grid(
            row=0, column=0, pady=10, padx=10, sticky="ne")

############################################################################################
##################    Historical judgments   ###############################################
############################################################################################

        self.history_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.history_title_label = customtkinter.CTkLabel(
            self.history_frame, text="Historical judgments  Page")
        self.history_title_label.grid(
            row=0, column=0, pady=10, padx=10, sticky="ne")
############################################################################################
##########################        # EDA page    ############################################
############################################################################################

        self.eda_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.eda_frame,
                                                                 label_text="EDA Page", corner_radius=25, fg_color="transparent", height=500, width=1000)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)


        def combobox_callback(choice):
            print(choice)
            if choice == "chart1":
                self.canvas_frame1 = customtkinter.CTkFrame(
                self.scrollable_frame, height=500, width=500)
                self.canvas_frame1.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

                new_dictionary = EDA.bar_graph_allcases()
                fig2, ax2 = plt.subplots()
                bar = ax2.bar(list(new_dictionary.keys()),
                      list(new_dictionary.values()))
                ax2.set_title("Total number of cases in each year from 2001-2014")
                ax2.set_xlabel("Year")
                ax2.set_ylabel("Total no of crimes")
                self.canvas = FigureCanvasTkAgg(fig2, self.canvas_frame1)
                self.canvas.draw()
                self.canvas.get_tk_widget().grid(row=1, column=0)
            else:
                self.canvas_frame1.grid_forget()

            if choice == "chart2":
                self.canvas_frame2 = customtkinter.CTkFrame(
                self.scrollable_frame, height=500, width=500)
                self.canvas_frame2.grid(row=1, column=0, pady=5, padx=5,  sticky="nw",)
    
                new_dictionary2 = EDA.piechart_crime()
                fig3, ax3 = plt.subplots()
                pie = ax3.pie(new_dictionary2.values(), labels=new_dictionary2.keys(),
                      autopct='%1.1f%%')
                ax3.set_title("Percentage of Each Crime during 2001 - 2014")
                self.canvas = FigureCanvasTkAgg(fig3, self.canvas_frame2)
                self.canvas.draw()
                self.canvas.get_tk_widget().grid(row=1, column=0)
            else:
                self.canvas_frame2.grid_forget()

            if choice == "chart3":
                self.canvas_frame3 = customtkinter.CTkFrame(
                self.scrollable_frame, height=500, width=500)
                self.canvas_frame3.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

                new_dictionary3 = EDA.bar_graph_rape()
                fig4, ax4 = plt.subplots()
                bar1 = ax4.bar(list(new_dictionary3.keys()),
                           list(new_dictionary3.values()))
                ax4.set_title("Year wise rape case count")
                ax4.set_xlabel("Year")
                ax4.set_ylabel("Rape")
                self.canvas = FigureCanvasTkAgg(fig4, self.canvas_frame3)
                self.canvas.draw()
                self.canvas.get_tk_widget().grid(row=1, column=0)
            else:
                self.canvas_frame3.grid_forget()

            if choice == "chart4":
                self.canvas_frame4 = customtkinter.CTkFrame(
                self.scrollable_frame, height=500, width=500)
                self.canvas_frame4.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

                new_dictionary5 = EDA.bar_graph_Kidnapping_and_Abduction()
                fig5, ax5 = plt.subplots()
                bar2 = ax5.bar(list(new_dictionary5.keys()),
                       list(new_dictionary5.values()))
                ax5.set_title("Year wise kidnapping case count")
                ax5.set_xlabel("Year")
                ax5.set_ylabel("Kidnapping and Abduction")
                self.canvas = FigureCanvasTkAgg(fig5, self.canvas_frame4)
                self.canvas.draw()
                self.canvas.get_tk_widget().grid(row=1, column=0)
            else:
                self.canvas_frame4.grid_forget()

            if choice == "chart5":
                self.canvas_frame5 = customtkinter.CTkFrame(
                self.scrollable_frame, height=500, width=500)
                self.canvas_frame5.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

                new_dictionary1 = EDA.up_graph()
                fig, ax = plt.subplots()
                line, = ax.plot(list(new_dictionary1.keys()),
                        list(new_dictionary1.values()))
                ax.set_title("Sales by Year")
                ax.set_xlabel("Year")
                ax.set_ylabel("Dowry Deaths")
                self.canvas = FigureCanvasTkAgg(fig, self.canvas_frame5)
                self.canvas.draw()
                self.canvas.get_tk_widget().grid(row=1, column=0)
            else:
                self.canvas_frame5.grid_forget()

        self.combobox = customtkinter.CTkComboBox(self.scrollable_frame,
                                     values=["chart1", "chart2","chart3","chart4","chart5"],
                                     command=combobox_callback)
        self.combobox.grid(row=0, column=0, pady=5, padx=5, sticky="nw")
        self.combobox.set("None")

        # YEAR VS TOTAL NO OF CASES (BAR-CHART)
            

        

        # PIE-CHART ON ALL CASES
        #def visual_2():
            

        # YEAR VS RAPE CASES (BAR-GRAPH)
        #def visual_3():
            

        # YEAR VS KIDNAPPING AND ABDUCTION (BAR-GRAPH)
        #def visual_4():
            

        # YEAR VS DOWRY DEATH IN UP (LINE-GRAPH)
        #def visual_5():

            






# active the home button start
        self.select_frame_by_name("home")


# analize frame change

    def analyze_frame_switch(self, name):
        if name == "analyze":
            self.analyze_file_frame.grid(
                row=1, column=0, pady=10, padx=10, sticky="new")
        else:
            self.analyze_file_frame.grid_forget()
        if name == "upload":
            self.analyze_upload_frame.grid(
                row=1, column=0, pady=10, padx=10, sticky="new")
        else:
            self.analyze_upload_frame.grid_forget()

    def analyze_btn(self):
        self.analyze_frame_switch("analyze")
        words = analyze.file_preprocese(file_path=file_path)

        self.analyze_doc_label1.configure(
            text="Crime Charge Name :"+str(analyze.most_frequent(analyze.extract_charges_names(words))))
        self.analyze_doc_label2.configure(
            text="Crime Crime Name :"+str(analyze.most_frequent(analyze.extract_crime_names(words))))
        self.analyze_doc_label3.configure(
            text="IPC Sections Applicable "+str(analyze.most_frequent(analyze.extract_charges_names(words))))
        self.analyze_doc_label4.configure(
            text="Found evidence related to "+str(analyze.most_frequent(analyze.assault_weapon(words))))
        self.analyze_doc_label1.grid(
            row=1, column=0, pady=5, padx=5, sticky="nw")
        self.analyze_doc_label2.grid(
            row=2, column=0, pady=5, padx=5, sticky="nw")
        self.analyze_doc_label3.grid(
            row=3, column=0, pady=5, padx=5, sticky="nw")
        self.analyze_doc_label4.grid(
            row=4, column=0, pady=5, padx=5, sticky="nw")
        self.search_entry.grid(
            row=5, column=0, pady=5, padx=5, sticky="nw")
        self.analyze_search_btn.grid(
            row=5, column=1, pady=5, padx=5, sticky="nw")
        
    def search_event(self,search_text):
        self.analyze_doc_search_label.configure(text=analyze.search_detaile(file_path,search_text))
        self.analyze_doc_search_label.grid(
            row=6, column=0, pady=5, padx=5, sticky="nw")
        
        

# function for active coler in nav

    def select_frame_by_name(self, name):
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.analyze_button.configure(
            fg_color=("gray75", "gray25") if name == "analyze" else "transparent")
        self.extract_button.configure(
            fg_color=("gray75", "gray25") if name == "extract" else "transparent")
        self.model_button.configure(
            fg_color=("gray75", "gray25") if name == "model" else "transparent")
        self.prediction_button.configure(
            fg_color=("gray75", "gray25") if name == "prediction" else "transparent")
        self.history_button.configure(
            fg_color=("gray75", "gray25") if name == "history" else "transparent")
        self.eda_button.configure(
            fg_color=("gray75", "gray25") if name == "eda" else "transparent")

# active the frame

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "analyze":
            self.analyze_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.analyze_frame.grid_forget()
        if name == "extract":
            self.extract_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.extract_frame.grid_forget()
        if name == "model":
            self.model_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.model_frame.grid_forget()
        if name == "prediction":
            self.prediction_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.prediction_frame.grid_forget()
        if name == "history":
            self.history_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.history_frame.grid_forget()
        if name == "eda":
            self.eda_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eda_frame.grid_forget()

# button functions

    def home_button_event(self):
        self.select_frame_by_name("home")

    def analyze_button_event(self):
        self.select_frame_by_name("analyze")

    def extract_button_event(self):
        self.select_frame_by_name("extract")

    def model_button_event(self):
        self.select_frame_by_name("model")

    def prediction_button_event(self):
        self.select_frame_by_name("prediction")

    def history_button_event(self):
        self.select_frame_by_name("history")

    def eda_button_event(self):
        self.select_frame_by_name("eda")

    def upload_file(self):
        global file_path
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF File", '.pdf')])
        if (file_path):
            self.file_location_label.configure(
                text="File Selected: "+file_path, text_color="black")
            self.analyze_file_btn.grid(
                row=1, column=1, pady=10, padx=10, sticky="nw")
            

    def analyze(self):
        self.analyze_upload_frame.grid_forget()
            


if __name__ == "__main__":
    app = App()
    app.mainloop()
