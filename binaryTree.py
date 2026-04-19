# class Node:
#     def __init__(self, NodeData:int):
#         self.__NodeData = NodeData
#         self.__LeftNode = None
#         self.__RightNode = None
#
#     def GetLeft(self):
#         return self.__LeftNode
#
#     def GetRight(self):
#         return self.__RightNode
#     def GetData(self):
#         return self.__NodeData
#
#     def SetLeft(self, NewNode):
#         self.__LeftNode = NewNode
#     def SetRight(self, NewNode):
#         self.__RightNode = NewNode
#
#
# Node1 = Node(10)
# Node2 = Node(20)
# Node3 = Node(5)
# Node4 = Node(15)
# Node5 = Node(7)
#
# class Tree:
#     def __init__(self, FirstNode):
#         self.__FirstNode = FirstNode
#
#     def GetRootNode(self):
#         return self.__FirstNode
#
#     def Insert(self, NewNode):
#         CurNode = self.__FirstNode
#         while True:
#             if NewNode.GetData() < CurNode.GetData():
#                 if CurNode.GetLeft() == None:
#                     CurNode.SetLeft(NewNode)
#                     return True
#                 else:
#                     CurNode = CurNode.GetLeft()
#             else:
#                 if CurNode.GetRight() == None:
#                     CurNode.SetRight(NewNode)
#                     return True
#                 else:
#                     CurNode = CurNode.GetRight()
#
# def OutputInOrder(RootNode):
#     if RootNode.GetLeft() != None:
#         OutputInOrder(RootNode.GetLeft())
#     print(RootNode.GetData())
#     if RootNode.GetRight() != None:
#         OutputInOrder(RootNode.GetRight())
#
#
# FirstNode = Node(10)
# SecondNode = Node(20)
# ThirdNode = Node(5)
# FourthNode = Node(15)
# FifthNode = Node(7)
# BinTree = Tree(FirstNode)
# BinTree.Insert(SecondNode)
# BinTree.Insert(ThirdNode)
# BinTree.Insert(FourthNode)
# BinTree.Insert(FifthNode)
#
# OutputInOrder(BinTree.GetRootNode())
# #
# #
# #
#
#
#
# #################################################################################################################
#
# class Node:
#     def __init__(self, Data):
#         self.__Data = Data
#         self.__LeftPointer = -1
#         self.__RightPointer = -1
#
#     def GetLeft(self):
#         return self.__LeftPointer
#     def GetRight(self):
#         return self.__RightPointer
#
#     def GetData(self):
#         return self.__Data
#
#     def SetLeft(self, NewNode):
#         self.__LeftPointer = NewNode
#     def SetRight(self, NewNode):
#         self.__RightPointer = NewNode
#     def SetData(self, NewNode):
#         self.__Data = NewNode
#
#
# class TreeClass:
#     def __init__(self):
#         self.__FirstNode = -1
#         self.__NumberNodes = 0
#         self.__Tree = []
#         for i in range(20):
#             self.__Tree[i] = Node(-1)
#
#     def InsertNode(self, NewNode):
#         if self.__NumberNodes == 0:
#             self.__Tree[self.__NumberNodes] = NewNode
#             self.__NumberNodes += 1
#             self.__FirstNode = 0
#
#         else:
#             self.__Tree[self.__NumberNodes] = NewNode
#             CurrNode = self.__Tree[self.__FirstNode].GetData()
#             if NewNode.GetData() < CurrNode:
#                 if CurrNode.GetLeft() == None:
#                     CurrNode.SetLeft(NewNode)
#                     return
#                 else:
#                     CurrNode = CurrNode.GetLeft()
#             else:
#                 if CurrNode.GetRigt() == None:
#                     CurrNode.SetRight(NewNode)
#                     return
#                 else:
#                     CurrNode = CurrNode.GetRigt()
#         self.__NumberNodes += 1
#
#     def OutputTree(self):
#         if self.__FirstNode == -1:
#             return "No nodes"
#         else:
#             while self.__Tree[self.__FirstNode] > self.__Tree[self.__NumberNodes]:
#                 print(self.__NumberNodes)
#                 self.__NumberNodes -= 1
#
#
#
#
#
#
#
#
#
#
##########################################################

class Node:
    def __init__(self, Data):
        self.__Data = Data
        self.__LeftPointer = -1
        self.__RightPointer = -1


    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft
    def SetRight(self, NewRight):
        self.__RightPointer = NewRight
    def SetData(self, NewData):
        self.__Data = NewData

class TreeClass:
    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNodes = 0
        self.__Tree = []
        for i in range(20):
            self.__Tree.append(Node(-1))

    def InsertNode(self, NewNode):
        if self.__NumberNodes >= len(self.__Tree):
            return False
        elif self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            CurrentNode = self.__FirstNode
            while True:
                if self.__Tree[CurrentNode].GetData() < NewNode.GetData():
                    nxt = self.__Tree[CurrentNode].GetLeft()
                    if nxt ==-1:
                        self.__Tree[CurrentNode].SetLeft(self.__NumberNodes)
                        break
                    else:
                        CurrentNode = nxt
                else:
                    nxt = self.__Tree[CurrentNode].GetRight()
                    if nxt == -1:
                        self.__Tree[CurrentNode].SetRight(self.__NumberNodes)
                        break
                    else:
                        CurrentNode = nxt
            self.__NumberNodes += 1
    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No Nodes")
        else:
            for i in range(self.__NumberNodes):
                print(self.__Tree[i].GetLeft(), self.__Tree[i].GetData(), self.__Tree[i].GetRight())





TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(15))
TheTree.InsertNode(Node(3))
TheTree.InsertNode(Node(7))

TheTree.OutputTree()
