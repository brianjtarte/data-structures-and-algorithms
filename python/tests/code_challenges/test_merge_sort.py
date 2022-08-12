from python.code_challenges.sorting.merge_sort import merge_sort


def test_import():
    assert merge_sort


def test_merge_sort():
    array = [8, 4, 23, 42, 16, 15]
    merge_sort(array)
    assert array == [4, 8, 15, 16, 23, 42]


def test_merge_sort_one():
    array = [8]
    merge_sort(array)
    assert array == [8]


def test_merge_sort_none():
    array = []
    merge_sort(array)
    assert array == []
