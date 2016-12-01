#! /usr/bin/python

import sys
import math

x = float(sys.argv[1])
m = float(sys.argv[2])
s = float(sys.argv[3])

print 1 / (s * math.sqrt(2 * math.pi)) * math.exp(-((x - m)**2 / (2 * s*s)))
