import unittest

from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):

    def setUp(self):
        self.base = Base()

    def test_instantiation(self):
        self.assertIs(type(Base()), Base)
        self.assertEqual(Base(5).id, 5)
        self.assertEqual(Base().id, 3)

    def test_to_json_string(self):
        r = Rectangle(5, 7)
        d = r.to_dictionary()
        self.assertEqual(self.base.to_json_string([d]), str([d]).replace("'", '"'))

if __name__ == '__main__':
    unittest.main()
