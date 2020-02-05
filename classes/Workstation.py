import threading
import time


class Workstation(threading.Thread):
    def __init__(self, name, buffer):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.name = name
        self.lst = []
        self.count = 0

    def processItem(self, t):
        if (self.buffer.getItem()):
            time.sleep(t)
            self.count += 1
            print("Workstation 1 made P1")

    def run(self):
        directory = "data/ws%s.dat" % self.name
        with open(directory, "r") as myfile:
            for myline in myfile:
                self.lst.append(myline.strip())
        while self.count < len(self.lst):
            self.processItem(float(self.lst[self.count]))
        print("Workstation 1 times done")
