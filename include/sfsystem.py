
import include.diskpy as diskpy
import include.blocks as blocks
class filesystem:

    # TODO: add fs_bitmap

    disks = []
    mounted_disk = None

    @classmethod
    def fs_format(cls,):
        open_disk = diskpy.Disk.disk_open(filesystem.mounted_disk)
        disk_size = diskpy.Disk.disk_size(open_disk)
        diskpy.Disk.disk_init(filesystem.mounted_disk, disk_size)
        filesystem.initialize_blocks(open_disk, disk_size) # TODO: Eventually make the initializing of the blocks happen in the disk
        diskpy.Disk.disk_close(open_disk)

    @classmethod
    def fs_debug(cls, ):
        print('Debugging...')

    def fs_mount():
        print('Mounting disk.')

    def fs_create():
        print('Creating disk.')

    def fs_delete( file ):
        print('Deleting.')

    def fs_getsize( file ):
        print('Disk size: ')

    def fs_read( file, length, offset ):
        print('Reading disk.')

    def fs_write( file, data, length, offset ):
        print('Writing to disk.')


    @classmethod
    def new_disk(cls, diskname, numblocks):
        diskpy.Disk.disk_init(diskname, numblocks)
        open_disk = diskpy.Disk.disk_open(diskname)
        filesystem.initialize_blocks(open_disk, numblocks)
        diskpy.Disk.disk_close(open_disk)
        filesystem.disks.append(diskname)


    @classmethod
    def initialize_blocks(cls, open_disk, disk_size): # TODO: Move this functionality to happen in the diskpy.py
        superblock = blocks.Superblock.make_block(nblocks=disk_size)
        inodeblock = blocks.InodeBlock.make_block()

        diskpy.Disk.disk_write(open_disk, 0, superblock)
        for i in range(1, 4):
            diskpy.Disk.disk_write(open_disk, i, inodeblock)