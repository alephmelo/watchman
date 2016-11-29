from __future__ import print_function
import sys
import os
from sh import cd, hg


def _get_subdirectories(current_dir):
    return [directory for directory in os.listdir(current_dir) 
            if os.path.isdir(os.path.join(current_dir, directory))
            and directory[0] != '.']


def check():
    current_working_directory = os.getcwd()
    child_dirs = _get_subdirectories(current_working_directory)
    for child in child_dirs:
        try:
            current_branch = hg('branch', '-R', './%s' % child)
            output = '%-25s is on branch: %s' % (child, current_branch)
            print(output, end='')

        except Exception as e:
            continue


def main():
    arguments = sys.argv    
    if 'check' == arguments[1]:
        check()
    else:
        print("type watchman help for, you know, help.")


if __name__ == '__main__':
    main()
