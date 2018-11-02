import include.sfsystem as fs
import include.diskpy as diskpy
from os import listdir, getcwd

class fileshell:

    continue_shell = True
    exit_shell = False
    disks = []
    working_disk = None

    commands = {'format': 'Format the current disk.', 
                'mount': 'Mount a disk to being writing and reading.',
                'debug': 'Debug the current disk.',
                'create': 'Create a new file.',
                'delete': '<inode> Delete a chosen disk.',
                'cat': '<inode> Cat command.', 
                'copyin': '<file> <inode> Copy an entire file in.',
                'copyout': '<inode> <file> Copy an entire file out.',
                'help': 'List all available commands.', 
                'quit': 'Quit running any current command.',
                'exit': 'Exit the shell.'}

    @classmethod
    def open_disks(cls, diskname, blocknum):
        fileshell.disks = listdir('{}/data'.format(getcwd()))
        if diskname not in fileshell.disks:
            diskpy.Disk(diskname, blocknum)
            fileshell.disks.append(diskname)
        fileshell.working_disk = diskname

    @classmethod
    def interpret_command(cls, command):
        command_string = command.split(' ', 1)
        command_root = command_string[0]
        # if len(command_string) >= 2:
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
            return_val = fileshell.shell_mount()
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
        
        return return_val

    @classmethod
    def shell_format(cls,):
        print('formatting...') # Implemented with the filesystem
        return fileshell.continue_shell

    @classmethod
    def shell_mount(cls,):
        print('mounting...') # Implemented with the filesystem
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

        
    