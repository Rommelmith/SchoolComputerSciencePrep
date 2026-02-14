# ################### Question 1 #####################
'''
TopOfStack = -1
Stack = ["-1"]*20

def Push(item:str):
    global TopOfStack, Stack
    if TopOfStack == 19:
        return -1

    else:
        TopOfStack += 1
        Stack[TopOfStack] = item
        return 1

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return "-1"

    else:
        item = Stack[TopOfStack]
        TopOfStack -= 1
        return item


def ReadData(filename):
    global TopOfStack, Stack
    try:
        with open(filename, "r") as file:
            for line in file:
                pushStatus = Push(line.strip())
                if pushStatus == -1:
                    print ("Stack full")
    except Exception as e:
        print(f"Error reading the file: {e}")


def Calculate():
    global TopOfStack, Stack
    total = Pop()
    total = float(total)


    while TopOfStack != -1:
        op = Pop()
        num = float(Pop())

        if op == "+":
            total = total + num
        elif op == "-":
            total = total - num
        elif op == "*":
            total = total * num
        elif op == "/":
            total = total / num
        elif op == "^":
            total = total ** num

    return total

filename = input("Enter the file name: ")
ReadData(filename)
calculatedNum = Calculate()
print(calculatedNum)
'''
#################### Question 2 #####################

''''
HashTable = [None]*200
Spare = [None]*100
FreeSpace = 0

class Record:
    def __init__(self, key:int, Item1:int, Item2:int):
        self.key = key
        self.Item1 = Item1
        self.Item2 = Item2

def initialize():
    global HashTable, Spare, FreeSpace
    for i in range(200):
        HashTable[i] = Record(-1, -1, -1)
    for d in range(100):
        Spare[d] = Record(-1, -1, -1)
    FreeSpace = 0

def CalculateHash(KeyField):
    keyVal = KeyField % 200
    return keyVal

def InsertIntoHash(NewRecord:Record):
    global HashTable, Spare, FreeSpace
    key = NewRecord.key
    place = CalculateHash(NewRecord.key)
    if HashTable[place].key != -1:
        Spare[FreeSpace] = NewRecord
        FreeSpace += 1
    else:
        HashTable[place] = NewRecord


def CreateHashTable():
    global HashTable, Spare, FreeSpace
    with open(r"C:\Users\romme\PycharmProjects\SchoolComputerSciencePrep\May_June_25_42\HashData.txt", "r") as f:
        for line in f:
            key = int(line.split(",")[0])
            item1 = int(line.split(",")[1])
            item2 = int(line.split(",")[2])
            new_record = Record(key, item1, item2)
            InsertIntoHash(new_record)

def PrintSpare():
    global Spare, FreeSpace
    for i in Spare:
        if i.key != -1:
            print(i.key)

if __name__ == '__main__':
    initialize()
    CreateHashTable()
    PrintSpare()
'''''