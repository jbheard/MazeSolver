from copy import deepcopy
class Stack:
	class Node:
		def __init__(self, data, next):
			self.data = data
			self.next = next

	def __init__(self):
		self._front = None
		return

	def is_empty(self):
		return self._front is None
	
	def push(self, data):
		self._front = Stack.Node(data, self._front)
		return
	
	def pop(self):
		assert self._front is not None, "Stack is empty"
		data = self._front.data
		self._front = self._front.next
		return data
			
	def peek(self):
		assert self._front is not None, "Stack is empty"
		return deepcopy(self._front.data)


# Test Stack methods
if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	print(s.pop())      # 3
	print(s.peek())     # 2
	print(s.pop())      # 2
	print(s.is_empty()) # False
	print(s.pop())      # 1
	print(s.is_empty()) # True