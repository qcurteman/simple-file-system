
import numpy as np
class Block:
    pass
    # size = Disk.BLOCK_SIZE

    # def __init__(self, start_address):
    #     self.start_address = start_address
        

class Superblock(Block):

    '''
        Superblock structure

            magic_number:
                - Number the verifies that the disk is good to read
            nblocks:
                - Number of blocks, including the superblock, that are on the disk
            ninodeblocks:
                - Number of blocks set aside for storing Inodes
            ninodes:
                - Number of I nodes that is in each InodeBlock
            bitmap_location:
                - Address where the bitmap block is stored
    
    '''

    # def __init__(self, nblocks, ninodeblocks, ninodes):
    #     super().__init__(0)
    #     self.magic_number = '0xf0f03410'
    #     self.nblocks = nblocks # includes the super block
    #     self.ninodeblocks = ninodeblocks # number of blocks set aside for storing inodes
    #     self.ninodes = ninodes # number of inodes that is in each inodeblock

    @classmethod
    def make_block(cls, block_size, nblocks=50, ninodeblocks=4, ninodes=2):
        arr = np.zeros(shape=(block_size), dtype='int8')
        arr[0] = 111
        arr[1] = nblocks # includes the super block
        arr[2] = ninodeblocks # number of blocks set aside for storing inodes
        arr[3] = ninodes # number of inodes that is in each inodeblock
        return bytearray(arr)


class Inode:

    '''
        Inode Structure:

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


    size = 8 # logical size of inode data in bytes

    # def __init__(self,):
    #     self.is_valid = False # 1 if the inode is valid (has been created) and is 0 otherwise.
    #     self.direct = [] * 5 # points to data blocks
    #     self.indirect = 0 # points to an indirect block

    # returns a bytearray
    @classmethod
    def make_inode(cls, is_valid=False, direct_blocks=[0]*5, indirect_loc=0):
        arr = np.zeros(shape=(Inode.size), dtype='int8')
        arr[0] = is_valid
        arr[1] = Inode.size
        index = 0
        for i in range(2, len(direct_blocks)):
            arr[i] = direct_blocks[index]
            index += 1
        arr[2 + len(direct_blocks)] = indirect_loc
        return bytearray(arr)


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
        num_inodes = int( block_size / Inode.size)
        merged_inodes = np.zeros(shape=(block_size), dtype='int8')
        inode = Inode.make_inode()
        index = 0
        for _ in range(num_inodes):
            for item in inode:
                merged_inodes[index] = item
                index += 1
        return bytearray(merged_inodes)


class IndirectBlock(Block):

    # consists of 1024 4-byte pointers that point to data blocks
    def __init__(self, ):
        pass


class DataBlock(Block):
    def __init__(self, ):
        pass


# print('Superblock: ', Superblock.make_block())
# print('Inode: ', Inode.make_inode())
# print('Inode Block: ', InodeBlock.make_block())