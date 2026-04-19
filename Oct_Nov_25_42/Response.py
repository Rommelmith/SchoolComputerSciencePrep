################## QUESTION 1 #########################
#
# class Bird:
#     def __init__(self, Species, DistancePerHour):
#         self.__Species = Species
#         self.__DistancePerHour = DistancePerHour
#         self.__XPosition = 500.0
#         self.__YPosition = 500.0
#
#     def GetSpecies(self):
#         return self.__Species
#
#     def GetPosition(self):
#         position = f"X = {self.__XPosition} Y = {self.__YPosition}"
#         return str(position)
#
#     def Move(self, direction:str, minofflying:int):
#
#         distanceTravelled = (self.__DistancePerHour/60)*minofflying
#
#
#         if direction == "N":
#             self.__YPosition = self.__YPosition + distanceTravelled
#
#         elif direction == "S":
#             self.__YPosition = self.__YPosition - distanceTravelled
#
#         elif direction ==  "E":
#             self.__XPosition = self.__XPosition + distanceTravelled
#
#         elif direction == "W":
#             self.__XPosition = self.__XPosition - distanceTravelled
#
# Bird1 = Bird("Cockatiel", 71.0)
# Bird2 = Bird('Macaw', 56.0)
#
# print(f"Bird1 species is {Bird1.GetSpecies()} and {Bird1.GetPosition()}")
# print(f"Bird2 species is {Bird2.GetSpecies()} and {Bird2.GetPosition()}")
#
# choice = int(input("Please enter 1 to Select Bird1 and 2 to select Bird 2 to move"))
#
# direction = input("Please enter the direction the bird is travelling N for North, S for South, E for East, W for West")
# time = int(input("Please enter the minute of the minute the bird has been travelling"))
#
# if choice ==  1:
#     Bird1.Move(direction, time)
# elif choice == 2:
#     Bird2.Move(direction, time)

###################### Question 2 #######################
import random

arr = [None]*20
count = 0
while count<20:
    num = random.randint(0, 100)
    if num in arr:
        print("")
    else:
        arr[count] = num
        count += 1

def PrintArray(Myarr):
    line = ""
    for i in range(len(Myarr)):
        line = line + str(Myarr[i]) + " "
    print(line)


def BubbleSort(Myarr):
    n = len(Myarr)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if Myarr[j] > Myarr[j + 1]:
                Myarr[j], Myarr[j + 1] = Myarr[j + 1], Myarr[j]
                swapped = True
        if not swapped:
                break
    return Myarr
# PrintArray(arr)
BubbleSort(arr)
# print("Sorted")
# PrintArray(arr)

# Part e forward

######################## Question 3 #################################

TreeArray = [
    [],# pointer
    [] # data
]
RootPointer = -1
FreeNode = 0

def RecursiveBinarySearch(Myarr, lowerBound, UpperBound, item):
    if UpperBound >= lowerBound:
        # ArrLen = len(Myarr)
        mid = int((UpperBound+lowerBound)/2)
        if Myarr[mid] == item:
            return mid
        else:
            if Myarr[mid] > item:
                # UpperBound =
                return RecursiveBinarySearch(Myarr, lowerBound, mid-1, item)
            else:
                # lowerBound =
                return RecursiveBinarySearch(Myarr, mid+1, UpperBound, item)


    else:
        return -1

arr1 = [1,2,3,4,5,6,7,88,90,91]
print(RecursiveBinarySearch(arr1, 0, len(arr1), 1))








