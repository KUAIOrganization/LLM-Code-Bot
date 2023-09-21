class TernaryNode:
    """Node for the Ternary Search Tree structure.
    
    Has three children: a left which has a key less than it, a right whose key is greater, and
    a center whose key is a continuation of a string this key is patr of."""
    def __init__(self, key: str, value):
        self.key = key
        self.value = value
        self.right: TernaryNode = None
        self.left: TernaryNode = None
        self.center: TernaryNode = None

    def hasCenter(self):
        return not (self.center is None)
    
    def hasRight(self):
        return not (self.right is None)
    
    def hasLeft(self):
        return not (self.left is None)
    
    def getAll(self) -> list[str]:
        out = []
        self._recGetAll("", out)
        return out

    def _recGetAll(self, parentString: str, allList: list[str]):
        """Recursively traverses the tree to fill a list with all the keys in the tree."""
        if self.hasLeft():
            self.left._recGetAll(parentString, allList)
        if not self.value is None:
            allList.append(parentString + self.key)
        if self.hasCenter():
            self.center._recGetAll(parentString + self.key, allList)
        if self.hasRight():
            self.right._recGetAll(parentString, allList)
    
    def doFunctionPreOrder(self, function):
        function(self.key, self.value)

        if self.hasLeft():
            self.left.doFunctionPreOrder(function)
        if self.hasCenter():
            self.center.doFunctionPreOrder(function)
        if self.hasRight():
            self.right.doFunctionPreOrder(function)

    def doFunctionInOrder(self, function):
        if self.hasLeft():
            self.left.doFunctionInOrder(function)
        function(self.key, self.value)
        if self.hasCenter():
            self.center.doFunctionInOrder(function)
        if self.hasRight():
            self.right.doFunctionInOrder(function)

    def getString(self, parentString) -> str:
        """Traverses the tree in order to produce a '||'-seperated list of keys in the tree."""
        out = ""
        if self.hasLeft():
            out += self.left.getString(parentString)
        if not (self.value is None):
            out += "|" + parentString + self.key + "|"
        if self.hasCenter():
            out += self.center.getString(parentString + self.key)
        if self.hasRight():
            out += self.right.getString(parentString)
        return out

    def __str__(self) -> str:
        return self.getString("")
        #return f"{(str(self.left) + ' ') if self.hasLeft() else ''}({self.key}, {self.value}): [{self.center if self.hasCenter() else ''}]{(str(self.right) + ' ') if self.hasRight() else ''}"