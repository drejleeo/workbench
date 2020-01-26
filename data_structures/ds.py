class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'{self.value}'


class LinkedList(object):
    """
    Simple linked list.
    """
    def __init__(self, iterable=None):
        self.head = None
        try:
            self.head = Node(value=iterable[0])
            current_node = self.head
            for el in iterable[1:]:
                current_node.next = Node(el)
                current_node = current_node.next
        except TypeError:
            pass

    def free(self):
        self.head = None

    def append(self, value):
        try:
            current = self.head
            while isinstance(current.next, Node):
                current = current.next
            current.next = Node(value)
        except AttributeError:
            self.head = Node(value)

    def index(self, i):
        for nr, node in enumerate(self.generate_elements()):
            if nr == i:
                return node

    def search(self, target):
        for node in self.generate_elements():
            if node.value == target:
                return node

    def delete(self, index):
        for i, node in enumerate(self.nodes_gen()):
            if i + 1 == index:
                node.next = node.next.next
        self.length -= 1

    def generate_elements(self):
        current = self.head
        while isinstance(current, Node):
            yield current
            current = current.next

    def insert_at_index(self, value, index):
        for nr, node in enumerate(self.nodes_gen()):
            if nr == index:
                new = Node(value, node)
                node.next = new

    def __repr__(self):
        gen = self.generate_elements()
        return f"[{', '.join(el.__str__() for el in gen)}]"


class DoubleLinkedList(object):
    def __init__(self, start, end):
        pass


class Stack(object):
    def __init__(self, iterable=None):
        try:
            self.list = [el for el in iterable]
        except TypeError:
            self.list = []

    def push(self, element):
        self.list.append(element)

    def pop(self):
        return self.list.pop()


class Queue(object):
    def __init__(self, iterable=None):
        try:
            self.list = [el for el in iterable]
        except TypeError:
            self.list = []

    def enqueue(self, element):
        self.list.append(element)

    def dequeue(self):
        self.list.pop(0)
