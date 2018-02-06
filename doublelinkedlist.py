class Node(object):
    _value = None
    _next = None
    _prev = None
    
    def __init__(self, value):
        self._value = value


class DoubleLinkedList(object):
    head = None
    tail = None
    curr = None
    size = 0

    def __init(self):
        pass

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            self.tail._next = node
            self.tail = node
            
        self.size += 1

    def push(self, node):
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.head._prev = node
            node._next = self.head
            self.head = node

        self.size += 1

    def pop(self):
        if self.head is None:
            return None

        else:
            node = self.head
            self.head = self.head._next
            self.size -= 1
            return node

    def remove(self, value):
        prev = None
        curr = self.head

        while curr is not None:
            if curr._value == value:
                if prev is not None:
                    prev._next = curr._next
                    if curr._next is not None:
                        curr._next._prev = prev
                        
                if self.head == curr:
                    self.head = curr._next
                if self.tail == curr:
                    self.tail = curr._prev
                self.size += 1
                break
            else:
                prev = curr
                curr = curr._next