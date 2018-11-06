
import include.blocks

class Disk:

    BLOCK_SIZE = 8 # 4096


    # a row is a block
    @classmethod
    def disk_init(cls, diskname, nbrOfBlocks=32):
        blank_block = bytearray(Disk.BLOCK_SIZE)
        with open('data/{}'.format(diskname), 'rb+') as f:
            [ f.write(blank_block) for _ in range(nbrOfBlocks) ]
                
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

        byte_data = bytearray(data)
        num_blocks = int(len(byte_data) / Disk.BLOCK_SIZE)

        open_file.write(byte_data[:])

    @classmethod
    def disk_status(cls, ):
        print('The disk is doing GREAT!!')

    @classmethod
    def disk_close(cls, open_file):
        open_file.close()

# disk1 = Disk('qdisk.bin', 6)
barr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
barr1 = [9,8,7,6,5,4,3,2,1]
# disk1.disk_write(3, barr)
# print(disk1.disk_read(3))


# Disk.disk_init('qdisk2.bin', 50)
open_file = Disk.disk_open('qdisk2.bin')

Disk.disk_write(open_file, 0, barr1)

print(Disk.disk_read(open_file, 0))

print(Disk.disk_read(open_file, 5))
print(Disk.disk_read(open_file, 6))
print(Disk.disk_read(open_file, 7))
print(Disk.disk_read(open_file, 8))

Disk.disk_close(open_file)
