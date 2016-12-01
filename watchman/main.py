from __future__ import print_function
from argparse   import ArgumentParser
from colorama   import Fore, init
from sh         import cd, hg, git, watchman
import sys
import os


init(autoreset=True)  # colorama init

SCM_OPTIONS = ['git', 'hg']
TEXT_COLOR = Fore.GREEN


def _get_subdirectories(current_dir):
    return [directory for directory in os.listdir(current_dir) 
            if os.path.isdir(os.path.join(current_dir, directory))
            and directory[0] != '.']


def check(scm):
    if scm == 'hg':
        command = "hg.branch('-R', './%s' % (child))"

    elif scm == 'git':
        command = "git('--git-dir', './%s/.git' % (child), 'name-rev', '--name-only', 'HEAD')"

    if scm in SCM_OPTIONS:
        current_working_directory = os.getcwd()
        child_dirs = _get_subdirectories(current_working_directory)
        for child in child_dirs:
            try:
                current_branch = eval(command)
                output = '%-25s is on branch: %s%s' % (child, TEXT_COLOR, current_branch)
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
        if arguments.scm is not None:
            check(arguments.scm)
        else:
            arguments.scm = 'hg'
            check(arguments.scm)


if __name__ == '__main__':
    main()
