import sys
import threading
import time

from classes.Shared import Shared

# workstation 3 creates P3 given C1, C3
# keeps a counter of P3s made 
class Workstation3(threading.Thread):
    datadir = "data/ws3.dat"
    def __init__(self, bufferbox, buffer2, blackbox):
        super(Workstation3, self).__init__(name="Workstation3")
        self.bufferbox = bufferbox
        self.buffer2 = buffer2
        self.blackbox = blackbox
        self.counter = 0

    # Processes item given t delay. C3 is received first because
    # it may take longer to get C1
    def processItem(self, t):
        item2 = self.buffer2.getItem()
        Shared.log("Workstation 3: Got C3")
        item1 = self.bufferbox.getItem3()
        Shared.log("Workstation 3: Got C1")
        Shared.log("Workstation 3 is processing P3 with %f delay" % t)
        self.blackbox.workstation3[0].append(time.time())
        time.sleep(t)
        self.blackbox.workstation3[1].append(time.time())
        self.blackbox.system[1].append(time.time())
        Shared.log("Workstation 3 made P3")
        self.counter += 1
        Shared.log("Workstation 3: Made {} so far".format(self.counter))

    def run(self):
        f = open(self.datadir, "r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))
