import unittest

from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_instantiation(self):
        self.assertIs(type(Base()), Base)
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base().id, 2)

if __name__ == '__main__':
    unittest.main()
