import os
import sys
# import unittest
import pytest

# to include app in the path
testdir = os.path.dirname(__file__)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

# import local libraries here (consider whether it is on common or within a module in the modules directory)
from modules.hello_world.tools.tools import say_hello

# to access app directories 
# os.chdir(appdir)


# class TestTools(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_something(self):
#         self.assertTrue(True)

#     def test_say_hello(self):
#         r = say_hello('message')
#         self.assertIsInstance(r, str)
#     def test_pytest(self):
#         self.assertFalse(True)


# if __name__ == '__main__':
#     unittest.main()



# def setUp():
#     pass

# def test_something():
#     self.assertTrue(True)

def test_say_hello():
    r = say_hello('message')
    assert isinstance(r, str)

# def test_pytest():
#     self.assertFalse(True)
