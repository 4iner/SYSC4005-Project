import threading

class Workstation1(threading.Thread):
    def __init__(self, buffer):
        self.buffer = buffer

    def processItem(self, time):
        pass

    def run(self):
        pass