import os
import sys
# import unittest
import pytest

testdir = os.path.dirname(__file__)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)



from modules.hello_world.tools.tools import say_hello

# change the here the function to test
from modules.pytest_mod.loguru_logging import func
# from common.tools.loguru_logging  import func

from _pytest.logging import caplog as _caplog

#accessing app dir
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
    print("test_something ran")
    
def test_func(caplog):
    # loguru_logging.func()
    func()
    assert("This is a log message." in caplog.text)
        

if __name__ == '__main__':
    test_say_hello()
    test_something()
    test_func(_caplog)
    # print(caplog.text)