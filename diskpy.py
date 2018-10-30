
import blocks
import numpy as np

class Disk:

    DISK_BLOCK_SIZE = 8 # 4096


    # a row is a block
    def __init__(self, diskname, nbrOfBlocks):
        self.BLOCKS = []
        self.diskname = diskname
        self.disk = np.zeros(shape=(nbrOfBlocks, Disk.DISK_BLOCK_SIZE), dtype='int16')
        with open(self.diskname, 'wb') as f:
            f.write(self.disk)

    def disk_open(filename): #this filename is the filename of a file in the file system
        pass

    def disk_read(blockNumber):
        f = open("qdisk.bin", "rb")
        try:
            byte = f.read(1)
            while byte != "":
                # Do stuff with byte.
                byte = f.read(1)
                print(byte)
        finally:
            f.close()

    def disk_write(self, blockNumber, byteArray): # why is this a bypteArray
        for i in range(len(self.disk[blockNumber])):
            self.disk[blockNumber][i] = byteArray[i]
        with open(self.diskname, 'wb') as f:
            f.write(self.disk)

    def disk_status():
        pass

    def disk_close():
        pass

disk1 = Disk('qdisk.bin', 5)
barr = bytearray([7,2,3,4,5,6,7,8])
disk1.disk_write(3, barr)