import tkinter
import customtkinter


# Setting up the App
app = customtkinter.CTk()
app.geometry("420x400")
app.title("Youtube Utility Tools")

# Setting Up the appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Deciding the font
font_welcome = ("Arial", 20, "bold")
font_YoutubeUtility = ("Arial", 30, "bold")
font_info =("Arial", 15, "bold")

# Setting up the welcome label text
Welcomelabel = customtkinter.CTkLabel(app,
                                      text="Welcome",
                                      fg_color="transparent",
                                      font=font_welcome)
Welcomelabel.pack(padx=20, pady=20)

# Setting up the Label for App text

Youtube_UtilityLabel = customtkinter.CTkLabel(app,
                                              text="Youtube Utility Tools",
                                              fg_color="transparent",
                                              font=font_YoutubeUtility)
Youtube_UtilityLabel.pack(padx=50, pady=50)

# Setting up the Label For information
infoLabel = customtkinter.CTkLabel(app,
                                   text="This tool will help you download,",
                                   fg_color="transparent",
                                   font=font_info)
infoLabel.pack()

infoLabel2 = customtkinter.CTkLabel(app,
                                   text="convert and edit youtube videos",
                                   fg_color="transparent",
                                   font=font_info)
infoLabel2.pack()


def startcreating():
    print("Button clicked")


# Button to enter the main app
Enter = customtkinter.CTkButton(app,
                                text="Start Creating",
                                fg_color= "white",
                                text_color="black",
                                hover_color="grey",
                                command=startcreating)
Enter.pack(padx=10, pady=20)

# app.wm_iconbitmap('Yd.png')
app.mainloop()
