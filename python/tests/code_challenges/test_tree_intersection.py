import pytest
from python.code_challenges.tree_intersection import tree_intersection
from python.code_challenges.trees.binary_tree import BinaryTree, Node
from python.code_challenges.stack_and_queue.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)

# @pytest.mark.skip("TODO")
def test_tree_intersection_string():

    tree_a = BinaryTree()
    values = ['a', 'b', 'c']
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = ['a', 'c', 'd']
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = ['a', 'c']

    assert sorted(actual) == sorted(expected)




@pytest.mark.xfail
def test_tree_intersection_string_int():

    tree_a = BinaryTree()
    values = ['a', 4, 'b', 'c', 2]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = ['a', 'c', 2, 'd']
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = ['a', 'c', 2]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
