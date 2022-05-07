class BinaryTree:
    def __init__(self, value) -> None:
        """Creates a binary tree

        Args:
            value (any): the value of the root node
        """
        self.root = Node(value)

    def get_root(self):
        return self.root


class Node:
    def __init__(self, value) -> None:
        """Creates a new instance of a tree node

        Args:
            value (any): the value to be stored in the node
        """
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def set_left_child(self, value):
        self.left = Node(value)

    def get_right_child(self):
        return self.right

    def set_right_child(self, value):
        self.right = Node(value)

    def has_left_child(self):
        return self.get_left_child() is not None

    def has_right_child(self):
        return self.get_right_child() is not None
