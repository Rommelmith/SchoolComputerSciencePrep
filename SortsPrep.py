################### Bubble #######################
def BubbleSort(MyArray):

    for i in range(len(MyArray)):
        for j in range(len(MyArray)-1):
            if MyArray[j] > MyArray[j+1]:
                MyArray[j], MyArray[j+1] = MyArray[j+1], MyArray[j]
    return MyArray


def InsertionSort(MyArray):
    for i in range(1, len(MyArray)):
        x = MyArray[i]
        j = MyArray[i-1]
        while MyArray[j] > MyArray[x]:
            MyArray[j+1] = MyArray[j]
            j -= 1
        MyArray[j+1] = x
        return MyArray



if __name__ == '__main__':
    mylist = [2,1,22,44,2,77,3,10,3]
    print(BubbleSort(mylist))
    print(InsertionSort(mylist))
