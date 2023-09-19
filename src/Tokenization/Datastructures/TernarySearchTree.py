from .TernaryNode import TernaryNode
from enum import Enum

class TernarySearchTree:
    
    def __init__(self):
        self.root: TernaryNode = None
        self._size = 0

    def add(self, key: str, value):
        index: int = 0

        if self.root == None:
            self.root = TernaryNode(key[index], value if index+1 == len(key) else None)
            self._size += 1 if index + 1 == len(key) else 0

        current: TernaryNode = self.root

        while index < len(key):
            if current.key == key[index]:
                if index + 1 == len(key):
                    current.value = value
                    return
                if not current.hasCenter():
                    if index + 2 == len(key):
                        current.center = TernaryNode(key[index + 1], value)
                        self._size += 1
                    else:
                        current.center = TernaryNode(key[index + 1], None)
                current = current.center
                index += 1
            elif key[index] < current.key:
                if not current.hasLeft():
                    current.left = TernaryNode(key[index], value if index + 1 == len(key) else None)
                    self._size += 1 if index + 1 == len(key) else 0
                current = current.left
            else:
                if not current.hasRight():
                    current.right = TernaryNode(key[index], value if index + 1 == len(key) else None)
                    self._size += 1 if index + 1 == len(key) else 0
                current = current.right

    class TSearchAnswer:
        def __init__(self, value, hasChild: bool, exists: bool):
            self.value = value
            self.hasChild = hasChild
            self.exists = exists

    def search(self, key: str) -> TSearchAnswer:
        index = 0
        size = len(key)
        current = self.root

        while index < size:
            if (current is None):
                return TernarySearchTree.TSearchAnswer(None, False, False)
            char = key[index]
            if char < current.key:
                current = current.left
            elif char > current.key:
                current = current.right
            else:
                if index + 1 == size:
                    return TernarySearchTree.TSearchAnswer(current.value, current.hasCenter(), True)
                current = current.center
                index += 1

        return TernarySearchTree.TSearchAnswer(None, False, False)
        raise RuntimeError("Search escaped while without returning!")
    
    def remove(self, key: str):
        index = 0
        current = self.root
        parent = current

        while index < len(key):
            if (current == None):
                return
            if current.key == key[index]:
                if index + 1 == len(key):
                    if current.hasCenter():
                        current.value = None
                        self._size -= 1
                        return
                    else:
                        if current.hasRight():
                            if current.right.hasLeft():
                                if parent.left == current:
                                    parent.left = TernarySearchTree.extractLeast(current.right.left, current.right)
                                    parent.left.left = current.left
                                    parent.left.right = current.right
                                elif parent.center == current:
                                    parent.center = TernarySearchTree.extractLeast(current.right.left, current.right)
                                    parent.center.left = current.left
                                    parent.center.right = current.right
                                else:
                                    parent.right = TernarySearchTree.extractLeast(current.right.left, current.right)
                                    parent.right.left = current.left
                                    parent.right.right = current.right
                            else:
                                if parent.left == current:
                                    parent.left = current.right
                                elif parent.center == current:
                                    parent.center = current.right
                                else:
                                    parent.right = current.right
                        else:
                            if parent.left == current:
                                    parent.left = current.left
                            elif parent.center == current:
                                parent.center = current.left
                            else:
                                parent.right = current.left
                    self._size -= 1
                    return
                parent = current
                current = current.center
                index += 1
            elif key[index] < current.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        raise RuntimeError("Remove escaped while without returning!")
    
    def getAll(self) -> list[str]:
        return self.root.getAll() if not (self.root == None) else []
    
    @staticmethod
    def extractLeast(node : TernaryNode, parent: TernaryNode) -> TernaryNode:
        if node.hasLeft():
            return TernarySearchTree.extractLeast(node.left, node)
        else:
            parent.left = node.right
            node.right = None
            return node
    
    @staticmethod
    def buildFromOrderedList(orderedList: list[str], values: list):
        out = TernarySearchTree()
        TernarySearchTree._buildingPrepper(orderedList, values, 0, out)
        return out

    def _buildingPrepper(orderedList: list[str], values: list, index: int, tree):
        bases: list[str] = []
        basesValues: list = []
        subs: list[list[str]] = []
        subsValues: list[list] = []
        for i in range(len(orderedList)):
            subs.append([])
            subsValues.append([])

        last: int = None
        
        for i in range(len(orderedList)):
            if not (orderedList[i][:index+1] in bases):
                bases.append(orderedList[i][:index+1])
                basesValues.append(values[i] if len(orderedList[i]) == index + 1 else None)
                #print(bases[-1], basesValues[-1])
                last = i
            if len(orderedList[i]) > index + 1:
                subs[last].append(orderedList[i])
                subsValues[last].append(values[i])
        
        TernarySearchTree._buildingSplitter(bases, basesValues, tree)

        for i in range(len(subs)):
            if len(subs[i]) == 0:
                continue
            TernarySearchTree._buildingPrepper(subs[i], subsValues[i], index + 1, tree)

            

    @staticmethod
    def _buildingSplitter(orderedList: list[str], values: list, tree):
        if len(orderedList) == 1:
            #print(orderedList[0], values[0])
            tree.add(orderedList[0], values[0])
            return
        
        if len(orderedList) == 0:
            return
        
        half = len(orderedList) // 2
        #print(orderedList[half], values[half])
        tree.add(orderedList[half], values[half])
        TernarySearchTree._buildingSplitter(orderedList[:half], values[:half], tree)
        TernarySearchTree._buildingSplitter(orderedList[half+1:], values[half+1:], tree)
            
    def size(self):
        return self._size