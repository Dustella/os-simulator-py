import asyncio
import threading
from time import sleep
from typing import List

from process.process import Process


class Scheduler:
    def __init__(self):
        self.blocking_list: List[Process] = []
        self.ready_list: List[Process] = []
        self.current_process = None
        self.scheduling_algorithm = None
        self.died_processes: List[Process] = []
        self.pre_ready_process: List[Process] = []

    def set_scheduling_algorithm(self, algorithm):
        self.scheduling_algorithm = algorithm

    def schedule(self):
        if self.scheduling_algorithm:
            self.scheduling_algorithm.schedule(self)

    def block_process(self, process: Process):
        self.blocking_list.append(process)

        def unblock_afterwards():
            sleep(6)
            self.wakeup_process(process)
        threading.Thread(target=unblock_afterwards).start()

    def wakeup_process(self, process: Process):
        self.blocking_list.remove(process)
        if process.pc >= len(process.commands) - 1:
            self.add_to_died_processes(process)
            return
        self.ready_list.append(process)

    def add_to_ready_list(self, process: Process):
        self.ready_list.append(process)

    def set_current_process(self, process: Process):
        # filter and remove same pid process in ready list
        self.ready_list = [p for p in self.ready_list if p.pid != process.pid]
        self.current_process = process

    def add_to_died_processes(self, process: Process):
        self.died_processes.append(process)

    def get_next_process(self) -> Process:
        if len(self.ready_list) > 0:
            return self.ready_list.pop(0)
        return None
