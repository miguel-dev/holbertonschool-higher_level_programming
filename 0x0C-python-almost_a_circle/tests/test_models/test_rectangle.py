import unittest
import io
import sys
from models.rectangle import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(3, 2, 4, 4)

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width_validation(self):
        self.assertRaises(TypeError, self.rectangle.__init__, "3", 2)
        self.assertRaises(ValueError, self.rectangle.__init__, 0, 4)

    def test_width_initialization(self):
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

    def test_height_validation(self):
        self.assertRaises(TypeError, self.rectangle.__init__, 4, 5.3)
        self.assertRaises(ValueError, self.rectangle.__init__, 8, -3)

    def test_height_initialization(self):
        self.rectangle.height = 7
        self.assertEqual(self.rectangle.height, 7)

    def test_x_validation(self):
        self.assertRaises(TypeError, self.rectangle.__init__, 6, 3, [3], 9)
        self.assertRaises(ValueError, self.rectangle.__init__, 2, 1, -8, 0)

    def test_x_initialization(self):
        self.rectangle.x = 1
        self.assertEqual(self.rectangle.x, 1)

    def test_y_validation(self):
        self.assertRaises(TypeError, self.rectangle.__init__, 7, 3, 0, "O")
        self.assertRaises(ValueError, self.rectangle.__init__, 2, 3, 4, -5)

    def text_y_initialization(self):
        self.rectangle.y = 9
        self.assertEqual(self.rectangle.y, 9)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 6)

    def test_display(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.rectangle.display()
        sys.stdout = sys.__stdout__
        output = "\n" * self.rectangle.y
        for row in range(self.rectangle.height):    
            output += " " * self.rectangle.x
            output += "#" * self.rectangle.width
            output += "\n"
        self.assertEqual(captured_output.getvalue(), output)

    def test__str__(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(self.rectangle)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}\n".format(self.rectangle.id, 
                                                                                                   self.rectangle.x,
                                                                                                   self.rectangle.y,
                                                                                                   self.rectangle.width,
                                                                                                   self.rectangle.height))

    def test_update_args(self):
        self.rectangle.update(1, 2, 3, 4, 5, id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_update_kwargs(self):
        self.rectangle.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 2)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

    def test_to_dictionary(self):
        dictionary = {'id': self.rectangle.id, 
                      'width': self.rectangle.width, 
                      'height': self.rectangle.height, 
                      'x': self.rectangle.x, 
                      'y': self.rectangle.y}
        self.assertEqual(self.rectangle.to_dictionary(), dictionary)

if __name__ == "__main__":
    unittest.main()
