import tkinter as tk
from tkinter import scrolledtext


class Logger:
    _instance = None
    log_text: scrolledtext.ScrolledText

    def __init__(self, root):
        self.root = root

        # Create a scrolled text widget for log display
        self.log_text = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=40, height=10)

    def clear_log(self):
        # Clear the log text
        self.log_text.delete(1.0, tk.END)

    def write_log(self, message):
        # Append a log message to the scrolled text widget
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)  # Scroll to the end of the log
