import tkinter as tk


class FeatureDisplayWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Start Creating")
        self.geometry("500x500")

        label = tk.Label(self, text="Start Creating")
        label.pack(padx=20, pady=20)


