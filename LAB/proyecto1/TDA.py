class Node:
    def __init__(self, data=None, next_element=None):
        self.data = data
        self.next_element = next_element


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        current = self.head
        while current.next_element:
            current = current.next_element
        current.next_element = Node(data=data)

    def delete(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next_element
        if previous is None:
            self.head = current.next_element
        elif current:
            previous.next_element = current.next_element
            current.next_element = None

    def __iter__(self):
        element = self.head
        while element:
            yield element.data
            element = element.next_element

    def size(self):
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next_element
        return i

    def get(self, name):
        node = self.head
        while node is not None:
            if str(node.data.name) == str(name):
                return node.data
            node = node.next_element
        return None
