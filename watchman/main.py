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
            change_dir = '%s/%s' % (current_working_directory, child)
            cd(change_dir)

            current_branch = hg('branch')

            output = '%-25s is on branch: %s' % (child, current_branch)
            print(output, end='')

            cd('..')
        except Exception:
            continue


def main():
    arguments = sys.argv    
    if 'check' == arguments[1]:
        check()
    else:
        print("type watchman help for, you know, help.")


if __name__ == '__main__':
    main()
