class Node(object):
	_value = 0
	_next = None
	
	def __init__(self, value):
		self._value = value

class Stack(object):
    top = None
    size = 0

    def __init__(self):
        pass

    def push(self, node):
        node._next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = node._next
        return node