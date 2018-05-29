import os
import sys
import argparse
import collections


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
    searched_files = collections.defaultdict(list)
    for base_path, directories, files in os.walk(path):
        for file in files:
            full_pass = '{}/{}'.format(base_path, file)
            searched_files[(
                file,
                os.path.getsize(full_pass)
            )].append(full_pass)
    return searched_files


if __name__ == '__main__':
    path = get_args().path
    if not os.path.isdir(path):
        sys.exit('Path must be a directory')
    files = collect_filenames(path)
    for name_size_unique_key, paths in files.items():
        if len(paths) > 1:
            print('File name: {} \t File size: {} \t'. format(
                *name_size_unique_key,
            ))
            for path in paths:
                print('\t{}'.format(path))
