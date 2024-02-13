from tkinter import *
import tkinter as tk

# Setting Up the app
window = Tk()
window.geometry("420x400")
window.title("Youtube Utility Tools")

# Setting up the appearance
window.configure(background="#242424")

# Setting up the font
font_welcome = ("Arial", 15, "bold")
font_YoutubeUtility = ("Arial", 20, "bold")
font_info = ("Arial", 10, "bold")

# Setting up the welcome label
Welcomelabel = tk.Label(window,
                        text="Welcome",
                        fg='white',
                        bg='#242424',
                        font=font_welcome)
Welcomelabel.pack(padx=20, pady=20)

# Setting up the Label for App text

Youtube_UtilityLabel = tk.Label(window,
                                text="Youtube Utility Tools",
                                fg='white',
                                bg='#242424',
                                font=font_YoutubeUtility)
Youtube_UtilityLabel.pack(padx=50, pady=50)

# Setting up the Label For information
infoLabel = tk.Label(window,
                     text="This tool will help you download,",
                     fg='white',
                     bg='#242424',
                     font=font_info)
infoLabel.pack()

infoLabel2 = tk.Label(window,
                      text="convert and edit youtube videos",
                      fg='white',
                      bg='#242424',
                      font=font_info)
infoLabel2.pack()

# Function for Entry window

def feature_display_window():
    entry_window = Toplevel(window)
    entry_window.title("Feature Display Window")


# Setting up the entry button

Entry = Button(window,
               text="Start creating",
               foreground='black',
               activeforeground='#f7f6f2',
               activebackground='#202120',
               command= feature_display_window
               )
Entry.pack(padx=10, pady=20)

window.mainloop()
