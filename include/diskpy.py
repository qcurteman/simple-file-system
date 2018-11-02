
import include.blocks
import numpy as np

class Disk:

    DISK_BLOCK_SIZE = 16 # 4096


    # a row is a block
    def __init__(self, diskname, nbrOfBlocks):
        self.BLOCKS = []
        self.NUM_BLOCKS = int(nbrOfBlocks)
        self.diskname = diskname
        self.disk = np.zeros(shape=(self.NUM_BLOCKS, Disk.DISK_BLOCK_SIZE), dtype='int8')
        with open('data/{}'.format(self.diskname), 'wb') as f:
            f.write(self.disk)

    def disk_open(self, diskname):
        # write what is in the disk called "diskname" to self.disk
        pass

    def disk_read(self, blockNumber):
        assert(blockNumber <= self.NUM_BLOCKS), 'The block number requested is greater than the number of total blocks.'

        start_address = Disk.DISK_BLOCK_SIZE * blockNumber
        byte_array, block_data = [], []

        with open('data/{}'.format(self.diskname), 'rb') as f:
            f.seek(start_address)
            for _ in range(Disk.DISK_BLOCK_SIZE):
                byte_array.append(f.read(1))

        for item in byte_array:
            block_data.append(int.from_bytes(item, 'little'))

        return block_data

                
                    

    def disk_write(self, blockNumber, byteArray):
        assert(blockNumber <= self.NUM_BLOCKS), 'The block number requested is greater than the number of total blocks.'
        # Handle the cases where it is trying to write more than 1 block and the case 
        # where it is writing less than 1 block (do this in the file system)
        for i in range(len(self.disk[blockNumber])):
            self.disk[blockNumber][i] = byteArray[i]
        with open('data/{}'.format(self.diskname), 'wb') as f:
            f.write(self.disk)


    def disk_status(self, ):
        print('The disk is doing GREAT!!')

    def disk_close(self, ):
        # I think we need to make the filesystem before we can make this method
        pass

# disk1 = Disk('qdisk.bin', 6)
# barr = bytearray([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8])
# disk1.disk_write(3, barr)
# print(disk1.disk_read(3))
