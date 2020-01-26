#!/usr/bin/python3
"""
Unittest for Class Base
"""
import unittest
from models.base import Base


class TestClassBase(unittest.TestCase):
    """Teste for Base"""

    def test_id(self):
        #test1
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        #test2
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        #test3
        obj3 = Base(89)
        self.assertEqual(obj3.id, 89)
        #test4
        obj4 = Base()
        self.assertEqual(obj4.id - 1, obj2.id)
        #test5
        obj5 = Base()
        self.assertEqual(obj4.id + 1, obj5.id)
        #test6
        obj6 = Base(None)
        self.assertEqual(obj6.id, obj5.id + 1)
        #test7
        obj7 = Base("id")
        self.assertEqual(obj7.id, "id")
        #test8
        obj8 = Base([1, 2])
        self.assertEqual(obj8.id, [1, 2])
        #test9
        obj9 = Base(2)
        obj9.id = 9
        self.assertEqual(obj9.id, 9)
        #test10
        obj10 = Base(2)
        obj10.id = "otro id"
        self.assertEqual(obj10.id, "otro id")
        #test11
        obj11 = Base(float("nan"))
        self.assertNotEqual(obj11.id, float("nan"))
