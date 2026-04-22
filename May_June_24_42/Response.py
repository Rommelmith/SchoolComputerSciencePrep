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
class Node:
    def __init__(self, Data):
        # --- Attribute Declarations ---
        self.__Data = Data
        self.__LeftPointer = -1
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data

    def SetLeft(self, pointer):
        self.__LeftPointer = pointer
    def SetRight(self, pointer):
        self.__RightPointer = pointer
    def SetData(self, data):
        self.__Data = data

class Tree:
    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNodes = 0
        self.__Tree = [Node(-1) for i in range(20)]

    def InsertNode(self, NewNode:Node):
        if self.__FirstNode == -1:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            currentNode = self.__FirstNode
            while True:
                if NewNode.GetData() < self.__Tree[currentNode].GetData():
                    if self.__Tree[currentNode].GetLeft() == -1:
                        self.__Tree[currentNode].SetLeft(self.__NumberNodes)
                        break
                    else:
                        currentNode = self.__Tree[currentNode].GetLeft()

                else:
                    if self.__Tree[currentNode].GetRight() == -1:
                        self.__Tree[currentNode].SetRight(self.__NumberNodes)
                        break
                    else:
                        currentNode = self.__Tree[currentNode].GetRight()
            self.__NumberNodes += 1





