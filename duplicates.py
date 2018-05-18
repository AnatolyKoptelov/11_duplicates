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


def analyze_directory_content(directory):
    directories = []
    files = {}
    for dir_entry in os.scandir(path=directory):
        if dir_entry.is_dir():
            directories.append(dir_entry.path)
        elif dir_entry.is_file():
            name_size_unique_key = '{}*{}'.format(
                dir_entry.name,
                os.path.getsize(dir_entry.path),
            )
            files[name_size_unique_key] = dir_entry.path
    return directories, files


def add_searched(searched_files, files):
    for name_size_unique_key in files.keys():
        if searched_files.get(name_size_unique_key, False):
            searched_files[name_size_unique_key].append(
                files[name_size_unique_key],
            )
        else:
            searched_files[name_size_unique_key] = [
                files[name_size_unique_key],
            ]
    return searched_files


def collect_filenames(path):
    directories_for_serching = [path, ]
    searched_files = {}
    while directories_for_serching:
        for directory in directories_for_serching:
            directories, files = analyze_directory_content(directory)
            directories_for_serching.extend(directories)
            searched_files = add_searched(searched_files, files)
            directories_for_serching.remove(directory)
    return searched_files


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
