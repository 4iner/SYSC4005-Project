import threading

class Workstation3(threading.Thread):
    def __init__(self, buffer1, buffer2):
        self.buffer1 = buffer1
        self.buffer2 = buffer2

    def processItem(self, time):
        pass

    def run(self):
        pass