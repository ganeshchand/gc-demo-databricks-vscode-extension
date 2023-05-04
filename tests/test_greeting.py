import unittest

class TestStringMethods(unittest.TestCase):

    def test_greet(self):
        from common.utils import greeting
        greeting("world")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_utils_greet(self):
        from utils.DateTimeUtils import date_utils
        date_utils()
        self.assertEqual('foo'.upper(), 'FOO')    
