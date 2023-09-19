from .TokenGenerator import TokenGenerator
from multiprocessing import Process, Queue, JoinableQueue, Value
from .Datastructures.TernarySearchTree import TernarySearchTree
from .Datastructures.MaxFibHeap import MaxFibonocciHeap
from queue import Empty
from ctypes import c_bool

class TokenGeneratorDriverMP(TokenGenerator):
    def __init__(self, directory: str, tokenAmount: int, tokensPerRound: int, threads:int = 0, removesBeforeClean = 10, allowWhitespace = True, allowTextAndSpecial = True):
        super().__init__(directory, tokenAmount, tokensPerRound, removesBeforeClean, allowWhitespace, allowTextAndSpceial=allowTextAndSpecial)
        self._threads = threads
        self.fileQueue = JoinableQueue(len(self.fileList))
        self.tokenPairQueue = Queue(threads * 2)
        self.outQueues: list[Queue] = []

    def run(self):
        print("Starting Processes")
        processes: list[Process] = []
        self.outQueues: list[Queue] = []

        for i in range(self._threads - 1):
                self.outQueues.append(Queue(self.tokensPerRound))
                processes.append(Process(target=TokenGeneratorDriverMP.processFiles, args=(self.fileQueue, self.tokenPairQueue, self.tokens, self.outQueues[i])))
                processes[i].start()

        while self.tokenCount() < self.tokenAmount:
            print("New Cycle")
            self.heap = MaxFibonocciHeap()
            if self._removes > self._removesBeforeClean:
                self._removes = 0
                print("***************Cleaning******************")
                self.clean()

                for process in processes:
                    process.terminate()

                print("Restarting Processes")
                processes: list[Process] = []
                self.outQueues: list[Queue] = []

                for i in range(self._threads - 1):
                    self.outQueues.append(Queue(self.tokensPerRound))
                    processes.append(Process(target=TokenGeneratorDriverMP.processFiles, args=(self.fileQueue, self.tokenPairQueue, self.tokens, self.outQueues[i])))
                    processes[i].start()

            for i in range(len(self.countArray)):
                for j in range(len(self.countArray[i])):
                    self.countArray[i][j] = None
            
            print("Filling file queue")
            for path in self.fileList:
                self.fileQueue.put(path)

            finished = Value(c_bool, False)
            listenerProcess = Process(target=TokenGeneratorDriverMP.finishListener, args=(self.fileQueue, finished))
            listenerProcess.start()

            print("Processing Files")

            while (not self.tokenPairQueue.empty()) or (not finished.value):
                try:
                    pairBuffer: list[list[int]] = self.tokenPairQueue.get(timeout=0.2)
                    for pair in pairBuffer:
                        # pair: list[int] = self.tokenPairQueue.get(timeout=0.1)
                        try:
                            if self.countArray[pair[0]][pair[1]] is None:
                                self.countArray[pair[0]][pair[1]] = self.heap.addValue(1, [pair[0], pair[1]])
                            else:
                                self.heap.increaseKey(self.countArray[pair[0]][pair[1]], self.countArray[pair[0]][pair[1]].key + 1)
                        except IndexError:
                            print("\n\nIndex Error on", str(pair[0]), str(pair[1]))
                            print(self.getCanonList())
                            print(len(self.getCanonList()))
                            print(self.tokenCount())
                            print(self.tokensList)
                            print(len(self.tokensList))
                except Empty:
                    print("Queue is empty")
                    continue
            print("Processes ended")
            
            #print("Actual end")
            print("Making New Tokens")
            self.makeNewToken()
            print("Token Count:", self.tokenCount())
        
        for process in processes:
            process.terminate()

    @staticmethod
    def processFiles(fileQueue: JoinableQueue, tokenOutQueue: Queue, tree: TernarySearchTree, newTokenQueue: Queue):
        while True:
            file = None
            startedFile = False
            TokenGeneratorDriverMP.updateTree(tree, newTokenQueue)
            if not fileQueue.empty():
                path = fileQueue.get()
                TokenGeneratorDriverMP.updateTree(tree, newTokenQueue)
                startedFile = True
                file = open(path, 'r')
                #print("Starting in path:", path)
            else:
                continue
            
            lastToken: int = TokenGenerator.getNextTokenGlobal(file, tree)
            if lastToken == -1:
                file.close()
                if fileQueue.empty():
                    if startedFile:
                        fileQueue.task_done()
                    continue
                if startedFile:
                    fileQueue.task_done()
                continue

            queueBuffer = []

            while True:
                thisIndex = TokenGenerator.getNextTokenGlobal(file, tree)
                if thisIndex == -1:
                    break
                
                queueBuffer.append([lastToken, thisIndex])
                if len(queueBuffer) >= TokenGenerator._PAIR_BUFFER:
                    tokenOutQueue.put(queueBuffer)
                    queueBuffer = []
                lastToken = thisIndex

            if len(queueBuffer) > 0:
                tokenOutQueue.put(queueBuffer)
            
            file.close()
            if fileQueue.empty():
                if startedFile:
                    fileQueue.task_done()
                continue
            if startedFile:
                fileQueue.task_done()

    @staticmethod
    def updateTree(tree: TernarySearchTree, queue: Queue):
        while not queue.empty():
            newPair = queue.get()
            tree.add(newPair[0], newPair[1])
    
    @staticmethod
    def finishListener(queue: JoinableQueue, boolean):
        boolean.value = False
        print("START")
        queue.join()
        print("END")
        boolean.value = True

    def addBaseToken(self, token: str):
        if token in self.getCanonList():
            raise ValueError("Token " + token + " is already in the canon list!")
        for queue in self.outQueues:
            queue.put([token, len(self.tokensList)])
        self.tokens.add(token, len(self.tokensList))
        self.tokensList.append(token)
        self.tokensExist.append(True)
        self._tokenCount += 1
        for i in range(len(self.tokensList) - 1):
            self.countArray[i].append(None)
        self.countArray.append([None for i in range(len(self.tokensList))])