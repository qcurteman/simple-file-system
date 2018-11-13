
import numpy as np
class Block:
    data_type = 'int32'
        

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
    def __init__(self, superblock=None):
        if superblock != None:
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
    def make_block(cls, block_size, nblocks=50, ninodeblocks=4,):
        arr = np.zeros(shape=(block_size), dtype=Block.data_type)
        arr[0] = 11111
        arr[1] = nblocks
        arr[2] = ninodeblocks 
        arr[3] = block_size // Inode.size
        arr[4] = 0
        arr[5] = 1
        arr[6] = 2
        arr[7] = arr[2] + arr[6] + 1 # put it right after the last inodeblock 
        arr[8] = arr[6] + 1 # put it right after the inodebitmap block
        return arr

class BlockBitmap(Block):

    '''
    BlockBitmap structure

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
        self.blockbitmap = np.zeros(shape=(block_size, 1), dtype=data_type)

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


    size = 32 # logical size of inode data in bytes
    num_indexes = 8 # This is the number of indexes 

# def __init__(self,):
    #     self.is_valid = False # 1 if the inode is valid (has been created) and is 0 otherwise.
    #     self.direct = [] * 5 # points to data blocks
    #     self.indirect = 0 # points to an indirect block
    @classmethod
    def make_inode(cls, is_valid=False, direct_blocks=[0]*5, indirect_loc=0):
        arr = np.zeros(shape=(Inode.num_indexes), dtype=Block.data_type)
        arr[0] = True
        arr[1] = Inode.size
        index = 0
        for i in range(2, len(direct_blocks)):
            arr[i] = direct_blocks[index]
            index += 1
        arr[2 + len(direct_blocks)] = indirect_loc
        return arr


class InodeBlock(Block):
    
    '''
        InodeBlock structure
            
            Holds however many Inodes will fit within the size of a single block
    
    '''


    # consists of 128 Inodes
    # def __init__(self, start_address):
    #     super().__init__(start_address)
    #     num_inodes = int( Block.size / Inode.size)
    #     self.inodes = []
    #     for _ in range(num_inodes):
    #         self.inodes.append(Inode())

    @classmethod
    def make_block(cls, block_size):
        num_inodes = block_size // Inode.size
        merged_inodes = np.zeros(shape=(block_size), dtype=Block.data_type)
        inode = Inode.make_inode()
        index = 0
        for _ in range(num_inodes):
            for item in inode:
                merged_inodes[index] = item
                index += 1
        return merged_inodes


class IndirectBlock(Block):

    # consists of 1024 4-byte pointers that point to data blocks
    def __init__(self, ):
        pass


class DataBlock(Block):
    def __init__(self, block_size):
        self.data = np.zeros(shape=(block_size, 1), dtype=Block.data_type)
