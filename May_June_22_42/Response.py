###################### Question 1 ###########################
# StackData = [[] for i in range(10)]
# StackPointer = 0
#
# def OutPutStack():
#     global StackData, StackPointer
#     print(f"stack pointer is {StackPointer}")
#     print("Stack: ")
#     for i in range(len(StackData)):
#         print(StackData[i])
#
# def Push(NewItem:int):
#     global StackData, StackPointer
#     if StackPointer >= 10:
#         return False
#     else:
#         StackData[StackPointer].append(NewItem)
#         StackPointer += 1
#         return True
#
# def Push():
#     global StackData, StackPointer
#     TotalNumIn = 1
#     while TotalNumIn < 12:
#         NewItem = int(input("Please enter a number"))
#         if StackPointer >= 10:
#             print("Stack Over, item not added")
#         else:
#             StackData[StackPointer] = NewItem
#             StackPointer += 1
#             print("Item added")
#         TotalNumIn += 1
#
#     OutPutStack()
# Push()
# def Pop():
#     global StackData, StackPointer
#     if StackPointer == 0:
#         return -1
#     else:
#         StackPointer -= 1
#         item = StackData[StackPointer]
#         StackData[StackPointer] = None
#         return item
#
# Pop()
# Pop()
# Pop()
# print(StackData)
from torch.utils.data import Dataset

################### Question 2 ###########################
import random
ArrayData =  [[random.randint(1,100) for i in range(10)] for j in range(10)]
ArrayLength = 10

def OutputArray():
    global ArrayLength, ArrayData

    for i in range(10):
        thisArr = [None for i in range(ArrayLength)]
        for j in range(10):
            thisArr[j] = ArrayData[i][j]
        print(thisArr)

OutputArray()
for x in range(0, ArrayLength):
    for y in range(0, ArrayLength-1):
        for z in range(0, ArrayLength - y -1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                TempValue =  ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z + 1] = TempValue
print("Sorted Array")
OutputArray()



def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower+Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            elif SearchArray[0][Mid] < SearchValue:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)

    else:
        return -1

Num = ArrayData[0][0]
print(Num)
print(BinarySearch(ArrayData, 0, 10, Num))

