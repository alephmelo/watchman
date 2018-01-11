from __future__ import print_function
from argparse import ArgumentParser
from colorama import Fore, init
import subprocess
import os


init(autoreset=True)  # colorama init

SCM_OPTIONS = ['git', 'hg']
TEXT_COLOR = Fore.GREEN


def _get_subdirectories(current_dir):
    dirs = [directory for directory in os.listdir(current_dir)
            if os.path.isdir(os.path.join(current_dir, directory)) and
            directory[0] != '.']
    return sorted(dirs)


def _get_command(scm, child_dir):
    if scm == 'hg':
        return ['hg', 'branch', '-R', './{}'.format(child_dir)]
    if scm == 'git':
        return ['git', '--git-dir', './{}/.git'.format(child_dir),
                'name-rev', '--name-only', 'HEAD']
    return None


def _clean_response(output):
    clean_output = output.decode()
    if '\n' in clean_output:
        clean_output = clean_output.replace('\n', '')
    if '\r' in clean_output:
        clean_output = clean_output.replace('\r', '')
    return clean_output


def check(scm):

    if scm in SCM_OPTIONS:
        current_working_directory = os.getcwd()
        child_dirs = _get_subdirectories(current_working_directory)
        for child in child_dirs:
            try:
                command = _get_command(scm, child)
                response = subprocess.check_output(command, stderr=subprocess.STDOUT)
                current_branch = _clean_response(response)
                output = '%-35s is on branch: %s%s' % (
                    child, TEXT_COLOR, current_branch)
                print(output)
            except:
                continue
    else:
        print("The scm you typed is not supported yet or you just misspelled\nCurrent options are: hg (mercurial) or git.\n")
        subprocess.call(['watchman', '--help'])


def main():
    parser = ArgumentParser()
    parser.add_argument(
        'check', help='checks branch status of all immediate subdirectories')
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
