import customtkinter
from downloadvideos_window import downloadvideos

class featureWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x500")
        self.title("Start creating")

        downloadframe = customtkinter.CTkFrame(master=self, width=200, height=200)
        downloadframe.pack(padx=50, pady=120, anchor="w")

        title_label = customtkinter.CTkLabel(master=downloadframe, text="Download Videos")
        title_label.pack(padx=50, pady=20)

        info_label = customtkinter.CTkLabel(master=downloadframe, text="This will help you,")
        info_label.pack()
        info_label2 = customtkinter.CTkLabel(master=downloadframe, text="download youtube videos")
        info_label2.pack()

        download_button = customtkinter.CTkButton(master=downloadframe, text="Download", command=self.open_toplevel)
        download_button.pack(pady=10)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = downloadvideos(self)  # create window if it's None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists, focus it

if __name__ == "__main__":
    app = featureWindow()
    app.mainloop()
