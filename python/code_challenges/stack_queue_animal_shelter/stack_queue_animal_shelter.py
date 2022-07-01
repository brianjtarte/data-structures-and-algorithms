from python.code_challenges.stack_and_queue.queue import Queue

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):
        if animal == 'dog':
            dog = Dog(animal)
            self.dog.enqueue(dog)
        elif animal == 'cat':
            cat = Cat(animal)
            self.cat.enqueue(cat)



    def dequeue(self, pref):
        if pref == 'dog':
            dog = Dog()
            self.dog.dequeue()
        elif pref == 'cat':
            cat = Cat()
            self.cat.dequeue()
        # if pref == 'cat' or pref == 'dog':
        #     while self.front.value != pref:
        #         if self.front:
        #             temp = self.front
        #             self.front = temp.next
        #             temp.next = None
        #             return temp.value
        #         else:
        #             return None
        #     return self.front.value
        # else:
        #     return None


class Dog:
    def __init__(self, dog='dog', next=None):
        self.dog = dog
        self.next = next


class Cat:
    def __init__(self, cat='cat', next=None):
        self.cat = cat
        self.next = next
