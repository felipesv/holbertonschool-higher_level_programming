#!/usr/bin/python3
"""
Unittest for Class Base
"""
import unittest
import sys
import io
from models.rectangle import Rectangle


class TestClassRectangle(unittest.TestCase):
    """Teste for Base"""

    def test_create(self):
        """
        creating a valid obj Rectangle
        """
        with self.assertRaises(TypeError):
            obj1 = Rectangle()
        with self.assertRaises(TypeError):
            obj2 = Rectangle(10, 9, 12, 12, 12, 12, 12, 12)
        with self.assertRaises(TypeError):
            obj3 = Rectangle(10, 12, 12, 12, 12, 12)

    def test_id(self):
        """
        test id in Base
        """
        pass

    def test_invalid_data(self):
        """
        test invalid data
        """
        with self.assertRaises(ValueError):
            obj4 = Rectangle(0, 9)
        with self.assertRaises(ValueError):
            obj5 = Rectangle(1, -1)
        with self.assertRaises(TypeError):
            obj6 = Rectangle(2, "2")
        with self.assertRaises(TypeError):
            obj7 = Rectangle(2, [1, 2, 3, 4])

    def test_area(self):
        """
        test area
        """
        obj1 = Rectangle(1, 1)
        self.assertEqual(obj1.area(), 1)
        obj1 = Rectangle(24, 24)
        self.assertEqual(obj1.area(), 576)
        obj1 = Rectangle(8, 7)
        obj1.width = 8
        self.assertEqual(obj1.area(), 56)

    def test_display(self):
        """
        test display
        """
        obj1 = Rectangle(1, 1)
        self.assertEqual(obj1.display(), None)
        obj1 = Rectangle(3, 1)
        obj1.id = 8
        self.assertEqual(obj1.display(), None)
        obj1 = Rectangle(1, 1)
        capture = TestClassRectangle.capture_stdout(obj1, "display")
        correct = "#\n"
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(1, 2)
        capture = TestClassRectangle.capture_stdout(obj1, "display")
        correct = "#\n#\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_(self):
        """
        test __str__
        """
        obj1 = Rectangle(4, 3)
        capture = TestClassRectangle.capture_stdout(obj1, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/3\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(12, 3, 1, 1)
        capture = TestClassRectangle.capture_stdout(obj1, "print")
        correct = "[Rectangle] ({}) 1/1 - 12/3\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())
        obj1 = Rectangle(12, 9, 1, 1)
        capture = TestClassRectangle.capture_stdout(obj1, "print")
        correct = "[Rectangle] ({}) 1/1 - 12/9\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())

    @staticmethod
    def capture_stdout(obj, method):
        """
        return the stdoutput bdbaraban
        """
        ioValue = io.StringIO()
        sys.stdout = ioValue
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return ioValue
