import unittest
from numeracion import binario2decimal
class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'), 92)
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal(97), '01100001')


if __name__ == '__main__':
    unittest.main()
