from typing import List
from external.device_man import DeviceManager
from external.filesystem_man import FilesystemManager
from external.thread_man import ThreadManager
from memory.mem_manager import MemoryManager
from process.process import Process
from process.schedular import Scheduler
from sync.channel import ChannelManager
from context import proceses
from process.command import Command


class OS:
    _instance = None
    memory_manager = MemoryManager(24)
    device_manager = DeviceManager()
    filesystem_manager = FilesystemManager()
    thread_manager = ThreadManager()
    schedular = Scheduler()
    channel_manager = ChannelManager()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # self.memory_manager = MemoryManager(100, 100)
        # self.device_manager = DeviceManager()
        # self.filesystem_manager = FilesystemManager()
        # self.thread_manager = ThreadManager()
        # self.schedular = schedular()
        # self.channel_manager = ChannelManager()
        pass

    def prepare_processes(self):
        pid_set = set()
        from random import randint
        for process in proceses:
            new_pid = randint(0, 100)
            while new_pid in pid_set:
                new_pid = randint(0, 100)
            process_item = Process(process["PID"])
            instructions: List[Command] = []
            for command in process["commands"]:
                command_line = Command(command)
                command_line.set_process(process_item)

                instructions.append(command_line)
            process_item.set_commands(commands=instructions)
            process_item.set_name(process["name"])
            self.schedular.add_to_ready_list(process=process_item)

    def run(self):
        self.schedular.schedule()
