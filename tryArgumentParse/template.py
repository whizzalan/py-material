#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__= 'George Chao'
__version__= '0.1'

'''
usuage: python test.py -i <inputFile> -o <outputFile> -l <logfile> -d <txdate>
'''


import os,sys
import getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    logfile = ''
    txdate = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["iflie=","ofile="])
    except getopt.GetoptError:
        print 'python test.py -i <inputFile> -o <outputFile> -l <logfile> -d <date>'
        sys.exit(2)
    if len(sys.argv) <2:
        print "Usage:", sys.argv[0], "please keyin argument"
        sys.exit(1)

    print "Your first argument is ", sys.argv[1]
    print "====="
    for x in sys.argv:
        print x
    for opt, arg in opts:
        if opt == '-h':
            print 'python test.py -i <inputFile> -o <outputFile> -l <logfile> -d <date>'
            sys.exit(1)
        elif opt in ("-i", "--file"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--date"):
            txdate = arg
        elif opt in ("-l", "--log"):
            logfile = arg
    print "輸入的文件:", inputfile
    print "輸出的文件:", outputfile
    print "寫出的logfile:", logfile
    print "Transaction 時間:", txdate

        

if __name__ == '__main__':
    main(sys.argv)
