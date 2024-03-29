import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.title("Youtube utility tools")

        # Setting up the appearance of the main app
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")




        # Setting up the welcome label text
        Welcomelabel = customtkinter.CTkLabel(app,
                                              text="Welcome",
                                              fg_color="transparent",
                                              font=font_welcome)
        Welcomelabel.pack(padx=20, pady=20)

        # self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        # self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


app = App()
app.mainloop()
