from python.data_structures.linked_list import LinkedList, Node


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):
        index = self.hash(key)
        if self._buckets[index] == None:
            new_ll = LinkedList()
            new_ll.insert({key: value})
            self._buckets[index] = new_ll

        else:
            self._buckets[index].insert({key: value})

        # set
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

    def get(self, key):
        index = self.hash(key)
        if self._buckets[index]:
            return self._buckets[index].head.value[key]

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        index = self.hash(key)

        if self._buckets[index]:
            current = self._buckets[index].head

            while current:
                keyslist = list(current.value.keys())
                if keyslist[0] == key:
                    return True
                current = current.next

            return False
        else:
            return False

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def keys(self):
        keys_list = []
        for head in self._buckets:

            if head is not None:
                current = head.head
                while current:
                    keys = list(current.value.keys())
                    keys_list.append(keys[0])
                    current = current.next
        return keys_list

    #     'roger' 10431 list: 1024
    def hash(self, key):

        total = 0
        if type(key) is int:
            for ch in str(key):
                total += ord(ch)

            primed = total * 19

            index = primed % self.size
            return index
        else:
            for ch in key:
                total += ord(ch)

            primed = total * 19

            index = primed % self.size
            return index


if __name__ == '__main__':
    new_hash = Hashtable()
    new_hash.set('tab', 'tarte')
    new_hash.set('tab', 'charlie')
    new_hash.set('brian', 'tarte')
    new_hash.set('apple', 'charlie')
    print(new_hash.keys())
