import time

from multiprocessing import Process, Queue, Value


class MyHandler:
    def __init__(self):
        self.frame_queue = Queue()
        self.record_in_progress = Value('i', 0)

    def start(self):
        # starting first process for creating data
        p1 = Process(target=MyHandler.create_list, args=(self.frame_queue,))
        p2 = Process(target=MyHandler.preview_list, args=(self.frame_queue,))
        p1.start()
        time.sleep(0.1)
        p2.start()
        p2.join()


    @staticmethod
    def create_list(frame_queue):
        print("Called create list method")
        for i in range(100):
            frame_queue.put(i)
            print("Writing: ", i)

    @staticmethod
    def preview_list(frame_queue):
        print("Called preview list method")
        while not frame_queue.empty():
            print("Preview: ", frame_queue.get())

    @staticmethod
    def print_list():
        pass

def run():
    m = MyHandler()
    m.start()