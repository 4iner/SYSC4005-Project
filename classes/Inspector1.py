import sys
import threading
import time

from classes.Shared import Shared


# Inspector1 inspects C1 components with the given delays and
# sends them to the bufferbox, which decides the routing policy to the workstations
class Inspector1(threading.Thread):
    datadir = "data/servinsp1.dat"
    def __init__(self, component, bufferbox, blackbox):
        super(Inspector1, self).__init__(name="Inspector1")
        self._lock = threading.Lock()
        self.component = component
        self.bufferbox = bufferbox
        self.blackbox = blackbox
        self.indicator = None

    # inspect an item given a delay
    def inspectItem(self, delay):
        Shared.log("Inspector 1: Inspecting Item - Time Delay: %s seconds" % delay)
        self.blackbox.inspector1[0].append(time.time())
        self.blackbox.system[0].append(time.time())
        time.sleep(delay)
        self.blackbox.inspector1[1].append(time.time())
        self.sendItem()

    # finished processing, send item to bufferbox
    def sendItem(self):
        self.bufferbox.putItem(self.component)
        Shared.log("Inspect 1: inspected %s" % self.component)
        return

    def run(self):
        with open(self.datadir, "r") as data:
            for dataline in data:
                self.inspectItem(Shared.timeFromString(dataline))
                if self.indicator:
                    break
        if not self.indicator:
            Shared.log("Inspector 1 is complete.")
            self.indicator = True
        else:
            Shared.log("Inspector 1 has been terminated.")
