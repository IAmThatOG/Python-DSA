class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = None

    def push(self, value):
        """Pushes an item to the top of the stack by appending to the head
        Time Complexity: O(1)

        Args:
            value (Any): The item to push to the stack
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self) -> Any:
        """Removes an item from the top of the stack
        Time Complexity: O(1)

        Returns:
            Node: The popped item
        """
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self) -> int:
        """Gets the size of the stack

        Returns:
            int: The size of the stack
        """
        return self.num_elements

    def is_empty(self) -> bool:
        """Checks if the stack is empty

        Returns:
            bool: True if stack is empty or False if otherwise
        """
        return self.num_elements <= 0
