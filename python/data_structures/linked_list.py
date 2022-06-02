class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        """
            Stringify the object and return value as string as well as concatenate the previous value to the next
        """

        current = self.head
        values = ""
        if self.head is None:
            return f"NULL"
        while current is not None:
            values += "{}".format('{ ' + f"{current.value}" + ' } -> ')
            current = current.next
        values += 'NULL'
        return values

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        pass


class TargetError:
    pass
