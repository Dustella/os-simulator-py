import threading
import threading
from typing import List
from context import get_all_channels


class Channel:
    def __init__(self, name):
        self.buffer = []
        self.lock = threading.Lock()
        self.empty = threading.Condition(self.lock)
        self.full = threading.Condition(self.lock)
        self.name = name

    def send(self, data):
        with self.full:
            self.buffer.append(data)
            self.empty.notify()

    def receive(self):
        with self.empty:
            while not self.buffer:
                self.empty.wait()
            return self.buffer.pop(0)


class ChannelManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.all_channels = get_all_channels()
        self.channel_status = {}

    def create_channel(self, name):
        with self.lock:
            channel = Channel(name)
            self.channel_status[name] = {
                "sending": [],
                "receiving": []
            }
            return channel

    def destroy_channel(self, channel):
        with self.lock:
            del self.channel_status[channel]

    def get_status(self) -> List[str]:
        result = []
        for channel in self.all_channels:
            if channel in self.channel_status:
                message = f"{channel} 激活，发送：{self.channel_status[channel]['sending']}，接收：{
                    self.channel_status[channel]['receiving']}"
            else:
                message = f"{channel} 不活动"
            result.append(message)
        return result

    def send(self, channel_name, process_name):
        self.channel_status[channel_name]["sending"].append(process_name)
        pass

    def receive(self, channel_name, process_name):
        self.channel_status[channel_name]["receiving"].append(process_name)
        pass
