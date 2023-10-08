#!/usr/bin/env python3

def power(n, x):
	if n == 0:
		return 1
	else:
		return x * power(n-1, x)
print(power(4, 2))