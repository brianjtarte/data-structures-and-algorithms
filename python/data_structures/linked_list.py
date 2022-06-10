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

    def append(self, new_value):
        current = self.head
        while current.next:
            current = current.next
        else:
            new_node = Node(new_value)
            current.next = new_node

    def insert_before(self, old_value, new_value):
        current = self.head
        if self.includes(old_value):
            while current:
                if current.value == old_value:
                    self.insert(new_value)
                    return
                elif current.next.value == old_value:
                    new_node = Node(new_value, current.next)
                    current.next = new_node
                    return
                current = current.next
        else:
            raise TargetError('WRONG')

    def insert_after(self, old_value, new_value):
        current = self.head
        while current.value is old_value:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node
            current = current.next

        else:
            current.next

    def kth_from_end(self, k):
        current = self.head
        kth_value = []
        while current:
            kth_value.append(current.value)
            current = current.next
        if k > len(kth_value):
            return None
        else:
            return kth_value[-k-1]

class TargetError:
    pass

