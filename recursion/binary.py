#!/usr/bin/env python3

def binary(array, target, low, high):
	if high >= low:
		mid = (low+high) // 2
		
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			return binary(array, target, mid + 1, high)
		else:
			return binary(array, target, low, mid-1)
	else:
		return -1

arr = [i for i in range(0, 50) if i % 2 == 0]
x = 48
print(binary(arr, x, 0, len(arr) -1))