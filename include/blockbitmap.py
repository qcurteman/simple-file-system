class BlockBitmap():

    def __init__(self, arraysize, blockNbr):
        self.blockNbr = blockNbr
        self.arraysize = arraysize
        self.blockbitmap = np.zeros(shape=(blocksize, 1), dtype='int8')

    def init(self):
        # initialize the array with FREE and BAD
        pass

    def setFree(self, atOffset):
        pass

    def setUsed(self, atOffset):
        pass

    def findFree(self):
        pass

    def saveToDisk(self):
        pass
    