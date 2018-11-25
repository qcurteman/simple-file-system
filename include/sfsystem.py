
import include.diskpy as diskpy
import include.blocks as blocks
import include.bitmaps as bitmap
from os import listdir, getcwd

class filesystem:

    disks = []
    mounted_disk = None
    inodebitmap = None
    databitmap = None

    @classmethod
    def fs_format(cls,):
        open_disk = diskpy.Disk.disk_open(filesystem.mounted_disk)
        disk_size = diskpy.Disk.disk_size(open_disk)
        diskpy.Disk.disk_init(filesystem.mounted_disk, disk_size)
        blocks.initialize_blocks(open_disk, disk_size)
        # filesystem.fs_scan(open_disk)
        diskpy.Disk.disk_close(open_disk)

    @classmethod
    def fs_debug(cls, ):
        print('Debugging...')

    @classmethod
    def fs_mount(cls, diskname):
        filesystem.fs_scan()
        filesystem.mounted_disk = diskname

    @classmethod
    def fs_create(cls, ):
        print('Creating disk.')

    @classmethod
    def fs_delete(cls, file ):
        print('Deleting.')

    @classmethod
    def fs_getsize(cls, file ):
        print('Disk size: ')

    @classmethod
    def fs_read(cls, file, length, offset ):
        print('Reading disk.')
        # open_disk = diskpy.Disk.disk_open(filesystem.mounted_disk)
        # sup = blocks.Superblock(diskpy.Disk.disk_read(open_disk, 0))
        # inodeblock = blocks.InodeBlock(diskpy.Disk.disk_read(open_disk, 3))
        # print(sup)
        # print(inodeblock)
        # diskpy.Disk.disk_close(open_disk)

    @classmethod
    def fs_write(cls, file, data, length, offset ):
        print('Writing to disk.')

    @classmethod
    def fs_open_disk(cls, diskname, numblocks):
        filesystem.disks = listdir('{}/data'.format(getcwd()))
        if diskname not in filesystem.disks:
            filesystem.new_disk(diskname, numblocks)
            filesystem.disks.append(diskname)
        filesystem.mounted_disk = diskname

    @classmethod
    def new_disk(cls, diskname, numblocks):
        diskpy.Disk.disk_init(diskname, numblocks)
        open_disk = diskpy.Disk.disk_open(diskname)
        blocks.initialize_blocks(open_disk, numblocks)
        # filesystem.fs_scan(open_disk)
        diskpy.Disk.disk_close(open_disk)
        return diskname
    
    @classmethod
    def fs_scan(cls, open_file=None):
        if open_file == None:
            open_file1 = diskpy.Disk.disk_open(filesystem.mounted_disk)
            filesystem.inodebitmap, filesystem.databitmap = bitmap.load_bitmaps(open_file1)
            diskpy.Disk.disk_close(open_file1)
        else:
            filesystem.inodebitmap, filesystem.databitmap = bitmap.load_bitmaps(open_file)

    @classmethod
    def fs_touch(cls, filename):
        pass

    @classmethod
    def fs_ls(cls, ):
        pass

    @classmethod
    def fs_open(cls, filename):
        # open_file = diskpy.Disk.disk_open(filesystem.mounted_disk)
        # diskpy.Disk.disk_write(open_file, 7, 'waterfungi')
        # diskpy.Disk.disk_close(open_file)
        blocks.DataBlock.make_block()

    @classmethod
    def fs_display(cls, filename):
        pass