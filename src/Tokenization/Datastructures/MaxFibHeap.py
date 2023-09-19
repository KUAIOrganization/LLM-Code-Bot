from .FibonacciNode import FibonacciNode
class MaxFibonocciHeap:
    def __init__(self):
        self.root: FibonacciNode = None
        self.max: FibonacciNode = None
        self.size = 0
        self.rootSize = 0

    def addValue(self, key, value) -> FibonacciNode:
        newNode = FibonacciNode(key, value)
        if self.root == None:
            self.root = newNode
            self.max = newNode
        else:
            if key > self.max.key:
                self.max = newNode
            self.root.insertInline(newNode)    

        self.size += 1
        self.rootSize += 1
        return newNode
    
    def increaseKey(self, node: FibonacciNode, newValue):
        if(node.key >= newValue):
            raise ValueError("Increase key must increase key!")
        
        node.key = newValue
        if(node.isRoot() and node.key > self.max.key):
            self.max = node

        if (not node.isRoot()) and node.key > node.parent.key:
            self.increaseKeyHelper(node)
        
    def increaseKeyHelper(self, node: FibonacciNode):
        node.isMarked = False
        
        if node.parent.isMarked and (not node.parent.isRoot()):
            self.increaseKeyHelper(node.parent)
        else:
            node.parent.isMarked = not node.parent.isRoot()
        
        self.root.insertInline(node)
        self.rootSize += 1

        if node.key > self.max.key:
            self.max = node

    def getMaximumNode(self) -> FibonacciNode:
        if self.max == None:
            raise RuntimeError("Can't get max because Fibonacci heap is empty!");
        return self.max
    
    def getMaximum(self):
        if(self.max == None):
            raise RuntimeError("Can't get max because Fibonacci heap is empty!")
        
        return self.max.value
    
    def extractMaximum(self):
        if(self.max == None):
            raise RuntimeError("Can't extract max because Fibonacci heap is empty!")
        
        #print(self.root.lineString())
        #print("Passed")
        '''while input("go") != "y":
            True == True'''

        self._removeRoot(self.max)
        out = self.max.value
        #print("Removed max")

        current = self.max.child

        if (self.root == None) and not(current == None):
            self.root = current
            while True:
                current.parent = None
                current.isMarked = False
                current = current.right
                if current == self.root:
                    break

        if not (current == None):
            end = current.left
            current.left = self.root.left
            current.left.right = current
            end.right = self.root
            end.right.left = end

            while True:
                current.parent = None
                current.isMarked = False

                current = current.right
                if current == end:
                    break

        #print("Unseated root childs")
        
        if self.root == None:
            self.max = None
            self.size -= 1
            return out
        
        #print("Checked empty")
        
        newRoots = [None] * (self.size//2 + 1)
        
        start = self.root
        current = self.root
        i = 0
        fin = self.rootSize
        
        while True:
            #print(self.root.lineString())
            next = current.right
            if newRoots[current.degree] == None:
                newRoots[current.degree] = current
            else:
                self.extractMaxMergingHelper(current, newRoots)
            current = next
            i += 1

            if current == start or i >= fin:
                break

        '''print("Made trees")
        print(self.root)
        print("dab")
        print(self.root.right)
        print("dab")
        print(self.root.right.right)
        print("dab")
        print(self.root.left)
        print("dab")'''
        
        self.max = self.root
        current = self.root
        while True:
            if self.max.key < current.key:
                self.max = current
            
            current = current.right
            if self.root == current:
                break

        #print("Returning ", out)
        return out

    def _removeRoot(self, node: FibonacciNode):
        if self.root == node:
            if self.root.right == self.root:
                self.root = None
            else:
                self.root = self.root.right
        node.removeSelfInline()
        self.rootSize -= 1

    def _addRoot(self, node: FibonacciNode):
        if(self.root == None):
            self.root = node
            node.removeSelfInline()
        else:
            self.root.insertInline(node)
        self.rootSize += 1
        node.isMarked = False

    def extractMaxMergingHelper(self, node: FibonacciNode, newRoots):

        target: FibonacciNode = newRoots[node.degree]
        combined = None

        #print("Merging helper")
        #print("Merging", node, "and", target)
        
        if(node.key > target.key):
            self._removeRoot(target)
            node.addChild(target)
            combined = node
            newRoots[target.degree] = None
        else:
            self._removeRoot(node)
            target.addChild(node)
            combined = target
            newRoots[node.degree] = None
        
        if not (newRoots[combined.degree] == None):
            self.extractMaxMergingHelper(combined, newRoots)
        else:
            newRoots[combined.degree] = combined

    def hasValue(self):
        return not (self.root == None)

    def __sizeof__(self) -> int:
        return self.size