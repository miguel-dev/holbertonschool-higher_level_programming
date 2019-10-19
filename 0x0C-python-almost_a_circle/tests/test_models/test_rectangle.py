import unittest
from models.rectangle import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width_setter(self):
        rectangle = Rectangle(3, 2)
        rectangle.width = 5
        self.assertEqual(rectangle.width, 5)

    def test_height_setter(self):
        rectangle = Rectangle(3, 2)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

    def test_x_setter(self):
        rectangle = Rectangle(3, 2, 4, 4)
        rectangle.x = 1
        self.assertEqual(rectangle.x, 1)

    def text_y_setter(self):
        rectangle = Rectangle(3, 2, 4, 4)
        rectangle.y = 9
        self.assertEqual(rectangle.y, 9)
