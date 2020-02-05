import threading

class Workstation3(threading.Thread):
    def __init__(self, buffer1, buffer2):
        super().__init__()
        self.buffer1 = buffer1
        self.buffer2 = buffer2

    def processItem(self, t):
        self.buffer1.getItem()
        self.buffer2.getItem()
        time.sleep(t)
        print("Workstation 3 made P3")

    def run(self):
        f = open("data/ws3.dat","r")
        lines = f.readlines()
        for line in lines:
            self.processItem(float(line))

        print("Workstation 3 times done")