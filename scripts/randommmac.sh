#!/usr/bin/env perl
for ($i=0;$i<6;$i++){@m[$i]=int(rand(256));} printf "%X:%X:%X:%X:%X:%X\n",@m;
