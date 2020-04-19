import queue
import threading
import time

from classes.Shared import Shared

# buffer23 is for C2,C3 components because it uses different logic from the other buffer
# queue.Queue() presents problems with a blocking get so we use our own thread synchronization methods of
# a condition variable cv, which lets us wait in the thread for something to happen
class Buffer23:

    def __init__(self):
        self.cv = threading.Condition()
        self.q = queue.Queue(3)
        self.blockedTime=0

    # get item from queue, blocking if empty
    def getItem(self):
            self.cv.acquire() # acquire lock

            while(self.q.qsize() == 0):
                # calculate time blocked here for workstation2/3, can be done here OR in workstation2/3 before/after get
                # can get workstation name from threading.currentThread().getName()
               
                self.cv.wait()  # release lock and wait


            item = self.q.get()
            self.cv.notifyAll() # notify waiting threads
            self.cv.release() # release lock
            return item
    # put item in queue, blocking if it is full
    def putItem(self, item):
            self.cv.acquire() # acquire lock
            blocked=False
            bt = time.time()
            while self.q.qsize() >= 2:
                Shared.log("Inspector 2: blocked")
                blocked=True
                # calculate time blocked here for inspector2
                # calculate inspector2 block time here maybe?
                self.cv.wait() # release lock and wait
            if (blocked):
                self.blockedTime += time.time() - bt
            self.q.put(item)
            self.cv.notifyAll() # notify waiting threads
            self.cv.release() # release lock
    def size(self):
        return self.q.qsize()
