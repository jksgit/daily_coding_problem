"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def solution(data):
	stack = []
	data = list(data)

	opening = '({[)}]'
	closing = ')}]({['

	if len(data) < 2:
		return false
	else:
		stack.append(data[0])
		for b in data[1:]:
			if opening.index(b) == closing.index(stack[-1]):
				stack.pop()
			else:
				stack.append(b)
	return not bool(stack)


data = '([])[]({})'
print(solution(data))