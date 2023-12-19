
from tkinter import ttk


class ProcessTable:
    def __init__(self, window):
        self.window = window
        self.create_tables()
        self.init_cols()

    def create_tables(self):
        self.ready_queue = ttk.Treeview(self.window)

        self.blocking_queue = ttk.Treeview(self.window)

        self.ended_processes = ttk.Treeview(self.window)

        self.current = ttk.Label(self.window, text="当前进程", font=("微软雅黑", 15))

    def get_current(self):
        return self.current

    def init_cols(self):
        self.ready_queue["columns"] = ("PID", "Memory", "Name")

        self.ready_queue.column("#0", width=0)
        self.ready_queue.column("PID", width=150)
        self.ready_queue.column("Memory", width=150)
        self.ready_queue.column("Name", width=150)
        self.ready_queue.heading("PID", text="PID")
        self.ready_queue.heading("Memory", text="Memory")
        self.ready_queue.heading("Name", text="Name")

        self.blocking_queue["columns"] = ("PID", "Memory", "Name")
        self.blocking_queue.column("#0", width=0)
        self.blocking_queue.column("PID", width=150)
        self.blocking_queue.column("Memory", width=150)
        self.blocking_queue.column("Name", width=150)
        self.blocking_queue.heading("PID", text="PID")
        self.blocking_queue.heading("Memory", text="Memory")
        self.blocking_queue.heading("Name", text="Name")

        self.ended_processes["columns"] = ("PID")
        self.ended_processes.column("#0", width=0)
        self.ended_processes.column("PID", width=150)
        self.ended_processes.heading("PID", text="PID")

    def update_rows(self):
        # Update the tables
        from core import OS

        os = OS()
        current_process = os.schedular.current_process
        ready_list = os.schedular.ready_list
        blocked_list = os.schedular.blocking_list
        died_list = os.schedular.died_processes

        self.ready_queue.delete(*self.ready_queue.get_children())
        for p in ready_list:
            row = (p.pid, p.get_mem_size(), p.name)
            self.ready_queue.insert("", "end", values=row)

        self.blocking_queue.delete(*self.blocking_queue.get_children())
        for p in blocked_list:
            row = (p.pid, p.get_mem_size(), p.name)
            self.blocking_queue.insert("", "end", values=row)

        self.ended_processes.delete(*self.ended_processes.get_children())
        for p in died_list:
            row = (p.pid)
            self.ended_processes.insert("", "end", values=row)

        self.current["text"] = "当前进程: " + \
            f"PID: {current_process.pid} 进程名: {
                current_process.name}" if current_process else "当前进程: None"

    def get_widgets(self):
        return self.ready_queue, self.blocking_queue, self.ended_processes