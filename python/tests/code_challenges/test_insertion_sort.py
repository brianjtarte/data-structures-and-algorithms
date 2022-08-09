import pytest
from python.code_challenges.sorting.insertion_sort import selection_sort

# @pytest.mark.skip('Insertion Sort')
def test_insertion_one():
    arr = [5, 1, 3, 7, 2, 14]
    actual = selection_sort(arr)
    expected = [1, 2, 3, 5, 7, 14]
    assert actual == expected

# @pytest.mark.skip('Insertion Sort')
def test_insertion_jenny():
    arr = [8, 6, 7, 5, 3, 0, 9]
    actual = selection_sort(arr)
    expected = [0, 3, 5, 6, 7, 8, 9]
    assert actual == expected

# @pytest.mark.skip('Insertion Sort')
def test_insertion_duplicates():
    arr = [5, 1, 3, 1, 2, 14]
    actual = selection_sort(arr)
    expected = [1, 1, 2, 3, 5, 14]
    assert actual == expected

# @pytest.mark.skip('Insertion Sort')
def test_insertion_high_number():
    arr = [986, 1, 546, 31, 2, 14]
    actual = selection_sort(arr)
    expected = [1, 2, 14, 31, 546, 986]
    assert actual == expected

# @pytest.mark.skip('Insertion Sort')
def test_insertion_negative():
    arr = [1, 0, -2, 3, 4, 5]
    actual = selection_sort(arr)
    expected = [-2, 0, 1, 3, 4, 5]
    assert actual == expected

# @pytest.mark.skip('Insertion Sort')
def test_insertion_triplicate():
    arr = [9, 23, 55, 9, 63, 9]
    actual = selection_sort(arr)
    expected = [9, 9, 9, 23, 55, 63]
    assert actual == expected

