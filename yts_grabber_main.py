import tkinter as tk
from tkinter import scrolledtext
import sys
import threading
import download_movies
import os

def donothing():
    pass

# Get the downloads directory of the current user and set the output directory
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
output_directory = os.path.join(downloads_dir, '')

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)  # Auto-scroll to the bottom

    def flush(self):
        pass

    def restore(self):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

main_window = tk.Tk()
main_window.title("YTS Grabber")
main_window.geometry("570x630")
main_window.configure(bg="#f0f0f0")

def show_about():
    tk.messagebox.showinfo("About", "Developed by: Mohammad Naim Elham\nVersion: 1.1\nMARCH 2024\n\nDedicated to my wife, to cancel his Netflix subscription\n   but she doesn't listen to me \n\nContact me on: solutionsstudioinbox@gmail.com for feedback or to report bugs")

def show_help():
    tk.messagebox.showinfo("Help", """Don't intefere with the app once a task start has started...
    Default output directory is current user's Downloads directory.
    Improvements are on the way....""")

menu_bar = tk.Menu(main_window)
help_menu = tk.Menu(menu_bar, tearoff=False)
help_menu.add_command(label="Help", command=show_help)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)
main_window.config(menu=menu_bar)

intro_message = tk.Message(main_window, text="Select Your Criteria:", anchor="center", bd=4, justify="center", width=400, bg="#f0f0f0", font=("Helvetica", 16, "bold"))
intro_message.grid(row=0, column=0, columnspan=6, pady=(10, 20))

labels = ["Min. Quality:", "Min. Rating:", "Genre:", "Sort By:", "Order By:"]
for col, label_text in enumerate(labels):
    label = tk.Label(main_window, text=label_text, bg="#f0f0f0", font=("Helvetica", 12))
    label.grid(row=1, column=col, padx=10)

quality_options = ["All", "480p", "720p", "1080p", "1080p.x265", "2160p", "3D"]
quality_selected_option = tk.StringVar(main_window)
quality_selected_option.set(quality_options[0])
final_quality = quality_options[0]