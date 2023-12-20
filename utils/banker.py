

class BankerAlgorithm:
    def __init__(self, max_resources):
        self.max_resources = max_resources
        self.allocated_resources = {}
        self.max_demands = {}

    def add_process(self, process_id, max_demand):
        if process_id in self.max_demands:
            raise ValueError(f"Process {process_id} already exists.")
        self.max_demands[process_id] = max_demand
        self.allocated_resources[process_id] = [0] * len(self.max_resources)

    def request_resources(self, process_id, request):
        if not self._can_allocate(process_id, request):
            return False
        for i in range(len(request)):
            self.allocated_resources[process_id][i] += request[i]
            self.max_resources[i] -= request[i]
        return True

    def release_resources(self, process_id, release):
        for i in range(len(release)):
            self.allocated_resources[process_id][i] -= release[i]
            self.max_resources[i] += release[i]

    def _can_allocate(self, process_id, request):
        for i in range(len(request)):
            if request[i] > self.max_resources[i] or \
               request[i] > (self.max_demands[process_id][i] - self.allocated_resources[process_id][i]):
                return False
        return True

    def is_safe_state(self):
        work = self.max_resources[:]
        finish = {process: False for process in self.max_demands}

        while True:
            made_progress = False
            for process, max_demand in self.max_demands.items():
                if not finish[process] and all(self.allocated_resources[process][i] + work[i] >= max_demand[i] for i in range(len(work))):
                    for i in range(len(work)):
                        work[i] += self.allocated_resources[process][i]
                    finish[process] = True
                    made_progress = True

            if not made_progress:
                break

        return all(finish.values())


# 示例使用
if __name__ == "__name__":
    # 此处是测试
    max_resources = [10, 5, 7]  # 定义系统资源
    banker = BankerAlgorithm(max_resources)

    # 添加进程
    banker.add_process("P1", [7, 5, 3])
    banker.add_process("P2", [3, 2, 2])
    banker.add_process("P3", [9, 0, 2])
    banker.add_process("P4", [2, 2, 2])
    banker.add_process("P5", [4, 3, 3])

    # 请求资源
    banker.request_resources("P1", [0, 1, 0])

    # 检查系统是否处于安全状态
    print("Is safe state:", banker.is_safe_state())


fin_entris = {}
# first_strike = True


def get_entries():
    from core import OS

    os = OS()

    res = {}
    ls = os.schedular.ready_list
    from random import randint
    for i in ls:
        men = randint(0, 3)*2
        dev = randint(0, 2)
        res[i] = (men, dev)
    return res
