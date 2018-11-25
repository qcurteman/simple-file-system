
import struct

class Disk:

    BLOCK_SIZE_BYTES = 512 # 4096
    ENCODING = 'utf8'

    # a row is a block
    @classmethod
    def disk_init(cls, diskname, nbrOfBlocks=32):
        blank_block = bytearray(Disk.BLOCK_SIZE_BYTES)
        with open('data/{}'.format(diskname), 'wb+') as f:
            [ f.write(blank_block) for _ in range(int(nbrOfBlocks)) ]
                
    @classmethod
    def disk_open(cls, diskname):
        fl = open('data/{}'.format(diskname), 'rb+')
        return fl

    @classmethod
    def disk_read(cls, open_file, blockNumber):
        start_address = Disk.BLOCK_SIZE_BYTES * blockNumber
        byte_array, block_data = [], []

        open_file.seek(start_address)
        # for _ in range(Disk.BLOCK_SIZE):
        #     byte_array.append(open_file.read(1))

        # for item in byte_array:
        #     block_data.append(int.from_bytes(item, 'little'))

        for _ in range(Disk.BLOCK_SIZE_BYTES // 4):
            block_data.append(struct.unpack('i', open_file.read(4))[0])

        return block_data

    @classmethod
    def disk_write(cls, open_file, blockNumber, data): 
        start_address = Disk.BLOCK_SIZE_BYTES * blockNumber
        open_file.seek(start_address)

        # if type(data) == list:
        #     for item in data:
        #         if type(item) == str:
        #             # byte_data += bytes(item, Disk.ENCODING)
        #             open_file.write(item.encode('ascii'))
        #             start_address += 24
        #             open_file.seek(start_address)
        #         else:
        #             # temp = item)
        #             # byte_data += bytes(item)
        #             open_file.write(bytearray(item))
        #             start_address += 4
        #             open_file.seek(start_address)
        # else:
        #     # Check the data type to determine how to convert to binary
        if type(data) == str:
            byte_data = bytearray(data, Disk.ENCODING)
        else:
            byte_data = bytearray(data)

            open_file.write(byte_data[:])

        # for debugging
        for i in range(10):
            print('Block ', i)
            print(Disk.disk_read(open_file, i))

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
        
        