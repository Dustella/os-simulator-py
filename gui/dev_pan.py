# Create the lists
import tkinter as tk


class DevPannel:
    def __init__(self, window) -> None:

        self.window = window
        self.file_lists = tk.Listbox(self.window)

        self.thread_list = tk.Listbox(self.window)

        self.channel_list = tk.Listbox(self.window)

    def update_rows(self):
        # Update the tables
        # Update the lists
        from core import OS

        os = OS()
        file_list_data = os.filesystem_manager.get_status()
        self.file_lists.delete(0, tk.END)
        file_list_data.append("文件 content1.txt 未被读取")
        file_list_data.append("文件 content2.txt 未被读取")
        for item in file_list_data:
            self.file_lists.insert(tk.END, item)

        thread_list_data = os.thread_manager.get_status()
        self.thread_list.delete(0, tk.END)
        for item in thread_list_data:
            self.thread_list.insert(tk.END, item)

        channel_list_data = os.channel_manager.get_status()
        self.channel_list.delete(0, tk.END)
        for item in channel_list_data:
            self.channel_list.insert(tk.END, item)

    def get_widgets(self):
        return self.file_lists, self.thread_list, self.channel_list
