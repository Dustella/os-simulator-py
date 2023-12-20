from process import schedular


class Job:
    def __init__(self, name, arrival_time, service_time):
        self.name = name
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.waiting_time = 0
        self.response_ratio = 0

    def calculate_response_ratio(self, current_time):
        self.waiting_time = current_time - self.arrival_time
        self.response_ratio = (self.waiting_time +
                               self.service_time) / self.service_time
        return self.response_ratio


def hrrn_scheduling(jobs):
    current_time = 0
    schedule = []

    while jobs:
        # 计算所有作业的响应比
        for job in jobs:
            job.calculate_response_ratio(current_time)

        # 选择响应比最高的作业
        next_job = max(jobs, key=lambda job: job.response_ratio)
        jobs.remove(next_job)

        # 更新当前时间并记录作业
        current_time = max(
            current_time, next_job.arrival_time) + next_job.service_time
        schedule.append(next_job.name)

    return schedule


# 示例作业
jobs = [
    Job("Job1", 0, 3),
    Job("Job2", 2, 6),
    Job("Job3", 4, 4),
    Job("Job4", 6, 5),
    Job("Job5", 8, 2)
]


class HRRN:
    def schedule(scheduler: schedular.Scheduler):
        next_process = scheduler.get_next_process()

        while next_process:
            scheduler.set_current_process(next_process)
            result = next_process.run_to_die()
            if result == "IO":
                scheduler.block_process(next_process)
            if result == "Done":
                scheduler.add_to_died_processes(next_process)
            next_process = scheduler.get_next_process()


# 执行调度
schedule = hrrn_scheduling(jobs)
print("Job scheduling order:", schedule)
