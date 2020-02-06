import threading
import asyncio

from classes.Shared import Shared

class BufferBox:

    

    def __init__(self, buffer1, buffer2, buffer3):
        self.buffer1 = buffer1
        self.buffer2 = buffer2
        self.buffer3 = buffer3
        self.cv = threading.Condition()
    
    def putItem(self, item):
            self.cv.acquire()
            while(self.buffer1.size() == 2 and self.buffer2.size() == 2 and self.buffer3.size() == 2):
                Shared.log("Inspector 1: blocked")
                print(self.buffer1.size())
                print(self.buffer2.size())
                print(self.buffer3.size())
                self.cv.notifyAll()
                self.cv.wait()  

            if self.buffer1.size() == 0 :
                self.buffer1.putItem(item)
            elif self.buffer2.size() == 0:
                self.buffer2.putItem(item)
            elif self.buffer3.size() == 0:
                self.buffer3.putItem(item)
            elif self.buffer1.size() == 1:
                self.buffer1.putItem(item)
            elif self.buffer2.size() == 1:
                self.buffer2.putItem(item)
            elif self.buffer3.size() == 1:
                self.buffer3.putItem(item)

            self.cv.notifyAll()
            self.cv.release()
            
    def getItem1(self):
            self.cv.acquire()
            while self.buffer1.size() == 0:
                
                self.cv.wait()
            item = self.buffer1.getItem()
            self.cv.notifyAll()
            self.cv.release()
            return item
    def getItem2(self):
            self.cv.acquire()
            while self.buffer2.size() == 0:
               
                self.cv.wait()
            item = self.buffer2.getItem()
            self.cv.notifyAll()
            self.cv.release()
            return item
    def getItem3(self):
            self.cv.acquire()
            while self.buffer3.size() == 0:
                
                self.cv.wait()
            item = self.buffer3.getItem()
            self.cv.notifyAll()
            self.cv.release()
            return item