#!/usr/bin/env python
"""
Author: Cameron Everhart <cameron.r.everhart@gmail.com>
Purpose: Say hello
"""

import argparse

def get_args():
    """ Get the command line arguments """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    args = parser.parse_args()

def main():
    """ Just the main function """
    args = get_args()
    print('Hello, ' + args.name + '!')

if __name__ == "main":
    main()