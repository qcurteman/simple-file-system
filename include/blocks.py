
class Block:

    def __init__(self, ):
        self.size = '4KB' # TODO: fill this in correclty
        self.address # ??? maybe have a start address and end address ??
        

class Superblock(Block):

    def __init__(self, nblocks, ninodeblocks, ninodes):
        self.magic_number = '0xf0f03410'
        self.nblocks = nblocks # includes the super block
        self.ninodeblocks = ninodeblocks
        self.ninodes = ninodes


class Inode():

    # each field is 32-bits
    def __init__(self, size):
        self.is_valid = False
        self.size = size
        self.direct = [] # points to data blocks
        self.indirect = 0 # points to an indirect block


class InodeBlock(Block):
    
    # consists of 128 Inodes
    def __init__(self, ):
        pass


class IndirectBlock(Block):

    # consists of 1024 4-byte pointers that point to data blocks
    def __init__(self, ):
        pass


class DataBlock(Block):
    def __init__(self, ):
        pass