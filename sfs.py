from include.fileshell import fileshell as fs
import click

@click.command()
@click.option('--diskname', help='Name of disk you want to create or open.')
@click.option('--blocknum', help='Number of blocks on the disk.')
def run_file_shell(diskname, blocknum):
    interpreted_command = True
    fs.open_disks(diskname, blocknum)

    while interpreted_command != False:
        command = input('sfs>')
        interpreted_command = fs.interpret_command(command)

if __name__ == '__main__':
    run_file_shell()