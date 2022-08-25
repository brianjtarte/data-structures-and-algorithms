from python.data_structures.hashtable import Hashtable
import string


def first_repeated_word(words):
    new_table = Hashtable()
    newstring = words.translate(str.maketrans('', '', string.punctuation))
    key_list = newstring.split()

    for key in key_list:
        newkey = key.lower()
        if new_table.contains(newkey):

            return newkey
        else:
            new_table.set(newkey, None)
    return None



