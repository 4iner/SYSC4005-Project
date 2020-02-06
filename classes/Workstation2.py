import threading
import time

from classes.Shared import Shared


class Workstation2(threading.Thread):
    def __init__(self, bufferbox, buffer2):
        super(Workstation2,self).__init__(name="Workstation2")
        self.bufferbox = bufferbox
        self.buffer2 = buffer2

    def processItem(self, t):
        self.bufferbox.getItem2()
        self.buffer2.getItem()
        Shared.log("Workstation 2 is processing P2 with %f delay" % t)
        time.sleep(t)
        Shared.log("Workstation 2 made P2")

    def run(self):
        f = open("data/ws2.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))

        Shared.log("Workstation 2 times done")