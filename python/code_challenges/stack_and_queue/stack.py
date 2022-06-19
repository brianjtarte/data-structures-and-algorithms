from python.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    We are performing push, pop, peek, and is_empty on a Stack
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp.value
        else:
            if self.top is None:
                raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if self.top:

            return self.top.value

        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.top is None
