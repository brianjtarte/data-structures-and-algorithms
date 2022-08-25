import pytest
from python.data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_contains_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.contains("apple")
    expected = True
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_keys_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set( "chicken", "Used for chicken wings")
    actual = hashtable.keys()
    expected = ["chicken", "apple"]
    assert actual == expected

@pytest.mark.xfail
def test_fail_keys_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set( "chicken", "Used for chicken wings")
    actual = hashtable.keys()
    expected = ["apple", "chicken"]
    assert actual == expected

def test_edge_case():
    hashtable = Hashtable()
    hashtable.set(1234, "Used for apple sauce")
    actual = hashtable.get(1234)
    expected = "Used for apple sauce"
    assert actual == expected

def test_collision_case():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "Used for apple juice")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce", "Used for apple juice"
    assert actual == expected


# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")
#
#     actual = []
#
#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())
#
#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
#
#     assert actual == expected
