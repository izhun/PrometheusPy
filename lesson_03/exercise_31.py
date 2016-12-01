#! /usr/bin/python

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if c < a + b and a < b + c and b < a + c : print "triangle"
else : print "not triangle"
