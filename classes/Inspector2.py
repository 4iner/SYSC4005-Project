import random
import threading
import time

from classes.Component import Component


class Inspector2(threading.Thread):

    def __init__(self, component, buffer2, buffer3):
        threading.Thread.__init__(self)
        self._lock = threading.Lock()
        self.component = component
        self.buffer2 = buffer2
        self.buffer3 = buffer3

    def inspectItem(self, delay, component, buffer):
        print("Inspector 2: Inspecting Item - Time Delay: %s seconds" % delay)
        time.sleep(float(delay))
        self.sendItem(component, buffer)

    def sendItem(self, component, buffer):
        if buffer.putItem(component):
            print("%s taken from Inspector 2" % component)
            return
        print("Inspector 2 blocked")

    def run(self):
        lst22 = []
        lst23 = []
        count22 = 0
        count23 = 0
        with open("data/servinsp22.dat", "rt") as data:
            for dataline in data:
                lst22.append(dataline.strip())
        with open("data/servinsp23.dat", "rt") as data:
            for dataline in data:
                lst23.append(dataline.strip())
        while count22 < len(lst22) and count23 < len(lst23):
            number = random.randint(0, 1)
            currentcomponent = self.component[number]
            if currentcomponent == Component.C2:
                count22 += 1
                self.inspectItem(lst22[count22], currentcomponent, self.buffer2)
            elif currentcomponent == Component.C3:
                count23 += 1
                self.inspectItem(lst23[count23], currentcomponent, self.buffer3)
