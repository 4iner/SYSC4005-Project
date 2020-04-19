import sys
import threading
import time

from classes.Shared import Shared

# workstation 2 creates P2 given C1, 2
# keeps a counter of P2s made 
class Workstation2(threading.Thread):
    datadir = "data/ws2.dat"
    def __init__(self, bufferbox, buffer2, blackbox):
        super(Workstation2, self).__init__(name="Workstation2")
        self.bufferbox = bufferbox
        self.buffer2 = buffer2
        self.blackbox = blackbox
        self.counter = 0

    # Processes item given t delay. C2 is received first because
    # it may take longer to get C1
    def processItem(self, t):
        item2 = self.buffer2.getItem()
        Shared.log("Workstation 2: Got C2")
        item1 = self.bufferbox.getItem2()
        Shared.log("Workstation 2: Got C1")
        Shared.log("Workstation 2 is processing P2 with %f delay" % t)
        self.blackbox.workstation2[0].append(time.time())
        time.sleep(t)
        self.blackbox.workstation2[1].append(time.time())
        Shared.log("Workstation 2 made P2")
        self.counter += 1
        Shared.log("{} so far".format(self.counter))

    def run(self):
        f = open(self.datadir, "r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))
