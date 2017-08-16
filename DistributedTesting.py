import math
class UnitTest:

    def __init__(self):
        self.version = 0.1
        self.description = "Distributed Indexing for Threads/Process based on ordered collections."
        self.author = "Javier Cienfuegos Jr"

    def test(self, numThreads, numItems):
        load = math.floor(numItems // numThreads)
        iterThread = numThreads - 1
        remainderItems = numItems % numThreads
        
        b_startIndex = [load*i for i in range(numThreads)]
        b_endIndex = [(load*(i + 1) - 1) for i in range(numThreads)]

        print("Before Starts : {}".format(b_startIndex))
        print("Before Ends {}".format(b_endIndex))

        print("\n\nBefore normalizing...")
        for i in range(numThreads):
            print("Thread {0} Distribution Count: {1}".format(i, b_endIndex[i] - b_startIndex[i]))

        f_startIndex = [0 for i in range(numThreads)]
        f_endIndex = [0 for i in range(numThreads)]

        for i in range(numThreads):
            f_startIndex[i] = b_startIndex[i]
            f_endIndex[i] = b_endIndex[i]
   
        if remainderItems != 0:
            # Normalization based on remainder
            while remainderItems > 0:
                offSet = f_endIndex[iterThread] - f_startIndex[iterThread] + 1
                f_endIndex[iterThread] = f_endIndex[iterThread] + remainderItems
                f_startIndex[iterThread] = f_endIndex[iterThread] - offSet
                remainderItems -= 1
                iterThread -= 1

            print("After Starts {0}".format(f_startIndex))
            print("After Ends {0}".format(f_endIndex))
            print("After normalizing...")
            for i in range(numThreads):
                print("Thread {0} Distribution Count: {1}".format(i, f_endIndex[i] - f_startIndex[i]))
