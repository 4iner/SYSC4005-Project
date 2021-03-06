import sys
import threading
import time

from classes.BlackBox import Blackbox
from classes.Shared import Shared


# workstation 1 creates P1 given C1
# keeps a counter of P1s made 
class Workstation1(threading.Thread):
    datadir = "data/ws1.dat"
    def __init__(self, bufferbox, blackbox):
        super(Workstation1,self).__init__(name="Workstation1")
        self.buffer = bufferbox
        self.blackbox = blackbox
        self.counter = 0

    # Processes item given t delay. This will produce most products since it only needs C1
    def processItem(self, t):
        self.buffer.getItem1()
        Shared.log("Workstation 1: Got C1")
        Shared.log("Workstation 1 is processing P1 with %f delay" % t)
        self.blackbox.workstation1[0].append(time.time())
        time.sleep(t)
        self.blackbox.workstation1[1].append(time.time())
        self.blackbox.system[1].append(time.time())
        Shared.log("Workstation 1 made P1")
        self.counter += 1
        Shared.log("Workstation 1: Made {} so far".format(self.counter))

    def run(self):
        f = open(self.datadir, "r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))
