#!/usr/bin/python

import os


def runcmd(cmd):
    print(cmd)
    os.system(cmd)


# Get the list of all files and directories
# in the root directory
path = "./"
dir_list = os.listdir(path)

dir_list.sort()

flist = ""

for fl in dir_list:
    if "pdf" in fl:
        flist += '"' + fl + '" '

cmd = "pdfjoin-norot " + flist + " -o output/joined1.pdf"
runcmd(cmd)

cmd = "pdfjam --nup 1x2 output/joined1.pdf --a4paper --outfile output/joined2.pdf"
runcmd(cmd)

cmd = "pdfjam --nup 2x1 output/joined2.pdf --landscape --a4paper --outfile output/joined3.pdf"
runcmd(cmd)

cmd = "pdfjam --twoside --landscape --offset '1.4cm 0cm' --scale 0.9 output/joined3.pdf --outfile output/joined4.pdf"
runcmd(cmd)
