class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):

        def traverse_tree(root):

            values.append(root.value)

            if root.left:
                traverse_tree(root.left)

            if root.right:
                traverse_tree(root.right)

        values = []

        traverse_tree(self.root)

        return values

    def in_order(self):

        def traverse_tree(root):

            if root.left:
                traverse_tree(root.left)
            values.append(root.value)

            if root.right:
                traverse_tree(root.right)

        values = []

        traverse_tree(self.root)

        return values

    def post_order(self):

        def traverse_tree(root):

            if root.left:
                traverse_tree(root.left)

            if root.right:
                traverse_tree(root.right)
            values.append(root.value)

        values = []

        traverse_tree(self.root)

        return values

    def find_maximum_value(self):

        def traverse_tree(root, max_value=0):
            if root is None:
                return max_value
            if root.value > max_value:
                max_value = root.value
            return traverse_tree(root.left, max_value)
            return traverse_tree(root.right, max_value)

        return traverse_tree(self.root)




class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
