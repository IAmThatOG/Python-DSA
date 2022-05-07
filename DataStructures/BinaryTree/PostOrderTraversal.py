from BinaryTree import BinaryTree
from Stack import Stack
from StateTracker import StateTracker


def postorder_traversal_recursive(tree):
    node = tree.get_root()
    visit_order = []
    return traverse(node, visit_order)


def traverse(node, visit_order):
    if node:
        traverse(node.get_left_child(), visit_order)
        traverse(node.get_right_child(), visit_order)
        visit_order.append(node.get_value())
    return visit_order


def postorder_traversal_iterative(tree):
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
            state.set_visited_right()
            node = node.get_right_child()
            state = StateTracker(node)
            stack.push(state)
            continue

        stack.pop()
        visited_order.append(node.get_value())
        if not stack.is_empty():
            state = stack.peek()
            node = state.get_node()
            continue

        return visited_order


tree = BinaryTree("apple")
tree.get_root().set_left_child("banana")
tree.get_root().set_right_child("cherry")
tree.get_root().get_left_child().set_left_child("dates")
recursive_result = postorder_traversal_recursive(tree)
print(recursive_result)
iterative_result = postorder_traversal_iterative(tree)
print(iterative_result)
