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

    def test_size_setter(self):
        self.square.size = 4
        self.assertEqual(self.square.size, 4)

    def test_args(self):
        self.square.update(1, 2, 3, 4, id=2, size=3, x=4, y=5)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.size, 2)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 4)

    def test_update_kwargs(self):
        self.square.update(id=2, size=3, x=4, y=5)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 3)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.x, 4)
