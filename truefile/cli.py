import click
import os
import imghdr
import sys

__file__

@click.group()
def cli():
    pass

def what(*args, **kwargs):
    try:
        return imghdr.what(*args, **kwargs)
    except PermissionError:
        return None

@cli.command()
def detect():
    path = os.getcwd()
    # Filter and map files down to absolute paths for FILES (not directories)
    files = map(lambda file : file, [file for file in os.listdir(path)]) # abspath of all files in curdir
    files = filter(os.path.isfile, files) # file not directory
    files = zip(files, map(what, files)) # get scan of file type
    files = filter(lambda x : x[1] is not None, files) # filter for only images
    files = map(lambda x : (x[0], os.path.splitext(x[0])[1], x[1]), files)
    largest = max(map(lambda x : len(x[0]), files))
    print(largest)
    print('\n'.join(map(lambda x : f'| {x[0]} -> {x[1]}', files)))

@cli.command()
def rename():
    pass