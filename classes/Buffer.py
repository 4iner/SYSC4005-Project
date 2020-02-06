import queue
import threading
import time

class Buffer:
    def __init__(self):
        self.q = queue.Queue(3)
        self.qsize = 0
        self.lock = threading.Lock()
    
    def getItem(self):
            self.lock.acquire()
            if(self.qsize == 0):
                self.lock.release()
                return False
            item = self.q.get()
            self.qsize = self.qsize - 1
            self.lock.release()
            return item
    
    def putItem(self, item):
            self.lock.acquire()
            if self.q.qsize == 2:
                self.lock.release()
                return False
            self.q.put(item)
            self.qsize = self.qsize + 1
            self.lock.release()
            return True
    def size(self):
        return self.qsize
