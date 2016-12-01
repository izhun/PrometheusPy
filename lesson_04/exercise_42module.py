#! /usr/bin/python

import sys

st = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_str = ''
result = ''
for i in range(len(st)):
	if st[i] == ' ':
		continue
	t_char_1 = st[i].lower()
	if st[i] == t_char_1:
		new_str = new_str + 'a'
	t_char_2 = st[i].upper()
	if st[i] == t_char_2:
		new_str = new_str + 'b'
for i in range(0, (len(new_str)-len(new_str)%5), 5):
	n = key.find(new_str[i:i+5])
	result = result + alphabet[n]
print result
