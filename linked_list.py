class Node(object):
    _value = None
    _next = None

    def __init__(self, value)
        self._value = value
        self._next = next

    def next(self, next):
		self._next = next

    def value(self):
        return self._value

    def value(self, value):
        self._value = value

class LinkedList(object):
    _head = None
    _tail = None
    _size = 0

    def __init(self):
        pass

    def append(self, value):
        if self._head is None:
			self._head = node

		else:
			curr = self._head

			while curr:
				if curr._next is None:
					curr._next = node
					return

		self._length += 1

    def pop(self):
        if self.head is None:
            return None

        else:
            node = self.head
            self.head = self.head._next
            self.size -= 1
            return node

    def push(self, node):
        if self.head is None:
            self.head = node

        else:
            node._next = self.head
            self.head = node

        self.size += 1

    def display(self):
		curr = self._head

l = LinkedList()
n1 = Node('A')
l.append(n1)
print(l.head._value)

n2 = Node('B')
l.append(n2)
print(l.head._next._value)

n3 = Node('C')
l.push(n3)
print(l.head._value)
print(l.head._next._value)