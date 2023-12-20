import tkinter as tk
from tkinter import ttk

from gui.logger import Logger
from gui.dev_pan import DevPannel

from gui.memory_table import MemoryTable
from gui.process_table import ProcessTable


class MainFrame:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, message: str):
        self.logger.write_log(message)

    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("OS Simulator")
        self.window.geometry("1200x700")
        self.init_widgets()
        self.init_titles()
        self.init_layout()

    def init_widgets(self):
        # Create the tables
        process_table = ProcessTable(self.window)
        self.process_table = process_table
        self.ready_queue, self.blocking_queue, self.ended_processes = process_table.get_widgets()

        # Create the lists
        dev_pan = DevPannel(self.window)
        self.device_pannel = dev_pan
        self.file_lists, self.thread_list, self.channel_list = dev_pan.get_widgets()
        self.current_process = process_table.get_current()

        # Create the text areas

        self.logger = Logger(root=self.window)
        self.logging = self.logger.log_text

        self.memory_table = MemoryTable(self.window, num_pages=24)

        self.bank_view = process_table.get_banker_view()
        # Add titles

    def init_titles(self):
        self.ready_queue_title = tk.Label(
            self.window, text="就绪队列", font=("微软雅黑", 13))
        self.blocked_queue_title = tk.Label(
            self.window, text="阻塞队列", font=("微软雅黑", 13))
        self.died_queue_title = tk.Label(
            self.window, text="结束的进程", font=("微软雅黑", 13))
        self.thread_title = tk.Label(self.window, text="线程", font=("微软雅黑", 13))
        self.filelist_title = tk.Label(
            self.window, text="文件列表", font=("微软雅黑", 13))
        self.channel_title = tk.Label(
            self.window, text="管道（进程同步）", font=("微软雅黑", 13))
        self.banker_title = tk.Label(
            self.window, text="银行家算法", font=("微软雅黑", 13))
        pass

    def init_layout(self):
        # row 0
        self.current_process.grid(row=0, column=0, columnspan=3, sticky="nsew")
        # row 1
        self.ready_queue_title.grid(
            row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.blocked_queue_title.grid(
            row=1, column=1, padx=5, pady=5, sticky="nsew")
        self.died_queue_title.grid(
            row=1, column=2, padx=5, pady=5, sticky="nsew")
        # row 2-3
        self.ready_queue.grid(row=2, column=0, padx=5,
                              pady=5, rowspan=2, sticky="nsew")
        self.blocking_queue.grid(
            row=2, column=1, padx=5, pady=5, rowspan=2, sticky="nsew")
        self.ended_processes.grid(
            row=2, column=2, padx=5, pady=5, rowspan=2, sticky="nsew")

        # row 4
        self.channel_title.grid(
            row=4, column=0, padx=5, pady=5, sticky="nsew")
        self.filelist_title.grid(
            row=4, column=1, padx=5, pady=5, sticky="nsew")
        self.thread_title.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        self.banker_title.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        # row 5-6
        self.channel_list.grid(row=5, column=0, padx=5,
                               pady=5, rowspan=2,  sticky="nsew")
        self.file_lists.grid(row=5, column=1, padx=5,
                             pady=5, rowspan=2, sticky="nsew")
        self.thread_list.grid(row=5, column=2, padx=5,
                              pady=5, rowspan=2, sticky="nsew")
        self.bank_view.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")
        #    row 7
        self.memory_table.get_widgets().grid(
            row=7, column=0, padx=5, pady=5, columnspan=3, sticky="nsew")
# row 8
        # self.logging.grid(row=8, column=0, columnspan=3, sticky="nsew")
        pass

    def update_data(self):
        self.device_pannel.update_rows()
        self.process_table.update_rows()
        self.memory_table.update_data()
        self.window.after(200, self.update_data)

    def run(self):
        # Run the main loop
        self.update_data()
        self.window.mainloop()


# Create an instance of the MainFrame class
