from __future__ import print_function
from argparse import ArgumentParser
import sys
import os
from sh import cd, hg, watchman, ls


SCM_OPTIONS = ['git', 'hg']


def _get_subdirectories(current_dir):
    return [directory for directory in os.listdir(current_dir) 
            if os.path.isdir(os.path.join(current_dir, directory))
            and directory[0] != '.']


def check(scm):
    if scm in SCM_OPTIONS:
        current_working_directory = os.getcwd()
        child_dirs = _get_subdirectories(current_working_directory)
        for child in child_dirs:
            try:
                current_branch = hg.branch('-R', './%s' % child)
                output = '%-25s is on branch: %s' % (child, current_branch)
                print(output, end='')
            except Exception as e:
                continue
    else:
        print("The scm you typed is not supported yet or you just misspelled\nCurrent options are: hg (mercurial) or git.\n")
        print(watchman('--help'))


def main():
    parser = ArgumentParser()
    parser.add_argument('check', help='checks branch status of all immediate subdirectories')
    parser.add_argument('-s',
                        '--scm',
                        help='specify source code management application commands\
                              options: hg (mercurial) or git',
                        action='store')

    arguments = parser.parse_args()
    if arguments.check:
        check(arguments.scm)


if __name__ == '__main__':
    main()
