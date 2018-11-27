
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
    def disk_read_int(cls, open_file, blockNumber, offset):
        start_address = Disk.BLOCK_SIZE_BYTES * blockNumber
        int_val = []
        open_file.seek(start_address + offset)
        int_val = struct.unpack('i', open_file.read(4))[0]
        return int_val

    @classmethod
    def disk_read_str(cls, open_file, blockNumber, offset):
        start_address = Disk.BLOCK_SIZE_BYTES * blockNumber
        str_val = []
        open_file.seek(start_address + offset)
        for _ in range(28):
            byte = open_file.read(1)
            str_temp = byte.decode('utf8')
            if str_temp != '\x00':
                str_val.append(str_temp)
        # str_val1 = open_file.read(28)
        # str_val = str_val1.decode('utf8')
        return ''.join(str_val)

    @classmethod
    def disk_read(cls, open_file, blockNumber):
        start_address = Disk.BLOCK_SIZE_BYTES * blockNumber
        block_data = []

        open_file.seek(start_address)

        for _ in range(Disk.BLOCK_SIZE_BYTES // 4):
            block_data.append(struct.unpack('i', open_file.read(4))[0])

        return block_data

    @classmethod
    def disk_write(cls, open_file, blockNumber, data, start_address=None): 
        if start_address == None:
            start_address = Disk.BLOCK_SIZE_BYTES * blockNumber
        
        open_file.seek(start_address)

        if type(data) == list:
            for item in data:
                open_file.seek(start_address)
                if type(item) == str:
                    open_file.write(item.encode('utf8'))
                    start_address += 28
                else:
                    temp = bytes([item])
                    open_file.write(temp[:])
                    start_address += 4
        else:
            # Check the data type to determine how to convert to binary
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
        
        