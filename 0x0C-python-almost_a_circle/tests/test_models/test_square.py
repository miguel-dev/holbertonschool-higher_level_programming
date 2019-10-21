import unittest
import io
import sys

from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(3, 1, 1, 5)

    def test_init(self):
        self.assertEqual(self.square.width, 3)
        self.assertEqual(self.square.height, 3)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 1)
        self.assertEqual(self.square.id, 5)

    def test__str__(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(self.square)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "[Square] ({:d}) {:d}/{:d} - {:d}\n".format(self.square.id, self.square.x, self.square.y, self.square.width))
