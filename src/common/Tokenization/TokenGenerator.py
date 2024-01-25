from .Datastructures.MaxFibHeap import MaxFibonocciHeap
from .Datastructures.FibonacciNode import FibonacciNode
from .Datastructures.TernarySearchTree import TernarySearchTree
from functools import reduce
import os

class TokenGenerator:
    _PAIR_BUFFER = 16

    def __init__(self, folder: str, tokenAmount: int, tokensPerRound: int, removesBeforeClean = 10, allowWhitespace = True, allowTextAndSpceial = True, startingTokens = None):
        self.tokenAmount: int = tokenAmount
        self.heap: MaxFibonocciHeap = MaxFibonocciHeap()
        self.tokensList: list[str] = [] if startingTokens is None else startingTokens
        self.tokens: TernarySearchTree = TernarySearchTree() if startingTokens is None else TernarySearchTree.buildFromOrderedList(startingTokens, [i for i in range(len(self.tokensList))])
        self.tokensExist: list[bool] = [True for token in self.tokensList]
        self._tokenCount: int = len(self.tokensList)
        self.countArray: list[list[FibonacciNode]] = []
        for i in range(self._tokenCount):
            self.countArray.append([None for j in range(self._tokenCount)])
        self.baseFolder = folder
        self.fileList: list[str] = []
        self.tokensPerRound: int = tokensPerRound
        self._removes: int = 0
        self._removesBeforeClean = removesBeforeClean
        self._allowWhitespace = allowWhitespace
        self._allowTextAndSpecial = allowTextAndSpceial
        self._initFileList()

    def addBaseToken(self, token: str, base0: str, base1: str):
        #print(self.tokensList)
        #print(self.countArray)

        self.tokens.add(token, len(self.tokensList))
        self.tokensList.append(token)
        self.tokensExist.append(True)
        self._tokenCount += 1
        for i in range(len(self.tokensList) - 1):
            self.countArray[i].append(None)
        self.countArray.append([None for i in range(len(self.tokensList))])

        #print(self.tokensList)
        #print(self.countArray)
        #print(self.tokens.root)

    def tokenCount(self) -> int:
        return self._tokenCount
    
    def getCanonList(self) -> list[str]:
        return self.tokens.getAll()

    def _initFileList(self):
        self._recInitFileList(self.baseFolder)

    def _recInitFileList(self, directoryPath: str):
        subFolders = os.listdir(directoryPath)
        for path in subFolders:
            newPath = os.path.join(directoryPath, path)
            if(os.path.isfile(newPath)):
                self.fileList.append(newPath)
            else:
                #print("Going deeper in ", newPath)
                self._recInitFileList(newPath)

    def initTokens(self):
        print("Initializing")
        if len(self.tokensList) > 0:
            return
        for path in self.fileList:
            #print("File", path)
            file = open(path, 'r')
            char = file.read(1)
            if not char:
                continue
            
            thisIndex = self.tokens.search(char).value

            if thisIndex == None:
                self.addBaseToken(char, None, None)
                thisIndex = self.tokens.search(char).value
            lastToken: int = thisIndex

            while True:
                char = file.read(1)
                if not char:
                    break
                
                thisIndex = self.tokens.search(char).value
                if thisIndex == None:
                    self.addBaseToken(char, None, None)
                    thisIndex = self.tokens.search(char).value
                #print(lastToken)
                #print(thisIndex)

                if self.countArray[lastToken][thisIndex] == None:
                    self.countArray[lastToken][thisIndex] = self.heap.addValue(1, [lastToken, thisIndex])
                else:
                    self.heap.increaseKey(self.countArray[lastToken][thisIndex], self.countArray[lastToken][thisIndex].key + 1)
                lastToken = thisIndex
            file.close()

    @staticmethod
    def hasOverlap(base: str, match: str) -> bool:
        for i in range(len(base)):
            if base[i] == match[0]:
                stop = True
                for j in range(1, len(base) - i):
                    if len(match) <= j:
                        return True
                    if not (base[i + j] == match[j]):
                        stop = False
                        break
                if stop:
                    return True
            if base[i] == match[-1]:
                stop = True
                for j in range(-1, -i-1, -1):
                    if len(match) < abs(j):
                        return True
                    if not (base[i + j] == match[j-1]):
                        stop = False
                        break
                if stop:
                    return True
        return False
                        

    def makeNewToken(self):
        forbidden = []

        while len(forbidden) < self.tokensPerRound:
            newPair = None
            newToken = None
            continueBool = True

            while continueBool:
                newPair: list[int] = self.heap.extractMaximum()
                new1 = self.tokensList[newPair[0]]
                new2 = self.tokensList[newPair[1]]

                if not self._allowWhitespace:
                    if new1.isspace() or new2.isspace():
                        #print("Eliminated", "|"+new1+new2+"|")
                        continue

                if not self._allowTextAndSpecial:
                    split1 = new1.split("_")
                    split2 = new2.split("_")

                    alNum1 = reduce(lambda sum, item : sum and (item.isalnum() or item == ""), split1, True)
                    alNum2 = reduce(lambda sum, item : sum and (item.isalnum() or item == ""), split2, True)

                    if not (alNum1 == alNum2):
                        #print("Eliminated", "|"+new1+new2+"|")
                        continue

                newToken = new1 + new2

                continueBool = False
                for item in forbidden:
                    if TokenGenerator.hasOverlap(item, newToken):
                        continueBool = True
                        #print("Eliminated", "|"+new1+new2+"|")
                        continue

            forbidden.append(newToken)

            print("Adding token:", newPair, "aka", "|" + newToken + "|")
            if len(self.tokensList[newPair[0]]) > 1 and self.tokensExist[newPair[0]]:
                print("Removing", str(newPair[0]) + ":", "|"+self.tokensList[newPair[0]]+"|")
                self.tokens.remove(self.tokensList[newPair[0]])
                self._tokenCount -= 1
                self._removes += 1
                self.tokensExist[newPair[0]] = False
            
            if (not (newPair[1] == newPair[0])) and len(self.tokensList[newPair[1]]) > 1 and self.tokensExist[newPair[1]]:
                print("Removing", str(newPair[1]) + ":", "|"+self.tokensList[newPair[1]]+"|")
                self.tokens.remove(self.tokensList[newPair[1]])
                self._tokenCount -= 1
                self._removes += 1
                self.tokensExist[newPair[1]] = False

            self.addBaseToken(newToken, new1, new2)
        #print(self.tokens.root)

    def genTokens(self):
        while self.tokenCount() < self.tokenAmount:
            self.heap = MaxFibonocciHeap()
            if self._removes > self._removesBeforeClean:
                self._removes = 0
                print("Cleaning")
                self.clean()

            for i in range(len(self.countArray)):
                for j in range(len(self.countArray[i])):
                    self.countArray[i][j] = None
            
            print("Processing Files")
            self.fillCountArray()
            print("Generating New Tokens")
            self.makeNewToken()
            print("Token Count:", self.tokenCount())

    def fillCountArray(self):
        for path in self.fileList:
            file = open(path, 'r')
            #print("Starting in path:", path)

            lastToken: int = self.getNextToken(file)
            if lastToken == -1:
                continue

            while True:
                thisIndex = self.getNextToken(file)
                if thisIndex == -1:
                    break

                if self.countArray[lastToken][thisIndex] is None:
                    self.countArray[lastToken][thisIndex] = self.heap.addValue(1, [lastToken, thisIndex])
                else:
                    self.heap.increaseKey(self.countArray[lastToken][thisIndex], self.countArray[lastToken][thisIndex].key + 1)
                lastToken = thisIndex
            file.close()

    def getNextToken(self, file) -> int:
        built = ""
        char = file.read(1)
        if not char:
            return -1
        built += char
        result = self.tokens.search(built)

        lastGoodResult = result.value
        lastGoodFileSpot = file.tell()
        
        while result.hasChild:
            char = file.read(1)
            if not char:
                if result.value == None:
                    return -1
                else:
                    return result.value
            result = self.tokens.search(built + char)
            if not result.exists:
                file.seek(lastGoodFileSpot)
                return lastGoodResult
            built += char
            if not(result.value == None):
                lastGoodResult = result.value
                lastGoodFileSpot = file.tell()
        
        file.seek(lastGoodFileSpot)
        return lastGoodResult
    
    def clean(self):
        self.tokensList = self.getCanonList()
        self.tokensExist = [True for i in range(self.tokenCount())]
        values = [i for i in range(len(self.tokensList))]
        self.tokens = TernarySearchTree.buildFromOrderedList(self.tokensList, values)
        self.countArray = []
        for i in range(len(self.tokensList)):
            self.countArray.append([None for j in range(len(self.tokensList))])
        print(self.getCanonList())

    @staticmethod
    def getNextTokenGlobal(file, tree: TernarySearchTree, allowWhitespace: bool) -> int:
        built = ""
        char: str = file.read(1)
        if (not char):
            return -1

        if (not allowWhitespace) and char.isspace():
            return tree.search(char).value
            
        built += char
        result = tree.search(built)

        lastGoodResult = result.value
        lastGoodFileSpot = file.tell()
        
        while result.hasChild:
            char = file.read(1)
            if (not char) or ((not allowWhitespace) and char.isspace()):
                break
            result = tree.search(built + char)
            if not result.exists:
                file.seek(lastGoodFileSpot)
                return lastGoodResult
            built += char
            if not(result.value is None):
                lastGoodResult = result.value
                lastGoodFileSpot = file.tell()
        
        file.seek(lastGoodFileSpot)
        return lastGoodResult
        