import queue
import threading
import time

class Buffer:
    def __init__(self, name, blackbox):
        self.q = queue.Queue(3)
        self.qsize = 0
        self.blackbox = blackbox
        self.name = name

    # comment
    def getItem(self):
        if(self.qsize == 0):
            return False
        item = self.q.get()
        self.qsize = self.qsize - 1
        if self.name == 1:
            self.blackbox.component1[1].append(time.time())
        elif self.name == 2:
            self.blackbox.component12[1].append(time.time())
        elif self.name == 3:
            self.blackbox.component13[1].append(time.time())
        return item

    def putItem(self, item):
        if self.q.qsize == 2:
            return False
        self.q.put(item)
        self.qsize = self.qsize + 1
        if self.name == 1:
            self.blackbox.component1[0].append(time.time())
        elif self.name == 2:
            self.blackbox.component12[0].append(time.time())
        elif self.name == 3:
            self.blackbox.component13[0].append(time.time())
        return True
    
    def size(self):
        return self.qsize
