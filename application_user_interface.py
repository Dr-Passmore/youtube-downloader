import logging
import tkinter as tk
from tkinter import messagebox


class UserInterface:
    
    def __init__(self) -> None:
        '''
        Initialise the UserInterface class.
        '''
        self.window = tk.Tk()
        self.window.title("YouTube Video Downloader")
        self.window.geometry("800x500")
        UserInterface.create_widgets(self)
        self.log_display()
        UserInterface.create_window(self)

    def create_window(self):
        '''
        Creates the main window of the application.
        '''
        self.window.mainloop()
        
    def exit(self):
        '''
        Exits the application.
        '''
        self.window.destroy()

    def confirm_exit(self):
        '''
        Displays a confirmation dialog box to confirm if the user wants
        to exit the application.
        '''
        result = messagebox.askquestion(
            "Confirm Exit", "Do you really want to exit the application?")
        if result == 'yes':
            UserInterface.exit(self)
    
    def setup_window_close_event(self):
        '''
        Sets up the close event for the main window.
        '''
        self.window.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    def create_widgets(self):
        # Exit confirmation checks for close event
        self.setup_window_close_event()
        # Exit button added
        exit_button = tk.Button(self.window, 
                                text="Exit", 
                                command=self.confirm_exit)
        exit_button.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)
        
        self.log_text = tk.Text(self.window, height=10, state=tk.DISABLED)
        self.log_text.pack(side=tk.BOTTOM,
                           anchor=tk.S,
                           fill=tk.X,
                           padx=20,
                           pady=20)
    def url_input():
        pass

    def display_quality():
        pass

    def select_file_location():
        pass

    def download_button():
        pass

    def log_display(self):
        '''
        Displays the last 5 log messages in the application window.
        '''
        log_messages = self.get_last_5_log_messages()
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)  # Clear previous log messages
        for message in log_messages:
            self.log_text.insert(tk.END, message)
        self.log_text.config(state=tk.DISABLED)
        
    def get_last_5_log_messages(self):
        '''
        Retrieves the last 5 log messages from the log file.
        '''
        # Function to retrieve the last 5 log messages from the log file
        log_messages = []
        with open('YouTubeVideoDownloader.log', 'r') as log_file:
            lines = log_file.readlines()
            log_messages = lines[-5:]
        return log_messages


logging.basicConfig(filename='YouTubeVideoDownloader.log',
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    UserInterface()
