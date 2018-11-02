
import include.diskpy

class FileSystem:

    # TODO: add fs_bitmap

    def fs_format():
        print('Formatting disk.')

    def fs_debug():
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