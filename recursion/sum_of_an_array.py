#!/usr/bin/env python3

def sum(n=None):
	if n == None:
		return 0
	elif len(n) == 1:
		return n[-1]
	else:
		return n[-1] + sum(n[:-1])
n = [1, 2, 3, 4, 5, 6, 30, 200]
print(sum(n))
