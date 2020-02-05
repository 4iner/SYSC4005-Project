import threading
import time


class Inspector1(threading.Thread):

    def __init__(self, component, buffers):
        threading.Thread.__init__(self)
        self._lock = threading.Lock()
        self.component = component
        self.buffers = buffers

    def inspectItem(self, delay):
        print("Inspector 1: Inspecting Item - Time Delay: %s seconds" % delay)
        time.sleep(delay)
        self.sendItem()

    def sendItem(self):
        for buffer in self.buffers:
            if buffer.putItem(self.component):
                print("%s taken from Inspector 1" % self.component)
                return
        print("Inspector 1 blocked")

    def run(self):
        with open("data/servinsp1.dat", "r") as data:
            for dataline in data:
                self.inspectItem(float(dataline))


