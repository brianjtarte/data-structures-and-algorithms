# Code Challenge 10

## Collaborators: Brendon
### Stack and Queue
**Problem Domain:**

#### Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

**Node**
 - Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
**Stack**
 - Create a Stack class that has a top property. It creates an empty Stack when instantiated.
 - This object should be aware of a default empty value assigned to top when the stack is created.
 - The class should contain the following methods:
 1. **push**
      - Arguments: value
      - adds a new node with that value to the top of the stack with an O(1) Time performance.
 2. **pop**
      - Arguments: none
 - Returns: the value from node from the top of the stack
 - Removes the node from the top of the stack
 - Should raise exception when called on empty stack
3. **peek**
 - Arguments: none
 - Returns: Value of the node located at the top of the stack
 - Should raise exception when called on empty stack
4. **is empty**
 - Arguments: none
 - Returns: Boolean indicating whether or not the stack is empty.

**Queue**
 - Create a Queue class that has a front property. It creates an empty Queue when instantiated.
 - This object should be aware of a default empty value assigned to front when the queue is created.
 - The class should contain the following methods:
1. **enqueue**
 - Arguments: value
 - adds a new node with that value to the back of the queue with an O(1) Time performance.
2. **dequeue**
 - Arguments: none
 - Returns: the value from node from the front of the queue
 - Removes the node from the front of the queue
 - Should raise exception when called on empty queue
3. **peek**
 - Arguments: none
 - Returns: Value of the node located at the front of the queue
 - Should raise exception when called on empty stack
4. **is empty**
 - Arguments: none
 - Returns: Boolean indicating whether or not the queue is empty

*You have access to the Node class and all the properties on the Linked List class.*


## Whiteboard Process
N/A

Linke to code:
[Stack](stack.py)
[Queue](queue.py)

## Approach & Efficiency

