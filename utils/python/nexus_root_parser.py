#!/usr/bin/env python

__author__  = 'Barry Baker'
__email__   = 'barry.baker@noaa.gov'
__license__ = 'GPL'

'''
Simple utility to modify the NEXUS_Config.rc ROOT emission path.
'''

import os
from glob import glob
import sys
import subprocess
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter



if __name__ == '__main__':

    parser = ArgumentParser(description='Modify the start and end date of the NEXUS config script', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--files', help='input nemsio file name', type=str, required=True)
    parser.add_argument('-d', '--root_directory', help='Root Directory', default='./', required=True)
    args = parser.parse_args()

    finput = args.files
    d = args.root_directory

    with open(finput,'r') as f:
        lines = f.readlines()
        for index,line in enumerate(lines):
            if not line.startswith('#'):
                if 'ROOT                        :' in line:
                    line = line.split(':')[0] + ': ' + d + '\n'
                    lines[index] = line
                    break
                elif 'ROOT        ' in line:
                    line = line.split(':')[0] + ': ' + d + '\n'
                    lines[index] = line
                    break
        f.close()
    
    with open(finput, 'w') as writer:
        writer.writelines(lines)
