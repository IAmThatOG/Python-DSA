class Stack:
    def __init__(self) -> None:
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list) <= 0:
            return None
        return self.list.pop()

    def peek(self):
        """Returns the top of the stack

        Returns:
            [any]: [the value at the top of the stack]
        """
        if len(self.list) <= 0:
            return None
        return self.list[-1]

    def is_empty(self):
        return len(self.list) <= 0
