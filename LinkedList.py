LinkedList = [[],[]]
FirstNode = -1
FirstEmpty = 0
for i in range(20):
    LinkedList[0].append(-1)
    LinkedList[1].append(i+1)

def InsertData():
    global LinkedList, FirstEmpty, FirstNode
    currFree = FirstEmpty
    for i in range(5):
        if FirstEmpty == -1:
            print("List full")
            return
        newNode = FirstEmpty
        FirstEmpty = LinkedList[newNode][1]
        userIn = int(input("Enter Value: "))
        LinkedList[newNode][0] = userIn
        LinkedList[newNode][1]= FirstNode
        FirstNode = newNode

def remove(val):
    global LinkedList, FirstEmpty, FirstNode
    current = FirstNode
    prev = -1

    while current != -1 and LinkedList[current][0] != val:
        prev = current
        current = LinkedList[current][1]
    if current==-1:
        return "Not Found"

    if prev == -1:
        FirstNode = LinkedList[current][1]
    else:
        LinkedList[prev][1] = LinkedList[current][1]

