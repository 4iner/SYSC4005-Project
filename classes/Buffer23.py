import queue
import threading

from classes.Shared import Shared

class Buffer23:
    
    def __init__(self):
        self.cv = threading.Condition()
        self.q = queue.Queue(3)
    
    def getItem(self):
            self.cv.acquire()

            while(self.q.qsize() == 0):
                self.cv.wait() 

           
            item = self.q.get()
            self.cv.notifyAll()
            self.cv.release()
            return item
    
    def putItem(self, item):
            self.cv.acquire()
            while self.q.qsize() >= 2:
                self.cv.wait()
            self.q.put(item)
            self.cv.notifyAll()
            self.cv.release()
    def size(self):
        return self.q.qsize()
