from time import sleep
from process import command
from typing import List


class Process:
    def __init__(self, pid):
        self.pid = pid
        self.pc = 0
        self.memory_mapping = {}

    def set_name(self, name):
        self.name = name

    def set_commands(self, commands: List[command.Command]):
        self.commands = commands

    def record_memory_mapping(self, var, start_page, size):
        self.memory_mapping[var] = (start_page, size)

    def get_mem_size(self):
        return sum([size for _, size in self.memory_mapping.values()])

    def run_to_die(self):
        while self.pc < len(self.commands):
            command = self.commands[self.pc]
            if command.is_io():
                command.excute()
                return "IO"
            command.excute()
            sleep(2)
            self.pc += 1

        return "Done"
