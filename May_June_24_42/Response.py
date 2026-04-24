# ###################### Question 1 ###############################
# WordArray = []
# NumberWords = 0
#
# def ReadWords(FileName):
#     global WordArray
#     global NumberWords
#     count = 0
#     with open(FileName, "r") as f:
#         for line in f:
#             WordArray.append(line.strip())
#             count = count + 1
#     NumberWords = count-1
#
# choice = input("Please enter 1:"
#                "- easy"
#                "- medium"
#                "- hard")
# if choice == "easy":
#     ReadWords("Easy.txt")
# elif choice == "medium":
#     ReadWords("Medium.txt")
# elif choice == "hard":
#     ReadWords("Hard.txt")
# else:
#     print("Wrong Input")
#
#
# def Play():
#     global WordArray, NumberWords
#     print(f"Main word is {WordArray[0]} and the Number of words are {NumberWords}")
#     TotalAnswers = 0
#     attempts = 0
#     useranswer = []
#     while True:
#         Userchoice = input("Please enter a word or 'no' to stop:")
#         if Userchoice == "no":
#             if attempts>0:
#                 print((len(useranswer)/len(WordArray))*100)
#                 for i in range(len(WordArray)):
#                     if WordArray[i] not in useranswer:
#                         print(WordArray[i])
#             break
#         else:
#             if Userchoice in WordArray:
#                 useranswer.append(Userchoice)
#                 TotalAnswers = TotalAnswers + 1
#                 print("This is an answer!")
#                 index = WordArray.index(Userchoice)
#                 WordArray[index] = None
#             else:
#                 print("This is not an answer")
#
#         attempts = attempts + 1


###################### Question 2 ###############################
# class Node:
#     def __init__(self, Data):
#         # --- Attribute Declarations ---
#         self.__Data = Data
#         self.__LeftPointer = -1
#         self.__RightPointer = -1
#
#     def GetLeft(self):
#         return self.__LeftPointer
#     def GetRight(self):
#         return self.__RightPointer
#     def GetData(self):
#         return self.__Data
#
#     def SetLeft(self, pointer):
#         self.__LeftPointer = pointer
#     def SetRight(self, pointer):
#         self.__RightPointer = pointer
#     def SetData(self, data):
#         self.__Data = data
#
# class Tree:
#     def __init__(self):
#         self.__FirstNode = -1
#         self.__NumberNodes = 0
#         self.__Tree = [Node(-1) for i in range(20)]
#
#     def InsertNode(self, NewNode:Node):
#         if self.__FirstNode == -1:
#             self.__Tree[self.__NumberNodes] = NewNode
#             self.__NumberNodes += 1
#             self.__FirstNode = 0
#         else:
#             self.__Tree[self.__NumberNodes] = NewNode
#             currentNode = self.__FirstNode
#             while True:
#                 if NewNode.GetData() < self.__Tree[currentNode].GetData():
#                     if self.__Tree[currentNode].GetLeft() == -1:
#                         self.__Tree[currentNode].SetLeft(self.__NumberNodes)
#                         break
#                     else:
#                         currentNode = self.__Tree[currentNode].GetLeft()
#
#                 else:
#                     if self.__Tree[currentNode].GetRight() == -1:
#                         self.__Tree[currentNode].SetRight(self.__NumberNodes)
#                         break
#                     else:
#                         currentNode = self.__Tree[currentNode].GetRight()
#             self.__NumberNodes += 1
#
#     def OutputTree(self):
#         if self.__NumberNodes == 0:
#             print("No nodes")
#         else:
#             for i in range(self.__NumberNodes):
#                 print(self.__Tree[i].GetLeft(), self.__Tree[i].GetData(), self.__Tree[i].GetRight())
#
#


################## Question 3 ##############################


NumberArray = [100, 85, 644, 22, 15, 8, 1]
LastItem = 0
LoopAgain = False

def RecursiveInsertion(IntegerArray, NumberElements: int):
    global LastItem, NumberArray, LoopAgain
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements -2

    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False

    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1

        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False

    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray

print("Recursive")
print(RecursiveInsertion(NumberArray, len(NumberArray)))


def IterativeInsertion(Myarr, NumberElemetns):

    if NumberElemetns <= 1:
        return Myarr
    else:
        for i in range(1, NumberElemetns):
            j=i
            while j > 0 and Myarr[j-1] > Myarr[j]:
                Myarr[j-1], Myarr[j] = Myarr[j], Myarr[j-1]
                j -=1
        return Myarr

print("Iterative")
print(IterativeInsertion(NumberArray, len(NumberArray)))


def BinarySearch(IntergerArray, First, Last, ToFind):
        if First > Last:
            return -1

        mid = (First + Last) // 2
        if IntergerArray[mid] ==  ToFind:
            return mid

        elif IntergerArray[mid] > ToFind:
            return BinarySearch(IntergerArray, First, mid - 1, ToFind)
        else:
            return BinarySearch(IntergerArray, mid + 1, Last, ToFind)

print("BinarySearch")
print(BinarySearch(NumberArray, 0, len(NumberArray)-1, 644))







