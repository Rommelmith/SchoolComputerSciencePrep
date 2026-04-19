# class Node:
#     def __init__(self, TheData:int):
#         self.__TheData = TheData
#         self.__NextNode = None
#
#     def GetData(self):
#         return self.__TheData
#     def GetNextNode(self):
#         return self.__NextNode
#
#     def SetNextNode(self, NewNode):
#         self.__NextNode = NewNode
#
# class LinkedList:
#     def __init__(self):
#         self.__HeadNode = None
#
#     def InsertNode(self, data:int):
#         NewNode = Node(data)
#         NewNode.SetNextNode(self.__HeadNode)
#         self.__HeadNode = NewNode
#
#     def Traverse(self):
#         result = ""
#         current = self.__HeadNode
#         while current is not None:
#             result = result + str(current.GetData()) + " "
#             current = current.GetNextNode()
#         return result
#
#     def RemoveData(self, IntRemove:int):
#         removed = False
#         if self.__HeadNode == None:
#             return removed
#         else:
#             if self.__HeadNode.GetData() == IntRemove:
#                 nextNode = self.__HeadNode.GetNextNode()
#                 self.__HeadNode = nextNode
#                 removed = True
#                 return removed
#         currentNode = self.__HeadNode
#         while currentNode.GetNextNode() is not None:
#             if currentNode.GetNextNode().GetData() == IntRemove:
#                 currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
#                 removed = True
#                 return removed
#             currentNode = currentNode.GetNextNode()
#         return False



class Node:
    def __init__(self, TheData):
        self.__TheData = TheData
        self.__NextNode = None


    def GetData(self):
        return self.__TheData
    def GetNextNode(self):
        return self.__NextNode
    def SetNextNode(self, NewNode):
        self.__NextNode = NewNode


class LinkedList:














