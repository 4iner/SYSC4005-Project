import threading
import time


class Workstation1(threading.Thread):
    def __init__(self, bufferbox):
        super().__init__()
        self.buffer = bufferbox
        super().__init__()

    def processItem(self, t):
        self.buffer.getItem1()
        time.sleep(t)
        print("Workstation 1 made P1")

    def run(self):
        f = open("data/ws1.dat","r")
        lines = f.readlines()
        for line in lines:
            print(line)
            self.processItem(float(line))

        print("Workstation 1 times done")
                