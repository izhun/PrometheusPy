#! /usr/bin/python

import sys

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
temp_string = ''
temp_str = [0, 0, 0, 0, 0, 0]
counter = 0

for i in range(min_n, max_n+1) :
    temp_string = str(i)
    while len(temp_string) < 6:
        temp_string = '0' + temp_string    
    for num in range(6):
        temp_str[num] = temp_string[num]
    sum_1 = int(temp_str[0]) + int(temp_str[1]) + int(temp_str[2])
    sum_2 = int(temp_str[3]) + int(temp_str[4]) + int(temp_str[5])
    if sum_1 == sum_2 :
        counter = counter + 1        
print counter
