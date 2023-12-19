class RRAlgorithm:
    def __init__(self, time_slice):
        self.time_slice = time_slice

    def schedule(self, scheduler):
        next_process = scheduler.get_next_process()
        if next_process:
            scheduler.set_current_process(next_process)
