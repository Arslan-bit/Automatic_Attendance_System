import random
import time
from Sorting_Algorithems import *
import numpy as np
import sys

def all_sorting():
    unsorted_list = []
    for i in range(0, 1000):
        n = random.randint(1, 99)
        unsorted_list.append(n)

    ANS = unsorted_list
    # print(ANS)
    D = ANS.copy()
    I = ANS.copy()
    S = ANS.copy()

    start = time.time()
    Bubbly(D)
    end = time.time()
    BT = end-start
    # print("Bubble time = ", BT)

    # print("-----------------------------------------")

    start1 = time.time()
    Insertion(I)
    end1 = time.time()
    IT = end1-start1
    # print("Insertion time = ", IT)

    # print("-----------------------------------------")

    start2 = time.time()
    selection_sort(S)
    end1 = time.time()
    ST = end1-start2

    # print("selection_sort time = ", ST)

    AA = (str("\n\n             --------------------Sorting----------------------  ") + str("\n                       Bubble time = " + str(BT)) + str("\n                       Insertion time = ")+str(IT) + str("\n                       selection_sort time = ") + str(ST) )
    return AA




def Arrey_List():

    list1 = [1]
    list3 =np.arange(1)
    print(str("Simple List[] 1 element size = ")+str(sys.getsizeof(list1))+str("\nSimple Array{} 1 element size = ")+str(list3.itemsize * list3.size))

    ZZ= (str("\n\n             ----------Difference btw List and Array Size-------")+str("\n                        Simple List[] 1 element size = ")+str(sys.getsizeof(list1))+str("\n                        Simple Array{} 1 element size = ")+str(list3.itemsize * list3.size))
    return ZZ






