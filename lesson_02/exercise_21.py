#! /usr/bin/python

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

ch = math.sqrt (a * b)
zn = math.exp (a) * b
dod = a * math.exp(2 * a / b)

print(ch / zn + dod)
