"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def func(data):
	min_positive = 1
	min_num = min([i for i in data if i>0], default=1)
	
	if min_num == min_positive:
		for n in range(min_num, max(data)+1):
			if n not in data:
				return n
		else:
			return max(data)+1
	else:
		for n in range(1, max(data)+1):
			if n not in data:
				return n
		else:
			return max(data)+1


print(func([3, 4, -1, 1]))
print(func([1, 2, 0]))
print(func([1, 1, 1, 2, 0]))
print(func([-1, -2, 0, -5, -2]))

# Note: This is not optimal solution.