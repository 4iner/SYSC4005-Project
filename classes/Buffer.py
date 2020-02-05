import queue

class Buffer:
    q = queue.Queue(3)
    def __init__(self):
        pass
    
    def getItem(self):
        item = self.q.get(block=True)
        return item
    
    def putItem(self, item):
        if self.q.qsize() == 2:
            return False
        else:
            self.q.put(item)
            return True
    def size(self):
        return self.q.qsize()
