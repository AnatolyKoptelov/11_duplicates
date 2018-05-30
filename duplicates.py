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


def collect_files_locations(path):
    files_locations = collections.defaultdict(list)
    for base_path, directories, file_names in os.walk(path):
        for file_name in file_names:
            full_path = os.path.join(base_path, file_name)
            files_locations[(
                file_name,
                os.path.getsize(full_path)
            )].append(full_path)
    return files_locations


if __name__ == '__main__':
    path = get_args().path
    if not os.path.isdir(path):
        sys.exit('Path must be a directory')
    files_locations = collect_files_locations(path)
    for (file_name, file_size), paths in files_locations.items():
        if len(paths) > 1:
            print('File name: {} \t File size: {} \t'. format(
                file_name,
                file_size,
            ))
            for path in paths:
                print('\t{}'.format(path))
