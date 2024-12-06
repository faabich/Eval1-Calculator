import unittest

class TestMathLib(unittest.TestCase):

    def setUp(self):
        self.ope1 = 3
        self.oper = '+'
        self.ope2 = 5
        self.mathLib = MathLib(self.ope1, self.oper, self.ope2)

    def test_get_addition(self):
        self.assertEqual(self.mathLib.get_ope1(), self.ope1)

    def test_get_oper(self):
        self.assertEqual(self.mathLib.get_oper(), self.oper)

    def test_get_ope2(self):
        self.assertEqual(self.mathLib.get_ope2(), self.ope2)

if __name__ == '__main__':
    unittest.main()