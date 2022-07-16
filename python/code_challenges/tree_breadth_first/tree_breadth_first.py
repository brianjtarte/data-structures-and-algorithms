from python.code_challenges.trees.binary_tree import BinaryTree, Node
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
    print(tree_list)
    return tree_list


if __name__ == '__main__':
    print('testing')
    binarytree = BinaryTree()

    level_0 = Node(2)
    level_1_first = Node(7)
    level_1_second = Node(5)

    level_2_first = Node(2)
    level_2_second = Node(6)
    level_2_third = Node(9)

    level_3_first = Node(5)
    level_3_second = Node(11)
    level_3_third = Node(4)

    binarytree.root = level_0
    level_0.left = level_1_first
    level_0.right = level_1_second
    level_1_first.left = level_2_first
    level_1_first.right = level_2_second
    level_1_second.right = level_2_third

    level_2_second.left = level_3_first
    level_2_second.right = level_3_second

    level_2_third.right = level_3_third
    breadth_first(binarytree)
