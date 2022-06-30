from python.code_challenges.stack_and_queue.queue import Queue

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        Queue.enqueue(self, animal)

    def dequeue(self, pref):
        if pref == 'cat' or pref == 'dog':
            if self.front:
                temp = self.front
                self.front = temp.next
                temp.next = None
                return temp.value
        else:
            return None


class Dog:
    pass


class Cat:
    pass
