import include.blocks as blocks

class Disk:

    BLOCK_SIZE = 16 # 4096
    ENCODING = 'utf8'

    # a row is a block
    @classmethod
    def disk_init(cls, diskname, nbrOfBlocks=32):
        blank_block = bytearray(Disk.BLOCK_SIZE)
        with open('data/{}'.format(diskname), 'wb+') as f:
            [ f.write(blank_block) for _ in range(int(nbrOfBlocks)) ]
                
    @classmethod
    def disk_open(cls, diskname):
        fl = open('data/{}'.format(diskname), 'rb+')
        return fl

    @classmethod
    def disk_read(cls, open_file, blockNumber):
        start_address = Disk.BLOCK_SIZE * blockNumber
        byte_array, block_data = [], []

        open_file.seek(start_address)
        for _ in range(Disk.BLOCK_SIZE):
            byte_array.append(open_file.read(1))

        for item in byte_array:
            block_data.append(int.from_bytes(item, 'little'))

        return block_data

    @classmethod
    def disk_write(cls, open_file, blockNumber, data): 
        start_address = Disk.BLOCK_SIZE * blockNumber
        open_file.seek(start_address)

        # Check the data type to determine how to convert to binary
        if type(data) == str:
            byte_data = bytearray(data, Disk.ENCODING)
        else:
            byte_data = bytearray(data)

        open_file.write(byte_data[:])

    @classmethod
    def disk_size(cls, open_file):
        superblock = Disk.disk_read(open_file, 0)
        return superblock[1]

    @classmethod
    def disk_status(cls, ):
        print('The disk is doing GREAT!!')

    @classmethod
    def disk_close(cls, open_file):
        open_file.close()

    @classmethod
    def new_disk(cls, diskname, numblocks):
        Disk.disk_init(diskname, numblocks)
        open_disk = Disk.disk_open(diskname)
        Disk.initialize_blocks(open_disk, numblocks)
        Disk.disk_close(open_disk)
        return diskname

    @classmethod
    def initialize_blocks(cls, open_disk, disk_size):
        superblock = blocks.Superblock.make_block(block_size=Disk.BLOCK_SIZE, nblocks=disk_size)
        inodeblock = blocks.InodeBlock.make_block(block_size=Disk.BLOCK_SIZE)

        Disk.disk_write(open_disk, 0, superblock)
        for i in range(1, 4):
            Disk.disk_write(open_disk, i, inodeblock)
