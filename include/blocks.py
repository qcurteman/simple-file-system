import numpy as np
import include.diskpy as diskpy

class Block:
    data_type = 'int32'
    block_size_bytes = diskpy.Disk.BLOCK_SIZE_BYTES
        

class Superblock:

    '''
        Superblock structure

        Attributes:

            magic_number (arr[0]):
                - Number the verifies that the disk is good to read
            nblocks (arr[1]):
                - Number of blocks, including the superblock, that are on the disk
            ninodeblocks (arr[2]):
                - Number of blocks set aside for storing Inodes
            ninodes (arr[3]):
                - Number of Inodes that is in each InodeBlock
            directory_inode (arr[4]):
                - ????
            datablock_bitmap_loc (arr[5]):
                - Blocknumber where the databitmap is stored
            inode_bitmap_loc (arr[6]):
                - Blocknumber where the inodebitmap is stored
            first_datablock (arr[7]):
                - Blocknumber where the first datablock is stored
            first_inodeblock (arr[8]):
                - Blocknumber where the first inodeblock is stored
    '''
    def __init__(self, superblock=[]):
        if any(superblock):
            self.magic_number = superblock[0]
            self.nblocks = superblock[1] # number of blocks on disk. Includes the super block
            self.ninodeblocks = superblock[2] # number of blocks set aside for storing inodes
            self.ninodes = superblock[3] # number of inodes that is in each inodeblock
            self.directory_inode = superblock[4]
            self.datablock_bitmap_loc = superblock[5]
            self.inode_bitmap_loc = superblock[6]
            self.first_datablock = superblock[7]
            self.first_inodeblock = superblock[8]


    @classmethod
    def make_block(cls, nblocks=50, ninodeblocks=4,):
        arr = np.zeros(shape=(Block.block_size_bytes // 4), dtype=Block.data_type)
        arr[0] = 11111
        arr[1] = nblocks
        arr[2] = ninodeblocks 
        arr[3] = Block.block_size_bytes // Inode.size_bytes
        arr[4] = 0
        arr[5] = 1
        arr[6] = 2
        arr[7] = arr[2] + arr[6] + 1 # put it right after the last inodeblock 
        arr[8] = arr[6] + 1 # put it right after the inodebitmap block   

        return arr


class Inode:

    '''
        Inode Structure:

        Attributes:

            is_valid:
                - 0 (False) if the inode has not been used yet
                - 1 (True) if the inode has been used
            size: 
                - Size of a single Inode
            direct:
                - list of addresses that point to data blocks
            indirect: 
                - holds an address that points to an indirect block
    '''


    size_bytes = 32 # logical size of inode data in bytes
    num_indexes = 8 # This is the number of indexes
    num_direct_pointers = 2
    FREE = 0
    USED = 1
    BAD = 99

    def __init__(self, inode):
        self.is_valid = inode[0]
        self.size_bytes = inode[1]
        self.direct = [] # points to data blocks
        for i in range(Inode.num_direct_pointers):
            self.direct.append(inode[i + 2])
        self.indirect = inode[2 + Inode.num_direct_pointers] # points to an indirect block

    @classmethod
    def make_inode(cls, is_valid=0, direct_blocks=[0]*num_direct_pointers, indirect_loc=0):
        arr = np.zeros(shape=(Inode.num_indexes), dtype=Block.data_type)
        arr[0] = Inode.FREE
        arr[1] = Inode.size_bytes
        index = 0
        for i in range(2, len(direct_blocks)):
            arr[i] = direct_blocks[index]
            index += 1
        arr[2 + len(direct_blocks)] = indirect_loc
        return arr


class InodeBlock:
    
    '''
        InodeBlock structure
            
            Holds however many Inodes will fit within the size of a single block
    
    '''

    def __init__(self, inodeblock):
        self.num_inodes = Block.block_size_bytes // Inode.size_bytes
        self.inodes = []
        for i in range(self.num_inodes):
            self.inodes.append(Inode(inodeblock[i*Inode.num_indexes : (i+1)*Inode.num_indexes]))

    @classmethod
    def make_block(cls, ):
        num_inodes = Block.block_size_bytes // Inode.size_bytes
        merged_inodes = np.zeros(shape=(Block.block_size_bytes // 4), dtype=Block.data_type)
        inode = Inode.make_inode()
        index = 0
        for _ in range(num_inodes):
            for item in inode:
                merged_inodes[index] = item
                index += 1
        return merged_inodes


class IndirectBlock:

    # consists of 1024 4-byte pointers that point to data blocks
    def __init__(self, ):
        pass


class DataBlock:
    def __init__(self, ):
        self.data = np.zeros(shape=(Block.block_size_bytes // 4, 1), dtype=Block.data_type)


def initialize_blocks(open_disk, disk_size):
    superblock_raw = Superblock.make_block(nblocks=disk_size)
    inodeblock_raw = InodeBlock.make_block()
    superblock = Superblock(superblock_raw)

    diskpy.Disk.disk_write(open_disk, 0, superblock_raw)
    for i in range(superblock.ninodeblocks):
        diskpy.Disk.disk_write(open_disk, superblock.first_inodeblock + i, inodeblock_raw)
