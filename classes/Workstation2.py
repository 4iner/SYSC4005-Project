import threading

class Workstation2(threading.Thread):
    def __init__(self, buffer1, buffer2):
        self.buffer1 = buffer1
        self.buffer2 = buffer2

    def processItem(self, t):
        self.buffer1.getItem()
        self.buffer2.getItem()
        time.sleep(t)
        print("Workstation 2 made P2")

    def run(self):
        f = open("data/ws2.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(float(line))

        print("Workstation 2 times done")