import click
import os
import imghdr
import sys

@click.group()
def cli():
    pass

def what(*args, **kwargs):
    try:
        return imghdr.what(*args, **kwargs)
    except PermissionError:
        return None

@cli.command()
@click.option('-s', '--showall', is_flag=True, help='Show all files regardless of detected extension mishaps', default=False)
def detect(showall):
    path = os.getcwd()
    # Filter and map files down to absolute paths for FILES (not directories)
    files = map(lambda file : file, [file for file in os.listdir(path)]) # abspath of all files in curdir
    files = filter(os.path.isfile, files) # file not directory
    files = zip(files, map(what, files)) # get scan of file type
    files = filter(lambda x : x[1] is not None, files) # filter for only images
    files = list(map(lambda x : (x[0], os.path.splitext(x[0])[1], x[1]), files)) # find just the file extension and put into tuple
    if not showall:
        files = list(filter(lambda x : x[1].replace('jpg', 'jpeg') != x[2], files)) # filter for differing extensions
    largest = max(map(lambda x : len(x[0]), files)) # get length of the longest file name
    print('\n'.join(map(lambda x : f'{x[0].ljust(largest)} | {x[1]} -> {x[2]}', files))) # print with proper spacing


@cli.command()
def rename():
    pass