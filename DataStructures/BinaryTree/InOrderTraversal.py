from StateTracker import StateTracker
from Stack import Stack
from BinaryTree import BinaryTree


def inorder_traversal_recursive(tree):
    visited_order = []
    node = tree.get_root()
    return traverse(node, visited_order)


def traverse(node, visited_order):
    if node:
        traverse(node.get_left_child(), visited_order)
        visited_order.append(node.get_value())
        traverse(node.get_right_child(), visited_order)
    return visited_order


def inorder_traversal_iterative(tree):
    visited_order = []
    stack = Stack()
    node = tree.get_root()
    state = StateTracker(node)
    stack.push(state)
    while node:
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            state = StateTracker(node)
            stack.push(state)
            continue

        if node.has_right_child() and not state.get_visited_right():
            visited_order.append(node.get_value())
            state.set_visited_right()
            node = node.get_right_child()
            state = StateTracker(node)
            stack.push(state)
            continue

        stack.pop()
        if not stack.is_empty():
            visited_order.append(node.get_value())
            state = stack.peek()
            node = state.get_node()
            continue
        node = None
    return visited_order


tree = BinaryTree("apple")
tree.get_root().set_left_child("banana")
tree.get_root().set_right_child("cherry")
tree.get_root().get_left_child().set_left_child("dates")
recursive_result = inorder_traversal_recursive(tree)
print(recursive_result)
iterative_result = inorder_traversal_iterative(tree)
print(iterative_result)
