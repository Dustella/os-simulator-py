import asyncio
import multiprocessing
import threading
from core import OS
from gui.main_frame import MainFrame
from utils.SCF import SCF


if __name__ == "__main__":

    print("请选择调度算法：")
    print("1、短任务优先")
    print("2、响应比调度")
    res = input()
    os = OS()
    os.prepare_processes()
    if res == "1":
        os.schedular.set_scheduling_algorithm(SCF)
        print("当前调度算法：短任务优先")
    elif res == "2":
        os.schedular.set_scheduling_algorithm()
        print("当前调度算法：响应比调度")
    threading.Thread(target=os.run).start()
    # os.run()
    main_frame = MainFrame()
    main_frame.run()
