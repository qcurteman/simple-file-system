
import click
import sfsystem as fs

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", help="The person to greet.")
def hello(count, name):
    for _ in range(count):
        click.echo("Hello, %s!" % name)


@click.command()
@click.option("--format_disk", is_flag=True, help="Format the current disk")
@click.option("--mount", is_flag=True, help="Mount the current disk")
@click.option("--debug", is_flag=True, help="Debug the current disk")
@click.option("--create", is_flag=True, help="Create a new disk")
def fileshell(format_disk, mount, debug, create):
    if format_disk:
        fs.FileSystem.fs_format()
    if mount:
        fs.FileSystem.fs_mount()
    if debug:
        fs.FileSystem.fs_debug()
    if create:
        fs.FileSystem.fs_create()


         
if __name__ == '__main__':
    fileshell()