import include.blocks as blocks
import include.diskpy as diskpy
import numpy as np

class bitmap:

    FREE = 0
    USED = 1
    BAD = 99
    '''
    bitmap structure

    Attributes:

        block_size:
            - Size of a single block.
        arraysize:
            - Equal to the total number of certain block types (inode or data blocks) on the disk 
        blockbitmap:
            - Actual bitmap

    Methods:

    '''

    def __init__(self, block_size, arraysize, blockNbr):
        self.blockNbr = blockNbr
        self.arraysize = arraysize
        self.blockbitmap = np.zero(shape=(block_size, 1), dtype=blocks.Block.data_type)

    def init(self):
        # initialize the array with FREE, USED, and BAD
        pass

    def setFree(self, atOffset):
        pass

    def setUsed(self, atOffset):
        pass

    def findFree(self):
        pass

    def saveToDisk(self): # save the contents of "self.blockbitmap" to the disk
        pass


def load_bitmaps(open_file):
    superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))

    inodebitmap = bitmap(diskpy.Disk.BLOCK_SIZE, superblock.ninodeblocks, superblock.inode_bitmap_loc)
    databitmap = bitmap(diskpy.Disk.BLOCK_SIZE, 4, superblock.datablock_bitmap_loc) # TODO: Change the 4 to be the num of data blocks on the disk. Maybe this: (superblock.nblocks - superblock.first_datablock)

    return inodebitmap, databitmap


