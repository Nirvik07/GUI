import customtkinter
from customtkinter import filedialog
import os
from PIL import Image
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string
import re

customtkinter.set_appearance_mode("light")


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
        self.analyze_doc_label = customtkinter.CTkLabel(
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
        self.eda_title_label = customtkinter.CTkLabel(
            self.eda_frame, text="EDA Page")
        self.eda_title_label.grid(
            row=0, column=0, pady=10, padx=10, sticky="ne")


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
        global words
        words=self.file_preprocese()
        self.analyze_doc_label.configure(
            text="Crime Type Find :"+str(self.extract_crime_names(words))+"\n IPC Find "+str(self.extract_charges_names(words))+"\n Found evidence related to "+str(self.assault_weapon()))
        self.analyze_doc_label.grid(row=0, column=0)

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
        # self.analyze_upload_frame.grid(
        # row=1, column=0, pady=10, padx=10, sticky="new")
        self.analyze_upload_frame.grid_forget()

    def stem_list(self, lst):
        stemmed_lst = []
        for word in lst:
            stemmed_word = PorterStemmer().stem(word)
            stemmed_lst.append(stemmed_word)
        return stemmed_lst

    def file_preprocese(self):
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        global pdf_text
        pdf_text = ''
        for page in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page]
            pdf_text += page_obj.extract_text()
        tokens = nltk.word_tokenize(pdf_text)
        lowercase_words = [word.lower() for word in tokens]
        stop_words = set(stopwords.words('english'))
        words = [word for word in lowercase_words if word not in stop_words]
        stemmed_words = self.stem_list(words)
        # create an instance of the WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        # lemmatize each word in the list
        lemmatized_words = [lemmatizer.lemmatize(
            word) for word in stemmed_words]
        # Create a string containing all punctuation characters
        punctuation_chars = string.punctuation
        # Use a list comprehension to filter out the punctuations
        my_list_without_punctuations = [
            word for word in lemmatized_words if word not in punctuation_chars]
        return my_list_without_punctuations

    def extract_crime_names(self, strings):
        # A list of common crime names to search for
        crime_names = ["theft", "robbery", "assault", "murder", "fraud", "burglary", "kidnapping",
                       "arson", "Criminal force", "Outrageof modesty", "Assault of woman", "rape"]

        # Compile a regular expression pattern to match any of the crime names
        pattern = re.compile("|".join(crime_names), re.IGNORECASE)

        # Iterate over each string in the input list and search for matches
        matches = []
        for string in strings:
            match = pattern.search(string)
            if match:
                matches.append(match.group(0))

        # Return the list of matches
        return matches

    def extract_charges_names(self, strings):
        # A list of common crime names to search for
        crime_names = ["363", "366", "376", "506",
                       "509", "indian penal code", "ipc"]

        # Compile a regular expression pattern to match any of the crime names
        pattern = re.compile("|".join(crime_names), re.IGNORECASE)

        # Iterate over each string in the input list and search for matches
        matches = []
        for string in strings:
            match = pattern.search(string)
            if match:
                matches.append(match.group(0))

        # Return the list of matches
        return matches
    def assault_weapon(self):
        keywords = ['murder', 'weapon', 'bloodstain', 'DNA','blood', 'fingerprints','Witness']
        for keyword in keywords:
            for item in words:
                if re.search(r'\b{}\b'.format(keyword), item, flags=re.IGNORECASE):
                    return item
                
    # def find_date(self):
    #     judge_name_pattern = r"The Hon\'ble Justice [A-Z][a-z]+\s[A-Z][a-z]+\s?[A-Z]?[a-z]+"
    #     match = re.search(judge_name_pattern, pdf_text)
    #     if match:
    #         judge_name = match.group(1)
    #         return ("Judge name:", judge_name)
    #     else:
    #         return ("Judge name not found.")
if __name__ == "__main__":
    app = App()
    app.mainloop()