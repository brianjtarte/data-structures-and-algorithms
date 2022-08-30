from python.code_challenges.trees.binary_tree import BinaryTree, Node
from python.data_structures.hashtable import Hashtable



# def tree_intersection(tree1, tree2):
#     new_hash = Hashtable()
#     tree_one = tree1.in_order()
#     tree_two = tree2.in_order()
#     tree_set1 = new_hash.set(tree_one, None)
#     tree_set2 = new_hash.set(tree_two, None)
#     common_tree_list = []
#     print(tree1)
#     # if tree_set1.contains(tree_set2):
#     #     common_tree_list.append(tree_set2.value)
#
#     # return common_tree_list
#     print(common_tree_list)
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

        # else:
        #     new_table.set(current1.value, current1.value)
        print('current1', current1.value)
    traverse_tree_one(current1)


    def traverse_tree_two(current2):
        if current2.left:
            if new_table.contains(current2.value):
                traverse_tree_two(current2.left)
                common_val.append(current2.value)

        if current2.right:
            if new_table.contains(current2.value):
                common_val.append(current2.value)
        print('current2', current2.value)

        # else:
        #     return common_val



    traverse_tree_two(current2)

    # return common_val
    print(new_table.keys())
    print(common_val)


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
    tree_b.root = node2
    tree_b.root.left = node6
    tree_b.root.right = node7
    tree_b.root.left.left = node8
    tree_b.root.right.right = node5
    tree_intersection(tree_a, tree_b)
