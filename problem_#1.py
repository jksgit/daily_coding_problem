"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from itertools import combinations

def func(data, k):
	for item in combinations(data, 2):
		if sum(item) == k:
			return True
	else:
		return False


data = [10, 15, 3, 7]
k = 17


print(func(data, k))

# Note: this is not optimal solution.