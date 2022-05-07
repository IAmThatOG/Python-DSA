class StateTracker:
    def __init__(self, node) -> None:
        self.node = node
        self.has_visited_left = False
        self.has_visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.has_visited_left

    def set_visited_left(self):
        self.has_visited_left = True

    def get_visited_right(self):
        return self.has_visited_right

    def set_visited_right(self):
        self.has_visited_right = True
