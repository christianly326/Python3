#!/usr/bin/env python3

def reverse(string):
	if len(string) == 1:
		return string[-1]
	else:
		return string[-1] + reverse(string[:-1])
s = "String"

print(reverse(s))