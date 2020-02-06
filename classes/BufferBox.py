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
                self.cv.wait()  
            # print("Buffer 1 size: "+str(self.buffer1.size()))
            # print("Buffer 2 size: "+str(self.buffer2.size()))
            # print("Buffer 3 size: "+str(self.buffer3.size()))
            if self.buffer1.size() == 0 :
                self.buffer1.putItem(item)
                print("put in 1")
            elif self.buffer2.size() == 0:
                print("put in 2")
                self.buffer2.putItem(item)
            elif self.buffer3.size() == 0:
                print("put in 3")
                self.buffer3.putItem(item)
            elif self.buffer1.size() == 1:
                print("put in 1")
                self.buffer1.putItem(item)
            elif self.buffer2.size() == 1:
                print("put in 2")
                self.buffer2.putItem(item)
            elif self.buffer3.size() == 1:
                print("put in 3")
                self.buffer3.putItem(item)
            # print("Buffer 1 size: "+str(self.buffer1.size()))
            # print("Buffer 2 size: "+str(self.buffer2.size()))
            # print("Buffer 3 size: "+str(self.buffer3.size()))
            self.cv.notifyAll()
            self.cv.release()
            
    def getItem1(self):
            self.cv.acquire()
            item = self.buffer1.getItem()
            while not item:
                print("waiting for item1")
                item = self.buffer1.getItem()
                self.cv.wait()
            print("Got item buf 1")
            print(item)
            self.cv.notifyAll()
            self.cv.release()
            return item
    def getItem2(self):
            self.cv.acquire()
            item = self.buffer2.getItem()
            while not item:
                item = self.buffer2.getItem()
                self.cv.wait()
            self.cv.notifyAll()
            self.cv.release()
            return item
    def getItem3(self):
            self.cv.acquire()
            item = self.buffer3.getItem()
            while not item:
                item = self.buffer3.getItem()
                self.cv.wait()
            self.cv.notifyAll()
            self.cv.release()
            return item