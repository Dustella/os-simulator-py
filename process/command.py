

from gui.main_frame import MainFrame


class Command:

    def __init__(self, info):
        print(info)
        self.action = info["actions"]
        if "target" in info:
            self.target = info["target"]
        if "amount" in info:
            self.amount = info["amount"]
        if "size" in info:
            self.size = info["size"]

    def set_process(self, process):
        self.process = process

    def excute(self):
        from core import OS
        os = OS()
        # mainfram = MainFrame()
        # mainfram.log("wiw")

        if self.action == "malloc":
            addr = os.memory_manager.allocate(self.size)
            if (addr == -1):
                print("Memory is full")
            self.process.record_memory_mapping(self.target, addr, self.size)

        if self.action == "free":

            start, size = self.process.memory_mapping[self.target]
            os.memory_manager.free(start, size)

        if self.action == "create_channel":

            os.channel_manager.create_channel(self.target)

        if self.action == "send":

            os.channel_manager.send(self.target, self.process.name)

        if self.action == "receive":

            os.channel_manager.receive(self.target, self.process.name)

        if self.action == "use_device":

            os.device_manager.use_device(self.target)

        if self.action == "release_device":

            os.device_manager.release_device(self.target)

        if self.action == "read_file":

            os.filesystem_manager.read_file(self.process.pid, self.target)
            return "IO"

        if self.action == "write_file":

            os.filesystem_manager.write_file(self.process.pid, self.target)
            return "IO"

        if self.action == "create_thread":

            os.thread_manager.create_thread(self.target, self.process.pid)

        if self.action == "destroy_thread":

            os.thread_manager.destroy_thread(self.target)

    def is_io(self):
        return self.action == "write_file" or self.action == "read_file"


#     {
#         "name": "P1",
#         "PID": 1,
#         "commands": [
#             {
#                 "actions": "malloc",
#                 "size": 1,
#                 "target": "var1"
#             },
#             {
#                 "receive": "channel1",
#                 "size": 10
#             },
#             {
#                 "actions": "free",
#                 "target": "var1"
#             },
#             {
#                 "actions": "malloc",
#                 "size": 1,
#                 "target": "var2"
#             },
#             {
#                 "actions": "free",
#                 "target": "var2"
#             },
#             {
#                 "actions": "malloc",
#                 "size": 1,
#                 "target": "var3"
#             },
#             {
#                 "actions": "free",
#                 "target": "var3"
#             }
#         ]
#     },
#     {
#         "name": "P2",
#         "PID": 2,
#         "commands": [
#             {
#                 "actions": "create_channel",
#                 "target": "channel1"
#             },
#             {
#                 "actions": "send",
#                 "target": "channel1",
#                 "amount": 10
#             },
#             {
#                 "actions": "use_device",
#                 "target": "device1"
#             },
#             {
#                 "actions": "release_device",
#                 "target": "device1"
#             },
#             {
#                 "actions": "use_device",
#                 "target": "printer1"
#             },
#             {
#                 "actions": "release_device",
#                 "target": "printer1"
#             },
#             {
#                 "actions": "use_device",
#                 "target": "printer2"
#             },
#             {
#                 "actions": "release_device",
#                 "target": "printer2"
#             }
#         ]
#     },
#     {
#         "name": "P3",
#         "PID": 3,
#         "commands": [
#             {
#                 "actions": "read_file",
#                 "target": "file1"
#             },
#             {
#                 "actions": "write_file",
#                 "target": "file1"
#             },
#             {
#                 "actions": "receive",
#                 "target": "channel1",
#                 "amount": 10
#             },
#             {
#                 "actions": "read_file",
#                 "target": "file2"
#             },
#             {
#                 "actions": "write_file",
#                 "target": "file2"
#             },
#             {
#                 "actions": "read_file",
#                 "target": "file3"
#             },
#             {
#                 "actions": "write_file",
#                 "target": "file3"
#             }

#         ]
#     }
# ]
