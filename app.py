import customtkinter
import os
from PIL import Image

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
        self.navigation_frame.grid_rowconfigure(6, weight=1)

# nav image variable

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"images")
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

# home frame

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

# analyze frame
        self.analyze_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_title_label = customtkinter.CTkLabel(
            self.analyze_frame, text="Analyze Page")
        self.home_title_label.grid(
            row=0, column=0, pady=10,padx=10,sticky="ne")

# active the home button start
        self.select_frame_by_name("home")

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

# active the frame

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "analyze":
            self.analyze_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.analyze_frame.grid_forget()

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


if __name__ == "__main__":
    app = App()
    app.mainloop()
