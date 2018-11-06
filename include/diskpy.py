
import include.blocks

class Disk:

    BLOCK_SIZE = 4 # 4096


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

        # Write full blocks to the disk
        for i in range(num_blocks):
            open_file.write(byte_data[Disk.BLOCK_SIZE * i : Disk.BLOCK_SIZE * (i+1)])

        # Write any left over blocks
        open_file.write(byte_data[Disk.BLOCK_SIZE * (num_blocks - 1):])

    @classmethod
    def disk_status(cls, ):
        print('The disk is doing GREAT!!')

    @classmethod
    def disk_close(cls, open_file):
        open_file.close()

# disk1 = Disk('qdisk.bin', 6)
barr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# disk1.disk_write(3, barr)
# print(disk1.disk_read(3))


Disk.disk_init('qdisk2.bin', 50)
open_file = Disk.disk_open('qdisk2.bin')
print(Disk.disk_read(open_file, 30))
Disk.disk_write(open_file, 30, barr)
print(Disk.disk_read(open_file, 30))
print(Disk.disk_read(open_file, 31))
print(Disk.disk_read(open_file, 32))
print(Disk.disk_read(open_file, 33))
Disk.disk_close(open_file)
