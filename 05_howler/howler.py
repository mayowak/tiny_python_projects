#!/usr/bin/env python3
"""
Author : mayowak <mayowak@localhost>
Date   : 2020-11-18
Purpose: Howler Task
"""

import argparse
import os
import sys
import io


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler Task',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    howler = args.text
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(howler.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()