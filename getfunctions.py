#!/usr/bin/python

import sys, getopt, os, re

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"i:",["ifile="])
    except getopt.GetoptError:
        usage()
    if len(opts)<2:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        else:
            usage()
    # abs_in is the absolute path of input file
    abs_in = os.path.realpath(os.path.join(inputfile))
    print abs_in

def usage():
    print './getfunctions.py -i <inputfile> '
    sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])