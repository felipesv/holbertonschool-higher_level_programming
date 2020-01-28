#!/usr/bin/python3
"""
Unittest for Class Base
"""
import unittest
import sys
import io
from models.square import Square


class TestClassSquare(unittest.TestCase):
    """Teste for Base"""

    def test_create(self):
        """
        creating a valid obj Squeare
        """
        with self.assertRaises(TypeError):
            obj1 = Square()
        with self.assertRaises(TypeError):
            obj2 = Square(10, 44, 23, 23, 23, 23, 23)
        with self.assertRaises(TypeError):
            obj3 = Square(10, 12, 12, 12, 12, 12, 12, 12)

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
            obj4 = Square(0, 9)
        with self.assertRaises(ValueError):
            obj5 = Square(1, -1)
        with self.assertRaises(TypeError):
            obj6 = Square(2, "2")
        with self.assertRaises(TypeError):
            obj7 = Square(2, [1, 2, 3, 4])

    def test_area(self):
        """
        test area
        """
        obj1 = Square(1)
        self.assertEqual(obj1.area(), 1)
        obj1 = Square(24)
        self.assertEqual(obj1.area(), 576)
        obj1 = Square(8)
        obj1.width = 8
        self.assertEqual(obj1.area(), 64)

    def test_display(self):
        """
        test display
        """
        obj1 = Square(1)
        self.assertEqual(obj1.display(), None)
        obj1 = Square(3)
        obj1.id = 8
        self.assertEqual(obj1.display(), None)
        obj1 = Square(1)
        capture = TestClassSquare.capture_stdout(obj1, "display")
        correct = "#\n"
        self.assertEqual(correct, capture.getvalue())
        obj1 = Square(1)
        capture = TestClassSquare.capture_stdout(obj1, "display")
        correct = "#\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_(self):
        """
        test __str__
        """
        obj1 = Square(4)
        capture = TestClassSquare.capture_stdout(obj1, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())
        obj1 = Square(12, 1, 1)
        capture = TestClassSquare.capture_stdout(obj1, "print")
        correct = "[Square] ({}) 1/1 - 12\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())
        obj1 = Square(12, 1, 1)
        capture = TestClassSquare.capture_stdout(obj1, "print")
        correct = "[Square] ({}) 1/1 - 12\n".format(obj1.id)
        self.assertEqual(correct, capture.getvalue())

    def test_update(self):
        """
        test update args
        """
        r1 = Square(10)
        r1.update(89)
        capture = TestClassSquare.capture_stdout(r1, "print")
        correct = "[Square] (89) 0/0 - 10\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Square(10, 10, 10, 10)
        r1.update(89, 29)
        capture = TestClassSquare.capture_stdout(r1, "print")
        correct = "[Square] (89) 10/10 - 29\n"
        self.assertEqual(correct, capture.getvalue())
        r1 = Square(10, 10, 10, 10)
        r1.update()
        capture = TestClassSquare.capture_stdout(r1, "print")
        correct = "[Square] (10) 10/10 - 10\n"
        self.assertEqual(correct, capture.getvalue())

    @staticmethod
    def capture_stdout(obj, method):
        """
        return the stdoutput by bdbaraban
        """
        ioValue = io.StringIO()
        sys.stdout = ioValue
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return ioValue
