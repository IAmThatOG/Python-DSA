from collections import deque


class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None
