import threading
import asyncio
import time

from classes.Shared import Shared

# Class BufferBox is a wrapper around buffer1,2,3 for C1 components
# so that Inspector1 and the three workstations can implement synchronizing logic
class BufferBox:

    def __init__(self, buffer1, buffer2, buffer3):
        self.buffer1 = buffer1
        self.buffer2 = buffer2
        self.buffer3 = buffer3
        self.cv = threading.Condition()
        self.blockedTime = 0

    # puts item into the buffer with the least amount of waiting components
    # if all 3 buffers are full, it blocks inspector 1 from adding components

    def putItem(self, item):
            self.cv.acquire()
            blocked = False
            bt = time.time()
            while(self.buffer1.size() == 2 and self.buffer2.size() == 2 and self.buffer3.size() == 2):
                Shared.log("Inspector 1: blocked")
                blocked = True
                # calculate time blocked here (can do in inspector1)
                self.cv.notifyAll()
                self.cv.wait()
            if(blocked):
                self.blockedTime += time.time() - bt
                
            if self.buffer3.size() == 0:
                self.buffer3.putItem(item)
            elif self.buffer2.size() == 0:
                self.buffer2.putItem(item)
            elif self.buffer3.size() == 1:
                self.buffer3.putItem(item)
            elif self.buffer2.size() == 1:
                self.buffer2.putItem(item)
            else: 
                self.buffer1.putItem(item)

            self.cv.notifyAll()
            self.cv.release()

    # gets item for workstation 1
    # blocks if the buffer is empty
    def getItem1(self):
            self.cv.acquire()
            while self.buffer1.size() == 0:
                # calc workstation1 block time here for c1, can either do it here or in workstation1
                self.cv.wait()
            item = self.buffer1.getItem()
            self.cv.notifyAll()
            self.cv.release()
            return item
    # gets item for workstation 2
    # blocks if the buffer is empty
    def getItem2(self):
            self.cv.acquire()
            while self.buffer2.size() == 0:
                # calc workstation2 block time here for c1, can either do it here or in workstation2
                self.cv.wait()
            item = self.buffer2.getItem()
            self.cv.notifyAll()
            self.cv.release()
            return item
    # gets item for workstation 3
    # blocks if the buffer is empty
    def getItem3(self):
            self.cv.acquire()
            while self.buffer3.size() == 0:
                # calc workstation3 block time here for c1, can either do it here or in workstation3
                self.cv.wait()
            item = self.buffer3.getItem()
            self.cv.notifyAll()
            self.cv.release()
            return item
