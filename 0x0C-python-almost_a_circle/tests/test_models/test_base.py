#!/usr/bin/python3
"""
Unittest for Class Base
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestClassBase(unittest.TestCase):
    """Teste for Base"""

    def test_id(self):
        """
        testing de id values
        """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base(89)
        self.assertEqual(obj3.id, 89)
        obj4 = Base()
        self.assertEqual(obj4.id - 1, obj2.id)
        obj5 = Base()
        self.assertEqual(obj4.id + 1, obj5.id)
        obj6 = Base(None)
        self.assertEqual(obj6.id, obj5.id + 1)
        obj7 = Base("id")
        self.assertEqual(obj7.id, "id")
        obj8 = Base([1, 2])
        self.assertEqual(obj8.id, [1, 2])
        obj9 = Base(2)
        obj9.id = 9
        self.assertEqual(obj9.id, 9)
        obj10 = Base(2)
        obj10.id = "otro id"
        self.assertEqual(obj10.id, "otro id")
        obj11 = Base(float("nan"))
        self.assertNotEqual(obj11.id, float("nan"))
        obj15 = Base(float("inf"))
        self.assertEqual(obj15.id, float("inf"))
        obj16 = Base(memoryview(b'asdfg'))
        self.assertEqual(obj16.id, memoryview(b'asdfg'))
        obj17 = Base(frozenset({"a", "b"}))
        self.assertEqual(obj17.id, frozenset({"a", "b"}))
        obj18 = Base(False)
        self.assertEqual(obj18.id, False)
        obj19 = Base(complex(123))
        self.assertEqual(obj19.id, complex(123))
        obj20 = Base({"a": 12, "v": 32})
        self.assertEqual(obj20.id, {"a": 12, "v": 32})
        obj20 = Base(None)
        self.assertEqual(obj20.id, 6)
        obj12 = Rectangle(1, 1, 1, 1)
        self.assertEqual(obj12.id, 7)
        obj12 = Rectangle(1, 1, 1, 1, 99)
        self.assertEqual(obj12.id, 99)
        obj13 = Rectangle(1, 1, 1, 1, 100)
        self.assertEqual(obj13.id, 100)
        obj14 = Rectangle(1, 1, 1, 1)
        self.assertEqual(obj14.id, 8)
