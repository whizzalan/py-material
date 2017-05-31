#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__= 'George Chao'
__version__= '0.1'

'''
usuage: python <name>.py -i <inputFile> -o <outputFile> -l <logfile> -d <txdate>
'''


import os,sys
import getopt
import logging


def usage():
    print 'Usage: python %s [-i|-o|-l|-d] [--help]' % sys.argv[0]
    print 'python %s -i <inputFile> -o <outputFile> -l <logfile> -d <date>' % sys.argv[0]

def main(argv):

    # 宣告
    inputfile = ''
    outputfile = ''
    logfile = 'log.txt'
    txdate = ''

    if len(sys.argv) <2:
        usage()
        print sys.argv[0], "please keyin argument"
        sys.exit(1)

    try:
        opts, args = getopt.getopt(argv[1:],"i:o:l:d:h",["iflie=","ofile="])
    except getopt.GetoptError:
        print "getopt error!"
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            usage()
            sys.exit(1)
        elif opt in ("-i", "--file"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--date"):
            txdate = arg
        elif opt in ("-l", "--log"):
            logfile = arg
        else:
            print "%s ==&gt; %s" %(opt,arg)

    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename = logfile)
            #handlers = [logging.FileHandler(logfile, 'w', 'utf-8'),])

    
    ## Define Handler, Output sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    ## Define Output Format
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)12s - %(levelname)8s - %(message)s')
    console.setFormatter(formatter)

    ## Setup Logger
    logging.getLogger('Logger Start"').addHandler(console)
    #logger.setLevel(logging.DEBUG)

    logging.debug('debug level')
    logging.info('info level')
    logging.warning('wran level')
    logging.error('error level')

    logger1 = logging.getLogger("myapp.first")
    logger2 = logging.getLogger("myapp.second")

    logger1.debug("低八葛")
    logger1.info("因佛")
    logger2.warning("亡靈")
    logger2.error("A羅")

    print "輸入的文件:", inputfile
    print "輸出的文件:", outputfile
    print "寫出的logfile:", logfile
    print "Transaction 時間:", txdate





        

if __name__ == '__main__':

    main(sys.argv)

