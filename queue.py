from copy import deepcopy
class Queue:
	class Node:
		def __init__(self, data, next):
			self.data = data
			self.next = next

	def __init__(self):
		self._front = None
		self._back = None
		return

	def is_empty(self):
		return self._front is None
	
	def insert(self, data):
		if self._front is None:
			self._front = self._back = Queue.Node(data, None)
		else:
			self._front.next = Queue.Node(data, None)
			self._front = self._front.next
		return
	
	def remove(self):
		assert self._back is not None, "Stack is empty"
		data = self._back.data
		self._back = self._back.next
		if self._back is None: 
			self._front = None
		return data
			
	def peek(self):
		assert self._back is not None, "Stack is empty"
		return deepcopy(self._back.data)


# Test Queue methods
if __name__ == '__main__':
	q = Queue()
	q.insert(1)
	q.insert(2)
	q.insert(3)
	print(q.remove())   # 1
	print(q.peek())     # 2
	print(q.remove())   # 2
	print(q.is_empty()) # False
	print(q.remove())   # 3
	print(q.is_empty()) # True
