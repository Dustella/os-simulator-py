
from process import schedular


class FCFSAlgorithm:
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
