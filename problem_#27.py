"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def solution(data):
	stack = []

	opening = '({['
	closing = ')}]'

	if len(data) < 2:
		return False
	else:
		for b in data:
			if b in opening:
				stack.append(b)
			else:
				if len(stack) != 0 and closing.index(b) == opening.index(stack[-1]):
					stack.pop()
				else:
					return False
	print(stack)
	return len(stack) == 0


data = '}([])[]({})'
print(solution(data))