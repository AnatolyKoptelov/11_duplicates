# Anti-Duplicator

Application for finding duplicated files on your filesystem. Anti-Duplicator searches into subdirectories of your custom path.
Give a directory path  by positional argument and get list of duplicated files, whith same name and size.

# Quickstart

Example of script launch on Linux, Python 3.*:

```
python duplicates.py /tmp/for_duplicates_test
```
Output:
```
File name: 2.txt         File size: 265833
        /tmp/for_duplicates_test/2.txt
        /tmp/for_duplicates_test/4/2/2.txt
File name: 1.txt         File size: 266461
        /tmp/for_duplicates_test/1.txt
        /tmp/for_duplicates_test/2/1.txt

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
