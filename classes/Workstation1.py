import threading
import time

class Workstation1(threading.Thread):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer

    def processItem(self, t):
        if(self.buffer.getItem()):
            time.sleep(t)
            print("Workstation 1 made P1")

    def run(self):
            f = open("data/ws1.dat","r")
            lines = f.readlines()
            for line in lines:
                self.processItem(float(line))

            print("Workstation 1 times done")
                