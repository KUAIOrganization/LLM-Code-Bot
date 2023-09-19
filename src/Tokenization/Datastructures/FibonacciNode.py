class FibonacciNode:
    def __init__(self, key, value):
        self.parent: FibonacciNode = None
        self.child: FibonacciNode = None
        self.left: FibonacciNode = self
        self.right: FibonacciNode = self
        self.key = key
        self.value = value
        self.isMarked: bool = False
        self.degree: int = 0

    def isRoot(self):
        return self.parent == None
    
    def hasChild(self):
        return not (self.child == None)
    
    """child is another Fib Node"""
    def addChild(self, child):
        if child == self:
            raise RuntimeError("WTF")

        if self.hasChild():
            self.child.insertInline(child)
        else:
            child.removeSelfInline()
            self.child = child
            child.parent = self
            self.degree += 1
    
    def insertInline(self, other):
        other.removeSelfInline()
        other.right = self
        other.left = self.left
        other.parent = self.parent
        if not(self.parent == None):
            self.parent.degree += 1 
        self.left.right = other
        self.left = other

    def removeSelfInline(self):
        if not self.isRoot():
            self.parent.degree -= 1

        if self.right == self and (not self.isRoot()):
            self.parent.child = None
        else:
            self.right.left = self.left
            self.left.right = self.right
            if (not self.isRoot()) and self.parent.child == self:
                self.parent.child = self.right
            self.right = self
            self.left = self
        self.parent = None

    def lineString(self) -> str:
        current = self
        out = ""
        while True:
            out += current.__str__()

            current = current.right
            if current == self:
                break
            out += ", "

        return out

    def __str__(self) -> str:
        #print(f"Calling on {str(self.value)}, Child is, {self.child.value if self.hasChild() else ''}, Parent is, {str(self.parent.value) if not self.isRoot() else ''}, {self.right.value}, {self.left.value}")
        return f'({self.key}, {self.value}) [{self.child.lineString() if self.hasChild() else ""}]'
    
    def __repr__(self) -> str:
        return self.__str__()#f"FibonacciNode({self.key}, {self.value})"