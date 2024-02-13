import tkinter
import customtkinter
from pytube import YouTube


class downloadvideos(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x500")
        self.title("Download Videos")

        # Adding title for the text/input field
        title = customtkinter.CTkLabel(self, text="Insert a youtube link")
        title.pack(padx=10, pady=10)

        # Link input
        url_var = tkinter.StringVar()
        link = customtkinter.CTkEntry(self, width=350, height=40, textvariable=url_var)
        link.pack()

        def startdownload():
            try:
                ytLink = link.get()
                ytObject = YouTube(ytLink, on_progress_callback=on_progress)
                video = ytObject.streams.get_highest_resolution()
                video.download()
                finishLabel.configure(text="Downloaded", text_color="blue")
            except:
                finishLabel.configure(text="Download Error", text_color="red")

        def on_progress(stream, chunk, bytesremaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytesremaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            per = str(int(percentage_of_completion))
            pPercentage.configure(text=per + '%')
            pPercentage.update()

            # Update progress bar
            progressBar.set(float(percentage_of_completion) / 100)

        # Progress Percentage
        pPercentage = customtkinter.CTkLabel(self, text="0%")
        pPercentage.pack()

        # Progress Bar
        progressBar = customtkinter.CTkProgressBar(self, width=400)
        progressBar.set(0)
        progressBar.pack(padx=10, pady=10)

        # Download Button

        download = customtkinter.CTkButton(self, text="Download", command=startdownload)
        download.pack(padx=10, pady=10)

        # Finished Downloading
        finishLabel = customtkinter.CTkLabel(self, text="")
        finishLabel.pack()

if __name__ == "__main__":
    app = downloadvideos()
    app.mainloop()
