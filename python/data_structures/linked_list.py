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
            raise TargetError

    def insert_after(self, old_value, new_value):
        current = self.head
        while current.value is old_value:  # while the current value is the old value
            new_node = Node(new_value)  # creating variable new_node and assigning it to a new Node w/new_value
            new_node.next = current.next  # new_node.next is now the current.next
            current.next = new_node  # current.next is now new_node, effectively inserting our newly created Node
            current = current.next

        else:
            current.next

    def kth_from_end(self, k):

        current = self.head
        kth_value = []
        if k < 0:  # if k is less than 0, we want to raise an exception
            raise TargetError
        else:

            try:

                while current:
                    kth_value.append(current.value)  # appending current node value to kth_value empty list
                    current = current.next
                if k > len(kth_value):  # if the value of k is greater than the length of the list, return none
                    return None
                else:
                    return kth_value[-k - 1]  # else, give us the last value of the list at the the value of k

            except:
                raise TargetError


class TargetError(Exception):
    pass
