
from typing import List
from context import get_all_threads


class ThreadManager:
    def __init__(self):
        self.threads = []
        self.thread_mapping = {}
        self.all_threads = get_all_threads()

    def create_thread(self, target, pid):
        self.thread_mapping[pid] = target
        self.threads.append(target)

    def destroy_thread(self, thread):
        self.threads.remove(thread)

    def get_status(self) -> List[str]:
        result = []
        for thread in self.all_threads:
            if thread in self.threads:
                message = f"Thread {thread} Running"
            else:
                message = f"Thread {thread} Not Running"
            result.append(message)
        return result
