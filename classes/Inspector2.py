import random
import sys
import threading
import time

from classes.Component import Component
from classes.Shared import Shared


# Inspector2 inspects C2,C3 components with the given delays and
# sends them to the respective buffer, which are also references in the workstations
class Inspector2(threading.Thread):
    datadir1 = "data/servinsp22.dat"
    datadir2 = "data/servinsp23.dat"
    def __init__(self, component, buffer2, buffer3):
        super(Inspector2, self).__init__(name="Inspector2")
        self._lock = threading.Lock()
        self.component = component
        self.buffer2 = buffer2
        self.buffer3 = buffer3
        self.indicator = None

    # inspects item then decides which buffer to send to
    def inspectItem(self, delay, component):
        Shared.log("Inspector 2: Inspecting Item {} with Time Delay: {} seconds".format(component, delay))
        time.sleep(delay)
        Shared.log("Inspector 2: Finished {}".format(component))
        if component == Component.C2:
            self.buffer2.putItem(component)
        elif component == Component.C3:
            self.buffer3.putItem(component)

    def run(self):
        lst22 = []
        lst23 = []
        count22 = 0
        count23 = 0
        with open(self.datadir1, "rt") as data:
            for dataline in data:
                lst22.append(dataline.strip())
        with open(self.datadir2, "rt") as data:
            for dataline in data:
                lst23.append(dataline.strip())
        while count22 < len(lst22) and count23 < len(lst23) and not self.indicator:
            # pick a random number to decide between c2,c3 to inspect
            number = random.randint(0, 1)
            currentcomponent = self.component[number]
            if currentcomponent == Component.C2:
                count22 += 1
                self.inspectItem(Shared.timeFromString(lst22[count22]), currentcomponent)
            elif currentcomponent == Component.C3:
                count23 += 1
                self.inspectItem(Shared.timeFromString(lst23[count23]), currentcomponent)
        if not self.indicator:
            Shared.log("Inspector 2 is complete.")
            self.indicator = True
        else:
            Shared.log("Inspector 2 has been terminated.")
