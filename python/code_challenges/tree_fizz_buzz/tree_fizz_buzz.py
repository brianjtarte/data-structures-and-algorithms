from python.code_challenges.trees.binary_tree import BinaryTree
from python.data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(kary_tree):
    if kary_tree is None:
        return None
    ktree = kary_tree

    def fizzy_helper(root):
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = 'FizzBuzz'
        elif root.value % 3 == 0:
            root.value = 'Fizz'
        elif root.value % 5 == 0:
            root.value = 'Buzz'
        elif root.value % 3 != 0 or root.value % 5 != 0:
            root.value = str(root.value)

        for kchild in root.children:
            fizzy_helper(kchild)

    fizzy_helper(ktree.root)
    return ktree


if __name__ == '__main__':
    tree = KaryTree()
    node = Node(1)
    tree.root = node
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(15)
    node.children = [node1, node2, node3]
    fizz_buzz_tree(tree)
