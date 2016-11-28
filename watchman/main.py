import sys
import os
from sh import cd, hg


def _get_subdirectories(current_dir):
    return [name for name in os.listdir(current_dir) 
            if os.path.isdir(os.path.join(current_dir, name))]


def check():
    current_working_directory = os.getcwd()
    child_dirs = _get_subdirectories(current_working_directory)
    for child in child_dirs:
        if child[0] != '.': 
            try:
                cd('%s/%s' % (current_working_directory, child))
                current_branch = hg('branch')
                print('%s is on branch: %s' % (child, current_branch), end='')
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
