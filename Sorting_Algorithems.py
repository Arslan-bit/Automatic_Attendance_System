def Bubbly(mylist):

    lenghtofList = len(mylist)

    rangeoflist = range(1,lenghtofList)
    # print(new1)
    for i in rangeoflist:

        numbertosort = mylist[i]

        while mylist[i-1] > numbertosort and i > 0:

            temp = mylist[i]

            mylist[i] = mylist[i-1]

            mylist[i-1] = temp

            i = i - 1
    # print(mylist)


def Insertion(list):

    lenoflist = len(list)
    rangeoflist = range(1, lenoflist)
    for eachvalue in rangeoflist:

        isSorted = list[eachvalue]
        while list[eachvalue - 1] > isSorted and eachvalue > 0:
            temp = list[eachvalue]

            list[eachvalue] = list[eachvalue - 1]
            list[eachvalue - 1] = temp
            eachvalue = eachvalue - 1
    # print(list)


def selection_sort(list):
    for i in range(0, len(list) - 1):
        minIndex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        if minIndex != i:
            list[i], list[minIndex] = list[minIndex], list[i]

    # print(list)