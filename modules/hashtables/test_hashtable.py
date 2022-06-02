# test_hashtable.py

# def test_should_always_pass():
#    assert 2-2 == 0, "simple addition pass"
#    assert 2+2==2, " this is just a practice fail"

# define a custom HashTable Class
from hashtable import HashTable, BLANK
import pytest


def test_should_create_hashtable():
    assert HashTable(size=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values ==[None, None, None]

@pytest.mark.skip
def test_should_inser_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values

    #raises a fail, len should be count of keys or None at init
    assert len(hash_table) == 100

def test_should_not_contain_none_value_on_init():
    assert None not in HashTable(capacity=100).values
