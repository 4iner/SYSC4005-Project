import threading
import time


class Workstation3(threading.Thread):
    def __init__(self, bufferbox, buffer2):
        super().__init__()
        self.bufferbox = bufferbox
        self.buffer2 = buffer2

    def processItem(self, t):
        self.bufferbox.getItem3()
        self.buffer2.getItem()
        print("Workstation 3 is processing P3 with %f delay" % t)
        time.sleep(t)
        print("Workstation 3 made P3")

    def run(self):
        f = open("data/ws3.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(float(line))

        print("Workstation 3 times done")