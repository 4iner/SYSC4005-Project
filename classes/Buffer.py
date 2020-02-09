import queue
import threading
import time

class Buffer:
    def __init__(self):
        self.q = queue.Queue(3)
        self.qsize = 0

    # comment
    def getItem(self):
            if(self.qsize == 0):
                return False
            item = self.q.get()
            self.qsize = self.qsize - 1
            return item

    def putItem(self, item):
            if self.q.qsize == 2:
                return False
            self.q.put(item)
            self.qsize = self.qsize + 1
            return True
    def size(self):
        return self.qsize
