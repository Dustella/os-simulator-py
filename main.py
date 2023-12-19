import asyncio
import multiprocessing
import threading
from core import OS
from gui.main_frame import MainFrame


if __name__ == "__main__":
    os = OS()
    os.prepare_processes()
    threading.Thread(target=os.run).start()
    # os.run()
    main_frame = MainFrame()
    main_frame.run()
