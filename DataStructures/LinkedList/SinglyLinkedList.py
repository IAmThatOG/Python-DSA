class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None


class SinglyLinkedList:
    def __init__(self, init_list=None):
        """Creates an instance of a singly linked list"""
        self.head: Node = None
        self.tail: Node = None  # when tail is tracked
        if init_list:
            for v in init_list:
                self.append(v)

    def append(self, value):
        """Append to the list without tracking tail
        Time Complexity: O(n)

        Args:
            value (Any): the data to add to the LinkedList
        """
        if self.head is None:
            self.head = Node(value)
            return
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def appendWithTail(self, value):
        """Append to the list with tail being tracked
        Time Complexity: O(1)

        Args:
            value (Any): the data to add to the LinkedList
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        return

    def prepend(self, value):
        """Adds a new node to the start of the linked list as the head
        Time Complexity: O(1)

        Args:
            value (Any): the data to add to the list
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head  # if tail is being tracked
            return
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        return

    def search(self, value):
        """Searches for a node with the required value
        Time Complexity: O(n)

        Args:
            value (Any): the data to search for

        Returns:
            Node: The node that holds the value
        """
        currentNode: Node = self.head
        while currentNode:
            if currentNode.value == value:
                return currentNode
            currentNode = currentNode.next
        return None

    def remove(self, value):
        """Remove first occurrence of value.
        Time Complexity: O(n)

        Args:
            value (Any): The value to be removed
        """
        if self.head.value == value:
            self.head = self.head.next
            return
        previousNode = self.head
        currentNode = self.head.next
        while currentNode is not None:
            if currentNode.value == value:
                previousNode.next = currentNode.next
                return
            previousNode = currentNode
            currentNode = currentNode.next
        return

    def pop(self):
        """Return the first node's value and remove it from the list.
        Time Complexity: O(n)

        Args:
            value (Any): The value to be popped from the list

        Returns:
            Any: The value popped from the list
        """
        if self.head:
            value = self.head.value
            self.head = self.head.next if self.head.next else None
            return value
        return None

    def insert(self, value, pos: int):
        """Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list.
        Time Complexity O(n)

            Args:
                value (Any): The value to be inserted
                pos (int): The index at which the value will be inserted in the linked list starting from zero (0)
        """
        newNode = Node(value)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return
        # currentNode = self.head.next
        currentNode = self.head
        previousNode = None
        index = 1
        while currentNode:
            if pos == index:
                newNode.next = currentNode.next
                currentNode.next = newNode
                return
            index += 1
            previousNode = currentNode
            currentNode = currentNode.next
        newNode.next = currentNode
        previousNode.next = newNode

    def size(self):
        """Return the size or length of the linked list.
        Time Complexity: O(n)

        Returns:
            int: The number of nodes in the linked list
        """
        size = 0
        currentNode = self.head
        while currentNode:
            size += 1
            currentNode = currentNode.next
        return size

    def traverse(self):
        """Traverse through the linked list
        Time Complexity: O(n)
        """
        currentNode = self.head
        output = ""
        while currentNode is not None:
            output += f"{currentNode.value} ==> "
            currentNode = currentNode.next
        print(output)

    def to_list(self) -> list:
        """Convert LinkedList to List

        Returns:
            list: A list of values
        """
        currentNode = self.head
        out_list = []
        while currentNode is not None:
            out_list.append(currentNode.value)
            currentNode = currentNode.next
        return out_list

    def reverse(self):
        """Reverse the inputted linked list
        Time Complexity: O(n)

        To Reverse a linked list, create a new empty linked list and iterate through the old linked list doing a prepend to the new linked list for each node

        Returns:
            SinglyLinkedList: The reversed linked list
        """
        if not self.head:
            return None
        currentNode = self.head
        newLinkedList = SinglyLinkedList()
        while currentNode:
            newLinkedList.prepend(currentNode.value)
            currentNode = currentNode.next
        return newLinkedList

    @staticmethod
    def reverseFromList(linkedList: list):
        """Reverse the inputted linked list
        Time Complexity: O(n)

        To convert a list into a reversed linked list, create a new empty linked list and iterate through the items of the old list doing a prepend to the new linked list for each node

        Args:
            linkedList (list): The input list

        Returns:
            SinglyLinkedList: The reversed Linked List
        """
        new_list = SinglyLinkedList()
        for value in linkedList:
            node = Node(value)
            node.next = new_list.head
            new_list.head = node
        return new_list

    def isCircular(self):
        """Determine whether the Linked List is circular or not
        Time Complexity: O(n)

        To tell if a linked list is circular you need 2 pointers
        A slow pointer that moves one step through the list
        A fast pointer that moves two steps through the list

        if at any point on iteration both pointers are on the same node then it's circular

        Returns:
            boolean: True if linked list is circular and false if otherwise
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            # slow pointer moves one node
            slow = slow.next
            # fast pointer moves two nodes
            fast = fast.next.next
            if fast == slow:
                return True
        # If we get to a node where fast doesn't have a next node or doesn't exist itself,
        # the list has an end and isn't circular
        return False

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


singlyLinkedList = SinglyLinkedList()

# Test prepend
singlyLinkedList.prepend(1)
assert singlyLinkedList.to_list() == [1], f"list contents: {singlyLinkedList.to_list()}"

# Test append - 1
singlyLinkedList.append(3)
singlyLinkedList.prepend(2)
assert singlyLinkedList.to_list() == [
    2,
    1,
    3,
], f"list contents: {singlyLinkedList.to_list()}"

# Test append - 2
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.append(1)
assert singlyLinkedList.to_list() == [1], f"list contents: {singlyLinkedList.to_list()}"
singlyLinkedList.append(3)
assert singlyLinkedList.to_list() == [
    1,
    3,
], f"list contents: {singlyLinkedList.to_list()}"

# Test search
singlyLinkedList.prepend(2)
singlyLinkedList.prepend(1)
singlyLinkedList.append(4)
singlyLinkedList.append(3)
assert (
    singlyLinkedList.search(1).value == 1
), f"list contents: {singlyLinkedList.to_list()}"
assert (
    singlyLinkedList.search(4).value == 4
), f"list contents: {singlyLinkedList.to_list()}"

# Test remove
singlyLinkedList.remove(1)
assert singlyLinkedList.to_list() == [
    2,
    1,
    3,
    4,
    3,
], f"list contents: {singlyLinkedList.to_list()}"
singlyLinkedList.remove(3)
assert singlyLinkedList.to_list() == [
    2,
    1,
    4,
    3,
], f"list contents: {singlyLinkedList.to_list()}"
singlyLinkedList.remove(3)
assert singlyLinkedList.to_list() == [
    2,
    1,
    4,
], f"list contents: {singlyLinkedList.to_list()}"

# Test pop
value = singlyLinkedList.pop()
assert value == 2, f"list contents: {singlyLinkedList.to_list()}"
assert singlyLinkedList.head.value == 1, f"list contents: {singlyLinkedList.to_list()}"

# Test insert
singlyLinkedList.insert(5, 0)
assert singlyLinkedList.to_list() == [
    5,
    1,
    4,
], f"list contents: {singlyLinkedList.to_list()}"
singlyLinkedList.insert(2, 1)
assert singlyLinkedList.to_list() == [
    5,
    2,
    1,
    4,
], f"list contents: {singlyLinkedList.to_list()}"
singlyLinkedList.insert(3, 6)
assert singlyLinkedList.to_list() == [
    5,
    2,
    1,
    4,
    3,
], f"list contents: {singlyLinkedList.to_list()}"

# Test size function
assert singlyLinkedList.size() == 5, f"list contents: {singlyLinkedList.to_list()}"

newList = singlyLinkedList.reverse()
newList.traverse()
reversedList = SinglyLinkedList.reverseFromList([2, 3, 4, 5])
reversedList.traverse()

# Test Circular
list_with_loop = SinglyLinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start
isCircular = list_with_loop.isCircular()
print(f"isCircular: {isCircular}")


def traverse_linked_list(head: Node):
    currentNode = head
    output = ""
    while currentNode is not None:
        output += f"{currentNode.value} ==> "
        currentNode = currentNode.next
    print(output)


def create_linked_list_one(new_list: list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    takes O(n)
    """
    head = None
    for value in new_list:
        if head is None:
            head = Node(value)
        else:
            currentNode = head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = Node(value)
    return head


def create_linked_list_two(input: list):
    head = None
    # TODO: Implement the more efficient version that keeps track of the tail takes O(n)
    tail = None
    for value in input:
        if head is None:
            head = Node(value)
            tail = (
                head  # when we only have 1 node, head and tail refer to the same node
            )
        else:
            tail.next = Node(value)  # attach the new node to the `next` of tail
            tail = tail.next  # update the tail
    return head


# head = Node(2)
# head.next = Node(1)
# head.next.next = Node(4)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(5)
head = create_linked_list_two([2, 1, 4, 3, 5])
traverse_linked_list(head)

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_two(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_two(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_two(input_list)
test_function(input_list, head)
