import threading
import time

from classes.Shared import Shared

class Inspector1(threading.Thread):

    def __init__(self, component, bufferbox):
        super(Inspector1,self).__init__(name="Inspector1")
        self._lock = threading.Lock()
        self.component = component
        self.bufferbox = bufferbox

    def inspectItem(self, delay):
        Shared.log("Inspector 1: Inspecting Item - Time Delay: %s seconds" % delay)
        time.sleep(delay)
        self.sendItem()

    def sendItem(self):
        self.bufferbox.putItem(self.component)
        Shared.log("Inspect 1: inspected %s" % self.component)
        return

    def run(self):
        with open("data/servinsp1.dat", "r") as data:
            for dataline in data:
                self.inspectItem(Shared.timeFromString(dataline))


