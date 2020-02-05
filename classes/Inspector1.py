import threading
import time


class Inspector1(threading.Thread):

    def __init__(self, component, bufferbox):
        threading.Thread.__init__(self)
        self._lock = threading.Lock()
        self.component = component
        self.bufferbox = bufferbox

    def inspectItem(self, delay):
        print("Inspector 1: Inspecting Item - Time Delay: %s seconds" % delay)
        time.sleep(delay)
        self.sendItem()

    def sendItem(self):
        self.bufferbox.putItem(self.component)
        print("Inspect 1 inspected %s" % self.component)
        return

    def run(self):
        with open("data/servinsp1.dat", "r") as data:
            for dataline in data:
                self.inspectItem(float(dataline))


