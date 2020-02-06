import queue
import threading

from classes.Shared import Shared

class Buffer23:
    
    def __init__(self):
        self.cv = threading.Condition()
        self.q = queue.Queue(3)
    
    def getItem(self):
            self.cv.acquire()
            while(self.q.empty()):
                Shared.log("Buffer 2: blocked")
                self.cv.wait() 
            item = self.q.get(block=True)
            self.cv.notify()
            self.cv.release()
            return item
    
    def putItem(self, item):
            self.cv.acquire()
            while self.q.qsize() == 2:
                self.cv.wait()
            self.q.put(item)
            self.cv.notify()
            self.cv.release()
    def size(self):
        return self.q.qsize()
