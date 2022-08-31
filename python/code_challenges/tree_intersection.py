from python.code_challenges.trees.binary_tree import BinaryTree, Node
from python.data_structures.hashtable import Hashtable
def tree_intersection(tree1, tree2):
    new_table = Hashtable()
    common_val = []
    current1 = tree1.root
    current2 = tree2.root

    def traverse_tree_one(current1):

        if current1.left:
            traverse_tree_one(current1.left)
        new_table.set(current1.value, current1.value)

        if current1.right:
            traverse_tree_one(current1.right)
    traverse_tree_one(current1)

    def traverse_tree_two(current2):

        if current2.left:
            traverse_tree_one(current2.left)
        new_table.set(current2.value, current2.value)

        if current2.right:
            traverse_tree_one(current2.right)
    traverse_tree_two(current2)
    common_val.append(new_table.keys())

    dupe_size = len(common_val[0])
    dupes = []
    for i in range(dupe_size):
        for j in range(i):
          k = j + 1
          for h in range(k, dupe_size):
            if common_val[0][j] == common_val[0][h] and common_val[0][j] not in dupes:
                dupes.append(common_val[0][j])

    return dupes


if __name__ == '__main__':
    tree_a = BinaryTree()
    tree_b = BinaryTree()
    node1 = Node(100)
    node2 = Node(175)
    node3 = Node(190)
    node4 = Node(180)
    node5 = Node(210)
    node6 = Node(100)
    node7 = Node(175)
    node8 = Node(180)
    tree_a.root = node1
    tree_a.root.left = node2
    tree_a.root.right = node3
    tree_a.root.left.left = node4
    tree_b.root = node5
    tree_b.root.left = node6
    tree_b.root.right = node7
    tree_b.root.left.left = node8

    tree_intersection(tree_a, tree_b)
