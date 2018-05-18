import os
import sys
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Find and print file duplicates'
    )
    parser.add_argument(
        'path',
        metavar='path',
        type=str,
        help='File path',
    )
    return parser.parse_args()


def collect_filenames(path):
    directories = [path, ]
    files = {}
    while directories:
        for directory in directories:
            for dir_entry in os.scandir(path=directory):
                if dir_entry.is_dir():
                    directories.append(dir_entry.path)
                elif dir_entry.is_file():
                    name_size_unique_key = '{}*{}'.format(
                        dir_entry.name,
                        os.path.getsize(dir_entry.path),
                    )
                    if files.get(name_size_unique_key, False):
                        files[name_size_unique_key].append(dir_entry.path)
                    else:
                        files[name_size_unique_key] = [dir_entry.path, ]
            directories.remove(directory)
    return files


if __name__ == '__main__':
    path = get_args().path
    if not os.path.isdir(path):
        sys.exit('Path must be a directory')
    files = collect_filenames(path)
    for name_size_unique_key, paths in files.items():
        if len(paths) > 1:
            print('File name: {} \t File size: {} \t'. format(
                *name_size_unique_key.split('*'),
            ))
            for path in paths:
                print('\t{}'.format(path))
