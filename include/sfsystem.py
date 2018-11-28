
import include.diskpy as diskpy
import include.blocks as blocks
import include.bitmaps as bitmap
from os import listdir, getcwd

class filesystem:

    disks = []
    mounted_disk = None
    current_directory = None
    inodebitmap = None
    databitmap = None

    @classmethod
    def fs_format(cls,):
        open_file = diskpy.Disk.disk_open(filesystem.mounted_disk)
        disk_size = diskpy.Disk.disk_size(open_file)
        diskpy.Disk.disk_init(filesystem.mounted_disk, disk_size)
        blocks.initialize_blocks(open_file, disk_size)
        filesystem.init_directory(open_file)
        filesystem.fs_scan(open_file)
        diskpy.Disk.disk_close(open_file)

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
        open_file = diskpy.Disk.disk_open(diskname)
        blocks.initialize_blocks(open_file, numblocks)
        filesystem.init_directory(open_file)
        filesystem.fs_scan(open_file)
        diskpy.Disk.disk_close(open_file)
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
        open_file = diskpy.Disk.disk_open(filesystem.mounted_disk)
        superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))
        inode = blocks.Inode.get_inode(open_file, superblock.directory_inode)
        directory = blocks.DirectoryBlock.get_data(open_file, inode.direct[0])
        for item in directory.data:
            if item['name'] != '':
                print('  ', item['name'])

    @classmethod
    def fs_open(cls, filename):
        pass

    @classmethod
    def fs_display(cls, filename):
        pass

    @classmethod
    def fs_pwd(cls, ):
        print(filesystem.current_directory)

    @classmethod
    def fs_mkdir(cls, dirname):
        free_inode_loc = filesystem.inodebitmap.findFree()
        blocks.DirectoryBlock.add_directory(filesystem.current_directory, dirname, free_inode_loc)


    @classmethod
    def init_directory(cls, open_file): #TODO: Implement how the different directories (etc, bin) are supposed to be represented in the inodes they have been assigned. See blocks.DirectoryBlock.makeblock()
        superblock = blocks.Superblock(diskpy.Disk.disk_read(open_file, 0))
        inodeblock = blocks.InodeBlock(diskpy.Disk.disk_read(open_file, superblock.first_inodeblock))
        inodeblock.inodes[0].is_valid = blocks.Inode.USED
        inodeblock.inodes[0].direct[0] = 0
        inodeblock.save_block(open_file, superblock.first_inodeblock)

        directoryblock_raw = blocks.DirectoryBlock.make_block()
        diskpy.Disk.disk_write(open_file, superblock.first_datablock, directoryblock_raw)
        filesystem.current_directory = '/'