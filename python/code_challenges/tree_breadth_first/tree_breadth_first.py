from python.code_challenges.trees.binary_tree import BinaryTree
from python.code_challenges.stack_and_queue.queue import Queue


def breadth_first(tree):
    tree_queue = Queue()

    tree_list = []

    if tree.root is None:
        return tree_list

    tree_queue.enqueue(tree.root)

    while tree_queue.front:
        front_node = tree_queue.dequeue()
        tree_list.append(front_node.value)
        if front_node.left:
            tree_queue.enqueue(front_node.left)
        if front_node.right:
            tree_queue.enqueue(front_node.right)
    return tree_list
