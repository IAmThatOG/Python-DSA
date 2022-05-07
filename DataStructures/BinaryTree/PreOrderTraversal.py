from BinaryTree import BinaryTree, Node
from Stack import Stack
from StateTracker import StateTracker


def preorder_traversal_recursive(tree: BinaryTree):
    visited_order = []
    node = tree.get_root()
    return traverse(node, visited_order)


def traverse(node: Node, visited_order):
    if node:
        visited_order.append(node.get_value())
        traverse(node.get_left_child(), visited_order)
        traverse(node.get_right_child(), visited_order)
    return visited_order


def preorder_traversal_iterative(tree: BinaryTree):
    visited_order = []
    stack = Stack()
    node = tree.get_root()
    visited_order.append(node.value)
    stateTracker = StateTracker(node)
    stack.push(stateTracker)
    while node:
        if node.has_left_child() and not stateTracker.get_visited_left():
            stateTracker.set_visited_left()
            node = node.get_left_child()
            visited_order.append(node.get_value())
            stateTracker = StateTracker(node)
            stack.push(stateTracker)
            continue

        if node.has_right_child() and not stateTracker.get_visited_right():
            stateTracker.set_visited_right()
            node = node.get_right_child()
            visited_order.append(node.get_value())
            stateTracker = StateTracker(node)
            stack.push(stateTracker)
            continue

        stack.pop()
        if not stack.is_empty():
            stateTracker: StateTracker = stack.peek()
            node = stateTracker.get_node()
            continue
        node = None

    return visited_order


tree = BinaryTree("apple")
tree.get_root().set_left_child("banana")
tree.get_root().set_right_child("cherry")
tree.get_root().get_left_child().set_left_child("dates")
recursive_result = preorder_traversal_recursive(tree)
print(recursive_result)
iterative_result = preorder_traversal_iterative(tree)
print(iterative_result)
