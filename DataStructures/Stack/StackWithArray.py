class Stack:
    def __init__(self, initial_size) -> None:
        self.arr = [0 for x in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        """Adds an item to the stack
        Time Complexity: O(n) - when the array limit is reached and needs increase

                Args:
                    value (Any): The value to add to the stack
        """
        if len(self.arr) == self.next_index:
            print("index out of range! incresing capacity...")
            self.increase_capacity()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def increase_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return True if self.num_elements <= 0 else False

    def pop(self):
        """Fetches an item from the stack
        Time Complexity: O(1)

        Returns:
            Any: he item fetched
        """
        if self.is_empty():
            self.next_index = 0
            self.num_elements = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]


stack = Stack(2)
print(stack.arr)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.arr)
stack.pop()
print(stack.arr)
