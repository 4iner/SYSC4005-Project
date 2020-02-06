import threading
import time

from classes.Shared import Shared


class Workstation1(threading.Thread):
    def __init__(self, bufferbox):
        super(Workstation1,self).__init__(name="Workstation1")
        self.buffer = bufferbox

    def processItem(self, t):
        self.buffer.getItem1()
        Shared.log("Workstation 1 is processing P1 with %f delay" % t)
        time.sleep(t)
        Shared.log("Workstation 1 made P1")

    def run(self):
        f = open("data/ws1.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))

        Shared.log("Workstation 1 times done")
                