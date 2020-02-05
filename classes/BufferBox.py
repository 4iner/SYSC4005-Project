import threading
import asyncio

class BufferBox:

    cv = threading.Condition()

    def __init__(self, buffer1, buffer2, buffer3):
        self.buffer1 = buffer1
        self.buffer2 = buffer2
        self.buffer3 = buffer3
    
    def putItem(self, item):
        with self.cv:
            while(self.buffer1.size() == 2 and self.buffer2.size() == 2 and self.buffer3.size() == 2):
                print("Inspector 1 is blocked")
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
            
    def getItem1(self):
        with self.cv:
            self.buffer1.getItem()
            self.cv.notify()
    def getItem2(self):
        with self.cv:
            self.buffer2.getItem()
            self.cv.notify()
    def getItem3(self):
        with self.cv:
            self.buffer3.getItem()
            self.cv.notify()