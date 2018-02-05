class Node(object):
	_value = 0
	_next = None
	
	def __init__(self, value):
		self._value = value

class Queue(object):
	front = None
	size = 0
	
	def __init__(self):
		pass
	
	def nqueue(self, node):
		if self.front is None:
			self.front = node

		else:
			curr = self.front

			while curr._next is not None:
				curr = curr._next
			curr._next = node

		self.size += 1
	
	def dqueue(self):
		if self.front is None:
			return None
            
        node = self.front
		self.front = node.next

		self.size -= 1
		return node

    def __len__(self):
		return self.size