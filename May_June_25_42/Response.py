# # ################### Question 1 #####################
#
# TopOfStack = -1
# Stack = ["-1"]*20
#
# def Push(item:str):
#     global TopOfStack, Stack
#     if TopOfStack == 19:
#         return -1
#
#     else:
#         TopOfStack += 1
#         Stack[TopOfStack] = item
#         return 1
#
# def Pop():
#     global TopOfStack, Stack
#     if TopOfStack == -1:
#         return "-1"
#
#     else:
#         item = Stack[TopOfStack]
#         TopOfStack -= 1
#         return item
#
#
# def ReadData(filename):
#     global TopOfStack, Stack
#     try:
#         with open(filename, "r") as file:
#             for line in file:
#                 pushStatus = Push(line.strip())
#                 if pushStatus == -1:
#                     print ("Stack full")
#     except Exception as e:
#         print(f"Error reading the file: {e}")
#
#
# def Calculate():
#     global TopOfStack, Stack
#     total = Pop()
#     total = float(total)
#
#
#     while TopOfStack != -1:
#         op = Pop()
#         num = float(Pop())
#
#         if op == "+":
#             total = total + num
#         elif op == "-":
#             total = total - num
#         elif op == "*":
#             total = total * num
#         elif op == "/":
#             total = total / num
#         elif op == "^":
#             total = total ** num
#
#     return total
#
# filename = input("Enter the file name: ")
# ReadData(filename)
# calculatedNum = Calculate()
# print(calculatedNum)
#
# #################### Question 2 #####################
#
# HashTable = [None]*200
# Spare = [None]*100
# FreeSpace = 0
#
# class Record:
#     def __init__(self, key:int, Item1:int, Item2:int):
#         self.key = key
#         self.Item1 = Item1
#         self.Item2 = Item2
#
# def initialize():
#     global HashTable, Spare, FreeSpace
#     for i in range(200):
#         HashTable[i] = Record(-1, -1, -1)
#     for d in range(100):
#         Spare[d] = Record(-1, -1, -1)
#     FreeSpace = 0
#
# def CalculateHash(KeyField):
#     keyVal = KeyField % 200
#     return keyVal
#
# def InsertIntoHash(NewRecord:Record):
#     global HashTable, Spare, FreeSpace
#     key = NewRecord.key
#     place = CalculateHash(NewRecord.key)
#     if HashTable[place].key != -1:
#         Spare[FreeSpace] = NewRecord
#         FreeSpace += 1
#     else:
#         HashTable[place] = NewRecord
#
#
# def CreateHashTable():
#     global HashTable, Spare, FreeSpace
#     with open(r"C:\Users\romme\PycharmProjects\SchoolComputerSciencePrep\May_June_25_42\HashData.txt", "r") as f:
#         for line in f:
#             key = int(line.split(",")[0])
#             item1 = int(line.split(",")[1])
#             item2 = int(line.split(",")[2])
#             new_record = Record(key, item1, item2)
#             InsertIntoHash(new_record)
#
# def PrintSpare():
#     global Spare, FreeSpace
#     for i in Spare:
#         if i.key != -1:
#             print(i.key)
#
# if __name__ == '__main__':
#     initialize()
#     CreateHashTable()
#     PrintSpare()


################# PAPER 43 ##############################
 ################## Question 1 ###############
# def ReadData():
#     ArrItem = [None for i in range(45)]
#     count = 0
#
#     with open("Data.txt", "r") as f:
#         for line in f.readlines():
#             ArrItem[count] = line.strip()
#             count += 1
#     return ArrItem
#
#
# def FormatArray(MyArr):
#     text = ""
#     for i in range(len(MyArr)):
#         item = str(MyArr[i])
#         item = item.strip()
#         text += f"{item} "
#     return text
#
# arr = ReadData()
# print(FormatArray(arr))
#
#
# def ComparrStrings(test1, test2):
#     for i in range(len(test1)):
#         if test1[i] < test2[i]:
#             return 1
#         else:
#             return 2
#
# def Bubble(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1-i):
#             if ComparrStrings(arr[j + 1], arr[j]) == 1:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     return arr

################## Question 2 ###############
class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.__Name = Name
        self.__MaxFenceHeight = MaxFenceHeight
        self.__PercentageSuccess = PercentageSuccess

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight


h1 = Horse("Beauty", 150, 72)
h2 = Horse("Jet", 160, 65)

Horses = [h1, h2]
print(Horses[0].GetName())
print(Horses[1].GetName())

class Fence:
    def __init__(self, Height, Risk):
        self.__Height = Height # height in Integer
        self.__Risk = Risk # Risk in Integer

    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk


Course = [None for i in range(4)]

for i in range(4):
    fence = int(input("Enter Fence Height : "))

    while fence>180 and fence<70:
        fence = int(input("Please enter number between 70 to 180 : "))

    risk = int(input("Enter Risk between 1 to 5 : "))
    while risk<1 and risk>5:
        risk = int(input("Please enter Risk between 1 to 5 : "))

    name = Fence(fence, risk)
    Course[i] = name
print(Course)



