from python.code_challenges.trees.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        def traverse_tree(root, node):
            if not root:
                return

            if node.value < root.value:
                if root.left:
                    traverse_tree(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    traverse_tree(root.right, node)
                else:
                    root.right = node

        traverse_tree(self.root, node)

    def contains(self, value):

        def traverse_tree(root):
            if not root:
                return False

            elif root.value == value:
                return True
            elif value < root.value:
                return traverse_tree(root.left)
            else:
                return traverse_tree(root.right)

        return traverse_tree(self.root)
