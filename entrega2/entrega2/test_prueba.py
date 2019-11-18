import unittest
from prueba import test, test2

class TestProbar(unittest.TestCase):
    def test_siHayUsuario(self):
        self.assertTrue(test('Usuario'))
    def test_noHayUsuario(self):
        self.assertTrue(test('Usuario'))