import queue
import threading
import time

class Buffer:
    def __init__(self, blackbox):
        self.q = queue.Queue(3)
        self.qsize = 0
        self.blackbox = blackbox

    # comment
    def getItem(self):
        if(self.qsize == 0):
            return False
        item = self.q.get()
        self.qsize = self.qsize - 1
        self.blackbox.component1[1].append(time.time())
        return item

    def putItem(self, item):
        if self.q.qsize == 2:
            return False
        self.q.put(item)
        self.qsize = self.qsize + 1
        self.blackbox.component1[0].append(time.time())
        return True
    
    def size(self):
        return self.qsize
