#!/usr/bin/python

import random, getopt, sys, os
from stat import *
from math import floor

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:")
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)
    file = ""
    fname = ""
    for o, a in opts:
        if o == "-f":
            file = a
    if len(file) and os.path.isfile(file):
        fname = os.path.split(file)[1]
    else:
        if len(file):
            print file, "does not exist"
        else:
            print "A filename must be provided"
        sys.exit(2)
    stats = os.stat(file)
    fsize = stats[ST_SIZE] / 512
    fcyl = floor(fsize  / 16065)
    newCID = random.randint(0, 4294967295)
    # Specify the file
    output = """# Disk DescriptorFile
version=1
CID=%(nCID)08x
parentCID=ffffffff
createType="monolithicFlat"

# Extent description
RW %(size)d FLAT "%(file)s" 0

# The Disk Data Base
#DDB

ddb.toolsVersion = "0"
ddb.virtualHWVersion = "6"
ddb.geometry.cylinders = "%(cyl)d"
ddb.geometry.heads = "255"
ddb.geometry.sectors = "63"
ddb.adapterType = "lsilogic"
ddb.encoding = "windows-1252"
""" % {"nCID": newCID, "file": fname, "size": fsize, "cyl": fcyl}
    print output

if __name__ == "__main__":
    main()
