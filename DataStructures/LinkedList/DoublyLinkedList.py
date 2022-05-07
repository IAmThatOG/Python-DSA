class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):

        # TODO: Implement this method to append to the tail of the list
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
