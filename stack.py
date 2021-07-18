
import numpy as np
import time

class Stack(object):

    def __init__(self):
        self.item = []
        self.S = 0

    def pushstack(self, size):

        unsorted_list = np.arange(size)
        n = 0
        self.S = size
        while n < len(unsorted_list):
            self.item.append(unsorted_list[n])
            n = n + 1
        # print(item)
        pass

    def popstack(self):
        n=0
        while n<self.S:
            self.item.pop()
            # print(self.item.pop())
            n=n+1


def StackAll():
    stack = Stack()
    startpush = time.time()
    stack.pushstack(100000)
    startend = time.time()

    startpop = time.time()
    stack.popstack()
    endpop = time.time()
    StackAll1 ='            -------------Stack Push Data Time----------------\n' + \
    str('                        Time :')+str(startend) + str('\n                        Stack PoP Data Time         \n')\
    + str('                        Time :')+str(endpop)
    return StackAll1
    # print(StackAll1)




#
# 
# a=[1]
# b=[2]
# c=[3]
# list = [a.copy(),b.copy(),c.copy()]
# print(list)
# a.pop()
# b.pop()
# c.pop()
# print(list)




