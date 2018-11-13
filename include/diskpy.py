
import struct

class Disk:

    BLOCK_SIZE = 512 # 4096
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
        # for _ in range(Disk.BLOCK_SIZE):
        #     byte_array.append(open_file.read(1))

        # for item in byte_array:
        #     block_data.append(int.from_bytes(item, 'little'))

        for _ in range(Disk.BLOCK_SIZE//4):
            block_data.append(struct.unpack('i', open_file.read(4))[0])

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
        
        