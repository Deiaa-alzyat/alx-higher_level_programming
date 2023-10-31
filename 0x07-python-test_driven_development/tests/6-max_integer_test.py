#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        x = __import__('6-max_integer').__doc__
        self.assertTrue(len(x) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        y = max_integer.__doc__
        self.assertTrue(len(y) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        r = []
        self.assertIsNone(max_integer(r))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        s = [1]
        self.assertEqual(max_integer(s), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        t = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(t), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        u = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(u), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        v = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(v), 200)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        w = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(w), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        a = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(a), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
