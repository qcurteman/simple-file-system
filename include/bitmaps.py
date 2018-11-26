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

    def __init__(self, arraysize, block_number, maptype):
        self.bitmap = np.zeros(shape=(arraysize), dtype=blocks.Block.data_type)
        self.arraysize = arraysize
        self.block_number = block_number
        self.maptype = maptype
        

    def init(self, open_file):
        # initialize the array with FREE, USED, and BAD
        superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))
        if self.maptype == 'inode':
            self.init_inode(open_file, superblock)
        elif self.maptype == 'data':
            pass
            # TODO: Figure out what this is supposed to be scanning cuz i'm having the prob where 1 block isn't big enough
            # self.init_data(open_file, superblock)
        else:
            raise('ERROR: Incorrect maptype set.')

    def init_inode(self, open_file, superblock):
        start_block = superblock.first_inodeblock
        index = 0

        for i in range(superblock.ninodeblocks):
            inodeblock = blocks.InodeBlock(diskpy.Disk.disk_read(open_file, start_block + i))
            for inode in inodeblock.inodes:
                self.bitmap[index] = inode.is_valid
                index += 1
        
        for i in range(superblock.ninodeblocks * superblock.ninodes, self.bitmap.shape[0]):
            self.bitmap[i] = bitmap.BAD

        self.saveToDisk(open_file)

    def init_data(self, open_file, superblock):# superblock  bitmaps  
        total_datablocks = superblock.nblocks       - 1       - 2    - superblock.ninodeblocks

        start_block = superblock.first_inodeblock
        index = 0

        for i in range(superblock.ninodeblocks):
            inodeblock = blocks.InodeBlock(diskpy.Disk.disk_read(open_file, start_block + i))
            for inode in inodeblock.inodes:
                if inode.is_valid == inode.USED:
                    for item in inode.direct:
                        if item != 0:
                            self.bitmap[index] = self.USED
                        else:
                            self.bitmap[index] = self.FREE
                        index += 1
                else:
                    for j in range(len(inode.direct)):
                        self.bitmap[index] = self.FREE
                        index += 1

        self.saveToDisk(open_file)


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
    arraysize32 = diskpy.Disk.BLOCK_SIZE_BYTES // 4

    inodebitmap = bitmap(arraysize32, superblock.inode_bitmap_loc, 'inode')
    inodebitmap.init(open_file)

    databitmap = bitmap(arraysize32, superblock.datablock_bitmap_loc, 'data') 
    databitmap.init(open_file)

    return inodebitmap, databitmap


