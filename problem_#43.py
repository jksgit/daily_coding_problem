"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

class Stack(object):
	def __init__(self):
		self._data = []

	def pop(self):
		if self._data:
			return self._data.pop()
		else:
			return None

	def push(self, item):
		self._data.append(item)

	def max_item(self):
		return max(self._data, default=None)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.max_item())
print(stack.pop())
print(stack.pop())
print(stack.pop())

# Check if it returns None if called on empty stack.
print(stack.pop())
# Check if it return max item as None in case called on empty stack.
print(stack.max_item())