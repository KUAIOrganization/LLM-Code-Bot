from .Datastructures.TernarySearchTree import TernarySearchTree
class Tokenizer:
    def __init__(self, tokens: tuple[list[str], list[int]], startOffest = 0):
        self._tokenList : list[str] = tokens[0]
        self._offset = startOffest
        self._tree = TernarySearchTree.buildFromOrderedList(tokens[0], tokens[1])
        self._count = len(self._tokenList)

    def tokenize(self, string: str) -> list[int]:
        """Tokenizes the given string using the tokens in tree.
        
        Turns the string into a list of integers, where each integer corresponds to a character or sequence of
        characters. These integers can be fed into a neural network.
        """
        index = 0
        out: list[int] = []
        while index < len(string):
            pair = self._getNextToken(string, index)
            if pair[0] == -1:
                break
            out.append(pair[0])
            index = pair[1]
        return out

    def _getNextToken(self, string: str, index: int) -> list[int]:
        """Gets the next token in the given string, starting at the given index. Returns the token and the index after its end.
        
        Uses the given tree to find the next token in the given string. Searches through the tree and finds the
        longest sequence of characters that has a token and matches the given string, and returns the token of that sequence."""
        built = ""
        if index + 1 == len(string):
            return [-1, -1]
        char = string[index]
        index += 1

        built += char
        result = self._tree.search(built)

        lastGoodResult = result.value
        lastGoodFileSpot = index
        
        while result.hasChild:
            if index + 1 == len(string):
                break
            char = string[index]
            index += 1
            result = self._tree.search(built + char)
            if not result.exists:
                return [lastGoodResult, lastGoodFileSpot]
            built += char
            if not(result.value is None):
                lastGoodResult = result.value
                lastGoodFileSpot = index
        
        return [lastGoodResult, lastGoodFileSpot]
    
    def detokenize(self, tokenList: list[int]):
        """Given a list of tokens, returns the string they represent."""
        out = ""
        for token in tokenList:
            if token < self._offset or token >= self._count + self._offset:
                continue
            out += self._tokenList[token - 1]
        return out
    
    def getCount(self):
        return self._count

