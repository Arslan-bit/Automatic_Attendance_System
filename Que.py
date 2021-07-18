
import numpy as np
import time

class Queue(object):

    def __init__(self):
        self.item = []
        self.S = 0

    def pushq(self,size ):

        unsorted_list = np.arange(size)
        n = 0
        self.S = size
        while n < len(unsorted_list):
            self.item.append(unsorted_list[n])
            n = n + 1
        # print(item)
        pass

    def popq(self):
        n=0
        while n<self.S:
            self.item.pop(0)
            # print(self.item.pop(0))
            n=n+1


def QueAll():

    queue = Queue()
    startpush = time.time()
    queue.pushq(100000)
    startend = time.time()
    startpop = time.time()
    queue.popq()
    endpop = time.time()
    QueueAll1 = '\n\n             -------------Queue Push Data Time----------------\n' + str('                        Time :')+str(startend)+str('\n                        Queue PoP Data Time            \n' )+ str('                        Time :')+str(endpop)
    return QueueAll1
    print(QueueAll1)