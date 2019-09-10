class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, start):
        self.start = start
        self.end = start

    def add_to_end(self, value):
        self.end.next = Node(value=value)
        self.end = self.end.next

    def add_at_beginning(self, value):
        refresh_start = Node(value=value, next=self.start)
        self.start = refresh_start

    def insert_after(self, node, new_value):
        new_node = Node(value=new_value)
        new_node.next = node.next
        node.next = new_node


class Stack(object):
    def __init__(self, iterable=None):
        self.list = []
        try:
            self.list = [element for element in iterable]
        except TypeError:
            pass

    def push(self, element):
        self.list.append(element)

    def pop(self):
        return self.list.pop()
