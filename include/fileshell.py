from include.sfsystem import filesystem

class fileshell:

    continue_shell = True
    exit_shell = False

    commands = {'cat': '<inode> Cat command.',
                'copyin': '<file> <inode> Copy an entire file in.',
                'copyout': '<inode> <file> Copy an entire file out.',
                'create': 'Create a new file.',
                'debug': 'Debug the current disk.',
                'delete': '<inode> Delete a chosen disk.',
                'disks': 'List the disks available and the mounted one.',
                'exit': 'Exit the shell.',
                'format': 'Format the current disk.', 
                'help': 'List all available commands.',
                'mount': '<diskname> Mount a disk for writing and reading.',
                'quit': 'Quit running any current command.',
                'scan': 'Create bitmap based on currently mounted disk.'}

    @classmethod
    def open_disk(cls, diskname, numblocks):
        filesystem.fs_open_disk(diskname, numblocks)
        

    @classmethod
    def interpret_command(cls, command):
        command_string = command.split(' ', 1)
        command_root = command_string[0]
        try:
            arguments = command_string[1].split(' ')
        except:
            arguments = []
        

        if command_root not in fileshell.commands:
            Exception(print('ERROR: command {} is not recognized.'.format(command)))
            return fileshell.continue_shell
        
        if command_root == 'format':
            return_val = fileshell.shell_format()
        elif command_root == 'mount':
            if len(arguments) == 1:
                return_val = fileshell.shell_mount(arguments)
            else:
                print('ERROR: Received {} arguments but expected 1.'.format(len(arguments)))
                return_val = fileshell.continue_shell
        elif command_root == 'debug':
            return_val = fileshell.shell_debug()
        elif command_root == 'create':
            return_val = fileshell.shell_create()
        elif command_root == 'delete':
            if len(arguments) == 1:
                return_val = fileshell.shell_delete(arguments)
            else:
                print('ERROR: Received {} arguments but expected 1.'.format(len(arguments)))
                return_val = fileshell.continue_shell
        elif command_root == 'cat':
            if len(arguments) == 1:
                return_val = fileshell.shell_cat(arguments)
            else:
                print('ERROR: Received {} arguments but expected 1.'.format(len(arguments)))
                return_val = fileshell.continue_shell
        elif command_root == 'copyin':
            if len(arguments) == 2:
                return_val = fileshell.shell_copyin(arguments)
            else:
                print('ERROR: Received {} arguments but expected 2.'.format(len(arguments)))
                return_val = fileshell.continue_shell
        elif command_root == 'copyout':
            if len(arguments) == 2:
                return_val = fileshell.shell_copyout(arguments)
            else:
                print('ERROR: Received {} arguments but expected 2.'.format(len(arguments)))
                return_val = fileshell.continue_shell
        elif command_root == 'help':
            return_val = fileshell.shell_help()
        elif command_root == 'quit':
            return_val = fileshell.shell_quit()
        elif command_root == 'exit':
            return_val = fileshell.shell_exit()
        elif command_root == 'disks':
            return_val = fileshell.shell_disks()
        elif command_root == 'scan':
            return_val = fileshell.shell_scan()
        
        return return_val

    @classmethod
    def shell_format(cls,):
        ans = input('Are you sure you want to format {}? (y/n) '.format(filesystem.mounted_disk))
        if ans == 'Y' or ans == 'y':
            print('formatting...')
            filesystem.fs_format()
        elif ans == 'N' or ans == 'n':
            print('canceling format.')
        else:
            print('canceling format, unrecognized response.')
        
        return fileshell.continue_shell

    @classmethod
    def shell_mount(cls, *args):
        diskname = list(args)[0][0]
        if diskname not in filesystem.disks:
            print('ERROR: Disk {} does not exist'.format(diskname))
        else:
            filesystem.fs_mount(diskname)
        return fileshell.continue_shell

    @classmethod
    def shell_debug(cls,):
        print('debugging...') # Implemented with the filesystem
        return fileshell.continue_shell

    @classmethod
    def shell_create(cls,):
        print('creating...') # Implemented with the filesystem
        return fileshell.continue_shell

    @classmethod
    def shell_delete(cls, *args):
        print('deleting...') # Implemented with the filesystem
        for arg in args:
            print('argument: ', arg)
        return fileshell.continue_shell

    @classmethod
    def shell_cat(cls, *args):
        print('run cat command') # Implemented with the filesystem
        for arg in args:
            print('argument: ', arg)
        return fileshell.continue_shell

    @classmethod
    def shell_copyin(cls, *args):
        print('run copyin command') # Implemented with the filesystem
        for arg in args:
            print('argument: ', arg)
        return fileshell.continue_shell

    @classmethod
    def shell_copyout(cls, *args):
        print('run copyout command') # Implemented with the filesystem
        for arg in args:
            print('argument: ', arg)
        return fileshell.continue_shell

    @classmethod
    def shell_help(cls,):
        for command in fileshell.commands:
            print(command.ljust(8), ':', fileshell.commands[command])
        return fileshell.continue_shell

    @classmethod
    def shell_quit(cls,):
        print('run quit command') # Implemented with the filesystem
        return fileshell.continue_shell

    @classmethod
    def shell_exit(cls,):
        print('exiting shell...')
        return fileshell.exit_shell

    @classmethod
    def shell_disks(cls,):
        for disk in filesystem.disks:
            if disk == filesystem.mounted_disk:
                print('  * {}'.format(disk))
            else:
                print('    {}'.format(disk))
        
    @classmethod
    def shell_scan(cls, ):
        print('scanning disk...')
        filesystem.fs_scan()
