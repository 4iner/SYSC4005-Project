import threading
import time

from classes.Shared import Shared


class Workstation2(threading.Thread):
    def __init__(self, bufferbox, buffer2):
        super(Workstation2,self).__init__(name="Workstation2")
        self.bufferbox = bufferbox
        self.buffer2 = buffer2
        self.counter = 0

    def processItem(self, t):
        item2 = self.buffer2.getItem()
        Shared.log("Workstation 2: Got C2")
        item1 = self.bufferbox.getItem2()
        Shared.log("Workstation 2: Got C1")

        Shared.log("Workstation 2 is processing P2 with %f delay" % t)
        time.sleep(t)
        Shared.log("Workstation 2 made P2")
        self.counter += 1
        Shared.log("{} so far".format(self.counter))

    def run(self):
        f = open("data/ws2.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))

        Shared.log("Workstation 2 times done")
        Shared.log("Workstation 2 made {} P2".format(self.counter))