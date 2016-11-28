import sys
import os


def _get_subdirectories(current_dir):
    return [name for name in os.listdir(current_dir) 
            if os.path.isdir(os.path.join(current_dir, name))]


def check():
    current_working_directory = os.getcwd()
    child_dirs = _get_subdirectories(current_working_directory)
    for child in child_dirs:
        print("checking folder %s..." % child)


def main():
    arguments = sys.argv    
    if 'check' in arguments:
        check()
    else:
        print("type watchman help for, you know, help.")

if __name__ == '__main__':
    main()