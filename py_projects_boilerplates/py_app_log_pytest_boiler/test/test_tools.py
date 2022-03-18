import os
import sys
# import unittest
import pytest

testdir = os.path.dirname(__file__)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

# import local libraries here (consider whether it is on common or within a module in the modules directory)
from modules.hello_world.tools.tools import say_hello


# accessing the /app directory
os.chdir(appdir)

# class TestTools(unittest.TestCase):

#     def setUp(self):
#         pass

#     def test_something(self):
#         self.assertTrue(True)

# def test_say_hello(self):
#     r = say_hello('message')
#     self.assertIsInstance(r, str)

def test_say_hello():
    r = say_hello('message')
    assert isinstance(r, str)
    assert isinstance(r, int)
 
def test_something():
    assert(True)

if __name__ == '__main__':
    test_say_hello()
