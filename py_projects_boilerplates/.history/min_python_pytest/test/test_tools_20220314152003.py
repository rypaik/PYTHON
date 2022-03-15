import os
import sys
import unittest

# para incluir app en el path
testdir = os.path.dirname(__file__)
print(testdir)
srcdir = '../app'
appdir = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, appdir)


from modules.hello_world.tools.tools import say_hello

# para poder acceder a los directorios de app
os.chdir(appdir)


class TestTools(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertTrue(True)

    def test_say_hello(self):
        r = say_hello('message')
        self.assertIsInstance(r, str)


if __name__ == '__main__':
    unittest.main()
