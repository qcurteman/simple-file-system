
import include.diskpy as diskpy
import include.blocks as blocks
from os import listdir, getcwd

class filesystem:

    disks = []
    mounted_disk = None

    @classmethod
    def fs_format(cls,):
        open_disk = diskpy.Disk.disk_open(filesystem.mounted_disk)
        disk_size = diskpy.Disk.disk_size(open_disk)
        diskpy.Disk.disk_init(filesystem.mounted_disk, disk_size)
        diskpy.Disk.initialize_blocks(open_disk, disk_size)
        diskpy.Disk.disk_close(open_disk)

    @classmethod
    def fs_debug(cls, ):
        print('Debugging...')

    @classmethod
    def fs_mount(cls, diskname):
        diskpy.Disk.disk_open(diskname)
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

    @classmethod
    def fs_write(cls, file, data, length, offset ):
        print('Writing to disk.')

    @classmethod
    def fs_open_disk(cls, diskname, numblocks):
        filesystem.disks = listdir('{}/data'.format(getcwd()))
        if diskname not in filesystem.disks:
            diskpy.Disk.new_disk(diskname, numblocks)
            filesystem.disks.append(diskname)
        filesystem.mounted_disk = diskname
    
    @classmethod
    def fs_scan(cls, ):
        pass

    
