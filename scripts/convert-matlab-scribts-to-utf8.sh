#!/bin/bash

# This script converts Matlab scripts from ISO-8859-1 to utf-8 (a modern standard)
# requirements: bash, iconv
#
# @author Mebus, https://mebus.github.io
#

for f in $(find . -iname "*.m" -exec file -i {} \; | grep "iso-8859-1" | grep -Eo '^.*\.m')
do
    echo $f
    iconv -f iso8859-1 -t utf-8 $f > $f.utf8
    mv $f.utf8 $f
done
