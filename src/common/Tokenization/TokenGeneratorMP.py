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

    def run(self):
        while self.tokenCount() < self.tokenAmount:
            print("New Cycle")
            self.heap = MaxFibonocciHeap()
            if self._removes > self._removesBeforeClean:
                self._removes = 0
                print("Cleaning")
                self.clean()

            for i in range(len(self.countArray)):
                for j in range(len(self.countArray[i])):
                    self.countArray[i][j] = None
            
            print("Filling file queue")
            for path in self.fileList:
                self.fileQueue.put(path)

            print("Making Processes")

            finished = Value(c_bool, False)
            listenerProcess = Process(target=TokenGeneratorDriverMP.finishListener, args=(self.fileQueue, finished))
            listenerProcess.start()

            processes: list[Process] = []

            for i in range(self._threads - 1):
                processes.append(Process(target=TokenGeneratorDriverMP.processFiles, args=(self.fileQueue, self.tokenPairQueue, self.tokens, self._allowWhitespace)))
                processes[-1].start()

            print("Beginning file analysis")

            while (not self.tokenPairQueue.empty()) or (not finished.value):
                try:
                    pairSet: list[list[int]] = self.tokenPairQueue.get(timeout=0.1)
                    for pair in pairSet: 
                        #pair: list[int] = self.tokenPairQueue.get(timeout=0.1)
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
            for process in processes:
                process.terminate()
            #print("Actual end")
            self.makeNewToken()
            print("Token count is:", self.tokenCount())

    @staticmethod
    def processFiles(fileQueue: JoinableQueue, tokenOutQueue: Queue, tree: TernarySearchTree, allowWhitespace: bool):
        while True:
            file = None
            if not fileQueue.empty():  
                path = fileQueue.get()
                file = open(path, 'r')
                #print("Starting in path:", path)
            else:
                break
            
            lastToken: int = TokenGenerator.getNextTokenGlobal(file, tree, allowWhitespace)
            if lastToken == -1:
                file.close()
                if fileQueue.empty():
                    fileQueue.task_done()
                    break
                fileQueue.task_done()
                continue

            queueBuffer = []

            while True:
                thisIndex = TokenGenerator.getNextTokenGlobal(file, tree, allowWhitespace)
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
                fileQueue.task_done()
                break
            fileQueue.task_done()
    
    @staticmethod
    def finishListener(queue: JoinableQueue, boolean):
        boolean.value = False
        print("START")
        queue.join()
        print("END")
        boolean.value = True