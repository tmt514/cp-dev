#!/usr/bin/env python3
import argparse
import os
from os import path

parser = argparse.ArgumentParser(description='Create New Problem.')
parser.add_argument('--format',
        nargs='?',
        default='cms',
        help='The format of this task (default: cms).')

parser.add_argument('name',
        nargs=1,
        help='Task folder shortname.')

args = parser.parse_args()


if __name__ == '__main__':
    folder_name = args.name[0]
    # Creates directories structure for CMS format.
    os.mkdir(folder_name)
    os.mkdir(path.join(folder_name, 'input'))
    os.mkdir(path.join(folder_name, 'output'))
    os.mkdir(path.join(folder_name, 'src'))
    os.mkdir(path.join(folder_name, 'sol'))
    os.system('wget -P {} https://raw.githubusercontent.com/MikeMirzayanov/testlib/master/testlib.h'.format(path.join(folder_name, 'src')))

    # Creates a test generator using testlib.
    with open(path.join(folder_name, 'src', 'gen.cpp'), 'w') as f:
        f.write('''\
#include "testlib.h"
#include <iostream>
using namespace std;

/* Generates one test file to STDOUT. */
int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);
    int subtask = atoi(argv[2]); // Subtask number.
    string tag = atoi(argv[3]); // The particular type of a test case.

}''')

    # Creates a validator uisng testlib.
    with open(path.join(folder_name, 'src', 'validator.cpp'), 'w') as f:
        f.write('''\
#include "testlib.h"

/* Reads a test file from STDIN. (using object inf to read.) */
int main(int argc, char *argv[]) {
    registerValidation(argc, argv);
    inf.readInt(1, 100);
    inf.readEoln();
    inf.readEof();
}''')

    # Creates solution file (default in CPP)
    os.system('touch {}'.format(path.join(folder_name, 'sol', 'sol.cpp')))
