import threading
import time
from random import randrange


class Inspector(threading.Thread):

    def __init__(self, name, component, buffer):
        threading.Thread.__init__(self)
        self._lock = threading.Lock()
        self.name = name
        self.component = component
        self.buffer = buffer

    def inspectItem(self, delay):
        print("Inspector %s: Inspecting Item - Time Delay: %s seconds" % (self.name, delay))
        time.sleep(delay)
        self.sendItem()

    def sendItem(self):
        currentcomponent = None
        if len(self.component):
            number = randrange(2)
            if number == 1:
                currentcomponent = self.component[0]
            elif number == 2:
                currentcomponent = self.component[1]
        else:
            currentcomponent = self.component
        self._lock.acquire()
        try:
            while not self.buffer.putItem(currentcomponent):
                pass
                # print("Inspector %s blocked" % self.name)
        finally:
            self._lock.release()

        print("%s taken from Inspector %s" % (currentcomponent, self.name))

    def run(self):
        print("Starting " + self.name)
        directory = "data/servinsp%s.dat" % self.name
        with open(directory, "r") as data:
            for dataline in data:
                self.inspectItem(float(dataline))
        print("Exiting " + self.name)
