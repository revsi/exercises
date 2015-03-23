#!/usr/bin/python

import sys, getopt, os, re

not_required = ['if', 'else', 'while', 'for', '+', 'switch']

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"i:",["ifile="])
    except getopt.GetoptError:
        usage()
    #if len(opts)<2:
        #usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        else:
            usage()
    # abs_in is the absolute path of input file
    abs_in = os.path.realpath(os.path.join(inputfile))
    #print abs_in
    parser(abs_in)

def parser(inp):
    openfile = open(inp,'r')
    methods=[] 
    for line in openfile:
        if '(' in line and '//' not in line:
            tokens=line.split('(')
            token=tokens[0].split()
            if(len(token)>0):
                if(('=' not in token[-1]) and ('/' not in token[-1] and '}' not in token[-1])):
                    methods.append(token[-1])
    methods=list(set(methods)-set(not_required)) #O(N)
    for x in methods:
        print x

def usage():
    print './getfunctions.py -i <inputfile> '
    sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])