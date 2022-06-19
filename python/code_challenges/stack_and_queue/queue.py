from python.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    We are performing enqueue, dequeue, peek and is_empty on a Queue
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if self.rear:
            self.rear.next = node

        if self.front is None:
            self.front = node

        self.rear = node


    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        else:
                raise InvalidOperationError()

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError()


    def is_empty(self):
        if self.front is None:
            return True
        else:
            raise InvalidOperationError()
