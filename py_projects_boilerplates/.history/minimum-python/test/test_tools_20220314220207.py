import os
import sys
# import unittest
import pytest
testdir = os.path.dirname(__file__)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)

# importar aquí librerías locales (considerar si está en common o dentro de un módulo en el directorio modules)
from modules.hello_world.tools.tools import say_hello

# para poder acceder a los directorios de app
os.chdir(appdir)

# class TestTools(unittest.TestCase):

#     def setUp(self):
#         pass

#     def test_something(self):
#         self.assertTrue(True)

def test_say_hello():
    r = say_hello('message')
    self.assertIsInstance(r, str)

def test_say_hello():
    r = say_hello('message')
    assert isinstance(r, str)


if __name__ == '__main__':
    test_say_hello()
    