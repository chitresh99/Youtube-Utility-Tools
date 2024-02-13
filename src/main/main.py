import customtkinter
from feature import featureWindow

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("420x400")
        self.title("Youtube utility tools")

        # Deciding the font
        font_welcome = ("Arial", 20, "bold")
        font_YoutubeUtility = ("Arial", 30, "bold")
        font_info = ("Arial", 15, "bold")

        # Setting up the appearance
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # Setting up the welcome label text
        Welcomelabel = customtkinter.CTkLabel(self,
                                              text="Welcome",
                                              fg_color="transparent",
                                              font=font_welcome)
        Welcomelabel.pack(padx=20, pady=20)

        # Setting up the Label for App text
        Youtube_UtilityLabel = customtkinter.CTkLabel(self,
                                                      text="Youtube Utility Tools",
                                                      fg_color="transparent",
                                                      font=font_YoutubeUtility)
        Youtube_UtilityLabel.pack(padx=50, pady=50)

        # Setting up the Label For information
        infoLabel = customtkinter.CTkLabel(self,
                                           text="This tool will help you download,",
                                           fg_color="transparent",
                                           font=font_info)
        infoLabel.pack()

        infoLabel2 = customtkinter.CTkLabel(self,
                                            text="convert and edit youtube videos",
                                            fg_color="transparent",
                                            font=font_info)
        infoLabel2.pack()

        # Button to enter the main app
        Enter = customtkinter.CTkButton(self,
                                        text="Start Creating",
                                        fg_color="white",
                                        text_color="black",
                                        hover_color="grey",
                                        command=self.open_toplevel)
        Enter.pack(padx=10, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window =featureWindow(self)  # create window if it's None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists, focus it

if __name__ == "__main__":
    app = App()
    app.mainloop()
