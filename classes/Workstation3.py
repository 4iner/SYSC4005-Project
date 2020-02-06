import threading
import time

from classes.Shared import Shared


class Workstation3(threading.Thread):
    def __init__(self, bufferbox, buffer2):
        super(Workstation3,self).__init__(name="Workstation3")
        self.bufferbox = bufferbox
        self.buffer2 = buffer2
        self.counter = 0

    def processItem(self, t):
        item2 = self.buffer2.getItem()
        Shared.log("Workstation 3: Got C3")
        item1 = self.bufferbox.getItem3()
        Shared.log("Workstation 3: Got C1")

        Shared.log("Workstation 3 is processing P3 with %f delay" % t)
        time.sleep(t)
        Shared.log("Workstation 3 made P3")
        self.counter += 1
        Shared.log("{} so far".format(self.counter))

    def run(self):
        f = open("data/ws3.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(Shared.timeFromString(line))

        Shared.log("Workstation 3 times done")
        Shared.log("Workstation 3 made {} P3".format(self.counter))