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
        bitmap:
            - Actual bitmap

    Methods:

    '''

    def __init__(self, block_size, arraysize, block_number, maptype):
        self.bitmap = np.zeros(shape=(block_size, 1), dtype=blocks.Block.data_type)
        self.arraysize = arraysize
        self.block_number = block_number
        self.maptype = maptype
        

    def init(self, open_file):
        # initialize the array with FREE, USED, and BAD
        superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))
        if self.maptype == 'inode':
            self.init_inode(open_file, superblock)
        elif self.maptype == 'data':
            self.init_data(open_file, superblock)
        else:
            raise('ERROR: Incorrect maptype set.')

    def init_inode(self, open_file, superblock):
        start_block = superblock.first_inodeblock
        index = 0

        for i in range(superblock.ninodeblocks):
            inodeblock = blocks.InodeBlock(diskpy.Disk.disk_read(open_file, start_block + i))
            for inode in inodeblock.inodes:
                self.bitmap[index][0] = inode.is_valid
                index += 1
        
        for i in range(superblock.ninodeblocks * superblock.ninodes, self.bitmap.shape[0]):
            self.bitmap[i][0] = bitmap.BAD

        self.saveToDisk(open_file)

    def init_data(self, open_file, superblock):
        pass

    def setFree(self, open_file, atOffset):
        pass

    def setUsed(self, open_file, atOffset):
        pass

    def findFree(self, open_file):
        pass

    def saveToDisk(self, open_file): # save the contents of "self.bitmap" to the disk
        superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))

        if self.maptype == 'inode':
            diskpy.Disk.disk_write(open_file, superblock.inode_bitmap_loc, self.bitmap)
        elif self.maptype == 'data':
            diskpy.Disk.disk_write(open_file, superblock.datablock_bitmap_loc, self.bitmap)
        else:
            raise('ERROR: Incorrect maptype set.')


def load_bitmaps(open_file):
    superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))

    inodebitmap = bitmap(diskpy.Disk.BLOCK_SIZE, superblock.ninodeblocks, superblock.inode_bitmap_loc, 'inode')
    inodebitmap.init(open_file)

    databitmap = bitmap(diskpy.Disk.BLOCK_SIZE, 4, superblock.datablock_bitmap_loc, 'data') # TODO: Change the 4 to be the num of data blocks on the disk. Maybe this: (superblock.nblocks - superblock.first_datablock)
    databitmap.init(open_file)

    return inodebitmap, databitmap


