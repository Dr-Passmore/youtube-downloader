import logging
import tkinter as tk

class UserInterface:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("YouTube Video Downloader")
        self.window.geometry("500x500") 
        

        UserInterface.create_window(self)

    def create_window(self):
        self.window.mainloop()
        

    def exit():
        pass

    def confirm_exit():
        pass

    def url_input():
        pass
    
    def display_quality():
        pass

    def select_file_location():
        pass

    def download_button():
        pass

logging.basicConfig(filename='YouTubeVideoDownloader.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    UserInterface()