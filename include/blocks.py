from include.diskpy import Disk
class Block:

    size = Disk.BLOCK_SIZE

    def __init__(self, start_address):
        self.start_address = start_address
        

class Superblock(Block):

    def __init__(self, nblocks, ninodeblocks, ninodes):
        super().__init__(0)
        self.magic_number = '0xf0f03410'
        self.nblocks = nblocks # includes the super block
        self.ninodeblocks = ninodeblocks # number of blocks set aside for storing inodes
        self.ninodes = ninodes # number of inodes that is in each inodeblock


class Inode:

    size = 8 # logical size of inode data in bytes

    # TODO: Figure out the size of an inode so that I can figure out how many I can fit in an inodeblock
    def __init__(self,):
        self.is_valid = False # 1 if the inode is valid (has been created) and is 0 otherwise.
        self.direct = [] * 5 # points to data blocks
        self.indirect = 0 # points to an indirect block


class InodeBlock(Block):
    
    # consists of 128 Inodes
    def __init__(self, start_address):
        super().__init__(start_address)
        num_inodes = int( Block.size / Inode.size)
        self.inodes = []
        for _ in range(num_inodes):
            self.inodes.append(Inode())


class IndirectBlock(Block):

    # consists of 1024 4-byte pointers that point to data blocks
    def __init__(self, ):
        pass


class DataBlock(Block):
    def __init__(self, ):
        pass




testblock = Superblock(1, 2, 5)
print(testblock.size)
print(testblock.start_address)

b2 = InodeBlock(16)

print(b2.inodes)