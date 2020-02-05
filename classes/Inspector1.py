import threading

class Inspector1(threading.Thread):

    def __init__(self, buffer1, buffer2, buffer3):
        self.buffer1 = buffer1
        self.buffer2 = buffer2
        self.buffer3 = buffer3

    def inspectItem(self, time):
        pass
    
    def sendItem(self):
        pass

    def run(self):
        file = open(" servinsp1.dat","r")
        while(true):


